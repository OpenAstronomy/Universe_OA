.. title: Chapter 1: First Flight
.. slug:
.. date: 2021-06-21 22:40:32 
.. tags: radis
.. author: anandxkumar
.. link: https://anandkumar-blog.netlify.app/2/
.. description:
.. category: gsoc2021


.. raw:: html

    <p>Hey! Missed me? I’m back with another blog, the first related to the Coding Period. Got some progress and interesting observation to share!</p>
    <h2>Ready -> Set -> Code -> Analyze</h2>
    <p>The first thing I did in the coding period, was analyse the problem and get a feasible approach to resolve it.<br /></p>
    <!-- TEASER_END -->
    <p><strong>Problem:</strong> Find the complexity of the Legacy and LDM method.<br />
    <strong>Solution:</strong> Run some benchmarks and find the bottleneck step.<br /></p>
    <p>First I chose the <strong>Legacy</strong> method because if its simpler architecture. I ran some benchmarks varying the <code class="language-text">spectral range</code> of <code class="language-text">OH</code> and <code class="language-text">CO2</code> molecule to get similar number of lines. I kept parameters like <code class="language-text">pressure</code>, <code class="language-text">temperature</code>, <code class="language-text">broadening_max_width</code>, <code class="language-text">wstep</code>, etc constant to see the dependence of Legacy method on <strong>Spectral range</strong>. <br /></p>
    <p>In order to get similar number of lines, I created a function which will take the <strong>Spectrum Factory</strong> <code class="language-text">dataframe</code> and select the target number of lines. But the issue with Pandas dataframe is that when modify the dataframe there are chances that the metadata will get lost and we will no longer be able to do Spectrum calculation. To avoid this we have to drop the right number of lines with <code class="language-text">inplace=True</code>. So we will need to fix the number of lines and then we can proceed ahead with the benchmarking. Every parameter is the same except the Spectral Range.  Full code <a href="https://gist.github.com/anandxkumar/cbe12f47170e1d71a82f4b246bd01dcc">here</a>.<br /></p>
    <p>Earlier we assumed that the complexity of Legacy method is: <br />
    <strong><code class="language-text">Voigt Broadening = Broadening_max_width * spectral_range/math.pow(wstep,2) * N</code></strong> <br /></p>
    <p>Thus I was expecting to have different calculation time for both benchmarks. But to my surprise the computational times were almost equivalent! I re-ran each benchmarks <strong>100 times</strong> just to be sure and more precise about it. Following were the observations:<br /></p>
    <ul>
    <li>Number of lines - <b>{‘OH’: 28143, ‘CO’: 26778}</b></li>
    <li>Total Calculation time(Avg) -  <b>{‘OH’: 4.4087, ‘CO’: 3.8404000000000003}</b></li>
    <li>Total Voigt_Broadening TIME(Avg) - <b>{‘OH’: 3.1428814244270327, ‘CO’: 3.081623389720917}</b></li>
    <li>spectral_range - <b>{‘OH’: 38010, ‘CO’: 8010}</b></li>
    <li>Legacy_Scale - <b>{‘OH’: 4x10^14, ‘CO’: 8x10^13}</b></li>
    </ul>
    <p>There are some inference we can make from the above observation:<br /></p>
    <p><strong>A)</strong> The bottleneck step(Voigt Broadening) loosely depends on <code class="language-text">Spectral Range</code>.<br />
    <strong>B)</strong> The complexity of Voigt Broadening needs to be modified because there is a difference of order of <strong>~10</strong> in the Legacy Scaled value of OH and CO2.<br /></p>
    <p align="center">
    <span class="gatsby-resp-image-wrapper" style="display: block; margin-left: auto; margin-right: auto;">
    <a class="gatsby-resp-image-link" href="https://anandkumar-blog.netlify.app/static/d9b32b4e96e6cd9a91016a49ad940239/0b533/Blog2.png" rel="noopener" style="display: block;" target="_blank">
    <span class="gatsby-resp-image-background-image" style="padding-bottom: 100%; display: block;"></span>
    <img alt="Blog2" class="gatsby-resp-image-image" src="https://anandkumar-blog.netlify.app/static/d9b32b4e96e6cd9a91016a49ad940239/0b533/Blog2.png" style="width: 100%; height: 100%; margin: 0; vertical-align: middle;" title="Blog2" />
    </a>
    </span><br />
    <b>Credits - Me :p</b><br />
    </p>
    <p>So in order to do some analysis, we first need data of different steps in the broadening phase and conditions of various Spectrum which brings me to the <strong>Code</strong> part in <strong>Coding Period.</strong><br /></p>
    <h2>Profiler Class</h2>
    <p>The aim of this class is to replace all the print statements by a common <code class="language-text">start</code>, <code class="language-text">stop</code>, <code class="language-text">_print</code> method. Earlier each step computational time was done using <code class="language-text">time()</code> library. Now the whole codebase is being refactored with the Profiler class that will do all the work based on the <code class="language-text">verbose</code> level. In addition to this the biggest benefit is that each step will be stored in a dictionary with its computational time that will help me gather data to find which step is in actual bottleneck and further which part of the function is the most expensive time wise. A simple example is below:</p>
    <p><strong>Before:</strong><br /></p>
    <div class="gatsby-highlight"><pre class="language-text"><code class="language-text">if __debug__:
    t0 = time()
    ..........
    ..........
    if __debug__:
    t1 = time()
    .........
    .........
    if __debug__:
    if self.verbose &gt;= 3:
    printg(&quot;... Initialized vectors in {0:.1f}s&quot;.format(t1 - t0))</code></pre></div>
    <p><strong>After:</strong><br /></p>
    <div class="gatsby-highlight"><pre class="language-text"><code class="language-text">self.profiler.start(
    key=&quot;init_vectors&quot;, verbose=3, details=&quot;Initialized vectors&quot;
    )
    .........
    .........
    self.profiler.stop(&quot;init_vectors&quot;)</code></pre></div>
    <p>So using a common key we can make it happen. This will be stored in the conditons of <code class="language-text">Spectrum</code> object in the <code class="language-text">'profiler'</code> key. All these Spectrums and their conditions can be exported using a <a href="https://radis.readthedocs.io/en/latest/spectrum/spectrum.html#spectrum-database">SpecDatabase</a>. This will create a csv file comprising of all the parameters of all Spectrums which will be useful in getting some insights.
    -> <a href="https://github.com/radis/radis/pull/286">PR LINK</a></p>
    <h2>Digging in whiting_jit</h2>
    <p>Based on several benchmarks, it is estimated that around <strong>70-80%</strong> time is spent on calculating the broadening. The broadening part has the following hierarchy:<br />
    <b></p>
    <div class="gatsby-highlight"><pre class="language-text"><code class="language-text">_calc_broadening()
    -&gt; _calc_lineshape()
    -&gt; _voigt_broadening()
    -&gt; _voigt_lineshape()
    -&gt; whiting_jit()</code></pre></div>
    </b>
    <p>On close inspection we observed that <strong>80-90%</strong> time is spent on <code class="language-text">whiting_jit</code> process. Going further down in <code class="language-text">whiting_jit</code>, <strong>60-80%</strong> time is spent on <strong>lineshape calculation.</strong> Below is the formula:<br /></p>
    <div class="gatsby-highlight"><pre class="language-text"><code class="language-text">lineshape = (
    (1 - wl_wv) * exp(-2.772 * w_wv_2)
    + wl_wv * 1 / (1 + 4 * w_wv_2)
    # ... 2nd order correction
    + 0.016 * (1 - wl_wv) * wl_wv * (exp(-0.4 * w_wv_225) - 10 / (10 + w_wv_225))
    )</code></pre></div>
    <p>The whole process can be divided into 4 parts:<br /></p>
    <div class="gatsby-highlight"><pre class="language-text"><code class="language-text">    part_1 =   (1 - wl_wv) * exp(-2.772 * w_wv_2)
    
    part_2 =    wl_wv * 1 / (1 + 4 * w_wv_2)
    
    # ... 2nd order correction
    part_3 =  0.016 * (1 - wl_wv) * wl_wv * exp(-0.4 * w_wv_225)
    
    part_4 =  - 10 / (10 + w_wv_225)</code></pre></div>
    <p>The complexity of each part comes out: <br />
    <b></p>
    <div class="gatsby-highlight"><pre class="language-text"><code class="language-text">    o1 = broadening__max_width * n_lines / wstep
    
    O(part_1) = n_lines * o1
    O(part_2) = n_lines * 4 * o1
    O(part_3) = (n_lines)**2 * o1
    O(part_4) = o1 </code></pre></div>
    </b>
    <p>Running several benchmark showed us that <strong>part_3</strong> takes the most time out of all steps. So clearly we can see that the complexity of Legacy method is not dependent on
    Spectral Range but rather <code class="language-text">Number of Calculated Lines</code>,<code class="language-text">broadening__max_width</code> and <code class="language-text">wstep</code>. It may seem that the complexity of Legacy method is:<br /></p>
    <p align="center"><b> n_lines^2 * broadening__max_width * n_lines / wstep</b></p> <br />
    <p>But inorder to prove this we need more benchmarks and evidence to verify this and it may involve normalization of all steps in lineshape calculation!<br /> </p>
    <p>So the goal for the next 2 weeks is clear:<br />
    <b>i)</b> Refactor the entire codebase with Profiler.<br />
    <b>ii)</b> Find the complexity of <strong>Legacy Method</strong> with the help of more benchmark and analysis.<br />
    <b>iii)</b> Do the same for <strong>LDM Method</strong>!<br /></p>
    <p>Ok I guess time’s up! See you after 2 weeks :)</p>

