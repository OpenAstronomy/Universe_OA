.. title: GSoC - Week 5-6
.. slug:
.. date: 2023-07-11 00:00:00 
.. tags: stingray
.. author: Gaurav Joshi
.. link: https://Gaurav17Joshi.github.io/Blogs/2023/07/11/W56.html
.. description:
.. category: gsoc2023


.. raw:: html

    <h2 id="making-a-demo">Making a Demo</h2>
    <p>I had recently made some changes to my GP and GPResult class on the advice of my mentors and I realised that I am not making the tool keeping the user in mind.</p>
    
    <!-- TEASER_END -->
    <p>See, in contemporary data analysis, Gaussian Processes GP’s are very useful to fit and extrapolate the data. If we have some data points, we can use any suitable kernel function and a 0 mean and we will get a nicely fitting GP, which will also allow us to know function values at new points with error bars. But this is not what the users need in astronomy. They do not usually need to extrapolate the data to get values at new points, rather, they want to make a compare models with different charachteristics, signals, and identify which signal is present in the time series.</p>
    
    <p>Thus making the demo notebook gave me an extrinsic view of the problem, and it made me change the arrangement of a lot of classes and functions in the code.</p>
    
    <h2 id="new-implimenatations">New implimenatations</h2>
    
    <h3 id="gpr-class">GPR class</h3>
    <p>The big new implimentation that I made, was to entirely change the feature from having a GP class for data fitting and a GPResult class for bayesian inference to just the GPResult class for inferencing and plotting.</p>
    
    <p>I changed the tool to just a GPResult class, that takes a suitable prior and log likelihood function samples out the posterior parameters. This also has a lot of new plotting features which are helpul to visualise the posterior parameter.</p>
    
    <div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">class</span> <span class="nc">GPResult</span><span class="p">:</span>
    <span class="s">"""
    Makes a GPResult object which takes in a Stingray.Lightcurve and samples parameters of a model
    (Gaussian Process) based on the given prior and log_likelihood function.
    """</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">Lc</span><span class="p">:</span> <span class="n">Lightcurve</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="bp">None</span><span class="p">:</span>
    <span class="bp">self</span><span class="p">.</span><span class="n">lc</span> <span class="o">=</span> <span class="n">Lc</span>
    <span class="bp">self</span><span class="p">.</span><span class="n">time</span> <span class="o">=</span> <span class="n">Lc</span><span class="p">.</span><span class="n">time</span>
    <span class="bp">self</span><span class="p">.</span><span class="n">counts</span> <span class="o">=</span> <span class="n">Lc</span><span class="p">.</span><span class="n">counts</span>
    <span class="bp">self</span><span class="p">.</span><span class="n">Result</span> <span class="o">=</span> <span class="bp">None</span>
    
    <span class="k">def</span> <span class="nf">sample</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prior_model</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">likelihood_model</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
    <span class="s">""" Makes a Jaxns nested sampler over the Gaussian Process, given the
    prior and likelihood model """</span>
    <span class="bp">self</span><span class="p">.</span><span class="n">prior_model</span> <span class="o">=</span> <span class="n">prior_model</span>
    <span class="bp">self</span><span class="p">.</span><span class="n">likelihood_model</span> <span class="o">=</span> <span class="n">likelihood_model</span>
    
    <span class="n">NSmodel</span> <span class="o">=</span> <span class="n">Model</span><span class="p">(</span><span class="n">prior_model</span><span class="o">=</span><span class="bp">self</span><span class="p">.</span><span class="n">prior_model</span><span class="p">,</span> <span class="n">log_likelihood</span><span class="o">=</span><span class="bp">self</span><span class="p">.</span><span class="n">likelihood_model</span><span class="p">)</span>
    <span class="n">NSmodel</span><span class="p">.</span><span class="n">sanity_check</span><span class="p">(</span><span class="n">random</span><span class="p">.</span><span class="n">PRNGKey</span><span class="p">(</span><span class="mi">10</span><span class="p">),</span> <span class="n">S</span><span class="o">=</span><span class="mi">100</span><span class="p">)</span>
    
    <span class="bp">self</span><span class="p">.</span><span class="n">Exact_ns</span> <span class="o">=</span> <span class="n">ExactNestedSampler</span><span class="p">(</span><span class="n">NSmodel</span><span class="p">,</span> <span class="n">num_live_points</span><span class="o">=</span><span class="mi">500</span><span class="p">,</span> <span class="n">max_samples</span><span class="o">=</span><span class="mf">1e4</span><span class="p">)</span>
    <span class="n">Termination_reason</span><span class="p">,</span> <span class="n">State</span> <span class="o">=</span> <span class="bp">self</span><span class="p">.</span><span class="n">Exact_ns</span><span class="p">(</span>
    <span class="n">random</span><span class="p">.</span><span class="n">PRNGKey</span><span class="p">(</span><span class="mi">42</span><span class="p">),</span> <span class="n">term_cond</span><span class="o">=</span><span class="n">TerminationCondition</span><span class="p">(</span><span class="n">live_evidence_frac</span><span class="o">=</span><span class="mf">1e-4</span><span class="p">)</span>
    <span class="p">)</span>
    <span class="bp">self</span><span class="p">.</span><span class="n">Results</span> <span class="o">=</span> <span class="bp">self</span><span class="p">.</span><span class="n">Exact_ns</span><span class="p">.</span><span class="n">to_results</span><span class="p">(</span><span class="n">State</span><span class="p">,</span> <span class="n">Termination_reason</span><span class="p">)</span>
    <span class="k">print</span><span class="p">(</span><span class="s">"Simulation Complete"</span><span class="p">)</span>
    
    <span class="k">def</span> <span class="nf">get_evidence</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
    <span class="s">""" Returns the log evidence of the model """</span>
    
    <span class="k">def</span> <span class="nf">print_summary</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
    <span class="s">""" Prints a summary table for the model parameters """</span>
    </code></pre></div></div>
    
    <p>And many other plotting functions like</p>
    
    <ul>
    <li>
    <p>plot_diagnostics</p>
    </li>
    <li>
    <p>plot_cornerplot</p>
    </li>
    <li>
    <p>get_parameters_name</p>
    </li>
    <li>
    <p>get_max_posterior_parameters</p>
    </li>
    <li>
    <p>get_max_likelihood_parameters</p>
    </li>
    <li>
    <p>posterior_plot</p>
    </li>
    <li>
    <p>weighted_posterior_plot</p>
    </li>
    <li>
    <p>corner_plot</p>
    </li>
    </ul>
    
    <h3 id="get-prior-function">Get Prior function</h3>
    <p>Earlier the <code class="language-plaintext highlighter-rouge">get_prior</code> function was a big function which took in your kernel and mean type, and gave you the prior function, but I had to write a separate function for each comibination making it a gignantic function of unecessary repeated code, also the prior ranges and distribution types (uniform, cauchy etc) was fixed according to what I had hard-coded without any way to change it. If someon wanted to implement a prior with even a small change, it was not possible.</p>
    
    <p>So My mentor suggested making the function, such that the user inputs the tensorflow priors based on their needs, and we just make a jaxns prior for it. This led to the new code:-</p>
    
    <div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">def</span> <span class="nf">get_prior</span><span class="p">(</span><span class="n">params_list</span><span class="p">,</span> <span class="n">prior_dict</span><span class="p">):</span>
    <span class="s">"""
    A prior generator function based on given values
    """</span>
    <span class="k">def</span> <span class="nf">prior_model</span><span class="p">():</span>
    <span class="n">prior_list</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">params_list</span><span class="p">:</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">prior_dict</span><span class="p">[</span><span class="n">i</span><span class="p">],</span> <span class="n">tfpd</span><span class="p">.</span><span class="n">Distribution</span><span class="p">):</span>
    <span class="n">parameter</span> <span class="o">=</span> <span class="k">yield</span> <span class="n">Prior</span><span class="p">(</span><span class="n">prior_dict</span><span class="p">[</span><span class="n">i</span><span class="p">],</span> <span class="n">name</span><span class="o">=</span><span class="n">i</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
    <span class="n">parameter</span> <span class="o">=</span> <span class="k">yield</span> <span class="n">prior_dict</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
    <span class="n">prior_list</span><span class="p">.</span><span class="n">append</span><span class="p">(</span><span class="n">parameter</span><span class="p">)</span>
    <span class="k">return</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">prior_list</span><span class="p">)</span>
    
    <span class="k">return</span> <span class="n">prior_model</span>
    </code></pre></div></div>
    
    <h3 id="get-likelihood-function">Get likelihood function:</h3>
    <p>Similarly I changed the likelihood functin so that it takes a parmeter array, and the kernel, mean type and gives us a log_likelihood function which calculates and gets the likelihood of the data being fitted for the parameters.</p>
    
    <div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">def</span> <span class="nf">get_likelihood</span><span class="p">(</span><span class="n">params_list</span><span class="p">,</span> <span class="n">kernel_type</span><span class="p">,</span> <span class="n">mean_type</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
    <span class="s">"""
    A likelihood generator function based on given values
    """</span>
    <span class="o">@</span><span class="n">jit</span>
    <span class="k">def</span> <span class="nf">likelihood_model</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">):</span>
    <span class="nb">dict</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">params</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">params_list</span><span class="p">):</span>
    <span class="nb">dict</span><span class="p">[</span><span class="n">params</span><span class="p">]</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
    <span class="n">kernel</span> <span class="o">=</span> <span class="n">get_kernel</span><span class="p">(</span><span class="n">kernel_type</span><span class="o">=</span><span class="n">kernel_type</span><span class="p">,</span> <span class="n">kernel_params</span><span class="o">=</span><span class="nb">dict</span><span class="p">)</span>
    <span class="n">mean</span> <span class="o">=</span> <span class="n">get_mean</span><span class="p">(</span><span class="n">mean_type</span><span class="o">=</span><span class="n">mean_type</span><span class="p">,</span> <span class="n">mean_params</span><span class="o">=</span><span class="nb">dict</span><span class="p">)</span>
    <span class="n">gp</span> <span class="o">=</span> <span class="n">GaussianProcess</span><span class="p">(</span><span class="n">kernel</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">[</span><span class="s">"Times"</span><span class="p">],</span> <span class="n">mean_value</span><span class="o">=</span><span class="n">mean</span><span class="p">(</span><span class="n">kwargs</span><span class="p">[</span><span class="s">"Times"</span><span class="p">]))</span>
    <span class="k">return</span> <span class="n">gp</span><span class="p">.</span><span class="n">log_probability</span><span class="p">(</span><span class="n">kwargs</span><span class="p">[</span><span class="s">"counts"</span><span class="p">])</span>
    
    <span class="k">return</span> <span class="n">likelihood_model</span>
    </code></pre></div></div>
    
    <h3 id="jit-issues">Jit issues</h3>

