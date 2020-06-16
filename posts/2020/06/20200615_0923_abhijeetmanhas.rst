.. title: GSOC 2020: The Coding period commences!
.. slug:
.. date: 2020-06-15 09:23:54 
.. tags: SunPy
.. author: Abhijeet Manhas
.. link: https://medium.com/@abhimanhas/gsoc-2020-the-coding-period-commences-b2eee33f274e?source=rss-7fac54a9b047------2
.. description:
.. category: gsoc2020


.. raw:: html

    <figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*TYpSW6DKJusjkp7EMXIhyA.png" /><figcaption>Sunrise in Gujarat, near Vadodara city</figcaption></figure><p>So we got started with the coding period, I had a couple of community meetings with my mentors and few full community meetings where I discussed what I was working upon and what was needed to be done.</p>
    <p>Major work in this fortnight was on refactoring<strong> </strong><em>Dataretriever Clients </em>QueryResponse tables Pull request, <a href="https://github.com/sunpy/sunpy/pull/4213">PR #<strong>4213</strong></a>. This enabled the simple clients to show more metadata information like SatelliteNumber , Detector, Level, etc. in their response tables. All this information was extracted from the URL corresponding to the desired files using the parser.</p>
    <p>What did it change? Earlier the things looked like this:</p>
    <!-- TEASER_END -->
    <iframe src="" width="0" height="0" frameborder="0" scrolling="no"><a href="https://medium.com/media/7f467616b2076a3bc10e61d6de755ee3/href">https://medium.com/media/7f467616b2076a3bc10e61d6de755ee3/href</a></iframe><p>And now:</p>
    <iframe src="" width="0" height="0" frameborder="0" scrolling="no"><a href="https://medium.com/media/c9f17aab04a6eac7d1ddd745b2d2f0bf/href">https://medium.com/media/c9f17aab04a6eac7d1ddd745b2d2f0bf/href</a></iframe><p>Those np.nan Wavelength values annoyed me the most and now we not only be having the correct wavelengths, but other details too reflected in the response table. All the columns which were not relevant to the client were removed.</p>
    <p>Was that all about it? No. We need to find better ways of implementing the same feature. Earlier I used a _get_metadata_for_url method to extract all details from the URL, which was separately implemented for all clients. After getting the suggestions from my mentors, I implemented it in a better way; extracting all info in the scraper itself. After completing all tests, we discovered that there can be an even better way of doing this; by removing the client-specific _get_url_for_timerange() method itself! I used the registered attrs for achieving the same. All attrs were iterated to get the list of all possible directories, and then the only thing scraper has to do was pattern matching.</p>
    <p>The idea was to closely link scraper and GenericClient to have minimum client-specific code in their class implementations. I’ll push the changes as I complete all failing tests due to the change and add documentation for the API.</p>
    <p>All the 4 Ground Clients PRs were closed, after a discussion with the SunPy and VSO community. I updated my<a href="https://github.com/sunpy/sunpy/pull/5055"> Gong Synoptic Client Pull Request</a> and got so far all reviews resolved. This would enable SunPy to access the Magnetogram Synoptic Map archives from NSO-GONG. Originally the issue was opened in <a href="https://github.com/dstansby/pfsspy">pfsspy</a><strong>. </strong>I also worked on a fix to the wrong goes Satellite Number issue in <a href="https://github.com/sunpy/sunpy/pull/4288">PR #<strong>4288</strong></a> recently. Using **kwargs in _get_overlap_urls method fixed the bug.</p>
    <p>There were other PRs too made and updated in this period which were merged before SunPy’s 2.0 release. I reduced the time for a goes_suvi client test from 8–10 secs to 1.5–2 secs on my system, in <a href="https://github.com/sunpy/sunpy/pull/4131">PR #<strong>4099</strong></a>. I had to explore why scraper took so much time for the test. Another one <a href="https://github.com/sunpy/sunpy/pull/4132">PR #<strong>4132</strong></a> was a way to prevent a future bug in scraper’s filelist method; so now it checks if the <em>&lt;a href&gt; </em>in any webpage is None or not.</p>
    <p><a href="https://github.com/sunpy/sunpy/pull/4011">PR #<strong>4011</strong></a> was also updated which will restore the ability to post search filter the responses from VSO. I also went through the JSOC codebase and fido_factory.py to understand the complexities of implementation of<em> Fido post-search filter</em> in SunPy. It is the next target in my Project. Just as a glimpse, this is how the VSO will look after post search filtering. I have added an extra concatenation routine by overloading + operator.</p>
    <iframe src="" width="0" height="0" frameborder="0" scrolling="no"><a href="https://medium.com/media/ef282104564e47da6f9bef13c237313e/href">https://medium.com/media/ef282104564e47da6f9bef13c237313e/href</a></iframe><p>I’m enjoying my summer now, wherever I face diffculties I talk with my mentors to get it resolved. I faced some issues in connectivity due to the thunderstorms out there in my city, but now everything is back to normal. The weather is pleasant now so I can engage more!</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*g_aP_bLgp1XI6ACBOrN69A.png" /><figcaption>Before Thuderstorms in Vadodara!</figcaption></figure><p>Looking forward to making more PRs in the next fortnight!</p>
    <p>CARPE NOCTEM!</p>
    <img src="https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=b2eee33f274e" width="1" height="1">

