.. title: GSoC - 2
.. slug:
.. date: 2021-07-19 03:00:06 
.. tags: radis
.. author: Gagan Aryan
.. link: https://gagan-aryan.netlify.app/posts/gsoc-2/
.. description:
.. category: gsoc2021


.. raw:: html

    <p>Welcome back !! So we are done with our first phase of the project and are shifting into the second one. I will be keeping this blog short since most of the details of the refactor have already been written in my previous post.</p>
    <p>By the time I was writing my previous post I had a pretty decent idea of how I would be doing each of the refactors. We had already decided that we may not have to implement all of them because Vaex might render a few of those changes redundant.</p>
    <p>I started out by writing a proof-of-concept to remove the column where partition function was added. Only the case of equilibrium molecules was handled here. The idea was to make use of pandas&rsquo; dictionary efficiently and remove the column. With the proof-of-concept we could conclude that not only did this approach reduce memory, but it also reduced CPU pressure by around 2x. For the lines of <code>HITEMP-CH4</code> molecules for the waverange 2000-3000 previously the dataframe occupied 1.2 GB but with this method we could compress that to around 100 MB. <sup id="fnref:1"><a class="footnote-ref" href="https://gagan-aryan.netlify.app/tags/gsoc21//index.xml#fn:1">1</a></sup></p>
    <!-- TEASER_END -->
    <p>Apart from this I wrote down another notebook that demostrated that we can radically improve memory usage by crunching the datatypes of the columns of <code>HITRAN/HITEMP</code> molecules. The notebook just contains elementary operations to arrive at the right datatype for each of the column. We haven&rsquo;t implemented this into the codebase yet because we still haven&rsquo;t figured out what we will be doing with the missing lines. A problem I had already mentioned in my first post. <sup id="fnref:2"><a class="footnote-ref" href="https://gagan-aryan.netlify.app/tags/gsoc21//index.xml#fn:2">2</a></sup></p>
    <p>I was somehow able to sneak my way into successfully completing GSoC phase one with feedback that has pumped me to do even better. I am looking forward to the second phase and hope to deliver.</p>
    <div class="footnotes">
    <hr />
    <ol>
    <li id="fn:1">
    <p><a href="https://github.com/radis/radis-benchmark/blob/master/manual_benchmarks/test_Qgas.ipynb">Proof-of-Concept for Qgas</a> <a class="footnote-backref" href="https://gagan-aryan.netlify.app/tags/gsoc21//index.xml#fnref:1">&#x21a9;&#xfe0e;</a></p>
    </li>
    <li id="fn:2">
    <p><a href="https://github.com/radis/radis-benchmark/pull/11">Proof-of-Concept for Datatype Crunching - WIP</a> <a class="footnote-backref" href="https://gagan-aryan.netlify.app/tags/gsoc21//index.xml#fnref:2">&#x21a9;&#xfe0e;</a></p>
    </li>
    </ol>
    </div>

