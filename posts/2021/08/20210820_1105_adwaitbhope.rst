.. title: Google Summer of Code Work Product Submission
.. slug:
.. date: 2021-08-20 11:05:17 
.. tags: SunPy
.. author: Adwait Bhope
.. link: https://adwaitbhope.medium.com/google-summer-of-code-work-product-submission-b35a6c6cba33?source=rss-95bf796cebb------2
.. description:
.. category: gsoc2021


.. raw:: html

    <p>This blog post is a consolidated report of my <a href="https://summerofcode.withgoogle.com/projects/#5357890195423232">GSoC ’21 project</a>. I’ve been contributing to <a href="https://github.com/sunpy/ndcube">ndcube</a> - a <a href="https://sunpy.org/">sunpy</a> affiliated package, which is itself a part of the umbrella organization called <a href="https://openastronomy.org/">openastronomy</a>. Phew, that’s quite some hierarchy.</p>
    <p>Here’s a list of pull requests that I’ve opened during the coding period:</p>
    <ol><li><a href="https://github.com/sunpy/ndcube/pull/433">Initial implementation for validating two WCS</a>: <em>Merged</em><br />Implements a function to check if two given WCS objects are compatible with each other for reprojecting the NDCube.</li><li><a href="https://github.com/sunpy/ndcube/pull/434">Reproject implementation</a>: <em>Merged</em><br />Adds a method to reproject an NDCube using the astropy package called reproject.</li><li><a href="https://github.com/sunpy/ndcube/pull/439">Reproject NDCube Documentation</a>: <em>Merged</em><br />Documentation for the above PR.</li><li><a href="https://github.com/sunpy/ndcube/pull/436">Combine cubes from NDCubeSequence using reproject</a>: <em>Unmerged</em><br />Stacks the data of all cubes in an NDCubeSequence together into one cube. This PR is ready to merge but awaits testing from the community.</li><li><a href="https://github.com/sunpy/ndcube/pull/441">Reproject NDCubeSequence Documentation</a>: <em>Unmerged</em><br />Documentation for the above PR. This will be merged after the code.</li><li><a href="https://github.com/sunpy/ndcube/pull/448">Support adaptive and exact algorithms for reproject</a>: <em>Unmerged</em><br />This PR is completed and is ready to merge.</li><li><a href="https://github.com/sunpy/ndcube/pull/459">Make reproject more efficient by identifying invariant axes</a>: <em>Unmerged</em><br />This PR is a work in progress and might need some time until it’s ready. The last commit on this PR as of writing this post can be found <a href="https://github.com/sunpy/ndcube/pull/459/commits/0c4c5a369c55f3f3e53837dd3db2b5f589b750ae">here</a>.</li></ol><p>I’ve also been writing blog posts throughout the coding period. Here are links to the 4 parts I’ve written so far: <a href="https://adwaitbhope.medium.com/about-my-google-summer-of-code-project-part-1-b56e7277046e">Part 1</a>, <a href="https://adwaitbhope.medium.com/so-here-i-am-a-month-into-the-coding-period-and-at-the-onset-of-the-first-evaluation-2e6f76a45653">Part 2</a>, <a href="https://adwaitbhope.medium.com/about-my-google-summer-of-code-project-part-3-f6354389b27f">Part 3</a>, and <a href="https://adwaitbhope.medium.com/about-my-google-summer-of-code-project-part-4-8c7c62861783">Part 4</a>. They contain a more technical description of the work along with some obstacles that we faced.</p>
    <!-- TEASER_END -->
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=b35a6c6cba33" width="1" />

