.. title: Week 3 & 4: The end of first month!
.. slug:
.. date: 2020-06-28 18:04:56 
.. tags: JuliaAstro
.. author: siddharthlal25
.. link: http://siddharthlal25.github.io/blog/gsoc/gsoc-blog-3
.. description:
.. category: gsoc2020


.. raw:: html

    <h2 id="hey-sid-you-mentioned-about-releasing-the-package-in-the-previous-post-did-you-go-for-the-release"><em>Hey Sid, you mentioned about releasing the package in the previous post, did you go for the release?</em></h2>
    
    <p>Yes, I wrote the interface for <code class="language-plaintext highlighter-rouge">combine</code> function with FITS files and finally released <em>version-0.2.0</em>, come check it! (<a href="https://github.com/JuliaAstro/CCDReduction.jl">CCDReduction.jl</a>)</p>
    <!-- TEASER_END -->
    
    <h2 id="so-how-were-the-weeks-3--4"><em>So, how were the weeks 3 &amp; 4?</em></h2>
    
    <p align="center"> <img src="https://beta.techcrunch.com/wp-content/uploads/2010/10/awesome.jpg" /> </p>
    
    <p>These two weeks were quite interesting! After packing all the basic functionalties in the package, <em>version-0.2.0</em> was released, the next problem to be tackled was collecting and listing all relevant files from a directory. So, to solve this <code class="language-plaintext highlighter-rouge">fitscollection</code> was created, it takes a path, searches it recursively (if the user wants) for FITS files with ImageHDUs, list them together and return them in a data frame. It has some advanced functionalities as well, check the <a href="https://juliaastro.github.io/CCDReduction.jl/dev/api/#CCDReduction.fitscollection-Tuple{String}">documentation</a> to know more!</p>
    
    <p>Next, we created generators for filenames, image arrays, and ImageHDUs which works something like this:</p>
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code># listing all FITS files present at some location with ImageHDUs
    df = fitscollection(“location_of_some_fits_files”)
    for arr in arrays(df)
    # arr is the array representation of images present in entries of the data frame
    # (i.e. array of ImageHDU's image data)
    end
    </code></pre></div></div>
    <p>The generators created were <code class="language-plaintext highlighter-rouge">filenames</code>, <code class="language-plaintext highlighter-rouge">arrays</code>, and <code class="language-plaintext highlighter-rouge">images</code>. <code class="language-plaintext highlighter-rouge">filenames</code> generates the path of the file, <code class="language-plaintext highlighter-rouge">arrays</code> generates the array representation of images in ImageHDU and <code class="language-plaintext highlighter-rouge">images</code> generates ImageHDU of FITS files. These generators work on output of <code class="language-plaintext highlighter-rouge">fitscollection</code> i.e. a data frame returned by the function. All these generators were written using <a href="https://github.com/BenLauwens/ResumableFunctions.jl">ResumableFunctions.jl</a>.</p>
    
    <h2 id="hmmm-interesting-whats-next"><em>Hmmm, interesting! What’s next?</em></h2>
    
    <p>Currently, I am working on issue <a href="https://github.com/JuliaAstro/CCDReduction.jl/issues/28">#28</a>, once this gets done, there will be a big release! Stay tuned to know more!</p>
    
    <p>-sl</p>

