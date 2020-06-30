.. title: GSoC 2020: Generalization of Clients
.. slug:
.. date: 2020-06-29 18:13:52 
.. tags: SunPy
.. author: Abhijeet Manhas
.. link: https://medium.com/@abhimanhas/gsoc-2020-generalization-of-clients-1879f5dfe436?source=rss-7fac54a9b047------2
.. description:
.. category: gsoc2020


.. raw:: html

    <figure><img alt="" src="https://cdn-images-1.medium.com/max/800/0*EsjuLxEt1BrtrdCG" /><figcaption>Solar Eclipse 2020 in Vadodara, Gujarat (Lucky Enough to witness it this year!)</figcaption></figure><p>This fortnight, I worked around iterating over different designs for redesigning the Dataretriever Clients so that its implementation can be simpler and more general. Generalization here means the ability to inherit most of the methods from the base class itself; therefore minimizing a number of similar methods in the subclasses.</p>
    <h4>Show Method for QueryResponse</h4><p>I got<a href="https://github.com/sunpy/sunpy/pull/4309"> PR #4309</a> merged which solved an old <a href="https://github.com/sunpy/sunpy/issues/556">Issue #556</a>. A simple show() function in ~sunpy.net.base_client.BaseQueryResponse enabled QueryResponse objects for Dataretriever, VSO, and JSOC clients to specify the columns to be shown in the result.</p>
    <p>This returns an ~astropy.table.Table instance, so table operations can also be easily performed on the result.</p>
    <!-- TEASER_END -->
    <iframe src="" width="0" height="0" frameborder="0" scrolling="no"><a href="https://medium.com/media/10fce45866473f2eb6ad74e7f98000eb/href">https://medium.com/media/10fce45866473f2eb6ad74e7f98000eb/href</a></iframe><h4>_extract_files_meta method in Scraper</h4><p><a href="https://github.com/sunpy/sunpy/pull/4313">PR #4313</a> was merged in sunpy:master that allows the scraper to extract the metadata stored in the file URLs. This function will prove very useful for refactoring the whole ~sunpy.net.dataretriever submodule.</p>
    <p>A new module parse was added in ~sunpy.extern which allowed to specify the extractor which will parse the file URL and return a dict containing the value of attrs like Wavelength, Time, Level, etc. Even the URL is returned by the method, which ensures no changes are to be made in fetch() methods for clients.</p>
    <iframe src="" width="0" height="0" frameborder="0" scrolling="no"><a href="https://medium.com/media/da15de642196febf9eab940219efac0f/href">https://medium.com/media/da15de642196febf9eab940219efac0f/href</a></iframe><h4>Playing with post filters</h4><p>Last fortnight I was working with post filters and concatenation of responses for VSO. Last week I dabbled a bit with post-filters for attrs used in all net clients. Using single_dispatch decorator over filter_results enabled post-filtering in dataretriver and VSO. It is pretty similar to the way it is done for ~sunpy.net.vso.attrs.</p>
    <iframe src="" width="0" height="0" frameborder="0" scrolling="no"><a href="https://medium.com/media/274b4e0b885d17b391589d15c593f046/href">https://medium.com/media/274b4e0b885d17b391589d15c593f046/href</a></iframe><h3>Redesigning GenericClient</h3><p>So there is a draft <a href="https://github.com/sunpy/sunpy/pull/4321">PR #4321</a> where work is in progress for the new implementation for the generalization. QueryResponeBlock is removed from the client.py since by few changes in the QueryResponse enables us to do it all using a dictionary. Similarly <a href="https://github.com/sunpy/sunpy/pull/4321/files">a lot of methods were removed or changed</a> under the aim to simplify the two Generic Classes.</p>
    <p>Not only the base class, even the client class were made simple. For simple clients, we are supposed to only define required attrs, optional attrs, a baseurl, and an extractor which makes the search working.</p>
    <p>After this refactoring, the example dataretriever source client class would look something like this:</p>
    <iframe src="" width="0" height="0" frameborder="0" scrolling="no"><a href="https://medium.com/media/759cceb1f744c525c6a55e80b8f9ecb9/href">https://medium.com/media/759cceb1f744c525c6a55e80b8f9ecb9/href</a></iframe><p>Only a class method and few class attributes are sufficient for defining a simple DR client!</p>
    <h4>Hooks for translating attrs</h4><p>There are some clients which deviate from generalization. For those clients, it was discussed in a meeting with mentors that post-hooks and pre-hooks for scraper are to be designed which shall perform a translation of attrs provided in the search to their representation in the url. While working around it, I discovered few bugs in fermi_gbm and other clients to be addressed in scraper hooks. Responses for Detector numbers 10 and 11 were never returned because in the url they were represented by na and nb respectively. They will be fixed by translators as a part of pre-hook before passing it to the scraper.</p>
    <h4>Moving Rhessi out from Generic</h4><p>Since rhessi didn’t follow the Generalization as the metadata can’t just be extracted from the file URL, so it is being implemented as subclass of base_client.</p>
    <p>Every week we move closer and closer to Generalization :). Enjoying the meetings where I and my mentors discuss the pros and cons of different designs of GenericClient!</p>
    <img src="https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=1879f5dfe436" width="1" height="1">

