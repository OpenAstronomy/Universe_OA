.. title: Week 11 & 12: Last two weeks of GSoC
.. slug:
.. date: 2020-08-30 11:13:56 
.. tags: JuliaAstro
.. author: siddharthlal25
.. link: http://siddharthlal25.github.io/blog/gsoc/gsoc-blog-7
.. description:
.. category: gsoc2020


.. raw:: html

    <h2 id="hey-sid-whats-the-progress-what-did-you-do-in-last-2-weeks"><em>Hey Sid! What’s the progress? What did you do in last 2 weeks?</em></h2>
    
    <p>The work was completed on time! I spent the last two weeks coding up the saving versions of <code class="language-plaintext highlighter-rouge">ccds</code>, <code class="language-plaintext highlighter-rouge">arrays</code> and <code class="language-plaintext highlighter-rouge">filenames</code>. With these, one can apply a function on the desired object (i.e. ccd or array or filename) and can also save it to FITS file. There are various options available for saving, like the prefix name of the saved file, suffix name of saved file and also the location at which to save, check out the repo for more info!</p>
    <!-- TEASER_END -->
    
    <h2 id="awesome-can-you-show-some-work-samples"><em>Awesome, Can you show some work samples?</em></h2>
    
    <p>Sure, here it is!</p>
    
    <p>This is a bias frame as captured:</p>
    
    <p align="center">
    <img src="https://raw.githubusercontent.com/siddharthlal25/blog/master/_images/bias/sample.png" />
    </p>
    
    <p>When the frame undergoes overscan subtraction followed by trimming the overscan region, it turns out to be:</p>
    
    <p align="center">
    <img src="https://raw.githubusercontent.com/siddharthlal25/blog/master/_images/bias/processed.png" />
    </p>
    
    <p>Several bias frames after overscan subtraction and trimming are stacked together and combined, this is the master bias frame used for subsequent processing of images. This is how it looks:</p>
    
    <p align="center">
    <img src="https://raw.githubusercontent.com/siddharthlal25/blog/master/_images/bias/master.png" />
    </p>
    
    <p>Next comes the processing of flat frames, this is a <em>dome flat r</em> frame as captured:</p>
    
    <p align="center">
    <img src="https://raw.githubusercontent.com/siddharthlal25/blog/master/_images/dome_flat/r/sample.png" />
    </p>
    
    <p>When the frame undergoes bias subtraction (by <em>master_bias</em>) followed by overscan subtraction and trimming, it looks something like:</p>
    
    <p align="center">
    <img src="https://raw.githubusercontent.com/siddharthlal25/blog/master/_images/dome_flat/r/processed.png" />
    </p>
    
    <p>Several <em>dome_flat_r</em> frames are stacked together and combined by mean, this results in:</p>
    
    <p align="center">
    <img src="https://raw.githubusercontent.com/siddharthlal25/blog/master/_images/dome_flat/r/master.png" />
    </p>
    
    <p>Similarly, below are processed and combined frames (i.e. master frame) of <em>dome_flat_i</em> and <em>dome_flat_z</em>:</p>
    
    <p><img src="https://raw.githubusercontent.com/siddharthlal25/blog/master/_images/dome_flat/i/master.png" width="390" height="260" style="float:left" /> <img src="https://raw.githubusercontent.com/siddharthlal25/blog/master/_images/dome_flat/z/master.png" width="390" height="260" style="float:right" /></p>
    
    <p>Now comes the most interesting part, processing of science. The raw image of scienc looks like (this one is <em>NEP2581-r</em>):</p>
    
    <p align="center">
    <img src="https://raw.githubusercontent.com/siddharthlal25/blog/master/_images/science/r/sample.png" />
    </p>
    
    <p>This frame when undergoes bias subtraction, overscan subtraction, trimming and flat correction (by the corresponding flat frame), looks like:</p>
    
    <p align="center">
    <img src="https://raw.githubusercontent.com/siddharthlal25/blog/master/_images/science/r/processed.png" />
    </p>
    
    <p>Finally these frames are stacked and combined by mean, so the final processed image looks like:</p>
    
    <p align="center">
    <img src="https://raw.githubusercontent.com/siddharthlal25/blog/master/_images/science/r/master.png" />
    </p>
    
    <p>Similarly, below are processed and combined frames (i.e. master_frame) of <em>NEP2581-i</em> and <em>NEP2581-z</em>:</p>
    
    <p><img src="https://raw.githubusercontent.com/siddharthlal25/blog/master/_images/science/i/master.png" width="390" height="260" style="float:left" /> <img src="https://raw.githubusercontent.com/siddharthlal25/blog/master/_images/science/z/master.png" width="390" height="260" style="float:right" /></p>
    
    <h2 id="thats-awesome-so-what-are-your-future-plans-about-the-package"><em>That’s awesome! So what are your future plans about the package?</em></h2>
    
    <p>There are some more advanced algorithms (i.e. cosmic ray detection, part of my future goals) left to be implemented, I have my next 2 weeks completed packed, so will implement these after the next two weeks!</p>
    
    <p>At the end, I would like to thank my mentors for being so kind and cooperative, thanks for guiding me at every step of this project! This project wouldn’t be possible without you guys, thanks a lot!</p>
    
    <p>-sl</p>

