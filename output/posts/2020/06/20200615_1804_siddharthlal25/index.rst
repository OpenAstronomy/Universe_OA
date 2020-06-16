.. title: Week 1 & 2: Coding Officially Begins!
.. slug:
.. date: 2020-06-15 18:04:56 
.. tags: JuliaAstro
.. author: siddharthlal25
.. link: http://siddharthlal25.github.io/blog/gsoc/gsoc-blog-2
.. description:
.. category: gsoc2020


.. raw:: html

    <h2 id="hey-sid-did-the-coding-period-officially-begin"><em>Hey Sid, did the coding period officially begin?</em></h2>
    
    <p>The community bonding period ended by the end of last month and the coding period officially began, I started to work on basic structure of the package and setting up the (not so user-friendly, PS: from astronomer’s perspective) interface for the image reduction methods.</p>
    <!-- TEASER_END -->
    
    <h2 id="hey-what-did-you-build-in-these-two-weeks"><em>Hey, what did you build in these two weeks?</em></h2>
    
    <p>I have set up the basic methods required for processing of astronomical images, let me explain it to you one by one:</p>
    
    <p>The first method implemented was <code class="language-plaintext highlighter-rouge">subtract_bias</code>, this de-biases the image with the help of a bias frame, it has a mutating version as well which de-biases the image in place.</p>
    
    <p>Next comes <code class="language-plaintext highlighter-rouge">subtract_overscan</code>, every CCD plate has some region which is unexposed to light and this is called overscan region. For pre-processing average of this region has to be obtained (there are models as well, that can fit into this region PS: model part has to be implemented later) and then subtracted from the whole image. It also has a mutating variant clubbed together.</p>
    
    <p>Next in line was <code class="language-plaintext highlighter-rouge">flat_correct</code>, this method removes the effect of variations in pixel to pixel sensitivity of detectors and by distortions in the optical path. The interesting point I learned while implementing this is fused broadcasting, believe me Julia keeps on blowing my mind with its speed and succinct syntaxes.</p>
    
    <p>Next, I implemented some basic functionalities for modifying the image sizes i.e. <code class="language-plaintext highlighter-rouge">trim</code> and <code class="language-plaintext highlighter-rouge">crop</code>. They are not much different but they are different, let me explain! Trimming is instructing the computer to remove some parts from the image, whereas cropping is instructing the computer to keep a certain part in the image (Yes, that’s the difference!). Sound’s pretty similar, right? The implementations were not that similar, <code class="language-plaintext highlighter-rouge">crop</code> was a bit tricky as compared to <code class="language-plaintext highlighter-rouge">trim</code> (check out the source code to find the difference). These functions are inherently non-mutating type, but I have also implemented a version of <code class="language-plaintext highlighter-rouge">crop</code> as <code class="language-plaintext highlighter-rouge">cropview</code>, this returns the <code class="language-plaintext highlighter-rouge">view</code> of the passed array. Mutating the <code class="language-plaintext highlighter-rouge">view</code> will mutate the initial frame passed, an analogous version for <code class="language-plaintext highlighter-rouge">trim</code> here is <code class="language-plaintext highlighter-rouge">trimview</code>.</p>
    
    <p>Next in line was the function <code class="language-plaintext highlighter-rouge">combine</code>, it basically takes a variable number of frames, stacks them together, and then finally combines them using medians (users can also have their custom combining functions).</p>
    
    <p>Okay, this one is last, <code class="language-plaintext highlighter-rouge">subtract_dark</code>, a way to reduce image noise in photographs shot with long exposure times, at high ISO sensor sensitivity, or at high temperatures. It takes advantage of the fact that two components of image noise, dark current and fixed-pattern noise, are the same from shot to shot. This function also has a mutating version clubbed along with it.</p>
    
    <h2 id="hmmm-interesting-whats-next"><em>Hmmm, interesting… What’s next?</em></h2>
    
    <p>Wait, it’s not yet over! I have also implemented these functions to interface directly with <code class="language-plaintext highlighter-rouge">FITS</code> files and <code class="language-plaintext highlighter-rouge">ImageHDU</code> (an element of the <code class="language-plaintext highlighter-rouge">FITS</code> files), putting it simply, a user can load the data (stored in <code class="language-plaintext highlighter-rouge">FITS</code> format) directly from the disk and then can play with all these functions!</p>
    
    <h2 id="okay-cool-so-whats-next-do-you-still-have-something-in-the-pipeline"><em>Okay, cool! So what’s next? Do you still have something in the pipeline?</em></h2>
    
    <p>Yes, the combine function still needs to be interfaced with <code class="language-plaintext highlighter-rouge">FITS</code> files, and once done, I will go for a release of the package. The next steps would be user-friendly processing pipelines, iterator reductions, and lot’s of documentation to be packed up together with the package.</p>
    
    <p>Stay tuned to know more!</p>
    
    <p>-sl</p>

