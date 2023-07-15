.. title: Wild Wild Tests
.. slug:
.. date: 2023-07-14 05:33:30 
.. tags: SunPy
.. author: exitflynn
.. link: https://exitflynn.github.io/blog/posts/gsoc-post-the-fourth/
.. description:
.. category: gsoc2023


.. raw:: html

    <h1 id="fool-proofing-the-rewrite">Fool-Proofing the Rewrite
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#fool-proofing-the-rewrite">
    <!-- TEASER_END -->
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h1><p>After the last post, I mostly kept working on fixing the other failing tests and rewriting the tests to go with the newer pattern.</p>
    <h1 id="not-all-failing-tests-are-built-same">Not All Failing Tests are Built Same
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#not-all-failing-tests-are-built-same">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h1><p>I managed to take care of them in a couple of days, except the <code>sunpy/net/tests/test_scraper.py::testFilesRange_sameDirectory_local</code> which proved to be a tough one to figure out. After discussing it a bit, I was able to figure it out, the error was caused because of a very unique flow of things which I think would be interesting to mention. I found out the test was failing because in the <code>_localfilelist()</code> function, we update the pattern class variable, call different functions on it and then fix it back at the end. Though once I realised this, I was able to spot that I needed to update the second pattern as well in a similar way and I discussed different approaches to do this with the mentors but the flow in the function was a very fun and intuitive way to do things that stood out to me for reason and I just wanted to make a note of it to look back on :P.</p>
    <p>I also discussed my doubt relating to trying to shorten parse patterns by avoiding repetitions somehow but we came to the conclusion that we don&rsquo;t really need to do that, if a pattern has repetitions in it then the user&rsquo;s got to repeat stuff!</p>
    <h1 id="was-that-it">Was that it?
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#was-that-it">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h1><p>Now once all the scraper tests were passing, I thought the PR should be ready for review. I informed my mentors for the same. The PR received some suggestions, which I discussed and implemented according to the code review.</p>
    <h1 id="the-plot-twist">The Plot Twist
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#the-plot-twist">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h1><p>For a few days, I remained under the impression that I had mostly rewritten the Scraper in a way that it works and only have to wait for suggestions from the code review. Nabil, Alasdair and I discussed that in the meanwhile I could look into which functions I can remove and move out of the Scraper. However, a plot twist unlike any other was still awaiting me and the realisation came when Nabil asked me if I had run the remote-tests yet. I had been running the <code>test-scraper.py</code> tests so far, even the remote ones so my response was a vehement yes. When he mentioned that some were still failing, I remembered I was still to fix the examples in the documentation and once I had fixed the doctests it&rsquo;d be passing. However at this point I was beginning to see the <em>real</em> issue, so far I had only been fixing the tests limited to the scraper and NOT the rest of the codebase.</p>
    <h1 id="a-whole-new-world">A Whole New World
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#a-whole-new-world">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h1><p>I ran the tests to be greeted with very polite <code>105 failing tests</code>. I informed this to my mentors and have begun working on fixing all the parts of the codebases which indirectly depend on this class. So far I&rsquo;ve been encountering functions that may / may not have possibly gone redundant and am now exploring and considering which reducing functions, or removing them while fixing tests.</p>
    <h1 id="next-steps">Next Steps
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#next-steps">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h1><p>I&rsquo;ll keep on working on these new tests, while analysing both the scraper and related parts of the codebase outside for functions to rewrite, remove and/or move at the same time.
    I also realised we&rsquo;ll be needing new documentation about how to write the new parse-style patterns.</p>
    <p>That is all so far, until next time!</p>

