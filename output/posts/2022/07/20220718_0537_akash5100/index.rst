.. title: GSoC 2022: Project Helioviewer — Facade for the API wrapper
.. slug:
.. date: 2022-07-18 05:37:22 
.. tags: SunPy
.. author: Akash
.. link: https://medium.com/@akash5100/gsoc-2022-project-helioviewer-facade-for-the-api-wrapper-69689b163879?source=rss-f3df2a889ecd------2
.. description:
.. category: gsoc2022


.. raw:: html

    <h3>GSoC 2022: Project Helioviewer — Facade for the API wrapper</h3><h3>Week 3</h3><p>The Generic Function got merged with PR <a href="https://github.com/Helioviewer-Project/python-api/pull/21">#21</a>. This PR adds a function that accepts a URL Endpoint, Input Parameters (dictionary), and a descriptor of Output Parameters (what the endpoint is expected to return), which all the endpoint classes will inherit.</p>
    <p>This PR also includes the unittest for the Generic function and brings the first endpoint to the API wrapper, which is <a href="https://hvpy.readthedocs.io/en/latest/api/hvpy.parameters.getJP2ImageInputParameters.html#getjp2imageinputparameters"><strong>getJP2Image</strong></a><strong>. </strong>This endpoint retrieves a JP2000 image from the <a href="http://helioviewer.org">helioviewer.org</a> API.</p>
    <h3>Week 4</h3><p>The next task was to create a frontend for the <strong>getJP2Image </strong>endpoint. The actual front end that users will interface with lives in a file called <strong>facade</strong> which will hide this internal design. This module contains the API interface in its simplest form. It is responsible for taking user input, constructing the <strong>HvpyParameters </strong>instance (the base class) and passing it to the <strong>core</strong> to perform the request.</p>
    <!-- TEASER_END -->
    <p>View the code in:</p>
    <ul><li>PR <a href="https://github.com/Helioviewer-Project/python-api/pull/33">#33</a></li></ul><h3>Week 5</h3><p>Finally, after the merging of the frontend function, we bring more JPEG2000 endpoints.</p>
    <ul><li>PR <a href="https://github.com/Helioviewer-Project/python-api/pull/34">#34</a> — Adds the endpoint to the backend.</li><li>PR <a href="https://github.com/Helioviewer-Project/python-api/pull/36">#36</a> — Adds the frontend function.</li></ul><h3>Week 6</h3><p>Still, a problem left to solve. There are several mirrors for Helioviewer and people might want to use a mirror instead of the main URL. So we will need to add a way to change this.</p>
    <p>PR <a href="https://github.com/Helioviewer-Project/python-api/pull/41">#41</a> closes this issue but it’s still under work. Hopefully, by the end of the week, it gets merged :)</p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=69689b163879" width="1" />

