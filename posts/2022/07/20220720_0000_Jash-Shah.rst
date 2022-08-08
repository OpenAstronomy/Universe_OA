.. title: My GSoC Journey - Part 4
.. slug:
.. date: 2022-07-20 00:00:00 
.. tags: gnuastro
.. author: Jash Shah
.. link: https://jash_shah.github.io/Blogs/2022/07/20/How-low-can-you-go.html
.. description:
.. category: gsoc2022


.. raw:: html

    <p><em>Writing the extension modules and Python wrappers for a package is one thing, but a step that is often overlooked is making a build system that complies with the rest of your program, ensures the correct installation based on your dependencies and also is portable enough to be distributable.</em></p>
    
    <p><em>I learned these things the hard way in Week 3 and 4, where I went as low level as I could to try to solve all the weird build errors and glitches I had while <strong>trying to build a Python Package using GNU Autotools</strong>.</em></p>
    <!-- TEASER_END -->
    
    <h2 id="building">Building</h2>
    <p>As discussed in my last GSoC blog, I was mainly using <code class="language-plaintext highlighter-rouge">distutils</code> along with it’s <code class="language-plaintext highlighter-rouge">distutils.setup</code> script to take care of all the building and linking required for building the <code class="language-plaintext highlighter-rouge">.so</code> (shared object) file required by the  Python Interpreter. However, one of my co-mentors brought up a good point that <code class="language-plaintext highlighter-rouge">setuptools</code> is the packaging tool that is recommended by <a href="https://packaging.python.org/en/latest/guides/tool-recommendations/">PyPA</a> and also using <code class="language-plaintext highlighter-rouge">wheels</code> to package the modules instead of the standard <code class="language-plaintext highlighter-rouge">setup.py build</code> command.</p>
    
    <p>Hence, <strong>Week 3 was spent mainly learning about <code class="language-plaintext highlighter-rouge">setuptools</code> and <code class="language-plaintext highlighter-rouge">wheels</code></strong>. <a href="https://realpython.com/python-wheels/#the-manylinux-wheel-tag">What Are Python Wheels and Why Should You Care?</a> is a great article to start with Python Wheels. The <a href="https://setuptools.pypa.io/en/latest/index.html">setuptools documentation</a> is a great place to know about setuptools, if you already know about distutils like me! Luckily, while <code class="language-plaintext highlighter-rouge">Setuptools</code> is a “beefier” version of distutils, as it offers better and more packaging utilities, it keeps the same functions, so in terms of code it was just a change of one line for me.</p>
    
    <p>Originally, with <code class="language-plaintext highlighter-rouge">distutils</code>, the plan was to have the files related to the Python Package in a separate <em><code class="language-plaintext highlighter-rouge">python/</code></em> directory at the root of the Gnuastro source like:</p>
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>📦python
    ┣ 📂gnuastro.arithmetic
    ┃ ┣ 📜arithmetic.c
    ┃ ┗ 🔧setup.py
    ┣ 📂gnuastro.cosmology
    ┃ ┣ 📜cosmology.c
    ┃ ┗ 🔧setup.py
    ┣ 📂gnuastro.fits
    ┃ ┣ 📜fits.c
    ┃ ┗ 🔧setup.py
    ┗ 📑Makefile.am
    </code></pre></div></div>
    
    <p>The idea was to have the <code class="language-plaintext highlighter-rouge">setup.py</code> script in each folder build that specific extension, and let the Makefile handle the linking. But I soon realized that this was too excessive. A better structure would be:</p>
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code> 📦python
    ┣ 📂src
    ┃ ┣ 📜arithmetic.c
    ┃ ┣ 📜cosmology.c
    ┃ ┗ 📜fits.c
    ┣ 📑Makefile.am
    ┗ 🔧setup.py
    </code></pre></div></div>
    
    <h3 id="using-autotools-to-build-python-package">Using Autotools to build Python Package</h3>
    <p>As the name suggests <strong>GNU</strong>astro is a GNU project, and thus depends on Autotools(<a href="https://www.gnu.org/software/automake/manual/html_node/index.html#SEC_Contents">Automake</a> and <a href="https://www.gnu.org/software/autoconf/">Autoconf</a> and <a href="https://www.gnu.org/software/libtool/">Libtool</a>) for its building and compiling. These are the tools behind the</p>
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>./configure
    make
    make check
    make install
    </code></pre></div></div>
    <p>set of instructions.</p>
    
    <p>Alongwith the setup script, I also added a new file(<a href="https://github.com/Jash-Shah/gnuastro-jash/blob/6997730fab6cb18fd7b34f77f9a0f65f0c7e0730/lib/python.c"><code class="language-plaintext highlighter-rouge">python.c</code></a>) to the <em>lib/</em> directory of Gnuastro. This file basically provides any utility functions I might require while building the Python package. Currently, the file provides type conversion functions, which facilitate converting between Gnuastro and NumPy’s datatypes.</p>
    
    <p>So, what is the difference between your traditional Makefile and using Autotools instead:-</p>
    <ul>
    <li><strong>Autoconf</strong> easily scans an existing tree to find its dependencies and creates a configure script that will run under almost any kind of shell. The configure script allows the user to control the build behavior (i.e. –with-foo, –without-python, –prefix, –sysconfdir, etc..) as well as doing checks to ensure that the system can compile the program.</li>
    </ul>
    
    <p>Configure generates a <code class="language-plaintext highlighter-rouge">config.h</code> file (from a template) which programs can include to work around portability issues. For example, if HAVE_NUMPY is not defined, don’t build the Python package.</p>
    
    <ul>
    <li><strong>Automake</strong> provides a short template that describes what programs will be built and what objects need to be linked to build them, thus Makefiles that adhere to GNU coding standards can automatically be created.</li>
    </ul>
    
    <p>My job was to use these tools to also call the <code class="language-plaintext highlighter-rouge">setup</code> script for building my Python package.</p>
    
    <p>My approach to building the package using Autotools involved 4 basic steps:</p>
    <ol>
    <li>Adding the necessary checks in the <code class="language-plaintext highlighter-rouge">configure.ac</code> script.
    <ul>
    <li>Check if a user has Python 3 on their system and get it’s include path i.e. path to <code class="language-plaintext highlighter-rouge">Python.h</code> file.</li>
    <li>If Python 3 is found, Check if the user has NumPy on their system and get it’s include path.</li>
    <li>Substitute the include paths as variables to be passed to all <code class="language-plaintext highlighter-rouge">Makefile.am's</code>.</li>
    </ul>
    </li>
    <li>Conditionally build the Python package and its utility functions module(<code class="language-plaintext highlighter-rouge">lib/python.c</code>) only if the above checks are passed.</li>
    <li>Write the <code class="language-plaintext highlighter-rouge">Makefile.am</code> in the <code class="language-plaintext highlighter-rouge">python/</code> directory which would handle the <em>build, install, uninstall and clean</em> targets for the Python package.</li>
    <li>Re-write the setup.py script to make it more generic, by using the environment variables passed by the configure script instead of hardcoding the include and install paths.
    <ul>
    <li>This also ensures that the Python package building supports <a href="https://www.gnu.org/software/automake/manual/html_node/VPATH-Builds.html">VPATH</a> builds, which is another great feature of Autotools. For the uninitiated, <code class="language-plaintext highlighter-rouge">VPATH builds</code> are basically a way to separate your source and build tree, so that all the built files (.o, .so, etc) are in a separate directory than your source files but are symlinked to the source tree.</li>
    </ul>
    </li>
    </ol>
    
    <p>This process took a lot of trial and error, digging into the Autotools(mostly Automake) documentation and playing around with the <code class="language-plaintext highlighter-rouge">Makefile.am</code> to get right. But it introduced me to these amazing tools and taught me how to make any scrawny personal project distributable!</p>
    
    <h2 id="installing">Installing</h2>
    <p>After running,</p>
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>python3 setup.py build_ext bdist_wheel
    </code></pre></div></div>
    <p>the distributable wheel file, with all of the package’s metadata, is created under the <code class="language-plaintext highlighter-rouge">dist/</code> folder. In order to install this file we use pip as follows:</p>
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>pip install Gnuastro.whl
    </code></pre></div></div>
    <p>YES! It is in fact as simple as that!</p>
    
    <p>But there is an issue that I faced here, suppose that a user wants to install the Gnuastro library in their root directory, or to any directory where they dont have privileges. This means they’ll run <code class="language-plaintext highlighter-rouge">sudo make install</code> from the root of the source. This cascades to calling the Makefile in the <em>python/</em> directory with root access as well. However, running <code class="language-plaintext highlighter-rouge">pip</code> with sudo access is a big NO, NO. And <code class="language-plaintext highlighter-rouge">pip</code> would warn you of that with a warning like:</p>
    
    <p><img alt="PIP sudo error message" height="50" src="https://jash-shah.github.io/Blogs/img/posts/gsoc-week3_4/pip_error.png" width="1000" /></p>
    
    <!-- ![PIP sudo error message](/Blogs/img/posts/gsoc-week3_4/pip_error.png) -->
    
    <p>This is because, Python packages are generally installed at a local level, in the <code class="language-plaintext highlighter-rouge">/usr/local</code> directory. However, if you call <code class="language-plaintext highlighter-rouge">pip</code> with <code class="language-plaintext highlighter-rouge">sudo</code> then it installs the packages in the root directory. To sove this, we use</p>
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>sudo -u "$SUDO_USER pip install Gnuastro,whl
    </code></pre></div></div>
    <p>which basically runs the pip command as the user who called sudo. This will ensure that your package gets installed in the local directory instead of root!</p>

