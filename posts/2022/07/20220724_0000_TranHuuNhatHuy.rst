.. title: First evaluation - Final rush for first milestone, advices from mentors, and keep going!
.. slug:
.. date: 2022-07-24 00:00:00 
.. tags: radis
.. author: TranHuuNhatHuy
.. link: https://https://gsoc2022tranhuunhathuy.gatsbyjs.io/7. first_evaluation/
.. description:
.. category: gsoc2022


.. raw:: html

    <p>In this final week, I fully dedicate myself into user-testing cases. As pointed out by Mr. Erwan Pannier, <em>“Things will definitely change after user feedback so don’t waste too much time before that”</em>. Thus, I must quickly bring up several notebooks for the users - our spectroscopic scientists - to test and provide feedbacks, and from then I can shape my fitting modules closer to the real usages and needs. Firstly, I will talk about several additional updates in this final week of phase 1:</p>
    <h3>1. Non-LTE support</h3>
    <p>Now the fitting module supports non-LTE input. The module will automatically switch to non-LTE mode when <code class="language-text">Tvib</code> is detected inside the input meterials.</p>
    <!-- TEASER_END -->
    <p>If there are more than one <code class="language-text">Tvib</code> due to non-diatomic molecules having more than one vibrational temperatures, the input of <code class="language-text">Tvib</code> will be either <code class="language-text">tuple</code> or <code class="language-text">list</code>, and thus needed to be treated differently. For this, the procedure is gonna be:</p>
    <ol>
    <li>After <code class="language-text">Tvib</code> is detected as a fitting parameter within <code class="language-text">fit</code>, if it is in type of either <code class="language-text">tuple</code> or <code class="language-text">list</code>, each of the constituting temperature will then be extracted, and assigned a number after it, for example, <code class="language-text">Tvib1</code>, <code class="language-text">Tvib2</code>, and so on.</li>
    <li>Then, these separated temperatures will be assigned to a Parameter object and from here, they will be treated as an individual fitting parameter, which will altogether enter the fitting process.</li>
    <li>After fitting process, all Parameter objects with <code class="language-text">Tvib</code> in their names will be collected and merged into the original <code class="language-text">Tvib</code> array.</li>
    </ol>
    <h3>2. Format refactor - more flexible ways to input</h3>
    <p>As I mentioned last week, the new fitting module should also support in-script JSON structure, because as Mr. Erwan Pannier pointed out, people would prefer adjusting everything within a single script, rather than switching between windows just to adjust a separated JSON file. So now the idea is to have 2 ways of input: either through in-script <code class="language-text">JSON</code> structures, or through an external <code class="language-text">JSON</code> file.</p>
    <p>Now the users can either use a separated JSON file as input, or directly input a bunch of <code class="language-text">dict</code> parameters.</p>
    <p>For example, when using JSON file:</p>
    <div class="gatsby-highlight"><pre class="language-python"><code class="language-python"><span class="token comment"># Get JSON file path (note that the experimental spectrum file MUST BE IN THE SAME FOLDER containing JSON file)</span>
    JSON_path <span class="token operator">=</span> <span class="token string">"../test_dir/test_JSON_file.json"</span>
    
    <span class="token comment"># Conduct the fitting process!</span>
    s_best<span class="token punctuation">,</span> result<span class="token punctuation">,</span> log <span class="token operator">=</span> fit_spectrum<span class="token punctuation">(</span>input_file <span class="token operator">=</span> JSON_path<span class="token punctuation">)</span></code></pre></div>
    <p>And when inputting a bunch of <code class="language-text">dict</code> parameters (pure Python way):</p>
    <div class="gatsby-highlight"><pre class="language-python"><code class="language-python"><span class="token comment"># Load experimental spectrum. You can prepare yours, or fetch one of them in the ground-truth folder like below.</span>
    s_experimental <span class="token operator">=</span> load_spec<span class="token punctuation">(</span><span class="token string">"./data/LTE/ground-truth/synth-NH3-1-500-2000-cm-1-P10-t1000-v-r-mf0.01-p1-sl1nm.spec"</span><span class="token punctuation">)</span>
    
    <span class="token comment"># Experimental conditions which will be used for spectrum modeling. Basically, these are known ground-truths.</span>
    experimental_conditions <span class="token operator">=</span> <span class="token punctuation">{</span>
    <span class="token string">"molecule"</span> <span class="token punctuation">:</span> <span class="token string">"NH3"</span><span class="token punctuation">,</span>         <span class="token comment"># Molecule ID</span>
    <span class="token string">"isotope"</span> <span class="token punctuation">:</span> <span class="token string">"1"</span><span class="token punctuation">,</span>            <span class="token comment"># Isotope ID, can have multiple at once</span>
    <span class="token string">"wmin"</span> <span class="token punctuation">:</span> <span class="token number">1000</span><span class="token punctuation">,</span>              <span class="token comment"># Starting wavelength/wavenumber to be cropped out from the original experimental spectrum.</span>
    <span class="token string">"wmax"</span> <span class="token punctuation">:</span> <span class="token number">1050</span><span class="token punctuation">,</span>              <span class="token comment"># Ending wavelength/wavenumber for the cropping range.</span>
    <span class="token string">"wunit"</span> <span class="token punctuation">:</span> <span class="token string">"cm-1"</span><span class="token punctuation">,</span>           <span class="token comment"># Accompanying unit of those 2 wavelengths/wavenumbers above.</span>
    <span class="token string">"mole_fraction"</span> <span class="token punctuation">:</span> <span class="token number">0.01</span><span class="token punctuation">,</span>     <span class="token comment"># Species mole fraction, from 0 to 1.</span>
    <span class="token string">"pressure"</span> <span class="token punctuation">:</span> <span class="token number">10</span><span class="token punctuation">,</span>            <span class="token comment"># Partial pressure of gas, in "bar" unit.</span>
    <span class="token string">"path_length"</span> <span class="token punctuation">:</span> <span class="token number">1</span><span class="token punctuation">,</span>          <span class="token comment"># Experimental path length, in "cm" unit.</span>
    <span class="token string">"slit"</span> <span class="token punctuation">:</span> <span class="token string">"1 nm"</span><span class="token punctuation">,</span>            <span class="token comment"># Experimental slit, must be a blank space separating slit amount and unit.</span>
    <span class="token string">"offset"</span> <span class="token punctuation">:</span> <span class="token string">"-0.2 nm"</span>        <span class="token comment"># Experimental offset, must be a blank space separating offset amount and unit.</span>
    <span class="token punctuation">}</span>
    
    <span class="token comment"># List of parameters to be fitted.</span>
    fit_parameters <span class="token operator">=</span> <span class="token punctuation">{</span>
    <span class="token string">"Tgas"</span> <span class="token punctuation">:</span> <span class="token number">700</span><span class="token punctuation">,</span>               <span class="token comment"># Fit parameter, accompanied by its initial value.</span>
    <span class="token punctuation">}</span>
    
    <span class="token comment"># List of bounding ranges applied for those fit parameters above.</span>
    bounding_ranges <span class="token operator">=</span> <span class="token punctuation">{</span>
    <span class="token string">"Tgas"</span> <span class="token punctuation">:</span> <span class="token punctuation">[</span><span class="token number">600</span><span class="token punctuation">,</span> <span class="token number">2000</span><span class="token punctuation">]</span><span class="token punctuation">,</span>       <span class="token comment"># Bounding ranges for each fit parameter stated above. You can skip this step, but not recommended.</span>
    <span class="token punctuation">}</span>
    
    <span class="token comment"># Fitting pipeline setups.</span>
    fit_properties <span class="token operator">=</span> <span class="token punctuation">{</span>
    <span class="token string">"method"</span> <span class="token punctuation">:</span> <span class="token string">"lbfgsb"</span><span class="token punctuation">,</span>        <span class="token comment"># Preferred fitting method from the 17 confirmed methods of LMFIT stated in week 4 blog. By default, "leastsq".</span>
    <span class="token string">"fit_var"</span> <span class="token punctuation">:</span> <span class="token string">"radiance"</span><span class="token punctuation">,</span>     <span class="token comment"># Spectral quantity to be extracted for fitting process, such as "radiance", "absorbance", etc.</span>
    <span class="token string">"normalize"</span> <span class="token punctuation">:</span> <span class="token boolean">False</span><span class="token punctuation">,</span>        <span class="token comment"># Either applying normalization on both spectra or not.</span>
    <span class="token string">"max_loop"</span> <span class="token punctuation">:</span> <span class="token number">150</span><span class="token punctuation">,</span>           <span class="token comment"># Max number of loops allowed. By default, 100.</span>
    <span class="token string">"tol"</span> <span class="token punctuation">:</span> <span class="token number">1e-10</span>               <span class="token comment"># Fitting tolerance, only applicable for "lbfgsb" method.</span>
    <span class="token punctuation">}</span>
    
    <span class="token comment"># Conduct the fitting process!</span>
    s_best<span class="token punctuation">,</span> result<span class="token punctuation">,</span> log <span class="token operator">=</span> fit_spectrum<span class="token punctuation">(</span>
    s_exp <span class="token operator">=</span> s_experimental<span class="token punctuation">,</span>
    fit_params <span class="token operator">=</span> fit_parameters<span class="token punctuation">,</span>
    bounds <span class="token operator">=</span> bounding_ranges<span class="token punctuation">,</span>
    model <span class="token operator">=</span> experimental_conditions<span class="token punctuation">,</span>
    pipeline <span class="token operator">=</span> fit_properties
    <span class="token punctuation">)</span></code></pre></div>
    <p>As we can see, this will be much more flexible for the users to input the ground-truth data and parameters.</p>
    <h3>3. Sample notebooks and test files</h3>
    <p>To support the user-testing process, 4 sample Jupyter notebooks and 4 corresponding Python test files have been added. They are:</p>
    <ul>
    <li><a href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/8400844d0a6880d50b65b66f8f8443d3/sample_LTE_Tgas.ipynb"><code class="language-text">sample_LTE_Tgas.ipynb</code></a> : LTE fitting case, with <code class="language-text">Tgas</code> as fit parameter, multiple-dict input.</li>
    <li><a href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/25a15b8b2ffbe5d4f45a3abac687d7bc/sample_LTE_Tgas-molfrac.ipynb"><code class="language-text">sample_LTE_Tgas-molfrac.ipynb</code></a> : LTE fitting case, with <code class="language-text">Tgas</code> and <code class="language-text">mole_fraction</code> as fit parameters, multiple-dict input.</li>
    <li><a href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/6c8401dc960f424c43da01b84f066926/sample_LTE-with-JSON_Tgas.ipynb"><code class="language-text">sample_LTE-with-JSON_Tgas.ipynb</code></a> : LTE fitting case, with <code class="language-text">Tgas</code> as fit parameter, JSON file input.</li>
    <li><a href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/3a7118b0d09be64d598dff8d16e7cff6/sample_nonLTE_1Tvib-Trot.ipynb"><code class="language-text">sample_nonLTE_1Tvib-Trot.ipynb</code></a> : non-LTE fitting case, with 1 <code class="language-text">Tvib</code> and 1 <code class="language-text">Trot</code> as fit parameters, multiple-dict input.</li>
    </ul>
    <p>Also, as the first evaluation is drawing near, and the fact that my fitting module for 1st phase is fundamentally finished (there might be some bugs, but now it’s just time for bug reporting, debugging and keep it that way), I believe now it’s a good time for me to reflect my progress during this first phase, and to plan accordingly for the next phase. Thus, I decide to ask my mentors to discuss about the current progress, and future plans as well. Also, I hope to receive several reviews about my work attitude, current impression of phase 1, and the current state of evaluation and room for improvements, too. Turned out that the comments are quite good, better than I expected. The only thing that I need to improve is, welp, don’t asking <em>too much</em> feedbacks, but instead just focus on the content and quality of the module development.</p>
    <p>I would like to conclude this final blog of phase 1 with words from Mr. Erwan Pannier:</p>
    <blockquote>
    <p>In other words : this is not a school-project. There is no right/wrong/expectations that you should.
    Just work, deliver, try things, fail, change direction, try again, succeed. But focus on the content, and focus on delivering a great product.
    In your case, a great fitting routine. When you will be happy with what you’ve done, people will follow.</p>
    </blockquote>

