.. title: GSoC 2026 Weeks 7-8: What Counts as One Spectrum?
.. slug:
.. date: 2026-07-26 15:28:59 
.. tags: JuliaAstro
.. author: James
.. link: https://jamesraffertylee.wordpress.com/2026/07/26/gsoc-2026-weeks-7-8-what-counts-as-one-spectrum/
.. description:
.. category: gsoc2026


.. raw:: html

    <h2 class="wp-block-heading">Looking beyond X-rays</h2>
    
    
    <!-- TEASER_END -->
    
    <figure class="wp-block-image size-large"><img alt="" class="wp-image-135" height="576" src="https://jamesraffertylee.wordpress.com/wp-content/uploads/2026/07/image-1.png?w=1024" width="1024" /></figure>
    
    
    
    <p class="wp-block-paragraph">After working with OGIP products and X-ray response matrices, I spent weeks 7 and 8 exploring infrared spectral data from JWST.</p>
    
    
    
    <p class="wp-block-paragraph">An already extracted JWST spectrum usually provides wavelength, flux, uncertainty, data-quality information, and other calibrated columns directly. It does not use the same PHA, RMF, and ARF workflow that shaped <code>XraySpectra.jl</code>. More importantly, a single JWST spectral product does not always contain only one spectrum.</p>
    
    
    
    <h2 class="wp-block-heading">The many shapes of an extracted spectrum</h2>
    
    
    
    <p class="wp-block-paragraph">The first NIRSpec fixed-slit <code>x1d</code> file I inspected looked reassuringly familiar. Its <code>EXTRACT1D</code> table had one scalar wavelength and one scalar flux value per row. The complete table represented one extracted spectrum and mapped naturally to a <code>SpectrumBase.SingleSpectrum</code>.</p>
    
    
    
    <p class="wp-block-paragraph">NIRISS wide-field slitless spectroscopy was very different. WFSS observes many sources in the same field without using a slit for each one. In the files I inspected, one FITS table row contained an entire vector of wavelengths and fluxes for one source. One extension could therefore produce many spectra, and the file could contain several <code>EXTRACT1D</code> extensions for different exposures or spectral orders.</p>
    
    
    
    <p class="wp-block-paragraph">NIRISS SOSS introduced another layout. Its spectra represented different spectral orders, with one extracted spectrum in each extension. NIRCam WFSS also produced a collection of extracted spectra. NIRSpec IFU and MIRI MRS began from spectral cubes, but their final <code>x1d</code> products could still contain one extracted 1D spectrum.</p>
    
    
    
    <p class="wp-block-paragraph">The same product suffix was not enough to tell me whether a file represented one spectrum, several orders, or hundreds of sources. The observing mode and the structure of the FITS table mattered.</p>
    
    
    
    <h2 class="wp-block-heading">Building <code>InfraredSpectra.jl</code></h2>
    
    
    
    <p class="wp-block-paragraph">To experiment with these products, I created a separate package called <code>InfraredSpectra.jl</code>. Its initial scope is deliberately limited to extracted JWST <code>x1d</code> and <code>c1d</code> products. Multidimensional products such as <code>cal</code>, <code>s2d</code>, <code>s3d</code>, and <code>i2d</code>, as well as time-series <code>x1dints</code>, remain outside the first version.</p>
    
    
    
    <p class="wp-block-paragraph">The public interface currently looks like this:</p>
    
    
    <div class="wp-block-code">
    <div class="cm-editor">
    <div class="cm-scroller">
    
    <pre>
    <code class="language-julia"><div class="cm-line"><span class="tok-variableName">read_spectrum</span>(<span class="tok-variableName">path</span>)</div><div class="cm-line"><span class="tok-variableName">read_spectra</span>(<span class="tok-variableName">path</span>)</div><div class="cm-line"><span class="tok-variableName">inspect_product</span>(<span class="tok-variableName">path</span>)</div></code></pre>
    </div>
    </div>
    </div>
    
    
    <p class="wp-block-paragraph"><code>read_spectrum</code> requires the file to contain exactly one usable spectrum. If it finds several, it reports how many were found and points the user toward <code>read_spectra</code>. <code>read_spectra</code> always returns a vector, so the same function works for fixed-slit, multi-source, and multi-order products. <code>inspect_product</code> reports the telescope, instrument, observing mode, product type, and HDU structure before the science arrays are fully parsed.</p>
    
    
    
    <p class="wp-block-paragraph">Internally, small <code>X1D</code> and <code>C1D</code> marker types use multiple dispatch to select the correct parser. They are not part of the public interface. Users should only need to ask for one spectrum, all spectra, or a product description.</p>
    
    
    
    <p class="wp-block-paragraph">The returned objects reuse <code>SpectrumBase.SingleSpectrum</code>. Wavelength and flux units from the FITS table are attached without converting the stored values. Uncertainty arrays, DQ values, source IDs, spectral orders, slit information, and extension identity are retained in metadata.</p>
    
    
    
    <h2 class="wp-block-heading"><code>x1d</code> versus <code>c1d</code></h2>
    
    
    
    <p class="wp-block-paragraph">Looking at corresponding <code>x1d</code> and <code>c1d</code> files helped me understand what &#8220;combined&#8221; means in the JWST pipeline.</p>
    
    
    
    <p class="wp-block-paragraph">An <code>x1d</code> product can preserve extracted spectra from separate exposures. A <code>c1d</code> product combines corresponding spectra, but it does not merge unrelated sources or spectral orders. A SOSS observation therefore still contains separate spectra for its different orders after combination.</p>
    
    
    
    <p class="wp-block-paragraph">In one NIRISS WFSS example, the <code>x1d</code> file produced 1,200 usable spectra spread across 12 <code>EXTRACT1D</code> extensions. The related <code>c1d</code> product contained 113 combined source spectra. Seeing those actual outputs made the distinction much clearer than the filenames alone.</p>
    
    
    
    <p class="wp-block-paragraph">For now, <code>read_spectra</code> flattens spectra from all matching extensions into one vector. Each spectrum keeps its source, order, slit, and extension metadata, so the original identity is not discarded. Whether a future API should also offer grouped lookup by source or extension is still something I want to discuss with my mentors.</p>
    
    
    
    <h2 class="wp-block-heading">Testing several observing modes</h2>
    
    
    
    <figure class="wp-block-image size-large"><img alt="" class="wp-image-138" height="544" src="https://jamesraffertylee.wordpress.com/wp-content/uploads/2026/07/image-2.png?w=1024" width="1024" /></figure>
    
    
    
    <p class="wp-block-paragraph">By the end of this exploration, I had tried the loader on extracted products from all four JWST science instruments used in the sample: NIRSpec, NIRISS, NIRCam, and MIRI.</p>
    
    
    
    <p class="wp-block-paragraph">The real-data checks include NIRSpec fixed-slit, IFU, and MSA products; NIRISS WFSS and SOSS; NIRCam WFSS; and MIRI LRS and MRS. These files cover the important table layouts I had encountered: scalar samples per row, complete spectrum vectors per row, one spectrum per extension, many spectra per extension, and several spectral orders.</p>
    
    
    
    <p class="wp-block-paragraph">The ordinary package tests still use small generated FITS tables so they remain portable. The larger real files live outside the repository and are enabled through an environment variable. This gives me both precise unit tests and realistic integration checks without putting large mission datasets directly into the package.</p>

