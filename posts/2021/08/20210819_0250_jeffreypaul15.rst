.. title: GSoC 2021 — Final Report
.. slug:
.. date: 2021-08-19 02:50:29 
.. tags: SunPy
.. author: Jeffrey Paul
.. link: https://jeffrey-paul2000.medium.com/gsoc-2021-final-report-87f74dd364df?source=rss-8a453260fb1------2
.. description:
.. category: gsoc2021


.. raw:: html

    <h3>GSoC 2021 — Final Report</h3><p>Summer of 2021 held quite a few surprises for me. I’d have never imagined working with SunPy as a GSoC student and here I am concluding it with the final report. Before I summarize all the 30+ pull requests I’ve made to Sunkit-Pyvista, I just want to take a moment to than the brilliant mentors I’ve gotten to work with. The were not only patient and understanding but also extremely helpful with making me understand how everything works.</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/300/1*SExFSpEK386SN8OQ_fOtEQ.png" /></figure><p>Coming to Sunpy, or should I say Sunkit-Pyvista.</p>
    <p>Sunkit-Pyvista was created with the intention of extending Sunpy’s extensive plotting capabilities to 3D with the help of a VTK wrapper for Python — Pyvista.</p>
    <!-- TEASER_END -->
    <p>My experience with either of these libraries were extremely short-lived, but over the summer I got my hands dirty with them and loved every bit of it. I would’ve never imagined me doing a project regarding astronomy or 3D plotting, but here we are today.</p>
    <p>The original idea was proposed by one of the mentors a while and after an entire summer of working on it, I’m proud to say that I was a part of this library’s initial setup.</p>
    <p>The entire project was planned out over the 10 weeks of the GSoC period and I’m pretty proud to say that we had gotten done with everything slightly ahead of time which left us a few buffer weeks for us to review code and catch some bugs. For now, majority of the plotting/visualization functionality from Sunpy has been added to Sunkit-Pyvista, and we do have plans for some pretty cool stuff later on! I’m excited to see how this project would be used.</p>
    <p>Now, here’s a list of all the significant PRs I’ve made to the library which were carefully reviewed by both my mentors before any merges happened. The entire list of all my PRs can be found <a href="https://github.com/sunpy/sunkit-pyvista/pulls?q=is%3Apr+is%3Aclosed">here</a>. Every PR came with it’s own change-log and was carefully documented throughout.</p>
    <ol><li><a href="https://github.com/sunpy/sunkit-pyvista/pull/4">Initial setup of the code written by one of the mentors</a></li><li><a href="https://github.com/sunpy/sunkit-pyvista/pull/10">Ability to set camera coordinates functionality</a></li><li><a href="https://github.com/sunpy/sunkit-pyvista/pull/12">Addition of Pfsspy field lines visualization</a></li><li><a href="https://github.com/sunpy/sunkit-pyvista/pull/17">Drawing_Quadrangle on a 3D map</a></li><li><a href="https://github.com/sunpy/sunkit-pyvista/pull/23">Unit test time!</a></li><li><a href="https://github.com/sunpy/sunkit-pyvista/pull/24">Efficient Plotting with MultiBlocks</a></li><li><a href="https://github.com/sunpy/sunkit-pyvista/pull/26">Clip Interval for clipping of data</a></li><li><a href="https://github.com/sunpy/sunkit-pyvista/pull/29">Functionality to Plot tiny sphere at a given coordinate</a></li><li><a href="https://github.com/sunpy/sunkit-pyvista/pull/30">Adding in some examples</a></li><li><a href="https://jeffrey-paul2000.medium.com/feed#34">Ah, bug-fixes</a></li><li><a href="https://github.com/sunpy/sunkit-pyvista/pull/37">Saving and loading plots</a></li><li><a href="https://github.com/sunpy/sunkit-pyvista/pull/38">Figure tests are now a thing!</a></li><li><a href="https://github.com/sunpy/sunkit-pyvista/pull/52">Performance enhancements to draw_quadrangle</a></li><li><a href="https://github.com/sunpy/sunkit-pyvista/pull/55">Plot_limb from Sunpy, but in 3D</a></li><li><a href="https://github.com/sunpy/sunkit-pyvista/pull/73">Color enhancements</a></li></ol><p>Aside from these PRs, a lot more smaller ones were made which were related these significant ones in terms of enhancements or bug-fixes, but for the most part, everything is covered here. I think we’re set to have our 0.1 release right after the mentors take care of how the documentation works.</p>
    <p>We also planned to work on some cool <a href="https://github.com/sunpy/sunkit-pyvista/pull/57">animations</a> using the Pyvistaqt module but this was out of the scope of the original GSoC project so we’ve put a pin in it for now.</p>
    <p>Of course, my work doesn’t stop here. Being one of the main developers of this project, I’d love to continue working and building on it. Here’s to the amazing folks at SunPy and GSoC for this opportunity. 🍻</p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=87f74dd364df" width="1" />

