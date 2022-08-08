.. title: First week - Spectra gazing and initial ideas for fitting module
.. slug:
.. date: 2022-06-19 00:00:00 
.. tags: radis
.. author: TranHuuNhatHuy
.. link: https://https://gsoc2022tranhuunhathuy.gatsbyjs.io/2. first-week/
.. description:
.. category: gsoc2022


.. raw:: html

    <p>So, according to the plan, in the first week I am supposed to finish these tasks:</p>
    <ul>
    <li>Setup a dedicated repository for reference database. Upload gathered spectra labelled with ground truths onto the database.</li>
    <!-- TEASER_END -->
    <li>Investigate and understand each spectra type’s nature, identification and complexity, under instructions of mentors.</li>
    <li>Prepare LMFIT modules for benchmarking process.</li>
    </ul>
    <p>First is about a dedicated repository for reference database. Since my project is about creating a brand-new feature for RADIS users instead of making changes in RADIS codebase to increase its performance of already-implemented features, I have to do all of my work in a separated repository, before committing to the main codebase upon mentor’s approval. Thus, I have created <a href="https://github.com/TranHuuNhatHuy/RADIS-Spectrum-Fitting-Benchmark">RADIS Spectrum Fitting Benchmark repository</a> specifically built for benchmarking process of RADIS spectrum fitting. This repository contains the spectra library with their curresponding ground-truths, as well as fitting modules and benchmarking results.</p>
    <p>The next step is to gain more knowledge and understanding regarding the spectrum types, and nature of each of them. So basically, now I’m expected to conduct extensive benchmarking process on 4 spectrum types and find now which pipeline fits best on which spectrum type. For now, the classification of spectrum is:</p>
    <ol>
    <li>Large spectra: spectra containing a lot of data points, maybe because there are too many lines that fill up the RAM capacity during spectrum calculation, or because spectrum’s coverage on large wavelength/wavenumber ranges (which also means “wide” spectra), leading to various empty spaces that can be optimized. Either way, the calculation step of these spectra is extensively heavy, both in time and memory required.</li>
    </ol>
    <p><span class="gatsby-resp-image-wrapper" style="display: block; margin-left: auto; margin-right: auto;">
    <a class="gatsby-resp-image-link" href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/daa4fbddc9721f104f2c6c55dd426484/73b94/large.png" rel="noopener" style="display: block;" target="_blank">
    <span class="gatsby-resp-image-background-image" style="display: block;"></span>
    <img alt="A large spectrum of CO2, retrieved from RADIS app. We can see the result as an extensive accumulation of lines." class="gatsby-resp-image-image" src="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/daa4fbddc9721f104f2c6c55dd426484/f058b/large.png" style="width: 100%; height: 100%; margin: 0; vertical-align: middle;" title="A large spectrum of CO2, retrieved from RADIS app. We can see the result as an extensive accumulation of lines." />
    </a>
    </span></p>
    <ol start="2">
    <li>Narrow spectra: spectra containing small amount of data points, in which lineshape can be line-wise calculated without the need of extensive collissional broadening.</li>
    </ol>
    <p><span class="gatsby-resp-image-wrapper" style="display: block; margin-left: auto; margin-right: auto;">
    <a class="gatsby-resp-image-link" href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/9a0d9b2b3ffb891b1483094c89083659/58bb7/small.png" rel="noopener" style="display: block;" target="_blank">
    <span class="gatsby-resp-image-background-image" style="display: block;"></span>
    <img alt="A small spectrum of H2O, retrieved from RADIS app. We can see very few lines, the rest is broadening result." class="gatsby-resp-image-image" src="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/9a0d9b2b3ffb891b1483094c89083659/f058b/small.png" style="width: 100%; height: 100%; margin: 0; vertical-align: middle;" title="A small spectrum of H2O, retrieved from RADIS app. We can see very few lines, the rest is broadening result." />
    </a>
    </span></p>
    <ol start="3">
    <li>LTE spectra: spectra featuring only gas temperature <em>Tgas</em>, basically the major type of spectrum usually encountered throughout multiple experiments. This type of spectrum can be derived using RADIS’s equilibrium claculation.</li>
    <li>Non-LTE spectra: spectra featuring multiple temperatures, not only gas temperature <em>Tgas</em> but also vibrational temperature <em>Tvib</em> and rotational temperature <em>Trot</em>. RADIS’s non-equilibrium calculation is required to calculate these spectra.</li>
    </ol>
    <p>In this project, I am expected to optimize these 4 types of spectrum. There are several optimization ideas that can be utilized and developed upon:</p>
    <ol>
    <li>For large spectra: as this type of spectrum has significant burden in the model calculation, a lot of rooms for improvement can be found in this process. For this, we can try to reduce the solution of experimental and model spectra for shorter calculation time, or we can even normalize them, since lineshape heavily relies on temperature components.</li>
    <li>For small spectra: as this type of spectrum has few data points, while the calculation process is very fast, the burden one is actually spectrum generation phase. Visualization of spectrum is convenient for human, but not for machine and the cost function. So, we can by-pass this spectrum generation process and just only focus on the calculation side.</li>
    <li>For LTE and Non-LTE spectra, the difference is all about the number of fitting parameters, and the choice of fitting users regarding fitting boundaries and dependencies. We can flexibly adapt these kinds of fitting pipelines.</li>
    </ol>
    <p>Finally is the tentative format for my brand-new fitting module. Have been in this spectroscopy community for months, I notice a lot of times newcomers arrive and get confused at the RADIS installation and its codebase. To add up, current <a href="https://radis.readthedocs.io/en/latest/auto_examples/plot_1T_fit.html">RADIS fitting example</a> is quite challenging, especially for new users of RADIS.</p>
    <p>So, when designing new fitting feature from the perspective of user experience, I want to make a user-friendly interface that can benefit both. Thus, my idea is a fitting module that:</p>
    <ul>
    <li>Users only need to fill the fitting conditions and parameteres into something like a JSON file, along with a <em>.spec</em> Spectrum file containing the experimental spectrum to be fitted. Basically, a JSON file is going to be like this:</li>
    </ul>
    <div class="gatsby-highlight"><pre class="language-json"><code class="language-json"><span class="token punctuation">{</span>
    <span class="token property">"fileName"</span><span class="token operator">:</span> <span class="token string">"CO2-1-1900-2300-cm-1.01325-t300-v300-r300-p1-sl0.5nm.spec"</span><span class="token punctuation">,</span>
    <span class="token property">"molecule"</span><span class="token operator">:</span> <span class="token string">"CO2"</span><span class="token punctuation">,</span>
    <span class="token property">"isotope"</span><span class="token operator">:</span> <span class="token string">"1"</span><span class="token punctuation">,</span>
    <span class="token property">"from_wavelength"</span><span class="token operator">:</span> <span class="token number">1900</span><span class="token punctuation">,</span>
    <span class="token property">"to_wavelength"</span><span class="token operator">:</span> <span class="token number">2300</span><span class="token punctuation">,</span>
    <span class="token property">"pressure"</span><span class="token operator">:</span> <span class="token number">1.01325</span><span class="token punctuation">,</span>
    <span class="token property">"mole_fraction"</span><span class="token operator">:</span> <span class="token number">0.1</span><span class="token punctuation">,</span>
    <span class="token property">"path_length"</span><span class="token operator">:</span> <span class="token number">1</span><span class="token punctuation">,</span>
    <span class="token property">"slit"</span><span class="token operator">:</span> <span class="token string">"0.5 nm"</span><span class="token punctuation">,</span>
    <span class="token property">"fit"</span><span class="token operator">:</span> <span class="token punctuation">{</span>
    <span class="token property">"Tgas"</span><span class="token operator">:</span> <span class="token number">300</span><span class="token punctuation">,</span>
    <span class="token property">"Tvib"</span><span class="token operator">:</span> <span class="token number">300</span><span class="token punctuation">,</span>
    <span class="token property">"Trot"</span><span class="token operator">:</span> <span class="token number">300</span><span class="token punctuation">,</span>
    <span class="token punctuation">}</span>
    <span class="token punctuation">}</span></code></pre></div>
    <ul>
    <li>The fitting module will read the JSON file and acquire the information, while loading the experimental spectrum.</li>
    <li>The whole fitting process is automatically conducted. Everything users need to do, is to fill out a JSON form, and prepare an experimental file. This is much more user-friendly instead of the above fitting example, where users have to manually define the model, refine experimental spectrum and other things.</li>
    </ul>
    <p>With all of this, I really hope to bring forth a brand-new fitting experience for RADIS users. Ambitions are set, now sit tight, and start coding!</p>

