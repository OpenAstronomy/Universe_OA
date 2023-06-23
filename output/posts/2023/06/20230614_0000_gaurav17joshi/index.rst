.. title: GSoC - Week 1-2
.. slug:
.. date: 2023-06-14 00:00:00 
.. tags: stingray
.. author: Gaurav Joshi
.. link: https://Gaurav17Joshi.github.io/Blogs/2023/06/14/W12.html
.. description:
.. category: gsoc2023


.. raw:: html

    <h2 id="my-adventure-with-the-implementation">My adventure with the implementation</h2>
    <p>While taking on this project, the thing I was most excited was that I would be getting to write rearch code (Code to be used by researchers in their work all over). With advent of large data from multiple telescopes and computational speed , Gaussian Processes are fast becoming the go to choice for astrophichal modelling.</p>
    
    <!-- TEASER_END -->
    <p>In the original Source paper, the authors had simulated 1000 lightcurves of varying intesity of QPO, and measured their evidence for QPO and RN priors to check how well this technique works, and ensure that it does not give any false positives.</p>
    
    <p>Hense, I set forth on my mission to calculate evidence of 1000 lightcurve on GPs with my new and beloved Macbook. Having full confidence that my computation machine is as good as they come, I set out to perform inference on my 1000 lightcurve, only for my pc to take 1 hour to without sampling a single lightcurve.</p>
    
    <p>On reducing the number of points from 256 to 64, the code took 4 min to complete. Considering O(N3) time complexity, it would have taken <strong>4 hours</strong> to complete the simulation for 1 curve :scream:.</p>
    
    <p>Here I had made my own implementation of the kernel using tinygp. At this point my mentor advice me to use <code class="language-plaintext highlighter-rouge">tinygp.quasisep.celerite</code> kernels, a special kernel, implemented based on the celerite algorithm. On changing to the new kernel, the code took just <strong>1 min</strong> to run.
    This made me realise how important such specialized code was, and how important making such faster and more effective code is.</p>
    
    <h2 id="the-implementation">The implementation</h2>
    <p>In the first two weeks I focussed on understanding the implementation of the project. In the source repository Celerite library was used for GP implimentation and Bilby was used for Bayesian Inferencing, while in my project my mentor and I decided to completely use a Jax based backend hense, Tinygp for GP, and Jaxns for Nested Sampling.</p>
    
    <p>I made a proof of Concept implimentation for the QPO kernel and gaussian mean model for a lightcurve, which is explained in breif here:-</p>
    
    <h3 id="kernel">Kernel:</h3>
    <p>For making the Kernel, I used Tingp.quasisep.celerite kernels which are a fast implementation (based on the celerite kernel) of the Qpo kernel.</p>
    
    <p>The <code class="language-plaintext highlighter-rouge">quasisep.exp</code> kernel for the red noise part and the <code class="language-plaintext highlighter-rouge">quasisep.celerite</code> kernel for the qpo part can be implemented as:</p>
    <div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">hqpokernel</span> <span class="o">=</span> <span class="n">kernels</span><span class="p">.</span><span class="n">quasisep</span><span class="p">.</span><span class="n">Exp</span><span class="p">(</span>
    <span class="n">scale</span> <span class="o">=</span> <span class="mi">1</span><span class="o">/</span><span class="n">hqpoparams</span><span class="p">[</span><span class="s">"crn"</span><span class="p">],</span> <span class="n">sigma</span> <span class="o">=</span> <span class="p">(</span><span class="n">hqpoparams</span><span class="p">[</span><span class="s">"arn"</span><span class="p">])</span><span class="o">**</span><span class="mf">0.5</span><span class="p">)</span> <span class="o">+</span> <span class="n">kernels</span><span class="p">.</span><span class="n">quasisep</span><span class="p">.</span><span class="n">Celerite</span><span class="p">(</span>
    <span class="n">a</span> <span class="o">=</span> <span class="n">hqpoparams</span><span class="p">[</span><span class="s">"aqpo"</span><span class="p">],</span> <span class="n">b</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="n">c</span> <span class="o">=</span> <span class="n">hqpoparams</span><span class="p">[</span><span class="s">"cqpo"</span><span class="p">],</span> <span class="n">d</span> <span class="o">=</span> <span class="mi">2</span><span class="o">*</span><span class="n">jnp</span><span class="p">.</span><span class="n">pi</span><span class="o">*</span><span class="n">hqpoparams</span><span class="p">[</span><span class="s">"freq"</span><span class="p">])</span>
    </code></pre></div></div>
    
    <p><img alt="Plot of High, low and non QPO kernel" src="https://gaurav17joshi.github.io/Blogs/img/assets/kernel1.png" /></p>
    
    <h3 id="mean">Mean:</h3>
    <p>We are working on Extremely powerful events in the universe which emit radiation in the Xray spectra. Many of these have some sort of flaring behaviour, and also in general, we wanted to add mean functions to our GPs as this feature will be extended to other astronomical time series.</p>
    
    <p>For this proof of concept implimentation, I used a simple gaussian mean to test out sampling using Jaxns
    Using the tinygp library to make the gaussian process and sample out some lightcurves from it.</p>
    
    <div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">def</span> <span class="nf">gaussian</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="n">mean_params</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">mean_params</span><span class="p">[</span><span class="s">"A"</span><span class="p">]</span> <span class="o">*</span> <span class="n">jnp</span><span class="p">.</span><span class="n">exp</span><span class="p">(</span><span class="o">-</span><span class="p">((</span><span class="n">t</span> <span class="o">-</span> <span class="n">mean_params</span><span class="p">[</span><span class="s">"t0"</span><span class="p">])</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span><span class="o">/</span><span class="p">(</span><span class="mi">2</span><span class="o">*</span><span class="p">(</span><span class="n">mean_params</span><span class="p">[</span><span class="s">"sig"</span><span class="p">]</span><span class="o">**</span><span class="mi">2</span><span class="p">)))</span>
    
    <span class="n">mean_params</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s">"A"</span> <span class="p">:</span> <span class="mi">3</span><span class="p">,</span>    <span class="s">"t0"</span> <span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span>    <span class="s">"sig"</span> <span class="p">:</span> <span class="mf">0.2</span><span class="p">,}</span>
    
    <span class="n">mean</span> <span class="o">=</span> <span class="n">functools</span><span class="p">.</span><span class="n">partial</span><span class="p">(</span><span class="n">gaussian</span><span class="p">,</span> <span class="n">mean_params</span> <span class="o">=</span> <span class="n">mean_params</span><span class="p">)</span>
    <span class="c1"># Making the Gp
    </span><span class="n">gp</span> <span class="o">=</span> <span class="n">tinygp</span><span class="p">.</span><span class="n">GaussianProcess</span><span class="p">(</span> <span class="n">kernel</span><span class="p">,</span> <span class="n">t</span><span class="p">,</span> <span class="n">mean</span><span class="o">=</span><span class="n">mean</span><span class="p">,</span> <span class="n">diag</span> <span class="o">=</span> <span class="n">diag</span><span class="p">)</span>
    <span class="n">gp_sample</span>   <span class="o">=</span>  <span class="n">gp</span><span class="p">.</span><span class="n">sample</span><span class="p">(</span> <span class="n">jax</span><span class="p">.</span><span class="n">random</span><span class="p">.</span><span class="n">PRNGKey</span><span class="p">(</span><span class="mi">11</span><span class="p">),</span> <span class="n">shape</span><span class="o">=</span><span class="p">(</span><span class="mi">1</span><span class="p">,))</span>
    </code></pre></div></div>
    
    <p><img alt="Plot of samples" src="https://gaurav17joshi.github.io/Blogs/img/assets/samples1.png" /></p>
    
    <h3 id="priors-and-likelihoods">Priors and likelihoods</h3>
    <p>As we want to fit our Red noise and Qpo + Red noise model on the lightcurve, we need to make suitable prior funcitons for them. We use Jaxns.Prior to make a generator prior function, and make a corresponding likelihood function, which makes the gp and calculates the log likehood of producing the given lightcurve.</p>
    
    <p>We set the bounds for the prior functions based on the suggestions given in the source paper, and plot the fitted maximum posterior gp on the lightcurve.</p>
    
    <div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Prior Model Function
    </span><span class="k">def</span> <span class="nf">RNprior_model</span><span class="p">():</span>
    <span class="n">T</span> <span class="o">=</span> <span class="n">Times</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">-</span> <span class="n">Times</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>    <span class="c1"># Total time
    </span>    <span class="n">f</span> <span class="o">=</span> <span class="mi">1</span><span class="o">/</span><span class="p">(</span><span class="n">Times</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">-</span> <span class="n">Times</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span> <span class="c1"># Sampling frequency
    </span>    <span class="nb">min</span> <span class="o">=</span> <span class="n">jnp</span><span class="p">.</span><span class="nb">min</span><span class="p">(</span><span class="n">lightcurve</span><span class="p">);</span> <span class="nb">max</span> <span class="o">=</span> <span class="n">jnp</span><span class="p">.</span><span class="nb">max</span><span class="p">(</span><span class="n">lightcurve</span><span class="p">)</span>
    <span class="n">span</span> <span class="o">=</span> <span class="nb">max</span> <span class="o">-</span> <span class="nb">min</span>
    
    <span class="c1"># Red noise kernel prior
    </span>    <span class="n">arn</span> <span class="o">=</span> <span class="k">yield</span> <span class="n">Prior</span><span class="p">(</span><span class="n">tfpd</span><span class="p">.</span><span class="n">Uniform</span><span class="p">(</span><span class="mf">0.1</span><span class="o">*</span><span class="n">span</span><span class="p">,</span> <span class="mi">2</span><span class="o">*</span><span class="n">span</span><span class="p">),</span> <span class="n">name</span><span class="o">=</span><span class="s">'arn'</span><span class="p">)</span>
    <span class="n">crn</span> <span class="o">=</span> <span class="k">yield</span> <span class="n">Prior</span><span class="p">(</span><span class="n">tfpd</span><span class="p">.</span><span class="n">Uniform</span><span class="p">(</span><span class="n">jnp</span><span class="p">.</span><span class="n">log</span><span class="p">(</span><span class="mi">1</span><span class="o">/</span><span class="n">T</span><span class="p">),</span> <span class="n">jnp</span><span class="p">.</span><span class="n">log</span><span class="p">(</span><span class="n">f</span><span class="p">)),</span> <span class="n">name</span><span class="o">=</span><span class="s">'crn'</span><span class="p">)</span>
    
    <span class="c1"># Gaussian mean priors
    </span>    <span class="n">A</span> <span class="o">=</span> <span class="k">yield</span> <span class="n">Prior</span><span class="p">(</span><span class="n">tfpd</span><span class="p">.</span><span class="n">Uniform</span><span class="p">(</span><span class="mf">0.1</span><span class="o">*</span><span class="n">span</span><span class="p">,</span> <span class="mi">2</span><span class="o">*</span><span class="n">span</span><span class="p">),</span> <span class="n">name</span><span class="o">=</span><span class="s">'A'</span><span class="p">)</span>
    <span class="n">t0</span> <span class="o">=</span> <span class="k">yield</span> <span class="n">ForcedIdentifiability</span><span class="p">(</span><span class="n">n</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="n">low</span> <span class="o">=</span> <span class="n">Times</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">-</span><span class="mf">0.1</span><span class="o">*</span><span class="n">T</span><span class="p">,</span> <span class="n">high</span> <span class="o">=</span> <span class="n">Times</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">+</span><span class="mf">0.1</span><span class="o">*</span><span class="n">T</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s">'t0'</span><span class="p">)</span>
    <span class="n">sig</span> <span class="o">=</span> <span class="k">yield</span> <span class="n">Prior</span><span class="p">(</span><span class="n">tfpd</span><span class="p">.</span><span class="n">Uniform</span><span class="p">(</span><span class="mf">0.5</span><span class="o">*</span><span class="mi">1</span><span class="o">/</span><span class="n">f</span><span class="p">,</span> <span class="mi">2</span><span class="o">*</span><span class="n">T</span><span class="p">),</span> <span class="n">name</span><span class="o">=</span><span class="s">'sig'</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">arn</span><span class="p">,</span> <span class="n">crn</span><span class="p">,</span> <span class="n">A</span><span class="p">,</span> <span class="n">t0</span><span class="p">,</span> <span class="n">sig</span>
    
    <span class="c1"># Log Likelihood Function
    </span><span class="o">@</span><span class="n">jit</span>
    <span class="k">def</span> <span class="nf">RNlog_likelihood2</span><span class="p">(</span><span class="n">arn</span><span class="p">,</span> <span class="n">crn</span><span class="p">,</span> <span class="n">A</span><span class="p">,</span> <span class="n">t0</span><span class="p">,</span> <span class="n">sig</span><span class="p">):</span>
    <span class="n">rnlikelihood_params</span> <span class="o">=</span> <span class="p">{</span><span class="s">"arn"</span><span class="p">:</span> <span class="n">arn</span><span class="p">,</span> <span class="s">"crn"</span><span class="p">:</span> <span class="n">crn</span><span class="p">,</span>
    <span class="s">"aqpo"</span><span class="p">:</span> <span class="mf">0.0</span><span class="p">,</span> <span class="s">"cqpo"</span><span class="p">:</span> <span class="mf">0.0</span><span class="p">,</span> <span class="s">"freq"</span><span class="p">:</span> <span class="mf">0.0</span><span class="p">,</span> <span class="p">}</span>
    
    <span class="n">mean_params</span> <span class="o">=</span> <span class="p">{</span> <span class="s">"A"</span><span class="p">:</span> <span class="n">A</span><span class="p">,</span> <span class="s">"t0"</span><span class="p">:</span> <span class="n">t0</span><span class="p">,</span> <span class="s">"sig"</span><span class="p">:</span> <span class="n">sig</span><span class="p">,</span> <span class="p">}</span>
    
    <span class="n">gp</span> <span class="o">=</span> <span class="n">build_gp</span><span class="p">(</span><span class="n">rnlikelihood_params</span><span class="p">,</span> <span class="n">mean_params</span><span class="p">,</span> <span class="n">Times</span><span class="p">,</span> <span class="n">kernel_type</span> <span class="o">=</span> <span class="s">"RN"</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">gp</span><span class="p">.</span><span class="n">log_probability</span><span class="p">(</span><span class="n">lightcurve</span><span class="p">)</span>
    
    <span class="c1"># Nested Sampling using Jaxns
    </span><span class="n">RNmodel</span> <span class="o">=</span> <span class="n">Model</span><span class="p">(</span><span class="n">prior_model</span><span class="o">=</span> <span class="n">RNprior_model</span><span class="p">,</span> <span class="n">log_likelihood</span><span class="o">=</span><span class="n">RNlog_likelihood2</span><span class="p">)</span>
    <span class="n">RNexact_ns</span> <span class="o">=</span> <span class="n">ExactNestedSampler</span><span class="p">(</span><span class="n">RNmodel</span><span class="p">,</span> <span class="n">num_live_points</span><span class="o">=</span> <span class="mi">500</span><span class="p">,</span> <span class="n">max_samples</span><span class="o">=</span> <span class="mf">1e4</span><span class="p">)</span>
    <span class="n">RNtermination_reason</span><span class="p">,</span> <span class="n">RNstate</span> <span class="o">=</span> <span class="n">RNexact_ns</span><span class="p">(</span><span class="n">random</span><span class="p">.</span><span class="n">PRNGKey</span><span class="p">(</span><span class="mi">42</span><span class="p">),</span> <span class="n">term_cond</span><span class="o">=</span><span class="n">TerminationCondition</span><span class="p">(</span><span class="n">live_evidence_frac</span><span class="o">=</span><span class="mf">1e-4</span><span class="p">))</span>
    <span class="n">RNresults</span> <span class="o">=</span> <span class="n">RNexact_ns</span><span class="p">.</span><span class="n">to_results</span><span class="p">(</span><span class="n">RNstate</span><span class="p">,</span> <span class="n">RNtermination_reason</span><span class="p">)</span>
    
    </code></pre></div></div>
    <p><img alt="Plot of samples" src="https://gaurav17joshi.github.io/Blogs/img/assets/rnplot.png" /></p>
    
    <p>But the main use is not just to fit a GP, but rather to acess whether it contains a QPO or not. For that, we compare the evidence (Bayes Factor) of the lightcurve for a QPO_RN Gp and RN GP, and as expected, for a high QPO sample, we get a high value of (-212 - (-262)) = 50.</p>
    
    <p>The image in the top is of the QPO model sampling.</p>
    
    <p>The corner plot shows the result of the sampling, and the frequency of 20Hz is captured well in it.</p>
    
    <p><img alt="Plot of samples" src="https://gaurav17joshi.github.io/Blogs/img/assets/qpocornerplot.png" /></p>
    
    <h2 id="tensor-flow-probability">Tensor flow probability</h2>
    <p>TensorFlow Probability (TFP) is a Python library built on TensorFlow that makes it easy to combine probabilistic models and deep learning on modern hardware (TPU, GPU).</p>
    
    <p>For this project, the jax backend requires that we also use tfpd to make our priors, and as I had to use some joint priors I explored the library.</p>
    
    <p>The joint priors could not be integrated with jaxns sampling, as multi-parameter priors lacked quantiles, but it was time well spent, as I was able to see a powerful library which had almost all kinds of priors and inferencing techniques under the sky, while supporting its own implementaions of NUTS and MCMC sampling.</p>

