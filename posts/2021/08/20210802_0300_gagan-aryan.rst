.. title: GSoC - 3
.. slug:
.. date: 2021-08-02 03:00:06 
.. tags: radis
.. author: Gagan Aryan
.. link: https://gagan-aryan.netlify.app/posts/gsoc-3/
.. description:
.. category: gsoc2021


.. raw:: html

    <p>Hello and welcome to the first blog of GSoC phase-2. Ever faced a time when there was way too much on the plate and you find it really hard to catch up on all the work? That is pretty much how the previous two weeks were for me. With the start of the oncampus internship drive, I was finding it really hard to give manage the project. Somehow I was able to make some progress but I am yet to complete the task.</p>
    <p>I am basically trying to parse the <code>.bz2</code> files of <code>HITEMP</code> databases into HDF5 files in a Vaex friendly format. Currently <code>.bz2</code> files are parsed into HDF5 files with the help of high level pandas functions. But as we already know pandas can be very memory consuming. So, I am trying to write to HDF5 files with <code>h5py</code> library and produce HDF5 files that are vaex friendly (column based).</p>
    <p>In order to do this, I am first converting <code>bz2</code> files to <code>.csv</code> upon download -&gt; mapping the datatypes of each of the columns -&gt; writing to a HDF5 file with <code>h5py</code>. I am currently stuck at mapping the datatypes and also trying to make optimizations with respect to the chunksize.</p>
    <!-- TEASER_END -->
    <p>This blog is just a quick update on the things that are happening currently. Once the writing to a HDF5 files is completed, look out for a detailed tutorial on the same on towardsdatascience :)</p>

