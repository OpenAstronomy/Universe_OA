.. title: GSoC - Community Bonding
.. slug:
.. date: 2023-06-02 00:00:00 
.. tags: stingray
.. author: Gaurav Joshi
.. link: https://Gaurav17Joshi.github.io/Blogs/2023/06/02/Cb.html
.. description:
.. category: gsoc2023


.. raw:: html

    <h2 id="what-is-the-community-bonding-period">What is the Community Bonding Period?</h2>
    <p>The community bonding period is the 3 weeks between GSoC student acceptance and the start of coding date. This is a vital time to engage with your GSoC contributor and set them up for success. In this time, I got in touch with my two mentors as well as my fellow Gsocers. We made plans for our project with my mentor describing some important aspects of it. The feature that I am implimenting is a GP interface for QPO oscillations, but it is useful for many other astronomical timeseries anaylsis so we discussed how it should be both flexible for the user, as well as automate all the complicated stuff.</p>
    
    <!-- TEASER_END -->
    <p>I studied the various python packages, that would be used, and also created a proof of concept code for the feature.</p>
    
    <h2 id="packages-used">Packages used</h2>
    <p>In this project, I will be using many differnent packages, hense I worked with them to understand their features in this CB period.</p>
    <ol>
    <li>Jax: Jax is an open-source Python library designed to facilitate high-performance numerical computing and automatic differentiation. It provides a combination of functional programming concepts and powerful array operations, making it well-suited for machine learning and scientific computing tasks. Jax can be understood as numpy on accelerators, with three important features, Jax.grad, Jax.jit and Jax.vamp.
    Jax.grad is used to calculate automatic derivatives of complex functions.
    Jax.jit is used to compile the code on XLA using the jaxpr language.
    Jax.vmap is used to wrap functions for batches without explicitly doing so.</li>
    </ol>
    
    <p>With its strong integration with NumPy and compatibility with modern hardware accelerators, Jax has become a popular choice among researchers and practitioners in the machine learning community.</p>
    
    <ol>
    <li>
    <p>TinyGP: TinyGP is a Python package aimed at providing a lightweight and user-friendly framework for Gaussian Processes (GPs). TinyGP offers essential functionalities for modeling and inference with GPs, including covariance functions, hyperparameter optimization, and predictive uncertainty estimation. The package is written in jax and well integrated with various optimisation libraries.</p>
    </li>
    <li>
    <p>Numpyro: NumPyro is a powerful probabilistic programming library built on top of NumPy, JAX, and Pyro. It combines the ease of use and familiar syntax of NumPy with the flexibility and automatic differentiation capabilities of JAX to enable efficient and scalable Bayesian inference. NumPyro provides a wide range of probabilistic models, inference algorithms, and tools for model specification, allowing users to express complex probabilistic models and perform inference tasks such as Markov chain Monte Carlo (MCMC) and variational inference.</p>
    </li>
    </ol>

