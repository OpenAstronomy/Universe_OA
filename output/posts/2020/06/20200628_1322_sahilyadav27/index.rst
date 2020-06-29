.. title: Week 3 & 4: First blood
.. slug:
.. date: 2020-06-28 13:22:03 
.. tags: CTLearn
.. author: Sahil Yadav
.. link: https://medium.com/@sahilyadav27/week-3-4-first-blood-dc1ba79de370?source=rss-fd2dd7b5be84------2
.. description:
.. category: gsoc2020


.. raw:: html

    <figure><img alt="" src="https://cdn-images-1.medium.com/max/680/1*eVG6uotsjTa5V092bqJ_uw.jpeg" /><figcaption>“Magic”</figcaption></figure><p>Since the last blog post, where there was a discussion about creating a script to convert the ROOT file into an HDF5 file with the CTA ML data format. So, during week 3 and 4 I was working on making this script. There were a few issues in this conversion.</p>
    <p>In the current DL1DataHandler, the event number is created conveniently in accordance with CTA data. But, the MAGIC data uses a different way to store event numbers. There are 2 arrays for each camera, one for the EvtNumber and another for StereoEvtNumber. The StereoEvtNumber array is mapped from the EvtNumber array. So, I used all the stereo events and stored their values in the HDF5 file. Mono study can be also done on these stereo events. Since MAGIC doesn’t currently do mono analysis on events triggering only one telescope, that part is currently omitted.</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*aDisON-sEtx0T9-w9Lvkeg.png" /></figure><p>So, now that this mapping is figured, we also mapped all the variables required in the HDF5 file with them in the ROOT file. Once everything was set up, I tried reading this converted file using the DL1DataReader. The first run yielded amazing results.</p>
    <!-- TEASER_END -->
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/365/1*gwcmu83NnKO8jYQUFYl5yA.png" /><figcaption>First run output for MAGIC cam 1 and 2 from the converted HDF5 file</figcaption></figure><p>So now I made <a href="https://github.com/cta-observatory/dl1-data-handler/pull/90">PR #90</a> to add this script to the DL1DataHandler. There are a few additions, like reading a runlist instead of filename, adding metadata, etc.</p>
    <p>Hence, the first milestone of the project is complete along with the first month.</p>
    <img src="https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=dc1ba79de370" width="1" height="1">

