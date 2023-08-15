.. title: Docs and Marty and the Moving Around of Code and Tests
.. slug:
.. date: 2023-08-12 05:33:30 
.. tags: SunPy
.. author: exitflynn
.. link: https://exitflynn.github.io/blog/posts/gsoc-sixth/
.. description:
.. category: gsoc2023


.. raw:: html

    <p>Since the last post, I worked on the moving-the-code task. Me, Nabil and Alasdair got on a call to discuss what should go where and I ended up creating a <code>scraper_utils.py</code> file to complement the <code>scraper.py</code> file. The other options were moving the functions to <code>.util.net</code> or inside the <code>scraper.py</code> file but outside the <code>Scraper</code> class. After I moved the tests as well, I wrote new tests, increased test coverage and renamed some functions which were previously named in the JavaScript-style CamelCase.
    I also added and extended doc-strings to some functions which could use some updating and made fixes as asked in Code-Reviews.</p>
    <!-- TEASER_END -->

