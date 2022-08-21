.. title: GSoC Blog #3
.. slug:
.. date: 2022-08-20 07:02:40 
.. tags: stingray
.. author: AMAN PANDEY
.. link: https://medium.com/@aman_p/gsoc-blog-3-350c7b7dad61?source=rss-1bafed5b4c37------2
.. description:
.. category: gsoc2022


.. raw:: html

    <figure><img alt="" src="https://cdn-images-1.medium.com/max/680/1*dfjiDfMcY8h9eEOySAnxbA.jpeg" /></figure><p>Mid Evaluations are over, and I’m glad to be back at work. As the base functionality is done now, I am on to provide user APIs to create cross spectra and periodograms from actual astronomical data easily.</p>
    <p>I was busy the first week after the mid-term due to intern season at my campus, so that I couldn’t contribute much. Afterward, I started by understanding different functionalities related to photon count events next week. The plan was to:</p>
    <ol><li>Read the photon count data from different file formats and get the essential information like time, GTIs, PI channels, etc.</li><li>Create EventList struct and handle different methods like sorting, joining, filtering, and simulating these data.</li><li>Test these methods by appropriately re-binning, creating periodograms, and plotting the data.</li></ol><p>There was also modification in the git workflow as the documentation branch was based on the gti one, which now has its parent main.</p>
    <!-- TEASER_END -->
    <p>For the 3rd week, I have worked on the EventList APIs and the data reading part. Its currently implemented for the FITS extension, but I will expand to other formats like HDF5 or ECSV. I have also studied LightCurve structure and implemented a to and from conversion with EventLists, although its methods are needed to be worked upon.</p>
    <p>In the coming weeks, I aim to create extensive tests, debug these methods, and optimize them in Julia. After these are done, other features like coherence and time lags will also be necessary. The period will <em>end</em> with documentation and refactoring of already existing codes, and <em>if</em> I get time, I will work on variability vs. energy spectrum.</p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=350c7b7dad61" width="1" />

