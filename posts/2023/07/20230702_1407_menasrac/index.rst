.. title: Setting Up for the Kurucz PR and transitioning to the TheoReTS
.. slug:
.. date: 2023-07-02 14:07:42 
.. tags: radis
.. author: Racim MENASRIA
.. link: https://medium.com/@menasrac/setting-up-for-the-kurucz-pr-and-transitioning-to-the-theorets-d9643c0269aa?source=rss-e63f6bf6735b------2
.. description:
.. category: gsoc2023


.. raw:: html

    <p>This week was not the most enjoyable phase of the project so far, as I had to exert considerable effort to fix failing tests before opening a pull request.</p>
    <p>Once I ensured that the initial tests passed, I wrote my own tests to confirm that the new AdB Kurucz class didn’t interfere with any part of the existing code. At this point, I encountered a primary issue. I hadn’t noticed that one of the methods I had adapted from ExoJAX was still reading a file which necessitated an ExoJAX package dependency. This caused the build to fail on GitHub due to one of the tests in my kurucz_test.py file failing.</p>
    <p>Since there’s a conflict related to the JAX installation on Windows, I couldn’t add it to the requirements file. Doing so would create a conflict for every Windows user installing Radis. Consequently, I had to write a program to extract the data from this package and store a copy of it in a local file called pfdat.txt. This enabled the problematic function to read from the local copy instead of the ExoJAX file. This solution successfully rectified the problem, and now my PR passes the tests and is awaiting review before merging.</p>
    <!-- TEASER_END -->
    <p>The next step is to transition to the TheoReTS as planned. According to the TheoReTS website, it is an information system for theoretical spectra based on variational predictions from molecular potential energy and dipole moment surfaces. It is jointly developed by the PMT team of GSMA (Reims), Tomsk University, and IAO Acad Sci. Russia. As a result, it provides two access points, one French and the other Russian. However, I noticed that the access to the French website (<a href="http://theorets.univ-reims.fr/">http://theorets.univ-reims.fr/</a>) is currently unavailable, preventing me from visualizing the data. This is an issue I should discuss with my mentors.</p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=d9643c0269aa" width="1" />

