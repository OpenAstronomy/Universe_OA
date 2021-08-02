.. title: About my Google Summer of Code Project: Part 3
.. slug:
.. date: 2021-08-01 18:53:41 
.. tags: SunPy
.. author: Adwait Bhope
.. link: https://adwaitbhope.medium.com/about-my-google-summer-of-code-project-part-3-f6354389b27f?source=rss-95bf796cebb------2
.. description:
.. category: gsoc2021


.. raw:: html

    <p>First and foremost, I celebrate the merging of the PR that brings reproject to NDCube! It defines a base-level functionality or MVP if you want to call it that, along with some relevant documentation. We also mark the release of ndcube’s 2.0 RC1. This is an important milestone since ndcube 2.0 brings significant changes, owing to the implementation of the new high-level WCS API.</p>
    <p>Our next plan of action was to extend the method to use other algorithms that reproject supports. Interpolation (the one that the above PR implements) supports multi-dimensional cubes but “adaptive” and “exact” algorithms do not. For the time being, they only work on 2D cubes containing celestial axes. So that’s what I’ve implemented them for in a new PR, which is currently under review and should hopefully get merged soon.</p>
    <p>The only problem for this PR was identifying celestial axes. We’ve taken a shortcut to solve this quickly and avoid creating a blocker, but a better implementation is due.</p>
    <!-- TEASER_END -->
    <p>The NDCubeSequence PR that I talked about in the last blog post hit a few unexpected edge cases which are under work.</p>
    <p>We’re nearing the end of GSoC’s official timeline and while that is saddening, the good thing is that open source doesn’t need a GSoC timeline for contributing. I do hope that I’ll be able to tie up any loose ends before the end date, but I suppose that does not matter in the community’s bigger picture. Functional additions, bug fixes, and performance improvements are always going to be coming in for reproject, and I plan to maintain at least that bit of code (or more) in the future.</p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=f6354389b27f" width="1" />

