.. title: Creating a new Data Structure for pyGnuastro
.. slug:
.. date: 2023-06-20 00:00:00 
.. tags: gnuastro
.. author: Labib Asari
.. link: https://labeeb-7z.github.io/Blogs/2023/06/20/Creating-new-datatype.html
.. description:
.. category: gsoc2023


.. raw:: html

    <h2 id="background">Background</h2>
    
    <p><a href="https://www.gnu.org/savannah-checkouts/gnu/gnuastro/gnuastro.html">GnuAstro</a> is a powerful and comprehensive library designed to handle various data formats(FITS/TIFF/TXT and more) and perform a wide range of operations, all while maintaining consistency across its entire codebase.</p>
    <!-- TEASER_END -->
    
    <p>This is done by representing all the data (acquired via input or created internally), regardless of its type, in a single data structure which encompasses the core data as well as metadata. This greatly assists in mainting uniformity.
    Internally all the data is represented in the form of a C struct : <code class="language-plaintext highlighter-rouge">gal_data_t</code>
    The following image describes how it keeps the core data as well as metadata :
    <img alt="Code-Block1" src="https://labeeb-7z.github.io/Blogs/img/posts/creating-data-structure/gal_data_t.png" /></p>
    
    <p>Explaining each attribute of this structure will require a seperate post of itself :). Instead I’ll focus on the main topic here : Since Im creating a python package for Gnuastro, and the <code class="language-plaintext highlighter-rouge">gal_data_t</code> is at the heart of this library, How do I represent this complex type in Python?!</p>
    
    <p>Normally we use Classes to define new and complex data types in Python, but hey.. I’m wrapping a C library in Python using the Python-C API. This means I write my wrappers in C!</p>
    
    <p>So the question comes down to how do I create a new type in Python using C language?</p>
    
    <h2 id="creating-new-data-types-in-python-without-classes-and-objects">Creating New Data Types in Python Without Classes and Objects</h2>
    
    <p>Before I continue, I’ve to appreciate <a href="https://numpy.org/">Numpy</a> for the incredible peice of software it is, the more I understand it, the more it amazes me.</p>
    
    <p>C is not an Object Oriented Programming Language, but Python is.</p>
    
    <p>In case you didn’t know the most common implementation of Python (the one you most probably have) is written in C! It’s called CPython.</p>
    
    <p>This raises an obvious question, how does Python implement its whole OOP paradigm in C?</p>
    
    <p>This question also answers our question of how to represent <code class="language-plaintext highlighter-rouge">gal_data_t</code> in Python, because essentially they’re looking for the same thing.</p>
    
    <p><code class="language-plaintext highlighter-rouge">PyObject</code> is the answer! To the Python interpreter(written in C) all the data types(built in as well as user defined) are of this type!</p>
    
    <p>and what is this <code class="language-plaintext highlighter-rouge">PyObject</code>? Its a simple struct in C.</p>

