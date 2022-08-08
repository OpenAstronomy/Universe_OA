.. title: Second week - Development of new fitting module
.. slug:
.. date: 2022-06-26 00:00:00 
.. tags: radis
.. author: TranHuuNhatHuy
.. link: https://https://gsoc2022tranhuunhathuy.gatsbyjs.io/3. second-week/
.. description:
.. category: gsoc2022


.. raw:: html

    <p>According to the project proposal, during the second week I am supposed to start the benchmarking process with a bunch of large-category synthentic spectra. Thus, I started to generate a bunch of large synthetic spectra.</p>
    <p>Firstly, I create a <a href="https://github.com/TranHuuNhatHuy/RADIS-Spectrum-Fitting-Benchmark/blob/main/data/synthetic_spectrum_generator.py">synthetic spectrum generator</a>. This module is to synthesize various spectra for the benchmarking process based on 4 groups:</p>
    <ul>
    <!-- TEASER_END -->
    <li>Large and LTE spectra.</li>
    <li>Large and non-LTE spectra.</li>
    <li>Narrow and LTE spectra.</li>
    <li>Narrow and non-LTE spectra.</li>
    </ul>
    <p>Generated spectra are stored in <code class="language-text">./data/&lt;spectrum-type>/spectrum</code> in RADIS .spec file, while their corresponding ground-truths are stored in <code class="language-text">./data/&lt;spectrum-type>/ground-truth</code> in JSON format. For each spectrum type, after acquiring most stable fitting pipeline, the model, the algorithm and other specific settings will be stored as a model file in <code class="language-text">./fitting-module/&lt;spectrum-type>/model.py</code>.</p>
    <p>For example, I want to generate a synthetic LTE spectrum whose ground-truth as:</p>
    <ul>
    <li>Molecule: CO2.</li>
    <li>HITRAN isotope ID: 1 (12C16O2).</li>
    <li>Wavelength range: from 3300 cm-1 to 3700 cm-1.</li>
    <li>Pressure: 0.005 bar.</li>
    <li>Tgas: 3000 C.</li>
    <li>Mole fraction: 0.01</li>
    <li>Path length: 1 cm.</li>
    <li>Experimental slit: 1.4 mm.</li>
    </ul>
    <p>Then, the JSON generated and registered for this spectrum is going to be like this:</p>
    <div class="gatsby-highlight"><pre class="language-json"><code class="language-json"><span class="token punctuation">{</span>
    <span class="token property">"fileName"</span><span class="token operator">:</span> <span class="token string">"synth-CO2-1-3300-3700-cm-1-P0.005-t3000-v-r-mf0.01-p1-sl1.4nm.spec"</span><span class="token punctuation">,</span>
    <span class="token property">"molecule"</span><span class="token operator">:</span> <span class="token string">"CO2"</span><span class="token punctuation">,</span>
    <span class="token property">"isotope"</span><span class="token operator">:</span> <span class="token string">"1"</span><span class="token punctuation">,</span>
    <span class="token property">"wmin"</span><span class="token operator">:</span> <span class="token number">3300</span><span class="token punctuation">,</span>
    <span class="token property">"wmax"</span><span class="token operator">:</span> <span class="token number">3700</span><span class="token punctuation">,</span>
    <span class="token property">"wunit"</span><span class="token operator">:</span> <span class="token string">"cm-1"</span><span class="token punctuation">,</span>
    <span class="token property">"pressure"</span><span class="token operator">:</span> <span class="token number">0.005</span><span class="token punctuation">,</span>
    <span class="token property">"mole_fraction"</span><span class="token operator">:</span> <span class="token number">0.01</span><span class="token punctuation">,</span>
    <span class="token property">"path_length"</span><span class="token operator">:</span> <span class="token number">1</span><span class="token punctuation">,</span>
    <span class="token property">"slit"</span><span class="token operator">:</span> <span class="token string">"1.4 nm"</span><span class="token punctuation">,</span>
    <span class="token property">"fit"</span><span class="token operator">:</span> <span class="token punctuation">{</span>
    <span class="token property">"Tgas"</span><span class="token operator">:</span> <span class="token number">3000</span><span class="token punctuation">,</span>
    <span class="token property">"bound_Tgas"</span><span class="token operator">:</span> <span class="token punctuation">[</span>
    <span class="token number">2500</span><span class="token punctuation">,</span>
    <span class="token number">4000</span>
    <span class="token punctuation">]</span>
    <span class="token punctuation">}</span>
    <span class="token punctuation">}</span></code></pre></div>
    <p>As you can see, the <code class="language-text">fileName</code> specifies <code class="language-text">.spec</code> file - the file which stores our experimental spectrum - in the data directory. Other parameters can be seen above. For the <code class="language-text">fit</code> group, it contains fit parameters, initial fitting value, and the fitting boundaries. For example, in the JSON file above, we fit the <code class="language-text">Tgas</code> parameter whose initial value is 3000 C, upper bound and lower bound are 2500 C and 4000 C respectively.</p>
    <p>Then, for the given initial conditions, and initial <code class="language-text">Tgas</code> value, we have this RADIS-calculated spectrum:</p>
    <p><span class="gatsby-resp-image-wrapper" style="display: block; margin-left: auto; margin-right: auto;">
    <a class="gatsby-resp-image-link" href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/0e9b5a48c6d76f32655c5fd59aa8797d/42de8/calculated.png" rel="noopener" style="display: block;" target="_blank">
    <span class="gatsby-resp-image-background-image" style="display: block;"></span>
    <img alt="Calculated-from-ground-truth spectrum" class="gatsby-resp-image-image" src="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/0e9b5a48c6d76f32655c5fd59aa8797d/f058b/calculated.png" style="width: 100%; height: 100%; margin: 0; vertical-align: middle;" title="Calculated-from-ground-truth spectrum" />
    </a>
    </span></p>
    <p>To make it look like an experimental one, after applying slit and around 0.2 mm of offset, noises will be added with scale at 1% of max radiance value.</p>
    <div class="gatsby-highlight"><pre class="language-python"><code class="language-python">s_wav<span class="token punctuation">,</span> s_val <span class="token operator">=</span> s<span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string">'radiance'</span><span class="token punctuation">)</span>
    noise_scale <span class="token operator">=</span> <span class="token builtin">max</span><span class="token punctuation">(</span><span class="token punctuation">[</span>val <span class="token keyword">for</span> val <span class="token keyword">in</span> s_val <span class="token keyword">if</span> <span class="token keyword">not</span><span class="token punctuation">(</span>math<span class="token punctuation">.</span>isnan<span class="token punctuation">(</span>val<span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">]</span><span class="token punctuation">)</span> <span class="token operator">*</span> <span class="token number">0.005</span> <span class="token comment"># Prevent NaN</span>
    s_val <span class="token operator">+=</span> np<span class="token punctuation">.</span>random<span class="token punctuation">.</span>normal<span class="token punctuation">(</span>size <span class="token operator">=</span> s_val<span class="token punctuation">.</span>size<span class="token punctuation">,</span> scale <span class="token operator">=</span> noise_scale<span class="token punctuation">)</span></code></pre></div>
    <p>Then, I reproduce dilatation by applying non-linear transformation, with scale 0.66% of deviation.</p>
    <div class="gatsby-highlight"><pre class="language-python"><code class="language-python">wav_mean <span class="token operator">=</span> np<span class="token punctuation">.</span>mean<span class="token punctuation">(</span><span class="token punctuation">[</span>wav <span class="token keyword">for</span> wav <span class="token keyword">in</span> s_wav <span class="token keyword">if</span> <span class="token keyword">not</span><span class="token punctuation">(</span>math<span class="token punctuation">.</span>isnan<span class="token punctuation">(</span>wav<span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">]</span><span class="token punctuation">)</span>
    s_wav <span class="token operator">=</span> wav_mean <span class="token operator">+</span> <span class="token punctuation">(</span>s_wav <span class="token operator">-</span> wav_mean<span class="token punctuation">)</span> <span class="token operator">*</span> <span class="token number">1.0066</span></code></pre></div>
    <p>Finally, the noise-added spectrum will be save as .spec file and its information will be stored as formatted JSON structure. The noise-added spectrum is like this:</p>
    <p><span class="gatsby-resp-image-wrapper" style="display: block; margin-left: auto; margin-right: auto;">
    <a class="gatsby-resp-image-link" href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/fa599fd0903315d279158c0ca38a6a5b/20751/noise-added.png" rel="noopener" style="display: block;" target="_blank">
    <span class="gatsby-resp-image-background-image" style="display: block;"></span>
    <img alt="Final product of generated synthetic spectrum" class="gatsby-resp-image-image" src="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/fa599fd0903315d279158c0ca38a6a5b/f058b/noise-added.png" style="width: 100%; height: 100%; margin: 0; vertical-align: middle;" title="Final product of generated synthetic spectrum" />
    </a>
    </span></p>
    <p>We can see the difference between these two spectra using <code class="language-text">plot_diff()</code>:</p>
    <p><span class="gatsby-resp-image-wrapper" style="display: block; margin-left: auto; margin-right: auto;">
    <a class="gatsby-resp-image-link" href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/51e2569008c18f1a2d54223ad885b2c8/5f7fb/compare.png" rel="noopener" style="display: block;" target="_blank">
    <span class="gatsby-resp-image-background-image" style="display: block;"></span>
    <img alt="Difference result between two spectra. As you can see, the synth spectrum features both noise and dilatation effects." class="gatsby-resp-image-image" src="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/51e2569008c18f1a2d54223ad885b2c8/f058b/compare.png" style="width: 100%; height: 100%; margin: 0; vertical-align: middle;" title="Difference result between two spectra. As you can see, the synth spectrum features both noise and dilatation effects." />
    </a>
    </span></p>
    <p>These files will later be used for benchmarking process to test multiple fitting pipelines, and more files will definitely be added later.</p>
    <p>About the fitting module, now I am still stuck with the development of it. The development seems harder and requires more time than I expected. I will try my best to keep up with the deadlines.</p>

