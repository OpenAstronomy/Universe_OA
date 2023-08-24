.. title: Integrating OpenCL with Gnuastro
.. slug:
.. date: 2023-08-12 00:00:00 
.. tags: gnuastro
.. author: Labib Asari
.. link: https://labeeb-7z.github.io/Blogs/2023/08/12/Integrating-OpenCL.html
.. description:
.. category: gsoc2023


.. raw:: html

    <h2 id="background">Background</h2>
    
    <p>In the last post, I discussed what is OpenCL and why we chose to integrate it with Gnuastro. In this post, I’ll be discussing the actual implementation and the challenges I faced.</p>
    <!-- TEASER_END -->
    
    <h2 id="programming-in-opencl">Programming in OpenCL</h2>
    
    <p>The OpenCL 3.0 standard has done a great job of simplifying the programming model. The OpenCL 3.0 API is a header-only library that provides a modern, object-oriented interface to the OpenCL runtime. It is designed to be easy to use and provides a abstraction of the OpenCL runtime, making it easier to write portable code across different OpenCL implementations. We still have to communicate with the driver (unlike CUDA) at a low level, but this becomes a mandatory step when we want to run our code on different hardware (CUDA always expects an NVIDIA device).</p>
    
    <p>Here’s a general overview of steps to be followed when writing an using OpenCL :</p>
    <ul>
    <li><strong>Check for available Platforms</strong> : A platform is a collection of OpenCL devices. A platform can be a CPU, GPU, or an FPGA (Remember OpenCL can work with any platform!). This is done specifically to identify which OpenCL implementation will be used during runtime. We can query the system for available platforms using the <code class="language-plaintext highlighter-rouge">clGetPlatformIDs</code> function. This function returns a list of platforms available on the system.</li>
    <li><strong>Check for available devices</strong> : A device is a physical device that can execute OpenCL kernels. A device can be a CPU, GPU, or an FPGA. We can query the system for available devices using the <code class="language-plaintext highlighter-rouge">clGetDeviceIDs</code> function. This function returns a list of devices available on the system.</li>
    <li><strong>Create a context</strong> : A context is a container for all the OpenCL objects. It is used to manage the memory, command queues, and other OpenCL objects. It is created by passing a list of devices to the constructor. Since OpenCL can work with multiple devices, we can create a context with multiple devices. This is useful when we want to run our code on multiple devices at the same time.</li>
    <li><strong>Create a command queue</strong> : A command queue is used to queue up commands for the device to execute. The command queue is used to give commands to the device. The device executes the commands in the order they are received. The commands can be kernel execution, memory transfer, or any other OpenCL command. We can also create multiple command queues. This is useful when we want to run to multiple commands. Command queues in OpenCL are asynchronous by default. This means that the commands are queued up and the control is returned to the host. The host can then continue with other tasks. We can also create a synchronous command queue. This means that the commands are queued up and the control is returned to the host only when the commands are executed.</li>
    <li><strong>Load the Kernel</strong> : A kernel is a function that is executed on the device. It is written as per the <code class="language-plaintext highlighter-rouge">C99 standard</code>. We can load the kernel from a file or we can write the kernel inline. To maintain portablitiy, OpenCL kernels are generally compiled at runtime using <code class="language-plaintext highlighter-rouge">clBuildProgram</code>. We can also compile the kernel offline. This is useful when we want to compile the kernel for a specific device.</li>
    <li><strong>Copy Data to device memory</strong> : All the data used in kernel, must be on the device memory. So we have to copy the data from the host to the device memory. We can do this using the <code class="language-plaintext highlighter-rouge">clCreateBuffer</code> function. This function creates a buffer on the device memory. We can then copy the data from the host to the device using the <code class="language-plaintext highlighter-rouge">clEnqueueWriteBuffer</code> function. This function copies the data from the host to the device.</li>
    <li><strong>Launch the kernel</strong> : We can launch the kernel by passing the kernel object to the command queue. We have to set the arguments for the kernel seperately, using the <code class="language-plaintext highlighter-rouge">clSetKernelArg</code> function. We can also set the global and local work size. The global work size is the total number of work items that will be executed. The local work size is the number of work items that will be executed in a work group. The global work size should be a multiple of the local work size. If the global work size is not a multiple of the local work size, then the global work size is rounded up to the next multiple of the local work size.</li>
    <li><strong>Read the output</strong> : We can read the output from the device using the <code class="language-plaintext highlighter-rouge">clEnqueueReadBuffer</code> function. This function copies the data from the device to the host.</li>
    </ul>
    
    <h2 id="implementation">Implementation</h2>
    
    <p>Among all the steps mentioned above, everything up till loading the kernel is common to all the programs that’ll be using OpenCL. So we defined a <code class="language-plaintext highlighter-rouge">gpu_utils</code> module which is responsible for querying for the available platforms and devices, creating the context and command queue, loading and compiling the kernel. The only external data it requires is the path to the kernel file. This is provided as an input.
    It also provides utility functions to copy specific data types to and from device memory.</p>
    
    <p>There’ll be 2 types of OpenCL program in Gnuastro :</p>
    <ol>
    <li>Programs using OpenCL to speed-up existing operations inside Gnuastro.</li>
    <li>User defined OpenCL kernels, responsible for performing a custom task.</li>
    </ol>
    
    <h3 id="programs-using-opencl-to-speed-up-existing-operations-inside-gnuastro">Programs using OpenCL to speed-up existing operations inside Gnuastro</h3>
    
    <p>These programs will be using OpenCL to speed-up existing operations inside Gnuastro. For example, we can use OpenCL to speed-up the <code class="language-plaintext highlighter-rouge">astconvolve</code> operation by passing an extra <code class="language-plaintext highlighter-rouge">--gpu</code>. For these programs, the OpenCL kernels will be part of the Gnuastro Library.</p>
    
    <p>The general flow of the program then becomes :</p>
    <ul>
    <li>The user passes the input data for a specific operation, and also choses the local and global work size.</li>
    <li>The program then initializes the device using <code class="language-plaintext highlighter-rouge">gpu_utils</code> module by providing the kernel file from the library, which does everything and returns a <code class="language-plaintext highlighter-rouge">cl_kernel</code> (which is essentially the compiled kernel).</li>
    <li>Data transfer from CPU to device (GPU) is done using the functions provided by <code class="language-plaintext highlighter-rouge">gpu_utils</code> module.</li>
    <li>The kernel is launched using with the provided global and local work size.</li>
    <li>Data is copied back to CPU memory and returned to the user.</li>
    </ul>
    
    <h3 id="user-defined-opencl-kernels-responsible-for-performing-a-custom-task">User defined OpenCL kernels, responsible for performing a custom task</h3>
    
    <p>These programs will be using OpenCL to perform a custom task. For example, we can use OpenCL to perform a custom convolution operation by passing a custom kernel. For these programs, the OpenCL kernels will be provided by the user. The exact design details yet to be determined for this.</p>
    
    <h2 id="results">Results</h2>
    <p>Input image is 10,000 x 20,000 random image with normal distribution.
    Kernel is 7 x 7 standard convolution kernel.
    CPU : Intel(R) Core(TM) i5-9300HF CPU @ 2.40GHz
    GPU : NVIDIA GeForce GTX 1650</p>
    
    <p>Convolution using existing convolution in Gnuastro :</p>
    
    <p><img alt="Convolution using existing convolution in Gnuastro" src="https://labeeb-7z.github.io/Blogs/img/posts/opencl-imp/conv_cpu.png" /></p>
    
    <p>Convolution on OpenCL :</p>
    
    <p><img alt="Convolution on OpenCL" src="https://labeeb-7z.github.io/Blogs/img/posts/opencl-imp/conv_gpu.png" /></p>
    
    <p>Result</p>
    
    <p><img alt="Result" src="https://labeeb-7z.github.io/Blogs/img/posts/opencl-imp/res.png" /></p>
    
    <p>The speed up for convolution operation is specifically ranges from 300-500x, but for the entire operation its around 3-5x due to the overhead of copying data to and from the device. Overcoming this is a big and important challenge!</p>
    
    <h2 id="challenges">Challenges</h2>
    
    <ul>
    <li><strong>No <code class="language-plaintext highlighter-rouge">GAL_DATA_T</code> inside OpenCL kernel!</strong> : Inside OpenCL, <code class="language-plaintext highlighter-rouge">cl_mem</code> is the primary object used to represent memory objects such as buffers and images. It is used to allocate memory on the device. Regardless of where the data is coming from on device (arrays, structs, etc), it’s all converted into a <code class="language-plaintext highlighter-rouge">cl_mem</code> object when copied to the device.</li>
    </ul>
    
    <p>However inside Gnuastro, the core data structure is <code class="language-plaintext highlighter-rouge">gal_data_t</code> which is essentially just a C struct.</p>
    
    <p>Why is this a problem? Well the raw data of the input image/table is not contained inside the <code class="language-plaintext highlighter-rouge">gal_data_t</code>. It merely consists a pointer to that data! So wehn we copy the <code class="language-plaintext highlighter-rouge">gal_data_t</code> to device, the raw data(which is huge) is not copied. (It lives on the CPU memory, and hence cant use CPU pointers on GPU memory).</p>
    
    <p>What about copying the raw data seperately on the GPU memory, and then replacing the pointer inside <code class="language-plaintext highlighter-rouge">gal_data_t</code> with a pointer which has the address on the GPU memory? Well, this is not possible either. Why? See, when we are on CPU, we’ve a good <code class="language-plaintext highlighter-rouge">gal_data_t</code> struct which is a single big object with ‘sub-objects’(one of which is the pointer). But on GPU, we’ve a <code class="language-plaintext highlighter-rouge">cl_mem</code> which is an object, but unlike structs, it cant have sub-objects!</p>
    
    <p>How do we solve this? Currently all the required pointers inside <code class="language-plaintext highlighter-rouge">gal_data_t</code> are passed as seperate arguments to the kernel. After a careful study of the internal implementation of the <code class="language-plaintext highlighter-rouge">cl_mem</code> object, we’ll see if we can directly pass the <code class="language-plaintext highlighter-rouge">gal_data_t</code> to the kernel.</p>
    
    <ul>
    <li><strong>Data Transfer Overhead</strong> : As mentioned multiple times, for using GPUs, we must copy data to and from the GPU memory. Astronomical datasets are huge, and copying them for each operation is a big overhead! Infact the data transfer overhead is so huge, that the actual operation is much faster than the data transfer. Adding more to that, its not just faster, its much much faster! So much so that around 95% of the time is spent in copying data to and from the GPU memory. It reduces performance by ~100x! It can’t continue this way!</li>
    </ul>
    
    <p>One solution we’ve figured is, when the External data is loaded for the first time in the program, we load it on the GPU memory instead of the CPU memory. This way, for each subsequent operation, we dont have to copy the data from CPU to GPU memory. After all the operations are done, we’ll copy the result back to CPU memory and save it to the disk. This will avoid almost all the Data Transfer overhead.</p>
    
    <p>This is about the same approach used by Machine Learning Libraries such as Tensorflow. Basically during initialization, it occupies all the GPU memory it can, and keeps it occupied. All the operations, their results and the subsequent operations are done on the GPU memory itself.</p>

