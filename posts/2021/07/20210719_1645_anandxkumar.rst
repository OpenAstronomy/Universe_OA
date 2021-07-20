.. title: Chapter 3: Midnight Sun
.. slug:
.. date: 2021-07-19 16:45:32 
.. tags: radis
.. author: anandxkumar
.. link: https://anandkumar-blog.netlify.app/4/
.. description:
.. category: gsoc2021


.. raw:: html

    <p>Phase 1 is over :) ! We are half way through the journey. Great learning experience so far. Let’s find out what I accomplished during the previous 2 weeks (since I believe you have been following me from the beginning ;)</p>
    <p>Getting straight to the point, most of the time was spent on fixing bugs of the Profiler class and other Pull requests regarding documentation and gallery example. A new gallery example was added to demonstrate the working of <code class="language-text">SpecDatabase</code> and <code class="language-text">init_database</code> to help user to store all Spectrums in the form of a <code class="language-text">.spec</code> file and all input parameters in a <code class="language-text">csv</code> file under a folder. The same folder can be used to retrieve all Spectrums thus saving a lot of time and also no need to recompute all spectrums, so quite a handy feature. Radis has <code class="language-text">plot_cond</code> function to plot a 2D heat map based on the parameters in csv file for all spectrums. Creates some good looking and informative plots :) <br />-> <a href="https://radis.readthedocs.io/en/latest/auto_examples/plot_SpecDatabase.html#sphx-glr-auto-examples-plot-specdatabase-py">Gallery Example</a><br /></p>
    <p>Back to the analysis part; for LDM we expected:<br /></p>
    <!-- TEASER_END -->
    <div class="gatsby-highlight"><pre class="language-text"><code class="language-text">time(LDM_fft) ~ c2*N_lines + c3*(N_G*N_L + 1)*N_v*log(N_v) (where N_v =  Spectral Points)
    time(LDM_voigt) ~ c2*N_lines + c3'*(N_G*N_L + 1)*N_truncation*log(N_truncation) (where N_truncation = broadening width / wstep)</code></pre></div>
    <p>For Legacy method I was able to prove that Calculation Time is independent of Spectral Range if we keep the N<em>lines and wstep constant but same is not for LDM voigt.<br />
    A straight up comparison between Legacy and LDM voigt for NO  keeping N</em>lines and wstep constant and varying the Spectral range:
    <a href="https://public.tableau.com/app/profile/anand.kumar4841/viz/LDMvsLegacyforSpectralRangeN_linesconstantandVoigtbroadening/Sheet1">Link</a><br />
    Here also for None optimization we are getting constant time for different spectral range but a linear dependency for LDM Voigt which will fail the assumption of</p>
    <div class="gatsby-highlight"><pre class="language-text"><code class="language-text">t_LDM_voigt ~ c2*N_lines + c3'*(N_G*N_L + 1)*N_truncation  *log(N_truncation  )
    but rather t_LDM_voigt ~ c2*N_lines + c3*(N_G*N_L + 1)*N_v*log(N_v)</code></pre></div>
    <h2>A New Discovery</h2>
    <p>On generating spectrum for millions of lines, one unique observation was seen. The bottleneck step was no longer taking the most time. Max time was spent upon an unknown process. Upon deep analysis it was found a part of code was using <code class="language-text">sys.getsizeof()</code> to get the size of dataframe, and when the dataframe consisited of <code class="language-text">object</code> type columns with millions of lines, most of the time was spent on this step only.</p>
    <p><span class="gatsby-resp-image-wrapper" style="display: block; margin-left: auto; margin-right: auto;">
    <a class="gatsby-resp-image-link" href="https://anandkumar-blog.netlify.app/static/95eda74e349d883f4a1fcc85291a91cc/6af66/ldm.png" rel="noopener" style="display: block;" target="_blank">
    <span class="gatsby-resp-image-background-image" style="display: block;"></span>
    <img alt="complexity.jpg" class="gatsby-resp-image-image" src="https://anandkumar-blog.netlify.app/static/95eda74e349d883f4a1fcc85291a91cc/f058b/ldm.png" style="width: 100%; height: 100%; margin: 0; vertical-align: middle;" title="complexity.jpg" />
    </a>
    </span><br /></p>
    <p>We replaced it with <code class="language-text">memory_usage(deep=False)</code> with a different threshold which made computation almost <strong>2x</strong> faster.</p>
    <p><span class="gatsby-resp-image-wrapper" style="display: block; margin-left: auto; margin-right: auto;">
    <a class="gatsby-resp-image-link" href="https://anandkumar-blog.netlify.app/static/28b1ad4d276fa9921520808bc6360002/87488/ba.png" rel="noopener" style="display: block;" target="_blank">
    <span class="gatsby-resp-image-background-image" style="display: block;"></span>
    <img alt="complexity.jpg" class="gatsby-resp-image-image" src="https://anandkumar-blog.netlify.app/static/28b1ad4d276fa9921520808bc6360002/f058b/ba.png" style="width: 100%; height: 100%; margin: 0; vertical-align: middle;" title="complexity.jpg" />
    </a>
    </span><br /></p>
    <p>So phase 1 is over,and phase 2 is going to begin which will mainly focus on optimizing the the existing LDM method with appropriate truncation and other possible areas!</p>
    <p>See you on the other side of the sea ;)</p>
    <p><span class="gatsby-resp-image-wrapper" style="display: block; margin-left: auto; margin-right: auto;">
    <a class="gatsby-resp-image-link" href="https://anandkumar-blog.netlify.app/static/6c695ad1951b1c737cc12c701ffce0e4/2551b/other.jpg" rel="noopener" style="display: block;" target="_blank">
    <span class="gatsby-resp-image-background-image" style="display: block;"></span>
    <img alt="complexity.jpg" class="gatsby-resp-image-image" src="https://anandkumar-blog.netlify.app/static/6c695ad1951b1c737cc12c701ffce0e4/828fb/other.jpg" style="width: 100%; height: 100%; margin: 0; vertical-align: middle;" title="complexity.jpg" />
    </a>
    </span><br /></p>

