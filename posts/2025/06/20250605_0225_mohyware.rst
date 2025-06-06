.. title: GSoC 2025 Blog — Week 1: Starting the Project
.. slug:
.. date: 2025-06-05 02:25:44 
.. tags: radis
.. author: mohyware
.. link: https://medium.com/@mohyware/gsoc-2025-blog-week-1-starting-the-project-59a02a05ae58?source=rss-9dc0b0efcdaa------2
.. description:
.. category: gsoc2025


.. raw:: html

    <h3>GSoC 2025 Blog — Starting the Project</h3><h3>Kicking Things Off</h3><p>The first weeks of GSoC were all about getting familiar with the project, understanding its current state, and laying the groundwork for upcoming work. We began by <strong>listing the key features</strong> we plan to implement and prioritizing them based on impact and feasibility.</p>
    <h3>Cleaning Up the Repo</h3><p>Before diving into development, we focused on improving the current state of the codebase:</p>
    <ul><li>Filtered through existing PRs.</li><li>Merged those that were ready.</li><li>Closed duplicates or low-quality submissions.</li><li>Requested changes when necessary.</li></ul><p>This cleanup helped fix some bugs and made the repository more maintainable moving forward.</p>
    <!-- TEASER_END -->
    <h3>CI Enhancements</h3><p>To ensure future contributions are smoother, we improved the Continuous Integration setup:</p>
    <ul><li>Added conditional CI jobs to run <strong>frontend or backend tests</strong> only when their respective files are changed.</li><li>Introduced <strong>Codecov comments</strong> to show coverage of newly added lines, making it easier to track test quality in PRs.</li></ul><p>These changes should streamline reviews and reduce unnecessary CI runs.</p>
    <h3>Early Contributions</h3><p>I also started contributing new features and improvements:</p>
    <ul><li><strong>Integrated ExoMol and NIST databases</strong> into the backend.</li></ul><p>While integrating the NIST database, I encountered a tricky error related to the RADIS package:</p>
    <pre>No databank named nist in `/home/mohy/radis.json`. Available databanks: […]</pre><p>It turned out that the version of RADIS in the was outdated and didn’t recognize the `nist` databank. This was fixed by upgrading RADIS:</p>
    <pre>pip install — upgrade radis</pre><p>Then, another error popped up related to pandas:</p>
    <pre>No such keys(s): 'future.no_silent_downcasting'</pre><p>This was caused by version incompatibility, which was resolved by upgrading pandas:</p>
    <pre>pip install — upgrade pandas</pre><p>After these upgrades, the databases worked correctly on the backend. The frontend integration and performance optimizations (e.g., caching) are next on my list.</p>
    <ul><li><strong>Increased backend test coverage</strong>, especially for newly added endpoints and database integrations.</li></ul><p>That’s a wrap for the first weeks! It’s been a productive start, and I’m excited to keep building and learning in the coming weeks. Stay tuned for more updates!</p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=59a02a05ae58" width="1" />

