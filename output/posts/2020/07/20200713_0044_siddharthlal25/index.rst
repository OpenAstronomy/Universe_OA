.. title: Week 5 & 6: The second month begins!
.. slug:
.. date: 2020-07-13 00:44:56 
.. tags: JuliaAstro
.. author: siddharthlal25
.. link: http://siddharthlal25.github.io/blog/gsoc/gsoc-blog-4
.. description:
.. category: gsoc2020


.. raw:: html

    <h2 id="hey-sid-did-you-pass-your-first-evaluations"><em>Hey Sid, did you pass your first evaluations?</em></h2>
    
    <p>The results of the first evaluation was declared on the 4th of July and yes, I successfully completed my first evaluation!</p>
    <!-- TEASER_END -->
    
    <h2 id="how-was-your-experience-till-now"><em>How was your experience till now?</em></h2>
    
    <p>It seems as if I started working yesterday, but reality is one and a half months are complete. The experience of working on this project was awesome, all thanks to my mentors.</p>
    
    <h2 id="so-what-are-the-updates-of-these-two-weeks"><em>So, what are the updates of these two weeks?</em></h2>
    
    <p>I have been a bit puzzled in designing the end-user interface of the package, I was working on the issue <a href="https://github.com/JuliaAstro/CCDReduction.jl/issues/28">#28</a> during which Miles figured out that use of <code class="language-plaintext highlighter-rouge">ImageHDU</code> is not good, since it is not operable upon once the <code class="language-plaintext highlighter-rouge">FITS</code> file is closed. So, we won’t be able to operate on some collected <code class="language-plaintext highlighter-rouge">ImageHDU</code>s via iteration, since their respective <code class="language-plaintext highlighter-rouge">FITS</code> files would have been closed after iteration.</p>
    
    <h2 id="hmmm-that-seems-like-a-problem-so-what-next"><em>Hmmm, that seems like a problem, so what next?</em></h2>
    
    <p>We have thought of designing a new data structure <code class="language-plaintext highlighter-rouge">CCDData</code>, that would keep the header and image data of <code class="language-plaintext highlighter-rouge">ImageHDU</code> coupled and can be even accessed when the <code class="language-plaintext highlighter-rouge">FITS</code> files are closed. Once, this is done we will go for release (the major one, about which I talked in the last blog). Stay tuned to find out more!</p>
    
    <p>-sl</p>

