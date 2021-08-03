.. title: GSoC update!
.. slug:
.. date: 2021-08-03 02:00:58 
.. tags: stingray
.. author: Raj Rashmi
.. link: https://raj-rashmi741.medium.com/gsoc-update-2d16a70cc267?source=rss-8f41b3524ac1------2
.. description:
.. category: gsoc2021


.. raw:: html

    <p>GSoC started four months ago and it is not just about knowing more about the open-source that made the experience great! My mentors made it way cooler than I thought it would be. I was writing my Master thesis, for the last three months and surely, it has been a super productive summer for me! The best part is I get to do things at my own pace. My project particularly hasn’t been very easy to implement. I need to bridge a Machine Learning algorithm in the existing codebase. The fun part is venturing with different notebooks and figuring out with intuition, what could be efficient in terms of computational time, efficiency, cost etc. But as of now, the struggle has been to define the problem as exactly to achieve the result. But I will keep working on finding a solution with my mentor Daniela, and trust that struggle will bring some positive construction in Stingray.</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/0*2GcUC2cgvKapk8Lj" /></figure><p>The current data fit for the evaluation of likelihood happens using scipy.optimize.minimize function. However, there exists numerous ways to do this. SciPy optimize provides functions for minimizing (or maximizing) objective functions, possibly subject to constraints. It includes solvers for nonlinear problems (with support for both local and global optimization algorithms), linear programming, constrained and nonlinear least-squares, root finding, and curve fitting. The problem with the current minimization algorithm is that it converges at local minimum instead of global, i.e. it is not very robust. Recently, Machine Learning has evident development in such optimization tools. The strategy for ahead is that I will work on finding alternatives that potentially accelerate the code, makes it robust.</p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=2d16a70cc267" width="1" />
    <!-- TEASER_END -->

