.. title: Summer with SunPy ☀️
.. slug:
.. date: 2021-06-03 08:34:39 
.. tags: SunPy
.. author: Jeffrey Paul
.. link: https://jeffrey-paul2000.medium.com/summer-with-sunpy-%EF%B8%8F-f51440cfe218?source=rss-8a453260fb1------2
.. description:
.. category: gsoc2021


.. raw:: html

    <p>A couple of months ago, I was introduced to the world of open source by a few peers of mine and despite having the many unanswered questions about why open source software exists, eventually I decided to try my hand at it.</p>
    <p>In my previous post I had mentioned how I’d continue to be a contributor to SunPy regardless of the outcome of GSOC.</p>
    <blockquote>“I made a promise to myself that regardless of the outcome of my proposal, I will continue to contribute to this organization that taught me so much.”</blockquote><p>With that in mind, this showed up a couple of weeks later :</p>
    <!-- TEASER_END -->
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/638/1*WnrYxkGo8nkbdKoDz-xCAA.png" /></figure><p>Turns out things went my way and this gave me the motivation I was lacking for this summer.</p>
    <p>Well, my project is quite simple actually. <strong>SunPy</strong> allows for visualization of spatially-aware data by means of Map objects. These objects have extensive 2D visualization capabilities for plotting various coordinate objects.</p>
    <p>My responsibility will be experimenting and tinkering around with these visualization capabilities and converting them into 3D with some extra added functionality! Seems pretty cool right? Well, it is!</p>
    <p>Here’s an example of what I’d be doing :</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/191/1*QlX4LmZXc7e_C96fL-qHRA.png" /><figcaption>Converting this</figcaption></figure><figure><img alt="" src="https://cdn-images-1.medium.com/max/917/1*Omv0aIRFxR7VR9F6ruIBaQ.png" /><figcaption>To this!</figcaption></figure><p>The entire project involves using <strong>Pyvista</strong>, a python api for using the Visualization Toolkit. The entire project is part of a separate package affiliated with SunPy and you can find it <a href="https://github.com/sunpy/sunkit-pyvista/">here</a>.</p>
    <p>My first 2 weeks with SunPy went great! It involved learning and tinkering around with <strong>Sphinx </strong>for documentation which I had never used before, figuring out what goes where and how it happens was pretty interesting.</p>
    <p>We’ve finally decided on how we’d go about producing unit tests for these plots, we uncovered an issue with <strong>PyVista </strong>as well. The project mentors and I had a few discussions on how to render these 3D plots for display in our documentation, how this would impact the continuous integration builds as our current one seemed to be having a few issues with <strong>XVFB</strong> server and displaying the plots correctly. These issues are yet to be fixed and a concrete solution is to be decided on.</p>
    <p>A few pull requests with the initial code to set up the package and provide basic plotting functionality was merged in and the package finally produces a 3D plot for any map in <strong>Sunpy</strong>!</p>
    <p>This marked the end of the community bonding phase of the project and in the coming weeks, I’ll be working on experimenting with rotation and <strong>AstroPy’s SkyCoord</strong>. I’ll also be working on some plotting field lines from <strong>PfssPy</strong> which would add some extra functionality to the library. I’ve finally gotten into getting my hands dirty with the code and I’m loving it.</p>
    <p>Well, that’s pretty much it for the first fortnight with <strong>SunPy</strong>, looking forward to see how this project turns out, everything seems to be going well and I’m grateful to be working on this project with my mentors.</p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=f51440cfe218" width="1" />

