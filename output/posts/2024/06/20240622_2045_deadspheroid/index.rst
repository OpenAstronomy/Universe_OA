.. title: Deeper into OpenCL
.. slug:
.. date: 2024-06-22 20:45:00 
.. tags: gnuastro
.. author: DeadSpheroid
.. link: https://deadspheroid.github.io/my-blog/post/DelvingDeeper/
.. description:
.. category: gsoc2024


.. raw:: html

    <p class="intro">In this post, I hope to give a high level understanding of OpenCL and its workings</p>
    
    <h1 id="setting-it-up">Setting it up</h1>
    <!-- TEASER_END -->
    <p align="center" width="100%">
    <img alt="OpenCL ICD" src="https://deadspheroid.github.io/my-blog/assets/img/ocl-icd.png" style="margin-bottom: 0; margin-top: 24px;" />
    </p>
    <p>OpenCL is relatively easy to get up and running on your system.</p>
    
    <ul>
    <li>
    <p>For users:
    All you need, is the OpenCL runtime for your device!
    In case of Nvidia, this comes with the Nvidia drivers, while for Intel CPUs, this has to be manually installed by a package manager.</p>
    </li>
    <li>
    <p>For developers:
    You will need the OpenCL library to link against, and the OpenCL headers as well, again easily available in your package manager.</p>
    </li>
    </ul>
    
    <h1 id="heres-a-new-perspective">Here’s a new perspective</h1>
    <p align="center" width="100%">
    <img alt="OpenCL Platform Model" src="https://deadspheroid.github.io/my-blog/assets/img/ocl-platform.png" style="margin-bottom: 0; margin-top: 24px;" />
    </p>
    <p>OpenCL presents a general interface to the developer, no matter what the device or the architecture.</p>
    
    <p>Firstly, we have the host, which is responsible for all the book-keeping, and task scheduling on the OpenCL device.</p>
    
    <p>Then, we have our OpenCL device, which is divided into a number of compute units.
    Each Compute Unit (CU) is further divided into a number of processing elements.</p>
    
    <p>But what do these words actually mean?</p>
    
    <p>Well, a Processing Element(PE) is a single unit, that is responsible for executing a single thread(also called a work item). Think of a single function being executed.</p>
    
    <p>Each PE has its own private memory, not accessible by anyone, but this PE</p>
    
    <p>A bunch of processing elements are grouped together to form a compute unit which, at a time, executes a single work group(grouping of many work items).</p>
    
    <p>The CUs all share a global memory, accessible by anyone</p>
    
    <p>So for a CPU, the maximum number of CU s is the number of CPU cores!</p>
    
    <p>But why do you want work groups? Why not have work items only?</p>
    
    <p>Well, having this grouping of work items, allows for a greater deal of complexity, because we can synchronize across items in a work group, have a local memory only for this work group, and more…</p>
    
    <h1 id="a-complete-walkthrough">A complete walkthrough</h1>
    <p align="center" width="100%">
    <img alt="OpenCL Execution Model" src="https://deadspheroid.github.io/my-blog/assets/img/ocl-exec.png" style="margin-bottom: 0; margin-top: 24px;" />
    </p>
    
    <p>Let’s look at a typical workflow for an OpenCL program</p>
    
    <h2 id="initialisation">Initialisation</h2>
    <p>First we need to check the currently available OpenCL platforms, which are basically implementations of OpenCL available on your system</p>
    
    <p>For example, you can have both Intel OpenCL and POCL OpenCL for your i7 CPU.</p>
    
    <p>Then from these platforms, you need to choose a device to execute on. OpenCL supports CPUs, GPUs, FPGAs, and all sorts of accelerators.</p>
    
    <h2 id="context">Context</h2>
    <p>Once you have the platform and device you wish to use, you need to create an OpenCL context, which will handle everything for that particular platform and device.</p>
    
    <h2 id="command-queue">Command Queue</h2>
    <p>Then, you have to create a command queue, which, as the name suggests, will store any commands(kernels) you queue for execution, and dispatch them in order(or even out of order if you like!).</p>
    
    <h2 id="kernel">Kernel</h2>
    <p>After the command queue, you must compile the kernel source code(the api provides functions to do this), so that it can be executed later.</p>
    
    <h2 id="memory">Memory</h2>
    <p>Finally, one of the most important parts of this entire process, is passing the input to the OpenCL device.</p>
    
    <p>Now, initially the data is stored on your CPU RAM, which is unfortunately inaccessible to your GPU.</p>
    
    <p>Therefore you need to copy the data to your GPU RAM, using the <code class="language-plaintext highlighter-rouge">cl_mem</code> interface that OpenCL provides.</p>
    
    <p>However, if you know that the device being used is the same CPU, then this copy can be skipped, to save time, using the <code class="language-plaintext highlighter-rouge">CL_MEM_USE_HOST_PTR</code> flag while creating a <code class="language-plaintext highlighter-rouge">cl_mem</code> object.</p>
    
    <h2 id="execution">Execution</h2>
    <p>At the end, you can use the command queue created earlier along with the <code class="language-plaintext highlighter-rouge">cl_mem</code> created previously to execute the compiled kernel on the device</p>
    
    <p>Subsequently don’t forget to copy the output data back to CPU RAM, if the execution was done on GPU.</p>
    
    <p>However, there’s still a ton of unexplained stuff like, “How do you save the time wasted in copying data to the device?” or “Can you pass any data to the device? Even structs?”</p>
    
    <p>We’ll explore OpenCL more in subsequent posts.</p>

