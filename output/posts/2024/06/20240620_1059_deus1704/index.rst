.. title: Blog 2: All Pieces Falling into place
.. slug:
.. date: 2024-06-20 10:59:31 
.. tags: SunPy
.. author: Deus1704
.. link: https://deus1704.vercel.app/posts/blog_2/
.. description:
.. category: gsoc2024


.. raw:: html

    <h2 id="update-on-new-coalignment">Update On New Coalignment</h2>
    <p>The very first version of the new Coalignment API has been completely implemented, with all the test cases written!
    The architecture of the proposed co-alignment API closely mirrors the design principles found in SunPy&rsquo;s rotation module, where a decorator pattern is employed to register specific methods designated for executing co-alignment tasks. Detailed documentation and guidelines on utilizing the new API are available for review at <a href="https://sunpy--207.org.readthedocs.build/projects/sunkit-image/en/207/how_to_guide/adding_a_coalignment_method.html">this</a> docs.</p>
    <!-- TEASER_END -->
    <h2 id="ideas-regarding-the-future-of-coalignment--major-concerns">Ideas regarding the Future of Coalignment &amp; Major Concerns</h2>
    <p>We have received numerous comments concerning the new co-alignment API, with the majority emphasizing the revision of the coalignment methods rather than the API structure itself.
    Consequently, I will be delving into the specific modifications occurring at the World Coordinate System (WCS) level throughout the coalignment process and the request of returning only the shifts and not applying the shift to the actual data.</p>
    <p>Although we are afraid that the suggestiong might be aiming to reinvent the reproject but again the fundamentally the approach for the two is different and needs to be thought of in brief before taking any major steps.
    We might be discussing this issue in the next community meet once Stuart is back.</p>
    <h2 id="update-on-stara">Update on STARA</h2>
    <p>The STARA module and the examples are completely ready, after along time of resolving conflicts, planning testing. We have come a long way with these test figures.</p>
    <table>
    <thead>
    <tr>
    <th style="text-align: center;"><img alt="HMI Map" src="https://deus1704.vercel.app/images/test_hmi.png" /></th>
    <th style="text-align: center;"><img alt="HMI Map with Sunspot Identified" src="https://deus1704.vercel.app/images/stara_hmi.png" /></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: center;">Test HMI Continuum Map</td>
    <td style="text-align: center;">Sunspot identified by STARA on the Test Map</td>
    </tr>
    </tbody>
    </table>

