.. title: Final Evaluation - A time to look back.
.. slug:
.. date: 2022-09-12 00:00:00 
.. tags: radis
.. author: TranHuuNhatHuy
.. link: https://https://gsoc2022tranhuunhathuy.gatsbyjs.io/11. final evaluation/
.. description:
.. category: gsoc2022


.. raw:: html

    <p><span class="gatsby-resp-image-wrapper" style="display: block; margin-left: auto; margin-right: auto;">
    <a class="gatsby-resp-image-link" href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/236320199c2c7323f80233362c6a584c/71b12/logoOA.png" rel="noopener" style="display: block;" target="_blank">
    <span class="gatsby-resp-image-background-image" style="display: block;"></span>
    <!-- TEASER_END -->
    <img alt="logo_OpenAstronomy" class="gatsby-resp-image-image" src="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/236320199c2c7323f80233362c6a584c/f058b/logoOA.png" style="width: 100%; height: 100%; margin: 0; vertical-align: middle;" title="logo_OpenAstronomy" />
    </a>
    </span></p>
    <h3>1. What I have done in OpenAstronomy and in RADIS</h3>
    <p>Throughout 3 months with RADIS, I have successfully developed a new fitting module for spectrum fitting purposes. RADIS has its own fitting feature, as shown in <a href="https://radis.readthedocs.io/en/latest/auto_examples/plot_1T_fit.html#sphx-glr-auto-examples-plot-1t-fit-py">1-temperature fit example</a>, where you have to manually create the spectrum model, input the experimental spectrum and other ground-truths into numerous RADIS native functions, as well as adjust the fitting pipeline yourself.</p>
    <p>Now with the new fitting module released, all you have to do is to prepare a <code class="language-text">.spec</code> file containing your experimental spectrum, fill some JSON forms describing the ground-truth conditions just like how you fill your medical checkup paper, call the function <a href="https://radis.readthedocs.io/en/latest/source/radis.tools.new_fitting.html#radis.tools.new_fitting.fit_spectrum"><code class="language-text">fit_spectrum()</code></a> and let it do all the work! If you are not satisfied with the result, you can simply adjust the parameters in your JSON, such as <code class="language-text">slit</code> and <code class="language-text">path_length</code>, then recall the function again, until the results are satisfied.</p>
    <p>This is way easier and more convenient than dwelling into RADIS documentation to find out and learn how to use the current example, especially for new RADIS users. Various <a href="https://github.com/radis/radis/pull/522#issue-1365475821">benchmarking efforts</a> have shown that this new fitting module has performance advantages over the old version. This new fitting module aims to provide an end-to-end fitting experience, with minimum amount of RADIS knowledge needed.</p>
    <p>You can see an overview of my project here: <a href="https://github.com/radis/radis/projects/6">https://github.com/radis/radis/projects/6</a></p>
    <h3>2. GSoC, RADIS and a learning curve that has been fulfilled</h3>
    <p>Throughout my GSoC journey with RADIS and working as a contributor, I really enjoyed all the experience of developing and contributing a meaningful improvement to a grand community-based project. Furthermore, I used to be a Computer Science majored student back in Vietnam, but after coming to Japan, I have been learning engineering for more than 2 years, enough for me to miss the old time coding projects and grinding hackathons, the days when I was truly a “CS student”. GSoC truly granted me a precious chance to rekindle the interest I have long lost, with wonderous opportunities to learn from prestigious mentors, and a huge boost for my background to get back to the run.</p>
    <p>In addition, one of the most satisfying moments in this GSoC, is when I finally nailed a bug or issue after days (or even weeks, trust me) of debugging, using the last brain cell to figure out what is the reason. The longer the suffering, the greater the hype that comes afterward. I guess we as developers all share this kind of experience often, but for a guy who starts coding again after a long time like, the ecstasy is at least three-fold.</p>
    <p>Furthermore, I don’t know what other open-source projects are, but RADIS is an extremely well-developed one. They have code coverage, pre-commit check, automatic documentation, and an extensive library of well-structured classes and methods for multiple purposes. This is a level of professional development I have never seen before, and I am extremely eager to learn all of this, not only within the GSoC, but also for a much longer time. This project also helped me to gain significant knowledge and experience</p>
    <p>So, to sum up, I really enjoyed this GSoC, especially with RADIS mentors and community. Thank you so much, GSoC and RADIS, for all of these wonderous experiences.</p>
    <h3>3. Of course, there were hard times, but hey, “Hard times come again no more”</h3>
    <p>I believe the most challenging part of my GSoC 2022 experience, is during the development of my project itself. My project is “Spectrum Fitting Improvement”, in which I will implement a brand-new fitting method that uses a different module than the original method’s, and there are several challenges that I only discovered after joining the project.</p>
    <p>Firstly, the fitting process itself is totally a black box, where I implemented a spectrum, along with its ground-truth parameters, and hopefully the result comes as I expect. In the early days, there were weeks when I could not understand why the result went bad. The reasons could be faulty ground-truth data (original ground-truth parameters are incorrect), or the spectrum itself (mistakes during spectral variable extraction), a code bug, or even from the RADIS limitation itself (currently RADIS only uses air broadening coefficients, which is not suitable for experiments in other gases). All of these costed me huge time and efforts just trying to figure out the culprit, and those were the most anxious times.</p>
    <p>Secondly, there are several problems and bugs, or required implementations that can only be discovered during the last weeks of this GSoC, which makes these time tough and sour for me.</p>
    <p>Finally, my laptop was abruptly broken beyond repair during the middle of second phase, in which I had to wait for one week before the new laptop arrived and I could continue my work. Truly the darkest, most desperate days back then.</p>
    <p>Gradually the learning curve is flattened, but still, there were tough times. Thanks to GSoC, I could experience what would happen in a real project, where you have to anticipate and be ready to deal with all possible accidents and troubles, while keeping on a tight schedule. These will be precious experience for me and my career ahead.</p>
    <h3>4. A little tribute to my mentors</h3>
    <p>Firstly, I would like to say, thank you so much, my mentors - Mr. Erwan, Mr. Minou, Anand, Gagan, as well as other unofficial mentors such as Mr. Corentin - for all the time and efforts you have put through to guide us – some random annoying students always trying to bother you with questions throughout 4 months.</p>
    <p>You helped us a lot in understanding the RADIS codebase and overall structure, as well as various skills in developing a grand-scaled project like RADIS. Throughout this GSoC, I had opportunity to familiarize with code coverage, pre-commit check and linting, automatic documentation such as readthedocs, a bunch of GitHub tips, and most important, a sheer confidence of open-source project contributing, by jumping into the source code itself, understanding it slow and steady, then finally pushing commits. Before this April, all of these were very scary for me. But now, as I look back, they are just breezes to me. Now I can truly understand and feel the scope of GSoC – to encourage students to contribute to open-source projects. Thanks to you, this is a huge success to me.</p>
    <p>All of these could not be done without you entrusting us from the very beginning of selection process. From the very moment of you accepting us, we are here today, wrapping up what we have learned, finishing our projects, and carving our names into the list of RADIS contributors. These will be precious experience for me and my career ahead.</p>
    <h3>5. And finally, to someone reading this</h3>
    <p>Ayyo, to whoever reading this,</p>
    <p>I believe that you must be some next year’s GSoC applicants sneaking around and patiently preparing for the upcoming turn. If you are reading this, then firstly I would like to say thank you for reading all the way here.</p>
    <p>I have so many things to share you about all the experiences I had during this GSoC, about every moment in all aspects during these 3 months. But I’m afraid I might accidentally spoil your fun in near future, so I will only give some necessary advice, hope they might help you enjoy better in the next GSoC.</p>
    <p>Firstly, the actual time required to complete the project always LONGER than the initially planned time, so try your best to finish everything as soon as possible.</p>
    <p>Secondly, there might be times when you confront an extremely hard issue which takes you A LOT of time and you still cannot deal with it. When that time comes, explain to your mentors, and find a way, instead of gazing on the screen trying to solve it singlehandedly while wasting 1-2 weeks for that, like I did.</p>
    <p>This is also relevant to the above advice but, if you find yourself scared to tell your mentors about a challenge you are facing, please do not be afraid and just tell them. I used to be extremely afraid of asking my mentors because sometimes they were deadly serious (in a professional way), and thus I forced myself to solve an impossible task for 2 weeks before finally reaching out to them. Please do not be afraid and share with them anything, if you want to find a solution, if you want to change the current objectives, or whatever. Just ask!</p>
    <p>And finally, try to enjoy GSoC, I meant, every moment of it. It worths. Really.</p>
    <p>Good luck to become a GSoC member and successfully carve your name among contributors!</p>
    <p>September 12, 2022
    Tran Huu Nhat Huy</p>
    <p><span class="gatsby-resp-image-wrapper" style="display: block; margin-left: auto; margin-right: auto;">
    <a class="gatsby-resp-image-link" href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/4d7ee6f3d3a81c95e441a7cc5dcadb98/ac99c/me.jpg" rel="noopener" style="display: block;" target="_blank">
    <span class="gatsby-resp-image-background-image" style="display: block;"></span>
    <img alt="Me, among the peaks of Shizuoka, Japan." class="gatsby-resp-image-image" src="https://gsoc2022tranhuunhathuy.gatsbyjs.io/static/4d7ee6f3d3a81c95e441a7cc5dcadb98/828fb/me.jpg" style="width: 100%; height: 100%; margin: 0; vertical-align: middle;" title="Me, among the peaks of Shizuoka, Japan." />
    </a>
    </span></p>

