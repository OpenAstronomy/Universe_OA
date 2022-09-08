.. title: Week 7 and 8 - User-testing, Mr. Minou's case, HAPPY BIRTHDAY TO ME!!!
.. slug:
.. date: 2022-08-07 00:00:00 
.. tags: radis
.. author: TranHuuNhatHuy
.. link: https://https://gsoc2022tranhuunhathuy.gatsbyjs.io/8. week 7-8/
.. description:
.. category: gsoc2022


.. raw:: html

    <p>For now, my priority is to focus on extensive user-testing cases from real-life experimental spectra, instead of the synthetic ones in first phase of the project. One of the very first experimental spectra I get, is from Mr. Nicolas MinesiMinesi, or Mr. Minou, a Post-doctoral Researcher at Universify of California, L.A. He specializes in laser spectroscopy and also one of my mentors in RADIS.</p>
    <h3>1. The spectrum</h3>
    <p>Mr. Minou introduced an absorbance CO spectrum near 2011 cm-1. He stored the data in a MAT (Matlab) file, which is extracted by this script:</p>
    <!-- TEASER_END -->
    <div class="gatsby-highlight"><pre class="language-python"><code class="language-python">fileName <span class="token operator">=</span> <span class="token string">"1857_VoigtCO_Minesi.mat"</span>
    data <span class="token operator">=</span>  scipy<span class="token punctuation">.</span>io<span class="token punctuation">.</span>loadmat<span class="token punctuation">(</span>fileName<span class="token punctuation">,</span> simplify_cells<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">)</span><span class="token punctuation">[</span><span class="token string">'CO_resu_Voigt'</span><span class="token punctuation">]</span>
    index <span class="token operator">=</span> <span class="token number">20</span>
    s_experimental <span class="token operator">=</span> Spectrum<span class="token punctuation">.</span>from_array<span class="token punctuation">(</span>
    data<span class="token punctuation">[</span><span class="token string">'nu'</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
    data<span class="token punctuation">[</span><span class="token string">'A_exp'</span><span class="token punctuation">]</span><span class="token punctuation">[</span><span class="token punctuation">:</span><span class="token punctuation">,</span>index<span class="token punctuation">]</span><span class="token punctuation">,</span>
    <span class="token string">'absorbance'</span><span class="token punctuation">,</span>
    wunit<span class="token operator">=</span><span class="token string">'cm-1'</span><span class="token punctuation">,</span>
    unit<span class="token operator">=</span><span class="token string">''</span>
    <span class="token punctuation">)</span> <span class="token comment"># adimensioned</span></code></pre></div>
    <p>With this, I acquire the experimental spectrum as below:</p>
    <p><span class="gatsby-resp-image-wrapper" style="display: block; margin-left: auto; margin-right: auto;">
    <a class="gatsby-resp-image-link" href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/e70ce9c33fa1293cdc0e69659560ada6/df5d6/exp_spectrum.png" rel="noopener" style="display: block;" target="_blank">
    <span class="gatsby-resp-image-background-image" style="display: block;"></span>
    <img alt="Mr. Minou's experimental spectrum, in absorbance." class="gatsby-resp-image-image" src="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/e70ce9c33fa1293cdc0e69659560ada6/f058b/exp_spectrum.png" style="width: 100%; height: 100%; margin: 0; vertical-align: middle;" title="Mr. Minou's experimental spectrum, in absorbance." />
    </a>
    </span></p>
    <p>And then, soon enough, I have also acquired his ground-truth data, which are fed to the JSON structures:</p>
    <div class="gatsby-highlight"><pre class="language-python"><code class="language-python"><span class="token comment"># Experimental conditions which will be used for spectrum modeling. Basically, these are known ground-truths.</span>
    experimental_conditions <span class="token operator">=</span> <span class="token punctuation">{</span>
    <span class="token string">"molecule"</span> <span class="token punctuation">:</span> <span class="token string">"CO"</span><span class="token punctuation">,</span>          <span class="token comment"># Molecule ID</span>
    <span class="token string">"isotope"</span> <span class="token punctuation">:</span> <span class="token string">"1"</span><span class="token punctuation">,</span>            <span class="token comment"># Isotope ID, can have multiple at once</span>
    <span class="token string">"wmin"</span> <span class="token punctuation">:</span> <span class="token number">2010.6</span><span class="token punctuation">,</span>            <span class="token comment"># Starting wavelength/wavenumber to be cropped out from the original experimental spectrum.</span>
    <span class="token string">"wmax"</span> <span class="token punctuation">:</span> <span class="token number">2011.6</span><span class="token punctuation">,</span>            <span class="token comment"># Ending wavelength/wavenumber for the cropping range.</span>
    <span class="token string">"wunit"</span> <span class="token punctuation">:</span> <span class="token string">"cm-1"</span><span class="token punctuation">,</span>           <span class="token comment"># Accompanying unit of those 2 wavelengths/wavenumbers above.</span>
    <span class="token string">"pressure"</span> <span class="token punctuation">:</span> <span class="token number">1</span><span class="token punctuation">,</span>             <span class="token comment"># Partial pressure of gas, in "bar" unit.</span>
    <span class="token string">"path_length"</span> <span class="token punctuation">:</span> <span class="token number">10</span><span class="token punctuation">,</span>         <span class="token comment"># Experimental path length, in "cm" unit.</span>
    <span class="token string">"wstep"</span> <span class="token punctuation">:</span> <span class="token number">0.001</span><span class="token punctuation">,</span>
    <span class="token string">"databank"</span> <span class="token punctuation">:</span> <span class="token string">"hitemp"</span>       <span class="token comment"># Databank used for calculation. Must be stated.</span>
    <span class="token punctuation">}</span>
    
    <span class="token comment"># List of parameters to be fitted.</span>
    fit_parameters <span class="token operator">=</span> <span class="token punctuation">{</span>
    <span class="token string">"Tgas"</span> <span class="token punctuation">:</span> <span class="token number">7170</span><span class="token punctuation">,</span>              <span class="token comment"># Fit parameter, accompanied by its initial value.</span>
    <span class="token string">"mole_fraction"</span> <span class="token punctuation">:</span> <span class="token number">0.07</span><span class="token punctuation">,</span>     <span class="token comment"># Species mole fraction, from 0 to 1.</span>
    <span class="token string">"offset"</span> <span class="token punctuation">:</span> <span class="token string">"0 cm-1"</span>         <span class="token comment"># Experimental offset, must be a blank space separating offset amount and unit.</span>
    <span class="token punctuation">}</span>
    
    <span class="token comment"># List of bounding ranges applied for those fit parameters above.</span>
    bounding_ranges <span class="token operator">=</span> <span class="token punctuation">{</span>
    <span class="token string">"Tgas"</span> <span class="token punctuation">:</span> <span class="token punctuation">[</span><span class="token number">2000</span><span class="token punctuation">,</span> <span class="token number">9000</span><span class="token punctuation">]</span><span class="token punctuation">,</span>      <span class="token comment"># Bounding ranges for each fit parameter stated above. You can skip this step, but not recommended.</span>
    <span class="token string">"mole_fraction"</span> <span class="token punctuation">:</span> <span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">,</span> <span class="token number">1</span><span class="token punctuation">]</span><span class="token punctuation">,</span>   <span class="token comment"># Species mole fraction, from 0 to 1.</span>
    <span class="token string">"offset"</span> <span class="token punctuation">:</span> <span class="token punctuation">[</span><span class="token operator">-</span><span class="token number">0.1</span><span class="token punctuation">,</span> <span class="token number">0.1</span><span class="token punctuation">]</span>      <span class="token comment"># Experimental offset, must be a blank space separating offset amount and unit</span>
    <span class="token punctuation">}</span>
    
    <span class="token comment"># Fitting pipeline setups.</span>
    fit_properties <span class="token operator">=</span> <span class="token punctuation">{</span>
    <span class="token string">"method"</span> <span class="token punctuation">:</span> <span class="token string">"lbfgsb"</span><span class="token punctuation">,</span>        <span class="token comment"># Preferred fitting method from the 17 confirmed methods of LMFIT stated in week 4 blog. By default, "leastsq".</span>
    <span class="token string">"fit_var"</span> <span class="token punctuation">:</span> <span class="token string">"absorbance"</span><span class="token punctuation">,</span>   <span class="token comment"># Spectral quantity to be extracted for fitting process, such as "radiance", "absorbance", etc.</span>
    <span class="token string">"normalize"</span> <span class="token punctuation">:</span> <span class="token boolean">False</span><span class="token punctuation">,</span>        <span class="token comment"># Either applying normalization on both spectra or not.</span>
    <span class="token string">"max_loop"</span> <span class="token punctuation">:</span> <span class="token number">300</span><span class="token punctuation">,</span>           <span class="token comment"># Max number of loops allowed. By default, 100.</span>
    <span class="token string">"tol"</span> <span class="token punctuation">:</span> <span class="token number">1e-20</span>               <span class="token comment"># Fitting tolerance, only applicable for "lbfgsb" method.</span>
    <span class="token punctuation">}</span></code></pre></div>
    <p>During my attempt to fit this spectrum, several bugs have been found and addressed.</p>
    <h3>2. Improvements</h3>
    <h4>a. Databank statement</h4>
    <p>Initially, the databank selection is hard-coded into my module, with <code class="language-text">hitran</code> for LTE cases and <code class="language-text">hitemp</code> for non-LTE cases. In this case, Mr. Minou’s spectrum is an LTE one, but he used <code class="language-text">hitemp</code> databank for calculation. Basically, for CO molecule, there are lines in <code class="language-text">hitemp</code> databank that are missing in <code class="language-text">hitran</code> databank, and thus the default <code class="language-text">hitran</code> for LTE does not provide a good result for Mr. Minou’s case.</p>
    <p>Thus, I make an implementation that allows users to specify the databank to be fetched into SpectrumFactory with <code class="language-text">fetch_databank</code>, by stating it directly in the script, as you can see above in <code class="language-text">experimental_conditions</code>.</p>
    <h4>b. Allow <code class="language-text">offset</code> to be fitted</h4>
    <p>Previously, as <code class="language-text">offset</code> and <code class="language-text">slit</code> are not parameters of <code class="language-text">calc_spectrum()</code>, but instead post-calculation convolution steps, so I did not include them as fit parameters. Now <code class="language-text">offset</code> is included and can be fitted as you can see above. As for <code class="language-text">slit</code>, according to Mr. Minou, usually the users know their FTIR spectrometer’s stats, and measure slit separately, so I have yet implemeted <code class="language-text">slit</code> as fittable parameter.</p>
    <h3>3. Result</h3>
    <p>Finally, we can see a not-perfect-but-good-enough result:</p>
    <p><span class="gatsby-resp-image-wrapper" style="display: block; margin-left: auto; margin-right: auto;">
    <a class="gatsby-resp-image-link" href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/178b6fac46562dfaf07965c4cb5ebe13/9451d/result.png" rel="noopener" style="display: block;" target="_blank">
    <span class="gatsby-resp-image-background-image" style="display: block;"></span>
    <img alt="Fitting result of Mr. Minou's case." class="gatsby-resp-image-image" src="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/178b6fac46562dfaf07965c4cb5ebe13/f058b/result.png" style="width: 100%; height: 100%; margin: 0; vertical-align: middle;" title="Fitting result of Mr. Minou's case." />
    </a>
    </span></p>
    <p>With best-fit parameters:</p>
    <ul>
    <li><code class="language-text">Tgas</code> : 6657.56 K (initially 7000 K).</li>
    <li><code class="language-text">mole_fraction</code> : 0.052 (initially 0.05).</li>
    <li><code class="language-text">offset</code> : -0.0177 cm-1 (initially 0 cm-1).</li>
    </ul>
    <p>And the fitting performance, which is really, really robust:</p>
    <ul>
    <li>Fitting method: L-BFGS-B.</li>
    <li>Number of fitting loops: 120.</li>
    <li>Total fitting time: 4.3125 s.</li>
    </ul>
    <p>To explain the discrepancy between experimental and best-fit spectra, Mr. Minou suggests that, this is some of physical problems, as RADIS currently only uses the air broadening parameters while originally he did this experiment in Argon. Future updates on other molecules’ broadening coefficients will be needed to increase the accuracy of these cases with non-air diluents.</p>
    <p>And so that’s it! My first complete case has done, and I have much better confidence in my fitting module, while being eager to confront other cases and gradually improve my module. This is such a good birthday evening.</p>

