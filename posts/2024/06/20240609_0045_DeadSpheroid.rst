.. title: OpenCL, meet the Gnuastro Build System
.. slug:
.. date: 2024-06-09 00:45:00 
.. tags: gnuastro
.. author: DeadSpheroid
.. link: https://deadspheroid.github.io/my-blog/post/GettingStarted/
.. description:
.. category: gsoc2024


.. raw:: html

    <p class="intro">In this post, I hope to summarize the work done so far towards my GSoC project for integrating OpenCL with the Gnuastro library and my relatively limited understanding of OpenCL.</p>
    
    <h1 id="what-is-opencl">What is OpenCL?</h1>
    <!-- TEASER_END -->
    <p align="center" width="100%">
    <img alt="OpenCL Logo" src="https://deadspheroid.github.io/my-blog/assets/img/opencl-logo.png" style="margin-bottom: 0; margin-top: 24px;" />
    </p>
    <p><strong><a href="https://www.khronos.org/opencl/">Open Computing Language</a></strong> is a framework for writing programs that execute across <strong>heterogenous</strong> platforms. In simpler terms, OpenCL provides a standard interface for programmers to execute the <strong>same</strong> code across <strong>multiple</strong> devices, be it a CPU or a GPU or <strong>any</strong> other accelerator.</p>
    
    <p>It comprises of the OpenCL standard which is maintained by <a href="https://www.khronos.org/opencl/">Khronos</a>, and implemented by the various hardware <strong>manufacturers</strong> and by the <strong>open source community</strong> across a wide variety of devices.</p>
    
    <p>Most modern devices all support OpenCL in some format or the other. <strong>Intel/Nvidia</strong> for example provide their own <strong>propietary</strong> implementations. On the other hand, <strong>POCL</strong> an <strong>open source</strong> project provides implementations for those that dont have actively maintained propietary ones, like <strong>AMD</strong>.</p>
    
    <h1 id="why-opencl">Why OpenCL?</h1>
    
    <p align="center" width="100%">
    <img alt="OpenCL versus CUDA" src="https://deadspheroid.github.io/my-blog/assets/img/cl-cuda.jpeg" style="margin-bottom: 0; margin-top: 24px;" />
    </p>
    
    <p>Unlike certain <strong>propietary</strong> frameworks <em>cough</em> <a href="https://developer.nvidia.com/about-cuda">CUDA</a> <em>cough</em>, OpenCL is not constrained to any particular <strong>manufacturer</strong>. You can target <strong>any GPU/CPU</strong> as long as you get the OpenCL implementation for that device. This is made easy thanks to projects like <a href="https://portablecl.org/">POCL</a>.</p>
    
    <p>The performance of <strong>CUDA versus OpenCL</strong> is heavily debated and leans towards CUDA for Nvidia hardware, but the difference depends on the use case and isn’t too much of a concern as compared to the way they are used.</p>
    
    <p>The <strong>downside</strong> of OpenCL is the <strong>smaller</strong> community and the lack of many <strong>modern features</strong> that CUDA brings.</p>
    
    <blockquote>
    The inner workings of OpenCL, how I managed to set it up, how the OpenCL C API works is another long story and is deserving of its own post.
    </blockquote>
    
    <h1 id="kickoff-with-gnuastro">Kickoff with Gnuastro</h1>
    
    <p>The first goal for the project was to figure out a way to <strong>integrate</strong> OpenCL with the Gnuastro build system.</p>
    
    <p>Gnuastro like many other free software uses the <strong>GNU Build System</strong> also called <a href="https://www.gnu.org/software/automake/faq/autotools-faq.html">GNU Autotools</a></p>
    
    <p align="center" width="100%">
    <img alt="GNU Autotools" src="https://deadspheroid.github.io/my-blog/assets/img/gnu-logo.png" style="margin-bottom: 0; margin-top: 24px;" />
    </p>
    
    <p>The <strong>three</strong> major components of Autotools are:</p>
    
    <h3 id="autoconf">Autoconf</h3>
    <p>At the heart of Autotools, we have <a href="https://www.gnu.org/software/autoconf/">Autoconf</a>, which generates a <strong>single</strong> <code class="language-plaintext highlighter-rouge">configure</code> <strong>script</strong> from a <code class="language-plaintext highlighter-rouge">configure.ac</code> file.</p>
    
    <p>This <code class="language-plaintext highlighter-rouge">configure</code> script scans the <strong>environment</strong> for various files and <strong>libraries</strong>, specific versions of them, the <strong>hardware</strong> being used, and more. Then, it <strong>configures</strong> the build of the project in certain ways enabling/disabling certain parts depending on what was found and what wasnt.</p>
    
    <p>In this way, the <strong>portability</strong> of any project can be ensured by simply distributing the <strong>configure</strong> script, along with the <code class="language-plaintext highlighter-rouge">Makefile.in</code>s.</p>
    
    <h3 id="automake">Automake</h3>
    <p><a href="https://www.gnu.org/software/automake/">Automake</a> makes use of information found by <code class="language-plaintext highlighter-rouge">configure</code> and <strong>generates</strong> the <code class="language-plaintext highlighter-rouge">Makefile</code>s necessary to <strong>build</strong> the project.</p>
    
    <p>To be more precise, it <strong>parses</strong> <code class="language-plaintext highlighter-rouge">Makefile.am</code>s into <code class="language-plaintext highlighter-rouge">Makefile.in</code>s which are in turn <strong>parsed</strong> by <code class="language-plaintext highlighter-rouge">configure</code> to produce the final <code class="language-plaintext highlighter-rouge">Makefile</code>s. Automake also performs <strong>automatic dependency tracking</strong>, so that recompilling isn’t done unless <strong>required</strong>.</p>
    
    <p>All you have to do, is specify the <strong>name</strong> and each of the <strong>sources</strong> involved in the library/binary, and Automake does the rest.</p>
    
    <h3 id="libtool">Libtool</h3>
    <p><a href="https://www.gnu.org/software/libtool/">Libtool</a> is responsible for abstracting the <strong>library</strong> creation process, since different platforms handle static/dynamic libraries <strong>differently</strong>.</p>
    
    <blockquote>
    I mainly worked with Automake and Autoconf during integration and didn't really touch Libtool.
    </blockquote>
    
    <h1 id="stepping-into-integration">Stepping into Integration</h1>
    
    <h3 id="inside-configureac">Inside <code class="language-plaintext highlighter-rouge">configure.ac</code></h3>
    <p>Without getting into detail, when checking for the <strong>presence</strong> of OpenCL, it suffices to check for <code class="language-plaintext highlighter-rouge">libOpenCL.so</code> and the <code class="language-plaintext highlighter-rouge">CL.h</code> header file.</p>
    
    <p>That is, Gnuastro should be able to <strong>include</strong> the OpenCL header file to use its C API, and then later <strong>link</strong> against the OpenCL library.</p>
    
    <p>Luckily for us, <a href="https://www.gnu.org/software/gnulib/">Gnulib</a> provides a simple <code class="language-plaintext highlighter-rouge">AC_LIB_HAVE_LINKFLAGS</code> <a href="https://www.gnu.org/software/gnulib/manual/html_node/Searching-for-Libraries.html">macro</a> which takes as input, a library <strong>name</strong> and a <strong>test code</strong> and tries to find the <strong>library</strong> and <strong>compile/link</strong> the test code.</p>
    
    <p>Upon successfully executing, it <strong>sets certain variables</strong>, so we can modify further building on the basis of <strong>finding OpenCL</strong>.</p>
    <div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code>AC_LIB_HAVE_LINKFLAGS<span class="o">([</span>OpenCL], <span class="o">[]</span>, <span class="o">[</span><span class="c">#include &lt;CL/cl.h&gt;])</span>
    AS_IF<span class="o">([</span><span class="nb">test</span> <span class="s2">"x</span><span class="nv">$LIBOPENCL</span><span class="s2">"</span> <span class="o">=</span> x],
    <span class="o">[</span>
    <span class="k">if </span>successfull ...
    <span class="o">]</span>,
    <span class="o">[</span>
    <span class="nv">LIBS</span><span class="o">=</span><span class="s2">"</span><span class="nv">$LIBOPENCL</span><span class="s2"> </span><span class="nv">$LIBS</span><span class="s2">"</span>
    <span class="nv">has_ocl</span><span class="o">=</span>1<span class="p">;</span>
    <span class="k">if </span>unsuccessfull ...
    <span class="o">])</span>
    AM_CONDITIONAL<span class="o">([</span>COND_HASOPENCL], <span class="o">[</span><span class="nb">test</span> <span class="s2">"x</span><span class="nv">$has_ocl</span><span class="s2">"</span> <span class="o">=</span> <span class="s2">"x1"</span><span class="o">])</span>
    </code></pre></div></div>
    <p>After making these modifications to <code class="language-plaintext highlighter-rouge">configure.ac</code>, we can now <strong>test</strong> whether OpenCL was found inside the various <code class="language-plaintext highlighter-rouge">Makefile.am</code>s and accordingly change the <strong>build</strong>.</p>
    
    <h3 id="inside-makefileam">Inside <code class="language-plaintext highlighter-rouge">Makefile.am</code></h3>
    <p>Now, we can use the <strong>variable</strong> we set previously in <code class="language-plaintext highlighter-rouge">configure.ac</code> and either include or exclude the OpenCL modules from being compiled and included in the <strong>library</strong>.</p>
    
    <div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">if </span>COND_HASOPENCL
    <span class="si">$(</span>info <span class="s2">"Found OpenCL"</span><span class="si">)</span>
    MAYBE_CL <span class="o">=</span> cl_utils.c
    MAYBE_CL_H <span class="o">=</span> <span class="si">$(</span>headersdir<span class="si">)</span>/cl_utils.h
    MAYBE_CONVOLVE_CL <span class="o">=</span> cl_convolve.c
    <span class="k">else</span>
    <span class="si">$(</span>info <span class="s2">"What is Opencl?"</span><span class="si">)</span>
    endif
    </code></pre></div></div>
    <div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code>libgnuastro_la_SOURCES <span class="o">=</span> <span class="se">\</span>
    <span class="si">$(</span>MAYBE_NUMPY_C<span class="si">)</span> <span class="se">\</span>
    <span class="si">$(</span>MAYBE_WCSDISTORTION<span class="si">)</span> <span class="se">\</span>
    <span class="si">$(</span>MAYBE_CL<span class="si">)</span> <span class="se">\</span>
    <span class="si">$(</span>MAYBE_CONVOLVE_CL<span class="si">)</span> <span class="se">\</span>
    arithmetic.c <span class="se">\</span>
    arithmetic-and.c <span class="se">\</span>
    ...
    </code></pre></div></div>
    
    <p>Additionally, we need to <strong>save</strong> this variable in Gnuastro’s <code class="language-plaintext highlighter-rouge">config.h</code> file for later use to <strong>prevent</strong> other modules from mistakenly including the OpenCL ones incase OpenCL was <strong>not compiled</strong>.</p>
    
    <h1 id="checking-for-build-system-yes">checking for build system… yes</h1>
    <p>Now when someone builds Gnuastro, if OpenCL is <strong>present</strong> on their system, then the OpenCL relevant files are <strong>compiled and included in the library</strong>.</p>
    
    <p>On the other hand, if OpenCL is <strong>absent</strong>, then the library is <strong>built as normal</strong>, as if OpenCL never existed.</p>
    
    <p>Finally, we can get started with the <strong>actual</strong> OpenCl part and we’ll have a look at Image Convolution(astconvolve) in the next post…</p>

