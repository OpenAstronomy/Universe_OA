.. title: Week 1 & 2: Tip-Off
.. slug:
.. date: 2020-06-13 09:50:12 
.. tags: CTLearn
.. author: Sahil Yadav
.. link: https://medium.com/@sahilyadav27/week-1-2-tip-off-1eb6744a41ea?source=rss-fd2dd7b5be84------2
.. description:
.. category: gsoc2020


.. raw:: html

    <p>The first week started off with having a video call with the mentors and trying to pave the path ahead for the next 3 months. There were 2 options: Either convert ROOT files to the hdf5 format from CTA or establish a new DL1 reader for ROOT. I decided to run some tests and get an idea about the speed and memory requirements for both the methods. We were more inclined to create a new class for the ROOT files so that we don’t have to save a separate hdf5 file for each ROOT file when using CTLearn. The reading times for both the file types were also similar, so we decided to implement a new child class for ROOT files.</p>
    <p>In order to move ahead with this plan, I first wrote down the entire DL1DataWriter code, highlighting the hdf5 dependent parts. This way, I was able to get a better understanding of the code and its intricacies. After talking with Tjark some more, we decided to implement 2 child classes for hdf5 and ROOT which inherited the parent Writer class.</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/251/1*JDweXFtW-o-ZqcIbIfzkoQ.png" /></figure><figure><img alt="" src="https://cdn-images-1.medium.com/max/251/1*BfDNzmeG5NYEQn8xTOGZrg.png" /><figcaption>MC simulated images from MAGIC Cam 1 &amp; 2, an event which only triggered one telescope and not the other.</figcaption></figure><p>After another video call, Ari suggested that I convert the ROOT files into an hdf5 file with the CTA ML Data format to understand the differences between the formats of MAGIC and CTA. Although there is already a library ctapipe_io_magic to produce the MAGICEventSource and use it for DL1DataReader and produce an hdf5 file, there were a lot of issues with trying to use it.</p>
    <!-- TEASER_END -->
    <p>So we decided to implement our own code to convert the file. This way, any ROOT file can be converted to hdf5 and used by CTLearn before the actual project is complete and in place. During week 2, I worked on writing code for the same. It is mostly complete and a few things need to be ironed out which will be done in the next call on 15th.</p>
    <p>Once this is done, I’ll start to work on creating separate child classes for ROOT and hdf5 inheriting from DL1DataWriter as discussed above.</p>
    <img src="https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=1eb6744a41ea" width="1" height="1">

