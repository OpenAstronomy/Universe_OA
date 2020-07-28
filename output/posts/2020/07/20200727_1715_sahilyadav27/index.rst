.. title: Week 7 & 8: Full Throttle Ahead!
.. slug:
.. date: 2020-07-27 17:15:13 
.. tags: CTLearn
.. author: Sahil Yadav
.. link: https://medium.com/@sahilyadav27/week-7-8-full-throttle-ahead-87dd0823ba1b?source=rss-fd2dd7b5be84------2
.. description:
.. category: gsoc2020


.. raw:: html

    <p>In the last blog post, I was discussing about creating a MAGICEventSource and calling it inside DL1DataWriter to make HDF5 files with the CTA ML data format from the ROOT files.</p>
    <p>I have integrated the MAGICEventSource to writer.py and also updated it to ctapipe v0.8.0. This code is housed at <a href="https://github.com/cta-observatory/dl1-data-handler/pull/90">PR #90</a>. There were a few small issues with the metadata and transformations. The current ctapipe MCHeader container has variables needed to be filled by the input file, but the ROOT file has separate RunHeaders, so we were in a dilemma as to which metadata to store.</p>
    <p>Finally, we decided to create our own MCHeader container inside the MAGICEventSource and use this to store metadata instead of using the ctapipe container.</p>
    <!-- TEASER_END -->
    <p>Also, for the simtel files that have been analysed till now, the telescope pointing Alt and Az are constant and can be hardcoded when we train the deep learning models, to subtract them from the arrival direction Alt and Az. But for the ROOT files, this value is not constant so we will have to create another column into the HDF5 file and pass this value to CTLearn when training on ROOT files.</p>
    <p>There was also some confusion regarding the transformations applied to these Alt and Az values before dumping them to the HDF5 file. We were finally able to figure out what was going wrong with our approach, and plotted the difference between arrival direction and pointing position.</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/386/1*FG648RrN8nWpKPCJ04IF8g.png" /><figcaption>Pointing position vs Arrival direction</figcaption></figure><p>So now all that is left is create the metadata container, and the MAGIC dataset to start training the CTLearn models before we start working on VERITAS data.</p>
    <img src="https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=87dd0823ba1b" width="1" height="1">

