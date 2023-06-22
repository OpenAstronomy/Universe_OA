.. title: GSoC - its finally here
.. slug:
.. date: 2023-06-05 00:00:00 
.. tags: gnuastro
.. author: Labib Asari
.. link: https://labeeb-7z.github.io/Blogs/2023/06/05/GSoC-Starts.html
.. description:
.. category: gsoc2023


.. raw:: html

    <h2 id="what-is-open-source-and-gsoc">What is Open-Source and Gsoc?</h2>
    <p>Open source software is software with source code that anyone can inspect, modify, and enhance. There are many institutions and individuals who write open software, mainly for research or free deployment purposes. Mostly these softwares, have only a few maintainers, and multiple people, writing and debugging the code, helps a lot. This is where Google Summer of Code <code class="language-plaintext highlighter-rouge">GSOC</code> comes into the picture. It is a global, online program focused on bringing new contributors into open source software development. Many organisations float projects for the developers to take over the summer and Google mediates in the process, while also paying the contributors for their work over the summer.</p>
    
    <!-- TEASER_END -->
    <h2 id="what-is-my-project-about">What is my project about?</h2>
    
    <p>It has 2 main components :</p>
    <ul>
    <li>Create a Python Library for Gnuastro
    <ul>
    <li>Design an error handling mechanism for Gnuastro</li>
    <li>Design corresponding data structures of Gnuastro in Python</li>
    <li>Write wrapper functions to be used in python</li>
    </ul>
    </li>
    <li>Add CUDA support in Gnuastro
    <ul>
    <li>Integrate CUDA with Gnuastro’s build system</li>
    <li>Write GPU kernels for compute heavy and parallelizable operations.</li>
    </ul>
    </li>
    </ul>
    
    <h2 id="what-have-i-completed-till-now">What have I completed till now?</h2>
    
    <ul>
    <li>On the Python Library Part :
    <ul>
    <li>Gnuastro now has an error handling mechanism!</li>
    <li>Added error handling in Python package for the 2 existing modules.</li>
    <li>Defined error types for each corresponding error type in C library.</li>
    <li>Implemented Python wrappers for 2 of the C library modules</li>
    </ul>
    </li>
    <li>On the CUDA support part :
    <ul>
    <li>Gnuastro can now build with cuda! this means it already supports GPU computations.</li>
    <li>Added docs for installing, configuring, and testing CUDA</li>
    <li>Added test CUDA kernels and demo programs to test them.</li>
    <li>Implementing CUDA kernel for Convolution operation.</li>
    </ul>
    </li>
    </ul>
    
    <p>##</p>

