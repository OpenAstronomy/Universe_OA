.. title: Week 5 & 6: Half-time
.. slug:
.. date: 2020-07-15 04:56:26 
.. tags: CTLearn
.. author: Sahil Yadav
.. link: https://medium.com/@sahilyadav27/week-5-6-half-time-e343ac6bd699?source=rss-fd2dd7b5be84------2
.. description:
.. category: gsoc2020


.. raw:: html

    <p>The first evaluation is successfully complete!</p>
    <p>In the last blog post, I discussed adding a script to the DL1DataHandler to convert ROOT files to HDF5. But, in order to maintain symmetry with the current DL1DataWriter, we decided to instead create a MAGICEventSource from this root2hdf5 format that initializes the DL1 data container with ROOT data and then is sent to the CTAMLDataDumper to dump this data into an HDF5 file. This will be analogous to the SimTelEventSource that is currently being used for CTA data from simtel files.</p>
    <p>So, I have been working on creating this MAGICEventSource. The basic code for the class structure is complete, and the containers are initialized correctly. All that remains now is to add some code to the DL1DataWriter and CTAMLDataDumper to accept and recognize MAGIC data and use the MAGICEventSource instead of the SimTelEventSource.</p>
    <!-- TEASER_END -->
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*EOSlgwziXKXKk76EYbnN2A.png" /></figure><p>In the meantime, I also adapted the generate_runlist script to create runlists specifically for MAGIC data, since the MAGICEventSource reads file masks instead of a couple of M1 and M2 files for each observation.</p>
    <p>Hence, both these changes will be pushed soon to the main repository and then we can start working on reading VERITAS data similarly as well as training MAGIC data using CTLearn models.</p>
    <img src="https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=e343ac6bd699" width="1" height="1">

