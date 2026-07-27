.. title: GSoC 2026 Weeks 5-6: Folding Models and Rebinning X-ray Data
.. slug:
.. date: 2026-07-26 15:24:28 
.. tags: JuliaAstro
.. author: James
.. link: https://jamesraffertylee.wordpress.com/2026/07/26/gsoc-2026-weeks-5-6-folding-models-and-rebinning-x-ray-data/
.. description:
.. category: gsoc2026


.. raw:: html

    <h2 class="wp-block-heading">Moving from loading to using the data</h2>
    
    
    <!-- TEASER_END -->
    
    <p class="wp-block-paragraph">During weeks 5 and 6, I moved from loading X-ray observation files toward actually doing something with the pieces that had been loaded. Until this point, much of my work in <code>XraySpectra.jl</code> had focused on reading PHA, RMF, ARF, background, and RSP products and deciding how they should be represented. The next step was response folding and channel rebinning.</p>
    
    
    
    <p class="wp-block-paragraph">These features made the earlier work feel more connected. A PHA file, response matrix, and ancillary response are not just separate files that happen to be shipped together. They describe different parts of the path from an incoming photon to the counts recorded by the detector.</p>
    
    
    
    <h2 class="wp-block-heading">Understanding response folding</h2>
    
    
    
    <p class="wp-block-paragraph">A physical model usually predicts flux as a function of energy. The telescope does not observe that model directly. The ARF describes the instrument&#8217;s effective collecting area, while the RMF describes how photons from each true energy bin are redistributed into detector channels. Folding applies those instrument effects to the model and produces the detector-space prediction that can eventually be compared with the observed PHA data.</p>
    
    
    
    <p class="wp-block-paragraph">The basic interface now looks like this:</p>
    
    
    <div class="wp-block-code">
    <div class="cm-editor">
    <div class="cm-scroller">
    
    <pre>
    <code class="language-julia"><div class="cm-line"><span class="tok-variableName">folded</span> <span class="tok-operator">=</span> <span class="tok-variableName">fold</span>(<span class="tok-variableName">response</span>, <span class="tok-variableName">flux</span>; <span class="tok-variableName">ancillary</span> <span class="tok-operator">=</span> <span class="tok-variableName">ancillary</span>)</div></code></pre>
    </div>
    </div>
    </div>
    
    
    <p class="wp-block-paragraph">This initially looked like a fairly small matrix operation. It became more interesting once I had to make the dimensions and physical meaning explicit. The model vector must match the response input-energy bins, while the output must match the detector-channel bins. A mismatched length is not merely an inconvenient Julia error; it can mean that two scientifically incompatible grids are being combined.</p>
    
    
    
    <p class="wp-block-paragraph">The loader also distinguishes between a redistribution-only RMF and a full RSP response where the effective area may already be included. I used response types rather than a Boolean flag to represent that difference. This lets multiple dispatch reject an attempt to combine another ARF with a response that is already complete, which helps avoid accidentally applying the effective area twice.</p>
    
    
    
    <h2 class="wp-block-heading">Sparse matrices and in-place operations</h2>
    
    
    
    <p class="wp-block-paragraph">Real response matrices contain many zero values, so they are normally stored as sparse matrices. Treating one as an ordinary dense matrix could use much more memory than necessary.</p>
    
    
    
    <p class="wp-block-paragraph">This became important while implementing <code>combine</code> and <code>combine!</code>. The first returns a new response matrix after applying the ancillary effective area. The second writes into an output matrix supplied by the caller:</p>
    
    
    <div class="wp-block-code">
    <div class="cm-editor">
    <div class="cm-scroller">
    
    <pre>
    <code class="language-julia"><div class="cm-line"><span class="tok-variableName">combined</span> <span class="tok-operator">=</span> <span class="tok-variableName">combine</span>(<span class="tok-variableName">response</span>, <span class="tok-variableName">ancillary</span>)</div><div class="cm-line"></div><div class="cm-line"><span class="tok-variableName">output</span> <span class="tok-operator">=</span> <span class="tok-variableName">copy</span>(<span class="tok-variableName">response</span><span class="tok-operator">.</span><span class="tok-variableName">matrix</span>)</div><div class="cm-line"><span class="tok-variableName">combine!</span>(<span class="tok-variableName">output</span>, <span class="tok-variableName">response</span>, <span class="tok-variableName">ancillary</span>)</div></code></pre>
    </div>
    </div>
    </div>
    
    
    <p class="wp-block-paragraph">The exclamation mark does not have special behavior built into Julia. It is a naming convention that tells users that the function mutates one of its arguments. For the sparse method, I scale only the stored non-zero values instead of constructing a large temporary dense array. This was a useful reminder that code can be mathematically correct while still behaving badly for real scientific data sizes.</p>
    
    
    
    <h2 class="wp-block-heading">Combining detector channels</h2>
    
    
    
    <p class="wp-block-paragraph">The next feature was channel-side rebinning. X-ray spectra can have thousands of detector channels, many of which contain few counts. Users often combine adjacent channels before fitting, either with a simple fixed factor or with the grouping information already stored in an OGIP file.</p>
    
    
    
    <p class="wp-block-paragraph">For the common case, the API is:</p>
    
    
    <div class="wp-block-code">
    <div class="cm-editor">
    <div class="cm-scroller">
    
    <pre>
    <code class="language-julia"><div class="cm-line"><span class="tok-variableName">rebinned</span> <span class="tok-operator">=</span> <span class="tok-variableName">rebin_channels</span>(<span class="tok-variableName">data</span>; <span class="tok-variableName">factor</span> <span class="tok-operator">=</span> <span class="tok-number">16</span>)</div></code></pre>
    </div>
    </div>
    </div>
    
    
    <p class="wp-block-paragraph">It also accepts an explicit grouping vector. In the OGIP convention used by the NuSTAR and XMM files I inspected, <code>1</code> starts a group and <code>-1</code> continues the current group. The implementation also accepts <code>0</code> as a continuation value to match behavior already used by <code>SpectralFitting.jl</code>.</p>
    
    
    
    <p class="wp-block-paragraph">Rebinning a complete dataset means more than summing the source counts. The corresponding response rows and background channels must be combined as well. Channel bounds need to expand to cover the complete group, and the new channels are renumbered sequentially. Users can also turn off response or background rebinning when they only want to operate on the source spectrum.</p>
    
    
    
    <p class="wp-block-paragraph">Uncertainties required another distinction. Explicit numeric errors are combined in quadrature. For Poisson data, the counts are grouped first and the Poisson uncertainty is then calculated from the grouped result. If the spectrum stores rates, the exposure time is used when moving between rates and the underlying count statistics.</p>
    
    
    
    <p class="wp-block-paragraph">Quality follows a conservative rule: if any channel in a new group is marked bad, the combined channel is also marked bad. Rebinning should reduce resolution, but it should not quietly erase warnings about the original data.</p>
    
    
    
    <h2 class="wp-block-heading">Checking the behavior with NuSTAR</h2>
    
    
    
    <p class="wp-block-paragraph">Small generated arrays are useful for testing individual rules, but I also wanted to know whether the complete workflow made sense with real mission files.</p>
    
    
    
    <p class="wp-block-paragraph">Using the NuSTAR test observation, I loaded the PHA, RMF, and ARF, folded a test model through the response, and then rebinned the detector channels by a factor of 16. The spectrum went from 4,096 channels to 256. The response output dimension changed to match, while its input-energy grid and the ARF stayed unchanged.</p>
    
    
    
    <p class="wp-block-paragraph">The tests check that grouped counts are preserved, response contributions are summed correctly, the first rebinned folded value equals the sum of the first 16 original values, and the total folded prediction remains the same apart from numerical precision. Those checks were more useful than only testing the final array dimensions because they describe what rebinning is supposed to preserve.</p>
    
    
    
    <h2 class="wp-block-heading">Deciding not to rebin the energy axis</h2>
    
    
    
    <p class="wp-block-paragraph">We also discussed rebinning the response on its input-energy axis. At first, this seemed like the natural companion to channel rebinning. However, directly averaging or combining response columns can introduce artificial response support. It may suggest that a photon can be detected in an energy range where the original instrument response assigned no probability.</p>
    
    
    
    <p class="wp-block-paragraph">For now, direct response energy-axis rebinning has been deferred. A safer direction is closer to the existing <code>SpectralFitting.jl</code> workflow: evaluate the model, then interpolate or rebin the model values onto the response input grid before folding. This keeps the calibrated response intact.</p>
    
    
    
    <p class="wp-block-paragraph">I think this was an important outcome of these weeks. Progress is not always adding the next function on a list. Sometimes it is understanding the scientific consequences well enough to decide that a feature needs a more careful design.</p>
    
    
    
    <h2 class="wp-block-heading">Looking ahead</h2>
    
    
    
    <p class="wp-block-paragraph">By the end of week 6, the X-ray loader could not only assemble the observation products but also support response folding and explicit channel rebinning. The next question was how much of this design was truly general to spectra and how much came specifically from the OGIP/X-ray workflow.</p>
    
    
    
    <p class="wp-block-paragraph">That led me to start looking at infrared spectra from JWST. I expected different units and wavelengths. I did not yet realize how many different meanings the phrase &#8220;one spectrum&#8221; was about to acquire.</p>

