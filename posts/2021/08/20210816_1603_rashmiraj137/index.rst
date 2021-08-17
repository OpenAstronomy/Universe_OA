.. title: Time to review my GSoC Project
.. slug:
.. date: 2021-08-16 16:03:25 
.. tags: stingray
.. author: Raj Rashmi
.. link: https://raj-rashmi741.medium.com/time-to-review-my-gsoc-project-c34297f2dc81?source=rss-8f41b3524ac1------2
.. description:
.. category: gsoc2021


.. raw:: html

    <p>With the end of the GSoC project, I will give this blog to summarise the JAX based optimization to analyze its applicability to enhance the loglikelihood calculation. The goal is to analyze, (i) the performance of different optimizers to evaluate the loglikelihood function, (ii) demonstrated the robustness of JAX to calculate gradients. And talk about the current code and corresponding improvement due to JAX.</p>
    <p>The application of loglikelihood fitting to periodograms is discussed in [1]. Let us start with analyzing best-fit power spectrum (i) with different sets of optimizers namely: <em>minimize(method=’Nelder-Mead’, ’Powell’, ’CG’, ’BFGS’, ’Newton-CG’, ’L-BFGS-B’, ’TNC’, ’COBYLA’, ’SLSQP’, ’trust-constr’, ’dogleg’, ’trust-ncg’, ’trust-krylov’, ’trust-exact’). </em>The problem setting shifts the start and test parameters to study the graph of best fit optimizer using different “methods” listed above. First, we will stick with the Powell optimizer and try to check what is the current sensitivity of the implementation.</p>
    <p>Currently, we seek to find a solution to the problem when the optimization algorithm often gets stuck in local minima, terminate without meeting its formal success criteria, or fails due to any contributing factor. Possible ways are: (1) add more Lorentzian components, (2) reduce the amplitude, (3) start the optimization process with parameters very far away from the true parameters, (4) experiment with the different optimizers/ “methods” to investigate if there is more superior algorithm compared to Powell.</p>
    <!-- TEASER_END -->
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*oEfdtoL2Fa0XAbjmugMvnA.png" /><figcaption>Reference: blog.gitguardian.com</figcaption></figure><p>So far the <em>Powell</em> and <em>Nelder-Mead </em>gives almost the same best-fit curve compared to other optimizers, surprisingly even better than <em>BFGS(which is a well-known </em>numerical optimizer for an iterative method for solving unconstrained nonlinear optimization problems. This directs to more investigation with (1) and (2) and (3). Both (2) and (3) makes the algorithm fail with the current <em>scipy.optimize.minimize, </em>and we can see the<em> </em>graph as given below.</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*1SA0BwGc48I8qRozxuK6CQ.png" /></figure><p>I am still holding on to try <a href="https://jax.readthedocs.io/en/latest/_autosummary/jax.scipy.optimize.minimize.html">jax.scipy.optimize.minimize</a> instead of <a href="https://jax.readthedocs.io/en/latest/_autosummary/jax.scipy.optimize.minimize.html">scipy.optimize.minimize</a> and analyze the increment in robustness. Another way to enhance the current algorithm alongside experimenting with different optimisers is:</p>
    <ol><li>Use a different gradient finding method.</li><li>Speed up objective function.</li><li>Reduce the number of design variables.</li><li>Choose a better initial guess.</li><li>Use parallel processing.</li></ol><p>In my next blog, I will provide a more detailed explanation of current events. In this blog, I highlighted the emphasis of analysis.</p>
    <p>References:</p>
    <p>[1] Maximum likelihood fitting of X-ray power density spectra: Application to high-frequency quasi-periodic oscillations from the neutron star X-ray binary 4U1608-522. Didier Barret, Simon Vaughan. <a href="https://arxiv.org/abs/1112.0535">https://arxiv.org/abs/1112.0535</a></p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=c34297f2dc81" width="1" />

