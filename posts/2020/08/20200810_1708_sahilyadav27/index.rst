.. title: Week 8 & 9: Buzzer Beater?
.. slug:
.. date: 2020-08-10 17:08:08 
.. tags: CTLearn
.. author: Sahil Yadav
.. link: https://medium.com/@sahilyadav27/week-8-9-buzzer-beater-80e03f9a5e1b?source=rss-fd2dd7b5be84------2
.. description:
.. category: gsoc2020


.. raw:: html

    <h3>Week 9 &amp; 10: Buzzer Beater?</h3><p>In the past two weeks, I worked on creating the MCHeader Container for MAGIC data. After discussing with people working at MAGIC, we used the RunHeaders TTree variables to create the Container.</p>
    <p>For the arrival direction and telescope pointing, we decided to use the MSrcPosCam variable from the ROOT file, which stores the shower direction relative to the telescope, i.e arrival direction-telescope pointing. Thus, we don’t need to think much about the Alt-Az transformations as well. And we don&#39;t have to create a separate column for telescope pointing in the HDF5 file. This saves computation time too.</p>
    <p>This solves two of the major issues we were having last time. Now, we will soon start training some MAGIC gamma data files from the two telescopes using the CTLearn deep learning models and get some benchmark results on the same.</p>
    <!-- TEASER_END -->
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/800/1*Ee0UeDUTC37W9_-ZioSEZQ.jpeg" /><figcaption>Devin Booker hitting the buzzer-beater in Kawhi and PG’s face. Hoping this is how GSoC ends.</figcaption></figure><p>We were also trying to create an event source for VERITAS data, but there were some issues with reading the data. We’ll see how this error progresses.</p>
    <img src="https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=80e03f9a5e1b" width="1" height="1">

