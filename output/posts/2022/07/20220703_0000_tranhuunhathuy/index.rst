.. title: Third week - Finalizing fitting module after long days of struggling
.. slug:
.. date: 2022-07-03 00:00:00 
.. tags: radis
.. author: TranHuuNhatHuy
.. link: https://https://gsoc2022tranhuunhathuy.gatsbyjs.io/4. third-week/
.. description:
.. category: gsoc2022


.. raw:: html

    <p>To be honest, I started this week realizing I was far behind the deadline. After suffering a traumatizing fever which incapacitated me for one week, I had a fitting module which did not run correctly. Starting this week, the JSON parsing worked normally, but for some reasons the fitting process kept plummeting the <code class="language-text">Tgas</code> value either to very high or very low guesses, always out of the boundaries. What are they trying to seek? I don’t know. So, I have spent this third week trying my best to fix the fitting module and make it run normally:</p>
    <ul>
    <li>At first, I suspected this was a fault in the return of cost function, so I tried either <a href="https://radis.readthedocs.io/en/latest/source/radis.spectrum.compare.html#radis.spectrum.compare.get_diff">get_diff()</a> or <a href="https://radis.readthedocs.io/en/latest/source/radis.spectrum.compare.html#radis.spectrum.compare.get_residual">get_residual()</a>. The fitting process varied between the two approaches, but in the end the plummeting value prevailed.</li>
    <!-- TEASER_END -->
    <li>Then, I thought my synthetic spectra were faulty, so I decided to regenerate and restructure them all over again, and the problem was still there.</li>
    <li>At this time I was still believing that the problem came from the difference between two spectra. So I tried my best to put the generation of two spectra as similar as possible, but still no progress.</li>
    </ul>
    <p>It was around this point that I received some mind-blowing feedbacks from Mr. Erwan Pannier - one of my mentors:</p>
    <blockquote>
    <p>Do not wasting time trying to determine a perfect threshold or categories.</p>
    <p>Work on real-life examples. CO2 4.2 - 5 µm is one.</p>
    <p>CO2 bandhead (the Single Temperature fit example) is another one.</p>
    <p>Works on the improving the fits from these real-life examples,
    and - maybe - you’ll generalize to categories/classifications eventually.</p>
    </blockquote>
    <p>At some point, I tried to use <a href="https://radis.readthedocs.io/en/latest/source/radis.spectrum.spectrum.html#radis.spectrum.spectrum.Spectrum.normalize">normalize()</a>. My idea is, since my current fitting target is temperature, the experimental and model spectra can be both normalized, as the spectrum lineshape is determined by the component temperatures. After normalizing, things worked perfectly out of my expectation!</p>
    <p>And so, after one week of pure suffering and perseverance, I have finished the fitting module! So, there are 3 important parts of my fitting feature:</p>
    <h3>1. Input JSON file</h3>
    <p>A JSON file containing every information, from path to experimental spectrum file, to initial conditions - known parameters that will be used for calculating model spectra, and fit parameter(s) are also stated here. For example:</p>
    <div class="gatsby-highlight"><pre class="language-json"><code class="language-json"><span class="token punctuation">{</span>
    <span class="token property">"fileName"</span><span class="token operator">:</span> <span class="token string">"CO2_measured_spectrum_4-5um.spec"</span><span class="token punctuation">,</span>
    <span class="token property">"molecule"</span><span class="token operator">:</span> <span class="token string">"CO2"</span><span class="token punctuation">,</span>
    <span class="token property">"isotope"</span><span class="token operator">:</span> <span class="token string">"1,2"</span><span class="token punctuation">,</span>
    <span class="token property">"wmin"</span><span class="token operator">:</span> <span class="token number">4167</span><span class="token punctuation">,</span>
    <span class="token property">"wmax"</span><span class="token operator">:</span> <span class="token number">4180</span><span class="token punctuation">,</span>
    <span class="token property">"wunit"</span><span class="token operator">:</span> <span class="token string">"nm"</span><span class="token punctuation">,</span>
    <span class="token property">"pressure"</span><span class="token operator">:</span> <span class="token number">1e-3</span><span class="token punctuation">,</span>
    <span class="token property">"mole_fraction"</span><span class="token operator">:</span> <span class="token number">1</span><span class="token punctuation">,</span>
    <span class="token property">"path_length"</span><span class="token operator">:</span> <span class="token number">10</span><span class="token punctuation">,</span>
    <span class="token property">"slit"</span><span class="token operator">:</span> <span class="token string">"1.4 nm"</span><span class="token punctuation">,</span>
    <span class="token property">"fit"</span><span class="token operator">:</span> <span class="token punctuation">{</span>
    <span class="token property">"Tgas"</span><span class="token operator">:</span> <span class="token number">1100</span><span class="token punctuation">,</span>
    <span class="token property">"bound_Tgas"</span><span class="token operator">:</span> <span class="token punctuation">[</span><span class="token number">300</span><span class="token punctuation">,</span> <span class="token number">2000</span><span class="token punctuation">]</span>
    <span class="token punctuation">}</span>
    <span class="token punctuation">}</span></code></pre></div>
    <p>As you can see from the JSON file above:</p>
    <ul>
    <li><code class="language-text">fileName</code> : path to the <code class="language-text">.spec</code> spectrum file from <code class="language-text">./data/</code>, will be changed when implementing to RADIS codebase. For now the format is <code class="language-text">&lt;spectrum-type>/spectrum/&lt;name>.spec</code>. For example: <code class="language-text">large/spectrum/CO2_measured_spectrum_4-5um.spec</code>.</li>
    <li>Parameters from <code class="language-text">molecule</code> to <code class="language-text">slit</code> are used for calculating model spectrum later. <code class="language-text">wmin</code> and <code class="language-text">wmax</code> are used to determine the range of wavelength/wavenumber that will be cropped from original experimental spectrum.</li>
    <li><code class="language-text">fit</code> section contains fit parameters and their corresponding initial values or fitting bounds. In the example above, fit parameter <code class="language-text">Tgas</code> has initial value of 1100 and fitting bound [300, 2000].</li>
    </ul>
    <h3>2. Fitting module <code class="language-text">fitting_module.py</code></h3>
    <p>Contains functions to load JSON file <code class="language-text">get_JSON()</code> and most importantly, <code class="language-text">fit_spectrum()</code> which receives only path of JSON file as input parameter, and will do all the fitting work for you.</p>
    <p>Firstly, when being called, <code class="language-text">fit_spectrum()</code> will call and parse the input path to <code class="language-text">get_JSON()</code> which reads necessary information from the JSON file. These information are returned to <code class="language-text">fit_spectrum()</code>, which will try to retrieve experimental data. Then, it crops, normalizes, removes NaN values, and some other refinements. Next, the read information and refined experimental spectrum will be sent to fitting models for the fitting process, which is described below.</p>
    <h3>3. Fitting models <code class="language-text">model_LTE.py</code> and <code class="language-text">model_nonLTE.py</code></h3>
    <p>These 2 files contain <code class="language-text">residual_LTE()</code> - for LTE spectra, and <code class="language-text">residual_NonLTE()</code> - for non-LTE spectra (I haven’t developed this yet, will be done this week according to timeline), respectively. These functions receives refined experimental spectrum and initial conditions read from JSON file before, then calculate model spectrum, refine it, and return the residual/difference/cost between 2 spectra.</p>
    <h3>4. Initial result when fitting <code class="language-text">CO2_measured_spectrum_4-5um.spec</code></h3>
    <p>I tried to recreate the same fitting scenario as <a href="https://radis.readthedocs.io/en/latest/auto_examples/plot_1T_fit.html#sphx-glr-auto-examples-plot-1t-fit-py">1-temp fit example</a>. The result of my module seems promising, with only 17 iterations compared to 32 iterations in the example.</p>
    <div class="gatsby-highlight"><pre class="language-text"><code class="language-text">Succesfully finished the fitting process in 7.901483058929443s.
    [[Fit Statistics]]
    # fitting method   = leastsq
    # function evals   = 17
    # data points      = 1
    # variables        = 1
    chi-square         = 7.4524e-06
    reduced chi-square = 7.4524e-06
    Akaike info crit   = -9.80697750
    Bayesian info crit = -11.8069775
    [[Variables]]
    Tgas:  1459.11902 +/- 26872889.5 (1841720.19%) (init = 1100)
    e:\radis\radis\misc\warning.py:354: HighTemperatureWarning: HITRAN is valid for low temperatures (typically &lt; 700 K). For higher temperatures you may need HITEMP or CDSD. See the 'databank=' parameter
    warnings.warn(WarningType(message))
    e:\radis\radis\misc\curve.py:241: UserWarning: Presence of NaN in curve_divide!
    Think about interpolation=2
    warnings.warn(</code></pre></div>
    <p><span class="gatsby-resp-image-wrapper" style="display: block; margin-left: auto; margin-right: auto;">
    <a class="gatsby-resp-image-link" href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/c1ca7b795588d0c7ddc1076fc8fce6b8/9e818/fitting_result.png" rel="noopener" style="display: block;" target="_blank">
    <span class="gatsby-resp-image-background-image" style="display: block;"></span>
    <img alt="Comparison between normalized experimental spectrum and best fitted spectrum" class="gatsby-resp-image-image" src="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/c1ca7b795588d0c7ddc1076fc8fce6b8/f058b/fitting_result.png" style="width: 100%; height: 100%; margin: 0; vertical-align: middle;" title="Comparison between normalized experimental spectrum and best fitted spectrum" />
    </a>
    </span></p>
    <h3>5. RADIS fitting process from user perspective in the future</h3>
    <p>If being implemented, this fitting pipeline will benefit RADIS users, especially new users, in the future. Imagine you have a spectrum to be fitted. All you need to do next, is to fill the information into a JSON form, and then call <code class="language-text">fit_spectrum(&lt;path-to-JSON-file>)</code> and let it do all the work. If you are not satisfied with the result, you can change the unknown information in the JSON, such as <code class="language-text">slit</code> and <code class="language-text">path_length</code>, and recall the function again, until you are satisfied.</p>
    <p>This is way easier and much friendlier for RADIS users than dwelling into RADIS documentation to find out and learn how to use existing fitting pipeline.</p>
    <p>For now, this user interface only allows LTE spectra to be fitted. But in the following weeks, more types will be implemented and covered along with results from benchmarking progress.</p>

