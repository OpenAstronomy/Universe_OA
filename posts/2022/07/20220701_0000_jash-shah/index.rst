.. title: My GSoC Journey - Part 3
.. slug:
.. date: 2022-07-01 00:00:00 
.. tags: gnuastro
.. author: Jash Shah
.. link: https://jash_shah.github.io/Blogs/2022/07/01/Coding-Begins.html
.. description:
.. category: gsoc2022


.. raw:: html

    <h2 id="coding-begins">Coding Begins!</h2>
    <p>So, now that I got to know the Gnuastro community a bit and had discussed the plan of attack with my mentor it was time to start with the actual coding.</p>
    
    <!-- TEASER_END -->
    <h3 id="week-1">Week 1</h3>
    <p>As planned, I started with the building the extension module for <a href="https://www.gnu.org/savannah-checkouts/gnu/gnuastro/manual/html_node/CosmicCalculator.html">Cosmic Calculator</a>(cosmiccal) library. A simple Python extension Module should be structed as:</p>
    
    <p><img alt="Code-Block1" src="https://jash-shah.github.io/Blogs/img/posts/gsoc-coding-begins/code-block-1.png" /></p>
    
    <p>The cosmical library was chosen as a starting point because it contained only 6 functions and solely dealt with <em>doubles, ints, and floats</em>. Consequently, there wasn’t yet a requirement for a NumPy Converter. It was pretty straight forward to create wrappers for these functions by following the aforementioned structure. The <code class="language-plaintext highlighter-rouge">setup.py</code> script for building and installing these modules was created at the following stage. For this, I followed the <a href="https://docs.python.org/3/extending/building.html#building">Python Extension documentation’s</a> advice and utilised <a href="https://docs.python.org/3/distutils/apiref.html"><code class="language-plaintext highlighter-rouge">distutils</code></a>, which offers two crucial functions:</p>
    <ul>
    <li><a href="https://docs.python.org/3/distutils/apiref.html#distutils.core.Extension"><u>distutils.core.Extension</u></a> which is used to describe a <code class="language-plaintext highlighter-rouge">C/C++</code> extension.</li>
    <li><a href="https://docs.python.org/3/distutils/apiref.html#distutils.core.setup"><u>distutils.core.setup</u></a> the frontman in actually building and compiling the modules.</li>
    </ul>
    
    <p><img alt="Code-Block2" src="https://jash-shah.github.io/Blogs/img/posts/gsoc-coding-begins/code-block-2.png" /></p>
    
    <p>After this, the commands to build and install these modules were simply:</p>
    <div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code>python3 setup.py build
    python3 setup.py <span class="nb">install</span>
    </code></pre></div></div>
    
    <h3 id="week-2">Week 2</h3>
    <p>At our subsequent meeting, my mentor confirmed my work, and we both agreed that the next step should be to write the NumPy converter so that this may be <em>expanded</em> to include the other library modules as well.</p>
    
    <p>Week 2 was a little light on work because I was out of town for a few days. However, the most of my reading time was devoted to learning about the <code class="language-plaintext highlighter-rouge">NumPy C-API</code> and how it connected with the <code class="language-plaintext highlighter-rouge">Python C-API</code>.</p>
    
    <p>I discovered that a NumPy array’s primary container object was the <a href="https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject"><code class="language-plaintext highlighter-rouge">PyArrayObject</code></a>, and its <code class="language-plaintext highlighter-rouge">PyTypeObject</code> was the <a href="https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Type"><code class="language-plaintext highlighter-rouge">PyArray_Type</code></a>. Therefore, in order for any <code class="language-plaintext highlighter-rouge">PyObject</code> to be regarded as a NumPy Array, it has to fulfil these two requirements.</p>
    
    <p>The API itself offered <a href="https://numpy.org/doc/stable/reference/c-api/array.html#creating-arrays">functions</a> that allowed any generic array type data container to be converted into <code class="language-plaintext highlighter-rouge">PyArray_Type</code> or one of its subclasses. For creating the converter, I would always turn to these!</p>

