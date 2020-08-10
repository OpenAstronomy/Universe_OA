.. title: GSoC 2020: glue-solar project 3.1
.. slug:
.. date: 2020-08-09 23:22:40 
.. tags: SunPy
.. author: Kris Stern
.. link: https://medium.com/@krisastern/gsoc-2020-glue-solar-project-3-1-4aebd6964154?source=rss-33703681b362------2
.. description:
.. category: gsoc2020


.. raw:: html

    <p>The 3rd coding period of GSoC 2020 will officially conclude in 2 weeks time. I would like to take this opportunity to review the progress made thus far, and to outline what other major feature can be added to glue-solar, perhaps over the remaining 2 weeks and beyond.</p>
    <p>We have finally resumed code reviews for the remaining PRs in the glue repo, and I am happy to report that the PR dealing with adding a preferred_cmap attribute to the visual module of glue/core has been merged four days ago from today. This is a very memorable milestone as this is my first contribution to the glue codebase. The remaining PRs which are being worked on include the 1D Profile PR (<a href="https://github.com/glue-viz/glue/pull/2156">PR #2156</a>) as well as the wcs auto-linking PR (<a href="https://github.com/glue-viz/glue/pull/2161">PR #2161</a>).</p>
    <p>Regarding our work at the glue-solar repo, all of the PRs reviewed except the two experimental ones has been merged. A User’s Guide and a Developer’s Guide have been added to the <a href="https://glue-solar.readthedocs.io/en/latest/">docs</a>, while there is one open WIP PR which I am working on to add both a contributing document and the code references (or API) for the repo. Also some docs introducing users on how to start their own extensions in glue-solar for conducting solar physics has been planned.</p>
    <!-- TEASER_END -->
    <p>All of the above will form the bulk of work to be submitted for the GSoC project.</p>
    <p>More can be done for glue-solar, including but not limited to the following:</p>
    <ol><li>Add NDData support to glue via glue-solar</li><li>Add instrument loader code from sunkit-instruments to glue-solar</li><li>Enable image / Movie exports, both with axes and without axes via matplotlib</li><li>Add support for pre-computed statistics in datasets / viewers.</li></ol><p>Hopefully with the support of the mentors much of what has been planned can be brought to fruition, so that this project will be a successful one.</p>
    <img src="https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=4aebd6964154" width="1" height="1">

