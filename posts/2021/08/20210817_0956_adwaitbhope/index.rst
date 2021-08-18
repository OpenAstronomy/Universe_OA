.. title: About my Google Summer of Code Project: Part 4
.. slug:
.. date: 2021-08-17 09:56:14 
.. tags: SunPy
.. author: Adwait Bhope
.. link: https://adwaitbhope.medium.com/about-my-google-summer-of-code-project-part-4-8c7c62861783?source=rss-95bf796cebb------2
.. description:
.. category: gsoc2021


.. raw:: html

    <p>The last few days haven’t been as productive as earlier. We fixed some issues with the NDCubeSequence’s stacking PR and it looks like it’s ready to merge now. With some feedback from the community, I think it will happen soon. There have also been some minor updates to the PR that brings reproject’s other algorithms to NDCube.</p>
    <p>A new task that I’ve taken up now is identifying invariant axes in a cube. Let’s say there’s a 3D data cube where one of the axes corresponds to a quantity like time, which you don’t want to reproject onto another grid. Identifying this axis would let us reproject at only one point along this axis and then apply it throughout. This will speed up the execution significantly and require a lesser amount of memory. It’s a tricky path though and the first implementation might not be very efficient. What we’re trying to do is convert pixel coordinates to world coordinates using the source WCS, and convert it back from world to pixel using the target WCS. If the original and final pixel coordinates match, we can conclude that the axis is invariant.</p>
    <p>I shall update its progress soon, but this is all for now. GSoC is officially coming to an end, but as I said in the previous post, it doesn’t matter much for continuing my contributions to this community. I’ve been fascinated by this open-source environment and culture and learned so much along the way. I guess GSoC did serve its purpose for me.</p>
    <!-- TEASER_END -->
    <p>There’s some work at sunraster, specifically updating it to work with ndcube 2.0 (whose RC1 was released recently). That sounds like a fun project given that I’m now familiar with ndcube. In fact, that was a project I had considered applying for as part of GSoC but hadn’t. I’ll let you all know how that goes. Cheers for now, I’ll talk to you in the next one!</p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=8c7c62861783" width="1" />

