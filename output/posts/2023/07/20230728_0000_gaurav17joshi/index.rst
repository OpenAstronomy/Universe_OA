.. title: GSoC - Week 7-8
.. slug:
.. date: 2023-07-28 00:00:00 
.. tags: stingray
.. author: Gaurav Joshi
.. link: https://Gaurav17Joshi.github.io/Blogs/2023/07/28/W78.html
.. description:
.. category: gsoc2023


.. raw:: html

    <h2 id="testing-features">Testing features</h2>
    
    <p>This week I refined my testing features for the code, and made the completed doctests.</p>
    <!-- TEASER_END -->
    
    <p>In my project, I was using 4 different kinds of dependencies, and none had been previously used by stingray, so I had to make some changes to the code structure to accomodate those exceptions.</p>
    
    <p>I also made updated and improved a lot of docstrings and added some doctests, which was a new experience. My <code class="language-plaintext highlighter-rouge">get_prior</code> doctest looked like:-</p>
    
    <div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="o">&gt;&gt;&gt;</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">can_sample</span><span class="p">:</span>
    <span class="p">...</span>     <span class="n">pytest</span><span class="p">.</span><span class="n">skip</span><span class="p">(</span><span class="s">"Jaxns not installed. Cannot make jaxns specific prior."</span><span class="p">)</span>
    <span class="o">&gt;&gt;&gt;</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">tfp_available</span><span class="p">:</span>
    <span class="p">...</span>     <span class="n">pytest</span><span class="p">.</span><span class="n">skip</span><span class="p">(</span><span class="s">"Tensorflow probability required to make priors."</span><span class="p">)</span>
    <span class="o">&gt;&gt;&gt;</span> <span class="n">params_list</span> <span class="o">=</span> <span class="n">get_gp_params</span><span class="p">(</span><span class="s">"RN"</span><span class="p">,</span> <span class="s">"gaussian"</span><span class="p">)</span>
    <span class="n">Make</span> <span class="n">a</span> <span class="n">prior</span> <span class="n">dictionary</span> <span class="n">using</span> <span class="n">tensorflow_probability</span> <span class="n">distributions</span>
    <span class="o">&gt;&gt;&gt;</span> <span class="n">prior_dict</span> <span class="o">=</span> <span class="p">{</span>
    <span class="p">...</span>    <span class="s">"A"</span><span class="p">:</span> <span class="n">tfpd</span><span class="p">.</span><span class="n">Uniform</span><span class="p">(</span><span class="n">low</span> <span class="o">=</span> <span class="mf">1e-1</span><span class="p">,</span> <span class="n">high</span> <span class="o">=</span> <span class="mf">2e+2</span><span class="p">),</span>
    <span class="p">...</span>    <span class="s">"t0"</span><span class="p">:</span> <span class="n">tfpd</span><span class="p">.</span><span class="n">Uniform</span><span class="p">(</span><span class="n">low</span> <span class="o">=</span> <span class="mf">0.0</span> <span class="o">-</span> <span class="mf">0.1</span><span class="p">,</span> <span class="n">high</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">+</span> <span class="mf">0.1</span><span class="p">),</span>
    <span class="p">...</span>    <span class="s">"sig"</span><span class="p">:</span> <span class="n">tfpd</span><span class="p">.</span><span class="n">Uniform</span><span class="p">(</span><span class="n">low</span> <span class="o">=</span> <span class="mf">0.5</span> <span class="o">*</span> <span class="mi">1</span> <span class="o">/</span> <span class="mi">20</span><span class="p">,</span> <span class="n">high</span> <span class="o">=</span> <span class="mi">2</span> <span class="p">),</span>
    <span class="p">...</span>    <span class="s">"arn"</span><span class="p">:</span> <span class="n">tfpd</span><span class="p">.</span><span class="n">Uniform</span><span class="p">(</span><span class="n">low</span> <span class="o">=</span> <span class="mf">0.1</span> <span class="p">,</span> <span class="n">high</span> <span class="o">=</span> <span class="mi">2</span> <span class="p">),</span>
    <span class="p">...</span>    <span class="s">"crn"</span><span class="p">:</span> <span class="n">tfpd</span><span class="p">.</span><span class="n">Uniform</span><span class="p">(</span><span class="n">low</span> <span class="o">=</span> <span class="n">jnp</span><span class="p">.</span><span class="n">log</span><span class="p">(</span><span class="mi">1</span> <span class="o">/</span><span class="mi">5</span><span class="p">),</span> <span class="n">high</span> <span class="o">=</span> <span class="n">jnp</span><span class="p">.</span><span class="n">log</span><span class="p">(</span><span class="mi">20</span><span class="p">)),</span>
    <span class="p">...</span> <span class="p">}</span>
    <span class="o">&gt;&gt;&gt;</span> <span class="n">prior_model</span> <span class="o">=</span> <span class="n">get_prior</span><span class="p">(</span><span class="n">params_list</span><span class="p">,</span> <span class="n">prior_dict</span><span class="p">)</span>
    </code></pre></div></div>
    
    <h2 id="jax-issues">Jax Issues</h2>
    
    <p>This week I also made a lot of futile tries in resolving an error in jax. As good and fast a library it is (I am yet to use some mindblowing features like pytrees), it has one limitation (or design decision), is that we cannot use not fixed sized arrays inside a jit function.</p>
    
    <p>In my project, one important issue that we wanted to tackle was the non stationarity of pulsar timeseries. The method to take this into account was to use a window over the data, ie only in the window we will asume a qpo and get its log likelihood and outside we will assume white noise outside. The problem in it was that jax jit functions wants to before handedly know the type and size of all its arrays and data structres, hense there was no way to create a window over the time-series.</p>
    
    <p>This while frustrating, also is a proof that code is often used in ways very different than intended or there are issues that we not taken into account when these important design desisions were made. (Though at no fault of the Jax library as before hand knowing the array shapes is crucial for fast parallel code)</p>

