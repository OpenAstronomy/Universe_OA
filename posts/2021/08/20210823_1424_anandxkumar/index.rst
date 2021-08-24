.. title: Chapter 5: Birds of a Feather
.. slug:
.. date: 2021-08-23 14:24:32 
.. tags: radis
.. author: anandxkumar
.. link: https://anandkumar-blog.netlify.app/6/
.. description:
.. category: gsoc2021


.. raw:: html

    <p align="center">
    <span class="gatsby-resp-image-wrapper" style="display: block; margin-left: auto; margin-right: auto;">
    <a class="gatsby-resp-image-link" href="https://anandkumar-blog.netlify.app/static/91ec1b99c3601cea5ada6089b36f443e/63868/Radis.png" rel="noopener" style="display: block;" target="_blank">
    <!-- TEASER_END -->
    <span class="gatsby-resp-image-background-image" style="padding-bottom: 100%; display: block;"></span>
    <img alt="Radis.png" class="gatsby-resp-image-image" src="https://anandkumar-blog.netlify.app/static/91ec1b99c3601cea5ada6089b36f443e/63868/Radis.png" style="width: 100%; height: 100%; margin: 0; vertical-align: middle;" title="Radis.png" />
    </a>
    </span><br />
    </p>
    <p>So <code class="language-text">GSoC 2021</code> has officially ended and I can say without a doubt that what a journey it was. I recently concluded with my GSoC project, the final PR got merged and I’m quite satisfied with the outcome. </p>
    <p>Earlier we were able to find the time complexity of <strong>LBL>Voigt</strong>, <strong>DIT>Voigt</strong> and <strong>DIT>FFT</strong> (Formely known as LDM>FFT). On a small test replacing <code class="language-text">np.convolve</code> with <code class="language-text">scipy.signal.oaconvolve</code>, we were able to achieve 2 to 30 times performance boost. So we re-ran the benchmarks and were able to confirm this fact.
    You can see the result at <a href="https://anandxkumar.github.io/Benchmark_Visualization_GSoC_2021/">Benchmark Visualization GSoC 2021</a>.</p>
    <p>The above results proved that <code class="language-text">DIT&gt;Voigt</code> performs better than <code class="language-text">DIT&gt;FFT</code> in almost every case. So we decided to use <code class="language-text">DIT&gt;Voigt</code> as the default setting in <code class="language-text">Radis</code>. </p>
    <p>A <strong>predict_time()</strong> function was added, which computes the predicted time for <strong>LBL>Voigt</strong>, <strong>DIT>Voigt</strong> and <strong>DIT>FFT</strong> using the derived time complexity, and on <code class="language-text">verbose&gt;=2</code> shows the user the predicted time.</p>
    <p>Also we Bifurcated <code class="language-text">broadening_max_width</code> into 2 parameters:<br />
    •  <strong>Truncation:</strong> Used in truncation of Voigt method.<br />
    •  <strong>neighbour_lines:</strong> Increases Spectral range<br /></p>
    <p>So now users have a lot of flexibility. Based on Physics, the default value of <strong>truncation</strong> is set to <strong>50cm-1</strong> and the default value of <strong>neighbour_lines</strong> is set to <strong>0 cm-1</strong>. Apart from this, some minor improvements were done in the <code class="language-text">Profiler class</code> such as an improved algorithm is used to store data and now calculation time gets appended to the same key rather than overwriting it, which useful when we use <code class="language-text">chunksize</code> or DIT optimization for <code class="language-text">Non_equilibrium</code> conditions. </p>
    <p>So overall the code has been optimized and a user can expect a performance boost upto <strong>40x</strong> in worst scenarios. </p>
    <p>You can find all my work during the GSoC period <a href="https://github.com/radis/radis/projects/5">here</a>.</p>
    <p>It was a great experience contributing to <strong>Radis</strong> and I definitely have learned alot along the way. And a big thanks to the great mentors at Radis especially <a href="https://github.com/erwanp">Erwan Pannier</a> who guided me at every stage of the program. The road doesn’t end here as I will stick around the organisation and will always find ways to contribute to Radis. One last thanks to <strong>GSoC</strong> for providing such a wonderful opportunity.</p>
    <p align="center">
    Till we meet again, keep <b>Swinging for the fences.</b>
    <br />
    <img alt="/08e70d471ee717d1624f04f21c586cd4/spidermanMM_traversal.gif" src="https://anandkumar-blog.netlify.app/08e70d471ee717d1624f04f21c586cd4/spidermanMM_traversal.gif" width="500" /><br />
    </p>

