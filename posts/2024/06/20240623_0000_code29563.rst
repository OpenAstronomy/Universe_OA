.. title: Stark broadening and the Common API
.. slug:
.. date: 2024-06-23 00:00:00 
.. tags: radis
.. author: code29563
.. link: http://code29563.github.io/Stark-broadening-and-the-Common-API/
.. description:
.. category: gsoc2024


.. raw:: html

    <p>Stark broadening for atomic lines has been implemented with different temperature scalings for neutral and ionised radiators.</p>
    
    <p>I integrated the API for atomic Kurucz linelists into the Common API, and in doing so the issue related to <code class="language-plaintext highlighter-rouge">truncation</code> and <code class="language-plaintext highlighter-rouge">optimization</code> seems to have been resolved.</p>
    <!-- TEASER_END -->
    
    <p>The main differentiating aspect so far in the Common API for Kurucz is that new versions of linelists and lab lines aren’t available for all species, the result being that the url from which to download the Kurucz linelist isn’t known with certainty before actually attempting to download it, so the possibilities are ranked and attempted in order of preference and the first to return a valid response is used.</p>

