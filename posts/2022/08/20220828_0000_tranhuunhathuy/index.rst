.. title: Week 9, 10 and 11 - The challenge, the calamity, the hope, and the salvation.
.. slug:
.. date: 2022-08-28 00:00:00 
.. tags: radis
.. author: TranHuuNhatHuy
.. link: https://https://gsoc2022tranhuunhathuy.gatsbyjs.io/9. week 9-10/
.. description:
.. category: gsoc2022


.. raw:: html

    <h3>1. The challenge</h3>
    <p>After successfully dealing with Mr. Minou’s case, I got a message from another RADIS spectroscopic scientist - Mr. Corentin Grimaldi, a Ph.D. candidate of CentraleSupélec, Paris. He had several experimental spectra containing CO and CO2 at different temperatures and possibly in non-equillibrium. There were 3 spectra in total, and he also provided 3 Python scripts he used to fit them:</p>
    <ul>
    <!-- TEASER_END -->
    <li><code class="language-text">Fit_init_V2.py</code> : the script for fitting initialization, which conducts all the basic functions such as normalization, crop, slit convolution &#x26; dispersion, residual calculation, etc.</li>
    <li><code class="language-text">Optimize_find_min_2D_V2.py</code> : the program that looks for optimum parameters such as <code class="language-text">Trot</code>, <code class="language-text">Tvib</code>, <code class="language-text">molfrac</code>, etc.</li>
    <li><code class="language-text">fit_CO_1T_CO2_2T_cv_V2.py</code> :  the master program that conducts main fitting job.</li>
    </ul>
    <p>So there is one thing that I need to mention first: these spectra are quite challenging to fit. Not hard, but challenging. Both CO2 and CO overlap in this spectral region, and a lot of parameters are unknown: <code class="language-text">Trot</code>, <code class="language-text">Tvib</code>, <code class="language-text">x_CO</code> for CO and <code class="language-text">Trot</code>, <code class="language-text">Tvib1</code>, <code class="language-text">Tvib2</code>, <code class="language-text">Tvib3</code>, <code class="language-text">x_CO2</code> for CO2. Furthermore, unfortunately some cold CO2 and H2O absorb the incomming radiance and the mole fraction is also unknown, too. So basically, there are a lot of fit parameters we need to find, and they don’t really follow the normal spectrum calculation that RADIS offers.</p>
    <p>Although Mr. Corentin provided a fitting pipeline for these cases, I still kinda doubt whether should I implement his very specific and exotic approach to my unified modules. After experiencing a lot of fitting scripts from various users in the community, I feel like although I can implement a common interface to support most of fitting cases, but definitely not all of them, since each experimental spectrum is suitable for a unique workflow. Mr. Corentin’s case and approach is just somewhat way too unique and completely different from mine. So basically, his approach is quite difficult to be generalized and implemented into a module aimed to serve general fitting cases.</p>
    <h3>2. The calamity</h3>
    <p>After spending the whole week 9 finding a solution for Mr. Corentin’s cases, at the beginning of week 10, all of sudden my MSI laptop - the 6-year buddy always accompanies me to all the coding contests and evreything - stopped working. The next day, the iPhone 11 I bought this February had its screen flickered intensively and thus unable to use. Within less than 48 hours, I, one of GSoC contributor, was cut off from the modern life! All the following days were desperate efforts trying to get my stuffs fixed but nothing worked, trying to communicate with the mentors, trying not to miss any important emails and news. Amidst the challenging second phase of GSoC, I was rendered useless for one week straight! I shudder recalling it, those dark and desperate days sitting in Japanese internet cafes to access the Internet, while extremely anxious about a future of failing GSoC.</p>
    <h3>3. The hope</h3>
    <p>After one week of despair, my new Macbook Air M1 finally arrived!</p>
    <p><span class="gatsby-resp-image-wrapper" style="display: block; margin-left: auto; margin-right: auto;">
    <a class="gatsby-resp-image-link" href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/235c694787085f9f7595ef9772eb4744/0f98f/new_Mac.jpg" rel="noopener" style="display: block;" target="_blank">
    <span class="gatsby-resp-image-background-image" style="display: block;"></span>
    <img alt="My new buddy!" class="gatsby-resp-image-image" src="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/235c694787085f9f7595ef9772eb4744/828fb/new_Mac.jpg" style="width: 100%; height: 100%; margin: 0; vertical-align: middle;" title="My new buddy!" />
    </a>
    </span></p>
    <p>Finally days and nights in extreme anxious of being unable to do anything while seeing my friends committing and pushing onto GitHub, have finally gone! Now I have my new Mac (with an exorbitant cost as Japanese Yen is dropping like my mental condition recently), and within the remaining days until the final evaluation, I will rush my best with all I have to deliver my module!</p>
    <h3>4. The salvation</h3>
    <p>After a long time of struggling, I finally received new experimental spectra from Mr. Corentin. He finally realized that those old cases were just too complicated, and now we have 4 simpler tests case with only CO, in the spectral range of 2000 nm to 2600 nm, non-equillibrium, not really absorbed:</p>
    <ol>
    <li>
    <p><a href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/0_100cm%20Down%20Sampled%20-%2010cm_10pctCO2_1-wc-gw450-gr300-sl1500-acc5000-.spec">0_100cm%20Down%20Sampled%20-%2010cm_10pctCO2_1-wc-gw450-gr300-sl1500-acc5000-.spec</a></p>
    </li>
    <li>
    <p><a href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/0_100cm%20Down%20Sampled%20-%2020cm_10pctCO2_1-wc-gw450-gr300-sl1500-acc5000-.spec">0_100cm%20Down%20Sampled%20-%2020cm_10pctCO2_1-wc-gw450-gr300-sl1500-acc5000-.spec</a></p>
    </li>
    <li>
    <p><a href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/0_200cm%20Down%20Sampled%20-%2035cm_10pctCO2_1-wc-gw450-gr300-sl1500-acc5000-.spec">0_200cm%20Down%20Sampled%20-%2035cm_10pctCO2_1-wc-gw450-gr300-sl1500-acc5000-.spec</a></p>
    </li>
    <li>
    <p><a href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/0_300cm%20Down%20Sampled%20-%2010cm_10pctCO2_1-wc-gw450-gr300-sl1500-acc5000-.spec">0_300cm%20Down%20Sampled%20-%2010cm_10pctCO2_1-wc-gw450-gr300-sl1500-acc5000-.spec</a></p>
    </li>
    </ol>
    <p>Also, in these cases Mr. Corentin introduced a complex slit settings like this:</p>
    <div class="gatsby-highlight"><pre class="language-python"><code class="language-python"><span class="token keyword">def</span> <span class="token function">slit_dispersion</span><span class="token punctuation">(</span>w<span class="token punctuation">)</span><span class="token punctuation">:</span>
    phi <span class="token operator">=</span> <span class="token operator">-</span><span class="token number">6.33</span>
    f <span class="token operator">=</span> <span class="token number">750</span>
    gr <span class="token operator">=</span> <span class="token number">300</span>
    m <span class="token operator">=</span> <span class="token number">1</span>
    phi <span class="token operator">*=</span> <span class="token operator">-</span> <span class="token number">2</span><span class="token operator">*</span>np<span class="token punctuation">.</span>pi<span class="token operator">/</span><span class="token number">360</span>
    d <span class="token operator">=</span> <span class="token number">1e-3</span><span class="token operator">/</span>gr
    disp <span class="token operator">=</span> w<span class="token operator">/</span><span class="token punctuation">(</span><span class="token number">2</span><span class="token operator">*</span>f<span class="token punctuation">)</span><span class="token operator">*</span><span class="token punctuation">(</span><span class="token operator">-</span>np<span class="token punctuation">.</span>tan<span class="token punctuation">(</span>phi<span class="token punctuation">)</span><span class="token operator">+</span>np<span class="token punctuation">.</span>sqrt<span class="token punctuation">(</span><span class="token punctuation">(</span><span class="token number">2</span><span class="token operator">*</span>d<span class="token operator">/</span>m<span class="token operator">/</span><span class="token punctuation">(</span>w<span class="token operator">*</span><span class="token number">1e-9</span><span class="token punctuation">)</span><span class="token operator">*</span>np<span class="token punctuation">.</span>cos<span class="token punctuation">(</span>phi<span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token operator">**</span><span class="token number">2</span><span class="token operator">-</span><span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
    <span class="token keyword">return</span> disp  <span class="token comment"># nm/mm</span>
    
    <span class="token keyword">def</span> <span class="token function">apply_my_slit</span><span class="token punctuation">(</span>spectrum<span class="token punctuation">,</span> inplace<span class="token operator">=</span><span class="token boolean">False</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
    slit <span class="token operator">=</span> <span class="token number">1500</span>  <span class="token comment"># µm</span>
    pitch <span class="token operator">=</span> <span class="token number">20</span>   <span class="token comment"># µm</span>
    top_slit_um <span class="token operator">=</span> slit <span class="token operator">-</span> pitch   <span class="token comment"># µm</span>
    base_slit_um <span class="token operator">=</span> slit <span class="token operator">+</span> pitch  <span class="token comment"># µm</span>
    center_slit <span class="token operator">=</span> <span class="token number">5090</span>
    dispersion <span class="token operator">=</span> slit_dispersion<span class="token punctuation">(</span>center_slit<span class="token punctuation">)</span>
    top_slit_nm <span class="token operator">=</span> top_slit_um<span class="token operator">*</span><span class="token number">1e-3</span><span class="token operator">*</span>dispersion
    base_slit_nm <span class="token operator">=</span> base_slit_um<span class="token operator">*</span><span class="token number">1e-3</span><span class="token operator">*</span>dispersion<span class="token operator">*</span><span class="token number">1.33</span>
    <span class="token keyword">return</span> spectrum<span class="token punctuation">.</span>apply_slit<span class="token punctuation">(</span><span class="token punctuation">(</span>top_slit_nm<span class="token punctuation">,</span> base_slit_nm<span class="token punctuation">)</span><span class="token punctuation">,</span> center_wavespace<span class="token operator">=</span>center_slit<span class="token punctuation">,</span> unit<span class="token operator">=</span><span class="token string">'nm'</span><span class="token punctuation">,</span> shape<span class="token operator">=</span><span class="token string">'trapezoidal'</span><span class="token punctuation">,</span> slit_dispersion<span class="token operator">=</span>slit_dispersion<span class="token punctuation">,</span> inplace<span class="token operator">=</span>inplace<span class="token punctuation">)</span></code></pre></div>
    <p>Initially, my fitting module only allows <code class="language-text">slit</code> to be enter with the format of a slit value accompanied by slit unit. For example:</p>
    <div class="gatsby-highlight"><pre class="language-python"><code class="language-python">experimental_conditions <span class="token operator">=</span> <span class="token punctuation">{</span>
    <span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>
    <span class="token string">"slit"</span> <span class="token punctuation">:</span> <span class="token string">"-0.2 nm"</span><span class="token punctuation">,</span>
    <span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>
    <span class="token punctuation">}</span></code></pre></div>
    <p>To support Mr. Corentin’s input, from now I implement input of complex slit settings in compliance with <a href="https://radis.readthedocs.io/en/latest/source/radis.spectrum.spectrum.html#radis.spectrum.spectrum.Spectrum.apply_slit">apply_slit()</a> function of RADIS. Advanced settings such like this can be inputted:</p>
    <div class="gatsby-highlight"><pre class="language-python"><code class="language-python">experimental_conditions <span class="token operator">=</span> <span class="token punctuation">{</span>
    <span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>
    <span class="token string">"slit"</span> <span class="token punctuation">:</span> <span class="token punctuation">{</span>
    <span class="token string">"slit_function"</span> <span class="token punctuation">:</span> <span class="token punctuation">(</span>top_slit_nm<span class="token punctuation">,</span> base_slit_nm<span class="token punctuation">)</span><span class="token punctuation">,</span>
    <span class="token string">"unit"</span> <span class="token punctuation">:</span> <span class="token string">"nm"</span><span class="token punctuation">,</span>
    <span class="token string">"shape"</span> <span class="token punctuation">:</span> <span class="token string">'trapezoidal'</span><span class="token punctuation">,</span>
    <span class="token string">"center_wavespace"</span> <span class="token punctuation">:</span> center_slit<span class="token punctuation">,</span>
    <span class="token string">"slit_dispersion"</span> <span class="token punctuation">:</span> slit_dispersion<span class="token punctuation">,</span>
    <span class="token string">"inplace"</span> <span class="token punctuation">:</span> <span class="token boolean">False</span><span class="token punctuation">,</span>
    <span class="token punctuation">}</span>
    <span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>
    <span class="token punctuation">}</span></code></pre></div>
    <p>And so, I have acquired very good results:</p>
    <h4>Spectrum 1:</h4>
    <ul>
    <li>Tvib:             5975.28759 (init = 6000)</li>
    <li>Trot:             5751.19260 (init = 4000)</li>
    <li>mole_fraction:    0.05501671 (init = 0.1)</li>
    </ul>
    <p><span class="gatsby-resp-image-wrapper" style="display: block; margin-left: auto; margin-right: auto;">
    <a class="gatsby-resp-image-link" href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/2385b33c685a75c2a93493ceed61841d/cca35/s1.png" rel="noopener" style="display: block;" target="_blank">
    <span class="gatsby-resp-image-background-image" style="display: block;"></span>
    <img alt="Fit result of spectrum 1" class="gatsby-resp-image-image" src="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/2385b33c685a75c2a93493ceed61841d/f058b/s1.png" style="width: 100%; height: 100%; margin: 0; vertical-align: middle;" title="Fit result of spectrum 1" />
    </a>
    </span></p>
    <h4>Spectrum 2:</h4>
    <ul>
    <li>Tvib:             4547.43903 (init = 6000)</li>
    <li>Trot:             4073.50694 (init = 4000)</li>
    <li>mole_fraction:    0.05939918 (init = 0.1)</li>
    </ul>
    <p><span class="gatsby-resp-image-wrapper" style="display: block; margin-left: auto; margin-right: auto;">
    <a class="gatsby-resp-image-link" href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/345f41ef9109afb638a3aa9eedb6e4f4/cca35/s2.png" rel="noopener" style="display: block;" target="_blank">
    <span class="gatsby-resp-image-background-image" style="display: block;"></span>
    <img alt="Fit result of spectrum 2" class="gatsby-resp-image-image" src="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/345f41ef9109afb638a3aa9eedb6e4f4/f058b/s2.png" style="width: 100%; height: 100%; margin: 0; vertical-align: middle;" title="Fit result of spectrum 2" />
    </a>
    </span></p>
    <h4>Spectrum 3:</h4>
    <ul>
    <li>Tvib:             2811.98218 (init = 6000)</li>
    <li>Trot:             2915.36318 (init = 4000)</li>
    <li>mole_fraction:    0.07739941 (init = 0.05)</li>
    </ul>
    <p><span class="gatsby-resp-image-wrapper" style="display: block; margin-left: auto; margin-right: auto;">
    <a class="gatsby-resp-image-link" href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/5b1fb36019eae53d82648d9fdf049153/cca35/s3.png" rel="noopener" style="display: block;" target="_blank">
    <span class="gatsby-resp-image-background-image" style="display: block;"></span>
    <img alt="Fit result of spectrum 3" class="gatsby-resp-image-image" src="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/5b1fb36019eae53d82648d9fdf049153/f058b/s3.png" style="width: 100%; height: 100%; margin: 0; vertical-align: middle;" title="Fit result of spectrum 3" />
    </a>
    </span></p>
    <h4>Spectrum 4:</h4>
    <ul>
    <li>Tvib:             4721.28892 (init = 6000)</li>
    <li>Trot:             4728.52960 (init = 4000)</li>
    <li>mole_fraction:    0.07008355 (init = 0.05)</li>
    </ul>
    <p><span class="gatsby-resp-image-wrapper" style="display: block; margin-left: auto; margin-right: auto;">
    <a class="gatsby-resp-image-link" href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/569114757da34f35d48661ef31830737/cca35/s4.png" rel="noopener" style="display: block;" target="_blank">
    <span class="gatsby-resp-image-background-image" style="display: block;"></span>
    <img alt="Fit result of spectrum 4" class="gatsby-resp-image-image" src="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/569114757da34f35d48661ef31830737/f058b/s4.png" style="width: 100%; height: 100%; margin: 0; vertical-align: middle;" title="Fit result of spectrum 4" />
    </a>
    </span></p>

