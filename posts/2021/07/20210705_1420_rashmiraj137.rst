.. title: Insight of Implementation of JAX to stingray- GSoC coding period!
.. slug:
.. date: 2021-07-05 14:20:55 
.. tags: stingray
.. author: Raj Rashmi
.. link: https://raj-rashmi741.medium.com/insight-of-implementation-of-jax-to-stingray-gsoc-coding-period-1756040fa5ae?source=rss-8f41b3524ac1------2
.. description:
.. category: gsoc2021


.. raw:: html

    <p>In the last blog, I wrote about Introduction to JAX and Automatic Differentiation. In this one, my plan for the next stage of implementation. Currently, I am working on the modeling notebook (<a href="https://github.com/StingraySoftware/notebooks/blob/main/Modeling/ModelingExamples.ipynb">https://github.com/StingraySoftware/notebooks/blob/main/Modeling/ModelingExamples.ipynb</a>) to re-design it using JAX, especially to make optimization more robust by having JAX compute gradients on the likelihood function.</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/380/1*u_c4S0h60T1IECOBQVTS1A.jpeg" /></figure><p>My mentor Daniela highlighted the issue that the current implementation is not robust using NumPy. The plan is to keep working on the current modeling notebook replacing NumPy by jax.numpy and also use grad, jit, vmap, random functionality of JAX.<br />When it comes to re-design, understanding the current design and the possible drawback and issues with corresponding packages comes on you first and I am trying them out. One such challenge is importing emcee into jupyter notebook for sampling. Despite making sure, I download the dependency in the current virtual environment and then making sure I import emcee into the notebook, it is still acting weird and showing an error: emcee not installed! Can’t sample! It looks like a clash of dependencies.</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/240/1*JtGB50sLscB1BBPt9k3pfw.jpeg" /><figcaption>Trying to have fun while it lasts!</figcaption></figure><p>For now, the plan is to solve every bug I face in the journey and then proceed with understanding how everything connects and the next step is to come up with the report of optimization using JAX. Stay tuned for more on how JAX can accelerate and augment the current modeling framework.</p>
    <!-- TEASER_END -->
    <p>I would recommend one video for anyone who wants to understand the functionality of JAX better and relate more to my study (click <a href="https://www.youtube.com/watch?v=0mVmRHMaOJ4&amp;ab_channel=GoogleCloudTech">here</a>).</p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=1756040fa5ae" width="1" />

