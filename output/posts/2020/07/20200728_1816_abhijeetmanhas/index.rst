.. title: GSOC 2020: Metadata searches using Fido
.. slug:
.. date: 2020-07-28 18:16:19 
.. tags: SunPy
.. author: Abhijeet Manhas
.. link: https://medium.com/@abhimanhas/gsoc-2020-metadata-searches-using-fido-909bda98b771?source=rss-7fac54a9b047------2
.. description:
.. category: gsoc2020


.. raw:: html

    <figure><img alt="" src="https://cdn-images-1.medium.com/max/816/0*hF5ggLHngI8p-yaa" /><figcaption>Missed Comet NEOWISE due to annoying cloud cover in Vadodara straight for 2 weeks :(</figcaption></figure><p>And that’s the central theme of the project :)</p>
    <p>It would now be possible to query clients that return metadata tables using Fido. So SunPy’s <strong>Fido</strong> is a unified interface that allows searching and downloading solar physics data. In other words, it is a consistent and easy way to query most forms of solar physics data. It searches various archives and web services based on search attributes specified in the query.</p>
    <p>SunPy currently supports metadata facilities viz., JSOC Client, HEK Client, and Helio Client.</p>
    <!-- TEASER_END -->
    <p>SunPy’s hek module is used to access the information in the <strong>Heliophysics Event Knowledgebase</strong> (HEK). HEK helps solar and heliospheric researchers locate features and events of interest.</p>
    <p><strong>Joint Science Operations Center</strong> (JSOC) supports data products from various observatories and solar physics instruments.</p>
    <p>But they were not Fido compatible for metadata searches. PR #4358 addresses it.</p>
    <h3>Generic Class for metadata clients</h3><p>Since a lot of methods were similar in these clients, so I made a new superclass for them. JSOC, Helio, and HEK responses now inherit BaseQueryResponseTable to ease inspecting data retrieved through their clients. The idea was to retain the old look of response tables and also support a method to show all columns if required.</p>
    <iframe src="" width="0" height="0" frameborder="0" scrolling="no"><a href="https://medium.com/media/abb67aed8bc120d39e874af9ef9ab599/href">https://medium.com/media/abb67aed8bc120d39e874af9ef9ab599/href</a></iframe><h3>Deprecations</h3><p>~sunpy.net.hek.attrs.Time is deprecated since we can now use ~sunpy.net.attrs.Time for HEK queries, making it redundant.</p>
    <p>I also deprecated ~sunpy.net.jsoc.attrs.Keys because now the response table contains all keys by default. Users can specify the column names as *args in :meth:~sunpy.net.hek.HEKResponse.show for getting an ~astropy.table.Table instance containing only those columns.</p>
    <iframe src="" width="0" height="0" frameborder="0" scrolling="no"><a href="https://medium.com/media/d663f6878e23ecc59cd3f0b7cce932ef/href">https://medium.com/media/d663f6878e23ecc59cd3f0b7cce932ef/href</a></iframe><p>Finally, HEKTable was renamed to HEKResponse for consistency in naming.</p>
    <h3>Devguide for writing Fido Clients</h3><p>I have explained how to write a simple Fido client in <a href="https://github.com/sunpy/sunpy/pull/4387">PR 4387</a>. This was the first documentation pull request that I made in SunPy. Work is in progress for adding details of writing an “AttrWalker” and registring an “Attr” for Fido.</p>
    <iframe src="" width="0" height="0" frameborder="0" scrolling="no"><a href="https://medium.com/media/449c51d6f6528dbb0a236344fe4a9524/href">https://medium.com/media/449c51d6f6528dbb0a236344fe4a9524/href</a></iframe><h3>Other Stuff</h3><p>I reviewed<a href="https://github.com/sunpy/sunpy/pull/4394"> PR #4394</a>, which allows XRSClient to download reprocessed data for GOES Satellites. I also need to add support for this new pattern in my <a href="https://github.com/sunpy/sunpy/pull/4321">dataretriever refactoring pull request, #4321</a>.</p>
    <p>I also go through the discussions present in the net issues so I can fit their fixes in my project. I also suggest updates to the description of outdated issues and check if they still persist, like in <a href="https://github.com/sunpy/sunpy/issues/2401">Issue #2401</a>.</p>
    <p><a href="https://github.com/sunpy/sunpy/issues/2032">Issue #2032</a> was fixed, so now helio wsdl_retriever returns the first valid taverna link.</p>
    <p>We are going to now enter the last phase of the work period!</p>
    <p><strong>CARPE NOCTEM!</strong></p>
    <img src="https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=909bda98b771" width="1" height="1">

