.. title: GSoC 2022: Project Helioviewer — Moving close to the First Release
.. slug:
.. date: 2022-08-10 05:51:50 
.. tags: SunPy
.. author: Akash
.. link: https://medium.com/@akash5100/gsoc-2022-project-helioviewer-moving-close-to-the-first-release-c43249d042d9?source=rss-f3df2a889ecd------2
.. description:
.. category: gsoc2022


.. raw:: html

    <h3>GSoC 2022: Project Helioviewer — Moving close to the First Release</h3><h3>Week 7</h3><p>The solution to switch the base URL of the python API wrapper got merged with PR <a href="https://github.com/Helioviewer-Project/python-api/pull/41">#41</a> and follow-up with PR <a href="https://github.com/Helioviewer-Project/python-api/pull/44">#44</a> by Nabil, now the next endpoint group was the movies.</p>
    <p>I rebased my old PR <a href="https://github.com/Helioviewer-Project/python-api/pull/38">#38</a> with the main branch, which brings the <strong>QueueMovie</strong> endpoint, and opened <a href="https://github.com/Helioviewer-Project/python-api/pull/51">#51</a> which brings <strong>reQueueMovie</strong> and <strong>getMovieStatus </strong>endpoint to facade and backend.</p>
    <p>By the end of the week, both the PR is merged and we now focus on the documentation before the first release.</p>
    <!-- TEASER_END -->
    <h3>Week 8</h3><p>I started working on creating new <strong>RST</strong> files (reStructuredText is a file format for textual data used primarily in the Python programming language community for technical documentation), writing developer's and installation documentation.</p>
    <p>With PR <a href="https://github.com/Helioviewer-Project/python-api/pull/48">#48</a>, the documentation for the first release is ready.</p>
    <p>See the documentation here: <a href="https://hvpy.readthedocs.io/en/latest/">https://hvpy.readthedocs.io/en/latest/</a></p>
    <h3>Week 9</h3><p>The current <strong>hvpy</strong> unittest tests the endpoint functions with the default API URL. But we also want to test the endpoint functions with the beta URL. Basically testing version 3 of the API before release.</p>
    <p>To achieve what we decided, we create an environment variable in the tox file, which triggers the function to <em>switch the base URL, </em>and now all the test in tox runs in the beta URL.</p>
    <ul><li>PR <a href="https://github.com/Helioviewer-Project/python-api/pull/55">#55</a></li></ul><img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=c43249d042d9" width="1" />

