.. title: Week 7 & 8: The end of second month!
.. slug:
.. date: 2020-07-29 11:13:56 
.. tags: JuliaAstro
.. author: siddharthlal25
.. link: http://siddharthlal25.github.io/blog/gsoc/gsoc-blog-5
.. description:
.. category: gsoc2020


.. raw:: html

    <h2 id="hey-sid-how-was-the-second-month"><em>Hey Sid, how was the second month?</em></h2>
    
    <p>Awesome, lot’s of new learning experiences!</p>
    <!-- TEASER_END -->
    
    <h2 id="so-tell-us-about-your-progress-in-the-last-two-weeks"><em>So, tell us about your progress in the last two weeks?</em></h2>
    
    <p>These two weeks went on designing the new data structure <code class="language-plaintext highlighter-rouge">CCDData</code> for storing <code class="language-plaintext highlighter-rouge">ImageHDU</code>, this was primarily done to make accessing data and header files easier, and secondly, to tackle the file closing issue that was encountered. Let me explain the file issue in brief:</p>
    
    <p>Suppose a user uses <code class="language-plaintext highlighter-rouge">fitscollection</code> at a location and gets a list of all <code class="language-plaintext highlighter-rouge">FITS</code> files, now by using the generator methods one can collect all <code class="language-plaintext highlighter-rouge">ImageHDU</code> listed in the data frame obtained from <code class="language-plaintext highlighter-rouge">fitscollection</code>, but once the generator is executed and used for collecting the <code class="language-plaintext highlighter-rouge">ImageHDU</code>s, the generator closes the open file handles from which <code class="language-plaintext highlighter-rouge">ImageHDU</code>s were accessed, this subsequently leads to error while accessing the collected <code class="language-plaintext highlighter-rouge">ImageHDU</code>s since its source <code class="language-plaintext highlighter-rouge">FITS</code> file were closed after the execution of generator. So, to tackle this we introduced <code class="language-plaintext highlighter-rouge">CCDData</code> which couples the data and header together in memory and can be accessed even if the filehandles get closed.</p>
    
    <p>The <code class="language-plaintext highlighter-rouge">CCDData</code> is based on <code class="language-plaintext highlighter-rouge">AbstractArray</code> interface which leads to a lot of code being reused with a bit of modification in the function signature.</p>
    
    <h2 id="hmmm-so-what-next"><em>Hmmm, so what next?</em></h2>
    
    <p>I will be copying the saving versions of <code class="language-plaintext highlighter-rouge">images</code>, <code class="language-plaintext highlighter-rouge">arrays</code> and <code class="language-plaintext highlighter-rouge">filenames</code> from the previously closed PR, which would probably take a day or two. With some minor modifications, it would be good to go to the main code. After this, one can easily see the code in action! Next, I will also be implementing some macros for getting values from header of <code class="language-plaintext highlighter-rouge">ImageHDU</code> using keys directly in a method. After all this, we can bump up the version!</p>
    
    <p>Stay tuned to know more!</p>
    
    <p>-sl</p>

