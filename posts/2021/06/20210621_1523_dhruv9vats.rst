.. title: GSoC Progress Report? Almost Done!
.. slug:
.. date: 2021-06-21 15:23:27 
.. tags: stingray
.. author: Dhruv Vats
.. link: https://dhruv9vats.medium.com/gsoc-progress-report-almost-done-6239f301b23?source=rss-f1d0746d59b5------2
.. description:
.. category: gsoc2021


.. raw:: html

    <p>With only 2 weeks into the coding period, it feels good to say that the bulk of the work associated with the 2 milestones is <em>almost </em>done. Almost because the newly added functionality is yet to be battle-tested and while there is always room for change and improvements, my focus will be shifting from the main objective to the optional objectives.</p>
    <h4>The Project</h4><p>Scientific jargon ahead!</p>
    <p>The study and interpretation of time-series data have become an integral part of modern-day astronomical studies and a common approach for characterizing the properties of time-series data is to estimate the power spectrum of the data using the periodogram. But the periodogram as an estimate suffers from being:</p>
    <!-- TEASER_END -->
    <ol><li>Statistically inconsistent (that is, its variance does not go to zero as the number of data samples reach infinity),</li></ol><p>2. Biased for finite samples, and</p>
    <p>3. Suffers from spectral leakage.</p>
    <figure><a href="https://github.com/StingraySoftware/stingray"><img alt="" src="https://cdn-images-1.medium.com/max/700/1*5GHLU2O-S9d06amIH5ESBA.png" /></a><figcaption>Stingray is a spectral-timing software package for astrophysical X-ray (and other) data.</figcaption></figure><p>My project aimed at implementing and integrating a superior spectral estimation technique, known as the Multitaper periodogram, into a Software Package called Stingray, a sub-organization of OpenAstronomy.</p>
    <p>This Multitaper algorithm uses windows or tapers (bell-shaped functions), which are multiplied with the time-series data before finding its frequency domain estimate. These windows, called the discrete prolate spheroidal sequences (DPSS), help mitigate the problems mentioned above.</p>
    <p>Any more technical stuff and this blog will start taking the shape of my proposal, so I’ll leave it here, but for anyone more interested, <a href="https://www.dropbox.com/s/g2m2p10en8ygpmz/Proposal.pdf?dl=0">here</a> is the proposal.</p>
    <h4>The Process</h4><p>I started working on the project in early March, before submitting the proposal, and it initially included writing a wrapper around an external package to make the use of this tool coherent with the rest of the project. While a proof-of-concept implementation was put together, it was later decided to use SciPy to do the grunt work, as it already was a dependency, somewhat changing the initial milestones.</p>
    <p>So in a way, I was already working on the project before the results were announced and ended up opening a pull request with the newly added method 1 week into the coding period and it got merged a week later, which happened to be fairly early in the GSoC program coding timeline. Perks of open-source?!</p>
    <p>So while there are sure to be improvements and additions in terms of coherency and features, this does give a bit more breathing room and time for experimentation and exploration, and I’ll try and make good use of it, primarily by working on the optional but quite good-to-have features.</p>
    <p>For anyone interested, <a href="https://github.com/StingraySoftware/stingray/pull/578">here</a> is the PR.</p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=6239f301b23" width="1" />

