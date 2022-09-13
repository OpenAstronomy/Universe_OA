.. title: Week 12 - Final implementation into RADIS, along with a plethora of illustrative examples.
.. slug:
.. date: 2022-09-05 00:00:00 
.. tags: radis
.. author: TranHuuNhatHuy
.. link: https://https://gsoc2022tranhuunhathuy.gatsbyjs.io/10. week 12/
.. description:
.. category: gsoc2022


.. raw:: html

    <h3>1. Implementation of modules into RADIS</h3>
    <p>Finally, after being approved by Mr. Erwan, I can implement all of my modules, developed separately in my repo <a href="https://github.com/TranHuuNhatHuy/RADIS-Spectrum-Fitting-Benchmark">RADIS-Spectrum-Fitting-Benchmark</a>, into RADIS codebase. The implementation features <a href="https://github.com/radis/radis/blob/develop/radis/tools/new_fitting.py"><code class="language-text">new_fitting.py</code></a>, the new fitting module that stores all the fitting functions and associated models, whose performance confirmed after a bunch of user-testing cases.</p>
    <h3>2. Accompanied illustrative examples</h3>
    <!-- TEASER_END -->
    <p>They are gallery examples that are added into <code class="language-text">radis/examples</code>, serving as illustrative scripts for my new fitting module:</p>
    <h4>(i) <code class="language-text">plot_newfitting_Tgas.py</code></h4>
    <p>The most basic example of how to use new fitting module, including the formats and so on.</p>
    <h4>(ii) <code class="language-text">plot_newfitting_Trot-Tvib-molfrac.py</code></h4>
    <p>The real-life fitting case provided by Mr. Corentin, featuring non-LTE CO spectrum in which we will fit <code class="language-text">Trot</code>, <code class="language-text">Tvib</code> and <code class="language-text">mole_fraction</code>.</p>
    <h4>(iii) <code class="language-text">plot_newfitting_Tgas-molfrac.py</code></h4>
    <p>Mr. Minou’s user-testing case of CO absorbance spectrum near 2011 cm-1. This case features spectrum extraction from a <code class="language-text">.mat</code> MATLAB file. Originally, this file was 1.2 MB, quite large to be added to RADIS. Thus, I removed all fields unnecessary for spectrum generation, and now it only has around 400 kB left.</p>
    <h4>(iv) <code class="language-text">plot_newfitting_comparison_oldnew.py</code></h4>
    <p>Performance comparison example between <a href="https://radis.readthedocs.io/en/latest/auto_examples/plot_1T_fit.html#sphx-glr-auto-examples-plot-1t-fit-py">current 1-temperature fitting</a> and my new fitting module, under exactly the same ground-truths and settings. The benchmark result shows that, under exactly the same conditions, the new best fitted value differ 0.45% from the old one (1464.1 K from the old 1457.5 K). New fitting module requires half as many iterations as the old one and hence faster, with much smaller residual. In detail:</p>
    <div class="gatsby-highlight"><pre class="language-text"><code class="language-text">====================  PERFORMANCE COMPARISON BETWEEN 2 FITTING METHODS  ====================
    
    1. LAST RESIDUAL
    
    - Old 1T fitting example:       0.002730027027336094
    - New fitting module:           0.0005174179496843629
    
    2. NUMBER OF FITTING LOOPS
    
    - Old 1T fitting example:       32 loops
    - New fitting module:           16 loops
    
    3. TOTAL TIME TAKEN (s)
    
    - Old 1T fitting example:       4.881942987442017 s
    - New fitting module:           2.7344970703125 s
    
    ==========================================================================================</code></pre></div>
    <p>I’m not sure this superiority will persist in all cases, but even so, I believe the value of my module still lies in its practical and easy to use/apply.</p>
    <h4>(v) <code class="language-text">plot_newfitting_comparison_methods.py</code></h4>
    <p>A benchmarking example which compares performance between different <a href="https://lmfit.github.io/lmfit-py/fitting.html#choosing-different-fitting-methods">LMFIT fitting algorithms</a>. It measures their last residual (for accuracy evaluation) and number of iterations (for robustness evaluation). The benchmark result shows that, under exactly the same conditions, <code class="language-text">leastsq</code> and <code class="language-text">lbfgsb</code> work best, with <code class="language-text">leastsq</code> good at accuracy, while <code class="language-text">lbfgsb</code> good at speed (and theoretically, memory requirement). Thus, I set <code class="language-text">leastsq</code> as default method for the module, but also encourage users to switch to <code class="language-text">lbfgsb</code> in case things turn sour.</p>
    <div class="gatsby-highlight"><pre class="language-text"><code class="language-text">======================== BENCHMARKING RESULT ========================
    
    ||           METHOD          ||          RESIDUAL         || LOOPS ||
    ||---------------------------||---------------------------||-------||
    || leastsq                   || 1.4739494411950239e-07    || 24    ||
    || least_squares             || 1.2170348021620847e-05    || 1     ||
    || differential_evolution    || 1.4739855740762716e-07    || 151   ||
    || brute                     || 1.2287258962300115e-06    || 20    ||
    || basinhopping              || 7.930954059631543e-06     || 151   ||
    || ampgo                     || 4.105104127826488e-07     || 151   ||
    || nelder                    || 1.4739942144030064e-07    || 30    ||
    || lbfgsb                    || 1.4739494411955646e-07    || 28    ||
    || powell                    || 1.473949441200994e-07     || 43    ||
    || cg                        || 1.4776331905574135e-07    || 30    ||
    || cobyla                    || 1.1524288718226295e-05    || 21    ||
    || bfgs                      || 1.4776331905574135e-07    || 30    ||
    || tnc                       || 1.4740393115424221e-07    || 28    ||
    || trust-constr              || 1.4739494411948182e-07    || 26    ||
    || slsqp                     || 1.2170348021620847e-05    || 2     ||
    || shgo                      || 1.0507694502308952e-05    || 5     ||
    || dual_annealing            || 1.5455930218501237e-05    || 151   ||
    ||---------------------------||---------------------------||-------||</code></pre></div>
    <p><span class="gatsby-resp-image-wrapper" style="display: block; margin-left: auto; margin-right: auto;">
    <a class="gatsby-resp-image-link" href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/dc95cb63a4457b8bb0d3d58fca7b8bbe/2bf90/method_compare_result.png" rel="noopener" style="display: block;" target="_blank">
    <span class="gatsby-resp-image-background-image" style="display: block;"></span>
    <img alt="Method benchmarking result." class="gatsby-resp-image-image" src="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/dc95cb63a4457b8bb0d3d58fca7b8bbe/f058b/method_compare_result.png" style="width: 100%; height: 100%; margin: 0; vertical-align: middle;" title="Method benchmarking result." />
    </a>
    </span></p>

