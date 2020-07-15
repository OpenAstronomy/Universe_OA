.. title: GSOC 2020: End of the First Half
.. slug:
.. date: 2020-07-14 22:12:28 
.. tags: SunPy
.. author: Abhijeet Manhas
.. link: https://medium.com/@abhimanhas/gsoc-2020-end-of-the-first-half-ec4589cc452f?source=rss-7fac54a9b047------2
.. description:
.. category: gsoc2020


.. raw:: html

    <figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/0*L9pxwg-v0q0SppOR.jpg" /><figcaption>Comet C/2020 F3 (NEOWISE) will be visible in India for the next 20 days!</figcaption></figure><p>So now I’m halfway through the Summer of Code Journey. The last two weeks have been full of code reviews, code refactoring, and documenting stuff. I also helped new contributors to the SunPy to get them started. Thus I interacted more with the community this time.</p>
    <h3>Making HEC Fido Compatible</h3><p>HEC stands for <strong>Heliophysics Event Catalogue</strong>. For your information, Heliophysics events are a large variety of phenomena that:</p>
    <ul><li>originate or occur on the Sun.</li><li>Propagate through the interplanetary medium.</li><li>Interact with the geospace and planetary analogs.</li></ul><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/0*7_zVGR8NSlvJ4vOi.jpg" /><figcaption>An illustration of an Heliophysics Event| Earth’s magnetic field shielding our planet from solar particles. Credit: NASA/GSFC/SVS</figcaption></figure><p>HEC allows complex searches for events stored in indexed catalogs. SunPy has a HECClient which allows you to interface with Helio web services.</p>
    <!-- TEASER_END -->
    <p>In <a href="https://github.com/sunpy/sunpy/pull/4358">PR #4358</a> to enable Helio metadata searches with Fido (Federated Internet Data Obtainer), I made it inherit ~sunpy.net.BaseClient and overwrote a few methods for the client. New hec-specific attrs like MaxRecords, TableName, and Catalogue were defined to make _can_handle_query() work.</p>
    <iframe src="" width="0" height="0" frameborder="0" scrolling="no"><a href="https://medium.com/media/8cebddc67806c7e7130b0e70722fa975/href">https://medium.com/media/8cebddc67806c7e7130b0e70722fa975/href</a></iframe><p>A new class HECResponse was added to contain the responses retrieved after the search is executed. This made helio queries possible through Fido, although there are yet a lot of things that can be improved.</p>
    <h3>Updated tests for client redesign!</h3><p><a href="https://github.com/sunpy/sunpy/pull/4321">PR #4321</a> (nice number!) is a major refactoring pull request for sunpy’s dataretriever module. So far it has negative 1500 lines of code.</p>
    <p>Finally SUVIClient was generalized which was the toughest of its counterparts. It supports the highest number of attributes. These are `Time`, Source, Instrument, Phsyobs, Provider, Level, Wavelength, and SatelliteNumber.</p>
    <p>The row data for the response table can either be contained as a dictionary or as data members of a class. A small hack made me achieve both. QueryResponseBlock was re-welcomed to the client.py. It now inherits OrderedDict and has dict values as class data members too. Passed Ordered Dictionary was used to update its self.__dict__.</p>
    <iframe src="" width="0" height="0" frameborder="0" scrolling="no"><a href="https://medium.com/media/b8dae93e3cdf41797f7797b54de3573b/href">https://medium.com/media/b8dae93e3cdf41797f7797b54de3573b/href</a></iframe><h3>Other Stuff</h3><p>My mentor made a list of 38 issues in Sunpy that were related to the project. I went through all of them and labeled them based on the submodules they are concerned with, how much I understand them, and their relevance with the GSoC project. Some of them were overlapping with things in my mind, so existing discussions on them shall be really helpful for me.</p>
    <p>I also spent time on writing the guidelines to extend Fido and how to add new sources to it, based on the redesign.</p>
    <p>Looking forward to capturing the comet in the coming days and having an awesome second half!</p>
    <p><strong>CARPE NOCTEM!</strong></p>
    <img src="https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=ec4589cc452f" width="1" height="1">

