.. title: Week 9 & 10: Beginning of the last month!
.. slug:
.. date: 2020-08-18 11:13:56 
.. tags: JuliaAstro
.. author: siddharthlal25
.. link: http://siddharthlal25.github.io/blog/gsoc/gsoc-blog-6
.. description:
.. category: gsoc2020


.. raw:: html

    <h2 id="hey-sid-lets-get-to-the-point-directly-did-your-previous-pr-get-merged"><em>Hey Sid! Let’s get to the point directly, did your previous PR get merged?</em></h2>
    
    <p>Yes! The PR which involved creation of new data structure for <code class="language-plaintext highlighter-rouge">ImageHDU</code>s got merged, the code is up and running now!</p>
    <!-- TEASER_END -->
    
    <h2 id="great-tell-us-whats-the-next-pr-all-about"><em>Great, tell us what’s the next PR all about</em>?</h2>
    
    <p>After creating the data structure <code class="language-plaintext highlighter-rouge">CCDData</code> and making it compatible with all methods in <a href="https://github.com/JuliaAstro/CCDReduction.jl/pull/31">#31</a>, I went back to my closed PR <a href="https://github.com/JuliaAstro/CCDReduction.jl/pull/30">#30</a> to take the code and make it compatible with <code class="language-plaintext highlighter-rouge">CCDData</code>. <a href="https://github.com/JuliaAstro/CCDReduction.jl/pull/30">#30</a> consists of code that enables a user to apply function on a collection of <code class="language-plaintext highlighter-rouge">ImageHDU</code>s and then save them in new <code class="language-plaintext highlighter-rouge">FITS</code> files. Now, the new PR <a href="https://github.com/JuliaAstro/CCDReduction.jl/pull/33">#33</a> enables the same functionalities but with <code class="language-plaintext highlighter-rouge">CCDData</code>s. This PR is in it’s last stages of review and will get merged soon!</p>
    
    <h2 id="hmmm-that-sounds-interesting-have-you-prepared-some-examples-to-show-the-code-in-action"><em>Hmmm, that sounds interesting, have you prepared some examples to show the code in action?</em></h2>
    
    <p>Not yet, but don’t worry, I have started working on proper usage guidelines and examples, will put it up soon!</p>
    
    <h2 id="cool-tell-us-about-your-future-plans"><em>Cool! Tell us about your future plans?</em></h2>
    
    <p>Currently, my primary goal is to get PR <a href="https://github.com/JuliaAstro/CCDReduction.jl/pull/33">#33</a> merged, after this I will put up some basic examples for complete reduction process. Following all this, I will push a new release and keep working on stretch goals!</p>
    
    <p>Stay tuned to know more!</p>
    
    <p>-sl</p>

