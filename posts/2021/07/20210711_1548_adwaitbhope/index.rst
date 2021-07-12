.. title: So here I am, a month into the coding period and at the onset of the first evaluation.
.. slug:
.. date: 2021-07-11 15:48:45 
.. tags: SunPy
.. author: Adwait Bhope
.. link: https://adwaitbhope.medium.com/so-here-i-am-a-month-into-the-coding-period-and-at-the-onset-of-the-first-evaluation-2e6f76a45653?source=rss-95bf796cebb------2
.. description:
.. category: gsoc2021


.. raw:: html

    <h3>About my Google Summer of Code Project: Part 2</h3><p>So here I am, a month into the coding period and at the onset of the first evaluation. I talked about what my project was in the <a href="https://adwaitbhope.medium.com/about-my-google-summer-of-code-project-part-1-b56e7277046e">last blog</a>, and I’ll use this one to cover the progress we’ve made.</p>
    <p>All the work so far has been compiled into 3 messy PRs. To start with, reprojecting an NDCube onto another WCS requires that you first validate whether the source and target WCS transformations are in fact compatible. It’s no good if they represent an entirely different coordinate system. They need to have the same number of world axes and in the same order. The first PR introduces a function to check this and it has been merged into the main branch.</p>
    <p>The second one implements the actual reproject method on NDCube, leveraging the reproject package. Currently, it serves as a wrapper around the interpolation algorithm, with plans to support more algorithms soon. But that bit is dependent on optimizing the current functionality by being a little smarter about detecting axes that do not need to be modified. This would also help speed up the function AND use less memory!</p>
    <!-- TEASER_END -->
    <p>The third PR is an interesting one. There is a class called NDCubeSequence, which is, as the name says, a sequence of NDCubes. Think of it as multiple NDCubes arranged in an array with some additional convenient functionality. Let’s say you have some information about an image that isn’t really related to any of the axes but applies to the whole image — the timestamp of the image, for example. If you have multiple similar images taken at different timestamps, they can form an NDCubeSequence, where the sequence axis represents time. You can also combine the sequence axis with an existing axis of the cubes so that they form a large panorama or mosaic, which is wider than the field of view that could’ve been captured in one image.</p>
    <p>In most cases, the individual cubes do not share the same WCS object even if they are images of the same entity. This is because of effects like wobble or rotation that introduce slight changes in the WCS. So we used the previously implemented reproject method to get all the cubes on the same grid, so they can share the WCS. Then, we stacked the data of all cubes together in one single numpy array, introducing an extra dimension that corresponds to the sequence. A new WCS is also constructed that includes this newly formed dimension. You combine this data and the WCS, and voila, you have reduced the NDCubeSequence to an NDCube!</p>
    <p>The next steps would be to refine this behaviour and try to optimize wherever possible. Then we’ll try to get these 2 remaining PRs merged in the main branch to avoid getting inundated later. So, this is all for this post, see you in the next one!</p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=2e6f76a45653" width="1" />

