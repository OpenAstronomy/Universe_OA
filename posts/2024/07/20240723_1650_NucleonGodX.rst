.. title: Enhancing SOAR Queries: Improved Error Handling and Support for Distance-Based Filtering
.. slug:
.. date: 2024-07-23 16:50:13 
.. tags: SunPy
.. author: Manit Singh
.. link: https://medium.com/@manitsingh018/enhancing-soar-queries-improved-error-handling-and-support-for-distance-based-filtering-79c57af30ffc?source=rss-472b9ac5a505------2
.. description:
.. category: gsoc2024


.. raw:: html

    <h3>Improved Error Handling and Support for Distance-Based Filtering</h3><h3>Introduction</h3><p>Over the past few weeks, I’ve been working on addressing and enhancing certain functionalities within the sunpy-soar package. This post delves into the two main improvements I’ve implemented: better error handling for server downtime and the introduction of support for distance-based query filtering.</p>
    <h3>Improved Error Handling for Server Downtime</h3><p>Previously, when the SOAR server was down, a generic JSONDecodeError would be raised. This was less than ideal as it did not provide a clear indication of what the actual issue was. To improve this, I worked on implementing a more descriptive error message that would be raised in such scenarios.</p>
    <pre>r = requests.get(f&quot;{tap_endpoint}/sync&quot;, params=payload)<br />try:<br />    response_json = r.json()<br />except JSONDecodeError:<br />    msg = &quot;Server returned an invalid JSON response. The SOAR server may be down or not functioning correctly.&quot;<br />    raise RuntimeError(msg)</pre><p>With this change, users will now see a RuntimeError with a clear message indicating that the server may be down or not functioning correctly, which makes troubleshooting much easier.</p>
    <!-- TEASER_END -->
    <h3>Implementing Support for Different REQUEST Types</h3><p>After resolving the error handling issue, I moved on to implementing support for different REQUEST types. Sunpy-soar initially only supported the doQuery REQUEST type. However, there was a need to expand this to support the doQueryFilteredByDistance REQUEST type as well.</p>
    <h3>What is doQueryFilteredByDistance?</h3><p>The doQueryFilteredByDistance REQUEST type allows for filtering the query results based on a specified distance range. The main change here is setting the REQUEST parameter to doQueryFilteredByDistance and appending &amp;DISTANCE(distancemin,distancemax) to the query.</p>
    <p><strong>Example Query:</strong></p>
    <pre>SELECT * FROM soar.v_sc_data_item WHERE instrument='MAG' AND level='LL02'</pre><p><strong>With Distance Filtering:</strong></p>
    <pre>SELECT * FROM soar.v_sc_data_item WHERE instrument='MAG' AND level='LL02' AND DISTANCE(0.28,0.49)</pre><h3>Conclusion</h3><p>These enhancements significantly improve the functionality and user experience of the sunpy-soar package. The improved error handling provides clearer feedback to users when the SOAR server is down, and the support for doQueryFilteredByDistance allows for more refined queries based on distance, opening up new possibilities for data analysis.</p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=79c57af30ffc" width="1" />

