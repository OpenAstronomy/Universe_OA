.. title: GSOC 2020: New additions to old PRs
.. slug:
.. date: 2020-08-11 18:29:54 
.. tags: SunPy
.. author: Abhijeet Manhas
.. link: https://medium.com/@abhimanhas/gsoc-2020-improvising-the-code-c2d1683fe428?source=rss-7fac54a9b047------2
.. description:
.. category: gsoc2020


.. raw:: html

    <h3>GSOC 2020: Polishing my code</h3><p>I spent last most of the previous two weeks on resolving reviews on my old PRs and improving gallery examples.</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/852/0*fsXbXhCmI6jKwUv6.jpg" /><figcaption>Heavy rains begins in Vadodara</figcaption></figure><h3>Knowing time intervals from URL patterns</h3><p>I created <a href="https://github.com/sunpy/sunpy/pull/4419">PR #4419</a> that allows getting file time-ranges from the URL using the scraper. The URL patterns from most of the archives have start time in them. Either the end time was usually hardcoded for all clients or we only used start time to validate the file URLs against a time interval.</p>
    <p>In my Clients Generalization, to escape this repetitiveness the code in post_search_hook() was somewhat less generalized. It was assumed that all files are day-long. Thus I generalized it and moved it to the scraper. From the base URL pattern, we can now the precision of time supported by the archive directories, and then using them we can find the end times. Say there are yearly files in an archive. Then we can default the end time to the end of that year. Moreover, if this time range overlaps with the searched time interval, the file is valid. We check it using _check_timerange().</p>
    <!-- TEASER_END -->
    <h3>Removed optional from class attributes</h3><p>We now need to register all ‘attrs’ supported by the client in PR #4321. This helped me to escape from defining optional attrs. We use register_values() only to know whether the client can serve the query or not.</p>
    <h3>Fido metadata queries Gallery Example</h3><p>I have added a new gallery example in <a href="https://github.com/sunpy/sunpy/pull/4358">PR #4358</a> which summarizes what we can do after the pull request is merged. We can make metadata queries and easily inspect them. A lot of minor improvements were also made in the PR.</p>
    <iframe src="" width="0" height="0" frameborder="0" scrolling="no"><a href="https://medium.com/media/0e1004e2649bfd262dda2f4e37fed4a8/href">https://medium.com/media/0e1004e2649bfd262dda2f4e37fed4a8/href</a></iframe><h3>Extracting client responses from Fido result</h3><p>Earlier we have to specify index as an argument to get_response() to do that. It required us to count the records to find the correct index. Now we can easily use the name of the client to retrieve QueryResponse instances for that client. If there are multiple such records, then a list of all matching records will be returned.</p>
    <h3>ToDos for the final two weeks</h3><p>I have to document how to write Fido clients and add tests to the Fido metadata compatibility. Let’s see what other issues I can tackle in these pull requests.</p>
    <p>Till then,</p>
    <p><strong>CAPRE NOCTEM!</strong></p>
    <img src="https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=c2d1683fe428" width="1" height="1">

