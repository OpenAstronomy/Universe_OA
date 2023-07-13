.. title: GPUs and Convolutions in Gnuastro
.. slug:
.. date: 2023-07-04 00:00:00 
.. tags: gnuastro
.. author: Labib Asari
.. link: https://labeeb-7z.github.io/Blogs/2023/07/04/GPUs-and-Convolution.html
.. description:
.. category: gsoc2023


.. raw:: html

    <h2 id="background">Background</h2>
    
    <p>This is an overview of what I’ve been upto for the past 2 weeks. Doesn’t go into much technical details and the actual code but just walks through the general idea.</p>
    <!-- TEASER_END -->
    
    <p><a href="https://en.wikipedia.org/wiki/Convolution">Convolution</a>  is a fundamental operation in various domains, such as image processing, signal processing, and deep learning. It is an important module in Gnuastro and is also used as a subroutine in other modules.</p>
    
    <p>Convolutional operations can be broken down into smaller tasks, such as applying the kernel to different portions of the input data. By utilizing multiple threads, each thread can independently process a subset of the input, reducing the overall execution time. This parallelization technique is particularly effective when dealing with large input tensors or performing multiple convolutions simultaneously.</p>
    
    <p>While traditional CPUs (Central Processing Units) excel at performing a wide range of tasks, they are not specifically designed for heavy parallel computations like convolutions. On the other hand, GPUs (Graphics Processing Units) are highly optimized for parallel processing, making them ideal for accelerating convolutional operations.</p>
    
    <h2 id="gpus-vs-cpus-architecture">GPUs vs CPUs Architecture</h2>
    <p><img alt="Architecture difference" src="https://labeeb-7z.github.io/Blogs/img/posts/gpus/architecture.png" /></p>
    
    <h3 id="cores-and-parallelism-">Cores and Parallelism :</h3>
    <p>CPUs have fewer, more powerful cores optimized for sequential processing, while GPUs have thousands of smaller cores designed for parallel processing. This parallelism allows GPUs to perform computations on multiple data elements simultaneously, leading to significant speedup in parallelizable tasks like graphics rendering and deep learning.</p>
    
    <h3 id="memory-hierarchy-">Memory Hierarchy :</h3>
    <p>CPUs typically have larger caches and more advanced memory management units (MMUs), focusing on low-latency operations and complex branch prediction. GPUs, prioritize high memory bandwidth and utilize smaller caches to efficiently handle large amounts of data simultaneously, crucial for tasks like image processing and scientific simulations.</p>
    
    <h3 id="emphasis-">Emphasis :</h3>
    <p>CPUs are designed with an emphasis on executing single threads - very fast. GPUs are designed with an emphasis on executing on executing multiple threads.</p>
    
    <h2 id="programming-model">Programming Model</h2>
    <p>For Programming GPUs, several frameworks (high level APIs) are available</p>
    
    <ul>
    <li>CUDA - developed by NVIDIA for its GPUs.</li>
    <li>OpenCL - Open Source, Cross Platform parallel programming standard for diverse accelerators.</li>
    <li>HIP - developed by AMD, portable.</li>
    <li>and many more….</li>
    </ul>
    
    <h2 id="cuda">CUDA</h2>
    
    <h3 id="the-cuda-platform-consists-of-a-programming-language-a-compiler-and-a-runtime-library">The CUDA platform consists of a programming language, a compiler, and a runtime library.</h3>
    
    <ul>
    <li><code class="language-plaintext highlighter-rouge">Programming Language</code> - Based on C, has extensions to write code for GPU.</li>
    <li><code class="language-plaintext highlighter-rouge">Compiler</code> - Based on clang, offloads host code to system compiler and translates device code into binary code that can be executed on the GPU.</li>
    <li><code class="language-plaintext highlighter-rouge">Runtime Library</code> - Provides the necessary functions and tools to manage the execution of the code on the GPU (interacts with the driver).</li>
    </ul>
    
    <p>Note : When we have multiple devices(GPUs, FPGAs, etc) on a single system, which can execute tasks apart from the main CPU, they’re generally referred to as <code class="language-plaintext highlighter-rouge">device</code> whereas the main CPU is referred to as <code class="language-plaintext highlighter-rouge">host</code>.</p>
    
    <h2 id="cuda-programs">CUDA Programs</h2>
    
    <p>CUDA programs consists of normal host code along with some <code class="language-plaintext highlighter-rouge">kernels</code>.
    Kernels are like other functions, but when you call a kernel, they’re executed N times parallely by N different CUDA threads, as opposed to only once like normal functions. They’re defined using the <code class="language-plaintext highlighter-rouge">__global__</code> keyword.</p>
    
    <p>Eg :
    <img alt="kernel example" src="https://labeeb-7z.github.io/Blogs/img/posts/gpus/kernel.png" /></p>
    
    <p>Normally, we put the above piece of code inside a loop, so all elements are covered.</p>
    
    <p>With GPUs, there’s no need for loops - for N elements, we launch N threads each of which add 1 element at the same time!</p>
    
    <h2 id="cuda-execution-configuration">CUDA Execution Configuration</h2>
    
    <p>Can we launch an arbitrary large number of threads?
    Technically No</p>
    <ul>
    <li>The maximum allowed threads depend on your GPUs compute capability.</li>
    <li>But generally it’s so large, it always covers all your elements</li>
    <li>For Compute Capability &gt; 3.0
    <ul>
    <li>Max Number of threads : (2^31)<em>(2^16)</em>(2^16)<em>(2</em>10) = 2^42!</li>
    </ul>
    </li>
    </ul>
    
    <h3 id="threads-and-blocks-">Threads and Blocks :</h3>
    
    <p><img alt="Threads and Blocks" src="https://labeeb-7z.github.io/Blogs/img/posts/gpus/config.png" /></p>
    
    <ul>
    <li>All threads are organized into groups called - Block.</li>
    <li>All blocks are organized into groups called - Grid.</li>
    </ul>
    
    <p>Blocks and Grids could be a 1D, 2D or 3D structures.</p>
    
    <p>When calling a GPU kernel, we specify the structure of each block, number of blocks, and number of threads/block - This is called the Execution Configuration.</p>
    
    <p>Example :
    <img alt="Launching a kernel example" src="https://labeeb-7z.github.io/Blogs/img/posts/gpus/launch-kernel.png" /></p>
    
    <p>The above code Launches
    32<em>32</em>1 = 1024 blocks
    Each having 16<em>16 = 256 threads
    Total no. of threads = 1024</em>256.</p>
    
    <h2 id="cuda-memory-hierarchy">CUDA Memory Hierarchy</h2>
    
    <p><img alt="Memory Hierarchy" src="https://labeeb-7z.github.io/Blogs/img/posts/gpus/memory.png" />
    CUDA threads may access data from multiple memory spaces during their execution as illustrated above.</p>
    <ul>
    <li>
    <p>Local memory for each thread.</p>
    </li>
    <li>
    <p>Shared memory b/w all threads of same block.</p>
    </li>
    <li>
    <p>Global memory b/w all blocks.</p>
    </li>
    </ul>
    
    <h2 id="cuda-hardware-abstraction">CUDA Hardware abstraction</h2>
    <p><img alt="Hardware Abstraction" src="https://labeeb-7z.github.io/Blogs/img/posts/gpus/hardware.png" /></p>
    
    <p>The entire GPU is divided into several Streaming MultiProcessors (SMs). They have different architecture than a typical CPU core. Each SM has several CUDA cores, which are the actual processing units.</p>
    
    <p>It is designed with SIMT/SIMD philosophy, which allow execution of multiple threads concurrently on them. One Block is executed at a time on a single SM.</p>
    
    <h2 id="cuda-developing-workflow">CUDA Developing Workflow</h2>
    <p><img alt="Workflow" src="https://labeeb-7z.github.io/Blogs/img/posts/gpus/workflow.png" /></p>
    
    <h2 id="results-of-convolution-on-gpu-for-gnuastro">Results of Convolution on GPU for Gnuastro</h2>
    
    <p>All tests were performed on a system with the following specifications:</p>
    
    <p>CPU :</p>
    
    <ul>
    <li>Intel(R) Core(TM) i5-9300HF CPU @ 2.40GHz</li>
    <li>Thread(s) per core:  2</li>
    <li>Core(s) per socket:  4</li>
    <li>Socket(s):           1</li>
    <li>CPU max MHz:         4100.0000</li>
    <li>CPU min MHz:         800.0000</li>
    </ul>
    
    <p>GPU :</p>
    
    <ul>
    <li>NVIDIA GeForce GTX 1650</li>
    <li>Turing Architecture</li>
    <li>Driver Version:      535.54.03</li>
    <li>CUDA Version:        12.2</li>
    <li>VRAM :               4GB</li>
    <li>Compute Capability : 7.5</li>
    </ul>
    
    <p>The input image was a 10k x 20k FITS file with 32-bit floating point values. The kernel was a 3x3 matrix with 32-bit floating point values.</p>
    
    <h3 id="cpu-multi-threaded">CPU Multi-threaded</h3>
    
    <p><img alt="CPU" src="https://labeeb-7z.github.io/Blogs/img/posts/gpus/cpu-result.png" /></p>
    
    <h3 id="gpu">GPU</h3>
    
    <p><img alt="GPU" src="https://labeeb-7z.github.io/Blogs/img/posts/gpus/gpu-result.png" /></p>
    
    <p>The overall speedups seems to only be 6X but this also counts the time taken to transfer the data from CPU to GPU and back. If we only consider the time taken to perform the convolution, the speedup is around ~700X!.</p>

