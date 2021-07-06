.. title: Chapter 2: Survey Corps
.. slug:
.. date: 2021-07-05 23:40:32 
.. tags: radis
.. author: anandxkumar
.. link: https://anandkumar-blog.netlify.app/3/
.. description:
.. category: gsoc2021


.. raw:: html

    <p>So its been around 4 weeks into the coding period, a lot of insights and progress so far!</p>
    <h2>Profiler Class</h2>
    <p>The good news is that the Profiler class has been successfully implemented in the develop branch and will be available to users by version <code class="language-text">0.9.30</code> .<br />
    <!-- TEASER_END -->
    Link : <a href="https://github.com/radis/radis/pull/286">Profiler PR</a><br /></p>
    <p>Below is a simple example how all steps are printed based on the verbose level:<br /></p>
    <div class="gatsby-highlight"><pre class="language-text"><code class="language-text">wmin = 2000
    wmax = 3300
    wstep = 0.01
    T = 3000.0 #K
    p = 0.1 #bar
    broadening_max_width=10
    
    sf = SpectrumFactory(wavenum_min=wmin, wavenum_max=wmax,
    pressure=p,
    wstep=wstep,
    broadening_max_width=broadening_max_width,
    molecule=&quot;CO&quot;,
    cutoff=0, # 1e-27,
    verbose=3,
    )
    sf.load_databank('HITEMP-CO')
    s = sf.eq_spectrum(T)</code></pre></div>
    <p>Output:</p>
    <div class="gatsby-highlight"><pre class="language-text"><code class="language-text">... Scaling equilibrium linestrength
    ... 0.01s - Scaled equilibrium linestrength
    ... 0.00s - Calculated lineshift
    ... 0.00s - Calculate broadening HWHM
    ... Calculating line broadening (60869 lines: expect ~ 6.09s on 1 CPU)
    ...... 0.16s - Precomputed DLM lineshapes (30)
    ...... 0.00s - Initialized vectors
    ...... 0.00s - Get closest matching line &amp; fraction
    ...... 0.02s - Distribute lines over DLM
    ...... 1.95s - Convolve and sum on spectral range
    ... 2.14s - Calculated line broadening
    ... 0.01s - Calculated other spectral quantities
    ... 2.21s - Spectrum calculated (before object generation)
    ... 0.01s - Generated Spectrum object
    2.22s - Spectrum calculated</code></pre></div>
    <p>Also we can access these steps and the time taken by them using <code class="language-text">Spectrum.get_conditions()['profiler']</code>. Also there is a parameter <code class="language-text">SpectrumFactory.profiler.relative_time_percentage</code> that stores the percentage of time taken by each steps at a particular verbose level, helpful seeing the most expensive steps in Spectrum calculation.<br /></p>
    <h2>Legacy Method Complexity</h2>
    <p>Several Spectrums were benchmarked against various parameters to see it’s correlation and derive its complexity. We used Profiler class with <a href="https://radis.readthedocs.io/en/latest/source/radis.lbl.loader.html#radis.lbl.loader.DatabankLoader.init_database">init_database()</a> which stores all parameters of Spectrum along the Profiler in a <code class="language-text">csv</code> generated file; all spectrum info got added into the csv file  which could be used to do create visualizations to analyze the data. We used <code class="language-text">Xexplorer</code> library and <code class="language-text">Tableau</code>(a visual analytics platform) to create visualizations. A <a href="https://github.com/anandxkumar/Benchmark_Visualization_GSoC_2021">github repository</a> was created to store the Visualization along the CSV data file of each benchmark.</p>
    <p>Following are the inference of the benchmarks for Legacy Method:</p>
    <b>
    •  Calculation Time ∝ Number of lines<br />
    •  Calculation Time ∝ Broadening max width<br />
    •  Calculation Time ∝ 1/wstep<br />
    •  Calculation Time not dependent on Spectral Range<br />
    </b><br />
    <p>So complexity of Legacy method can be derived as: <br />
    <strong><code class="language-text">complexity = constant * Number of lines * Broadening Max Width / Wstep</code></strong> <br /></p>
    <h2>LDM Method Complexity</h2>
    <p>Similar technique was used to benchmark LDM method. Now LDM uses 2 types of broadening method that are <code class="language-text">voigt</code> and <code class="language-text">fft</code>. <code class="language-text">voigt</code> uses truncation for calculating spectrum  in wavenmber space where as <code class="language-text">fft</code> calculates spectrum on entire spectral range in fourier space. So benchmarks were done on both methods to compare their performance against various parameters.</p>
    <p>Spectrum were benchmarked against parameters like Spectral Range, Wstep, Spectral Points, Number of Lines and Broadening Max Width. Following are the inferences.</p>
    <p>For <code class="language-text">fft</code>:<br />
    <b>
    • Calculation Time ∝ Spectral Points<br />
    • Calculation Time ∝ Number of Lines<br />
    </b></p>
    <p>For <code class="language-text">voigt</code>:<br />
    <b>
    • Calculation Time ∝ Spectral Points<br />
    • Calculation Time ∝ Number of Lines<br />
    • Calculation Time ∝ Broadening Max Width<br />
    </b></p>
    <p>For LDM we are expecting the following complexity:<br />
    <strong><code class="language-text">t_LDM_fft ~ c2*N_lines + c3*(N_G*N_L + 1)*N_v*log(N_v)</code></strong><br />
    <strong><code class="language-text">t_LDM_voigt ~ c2*N_lines + c3'*(N_G*N_L + 1)*N_truncation*log(N_truncation)</code></strong><br /></p>
    <p> So the goal for the next 2 weeks will be to get the complexity of both <code class="language-text">voigt</code> and <code class="language-text">fft</code> method and see places for improving both methods and quite possibily create a <code class="language-text">Hybrid</code> method taking the best of both worlds. </p>

