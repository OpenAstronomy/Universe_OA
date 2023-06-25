.. title: Into the Summer of Code
.. slug:
.. date: 2023-06-24 01:33:30 
.. tags: SunPy
.. author: exitflynn
.. link: https://exitflynn.github.io/blog/posts/gsoc-began/
.. description:
.. category: gsoc2023


.. raw:: html

    <p>I had my end-semester exams during the Community Bonding Period and the real-early part of the Coding Period. However, my mentors were super-accomodating.
    I spent a few days on plans with friends before bidding goodbye for the summers, travelling home and relaxing a bit.</p>
    <h2 id="the-talk">The Talk
    <!-- TEASER_END -->
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#the-talk">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h2><p>This was also the time when IIT BHU reached out to me for a talk as part of a collab between their Astronomy and Open-Source clubs about Astronomy in tech and OSS. This was a  g r e a t  experience! I&rsquo;ve always wanted to improve at public-speaking stuff and to finally pull off a satisfactory talk was a great experience. Also Prayash was a great host.</p>
    <h2 id="beginning-with-the-project">Beginning with the Project
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#beginning-with-the-project">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h2><p>My mentor, Nabil, had asked me to start by writing tests for the scraper, even if they may not return a -ve)for all the URLs it doesn&rsquo;t support now.
    Looking closely though, all the issues were due to limitations of the way regex is implemented for inputting URLs, i.e. since one of the main goals of the project was to remove regex and use parse instead, these tests would have proven to be quite redundant. I asked my mentors and understandably so, Nabil said that he doesn&rsquo;t want me working on code that I might have to remove soon enough and said I can proceed to the rest of the rewrite.</p>
    <p>After that, I began reading up on what Metaclasses, Abstract Base Classes (ABCs), etc are, their advantages and how they can be implemented in python to decide which would be better for the purpose of the project. However, at this point I wasn&rsquo;t really maintaining good communication with my mentors. When they asked me for any updates and then inquired about why I had been reading up on ABCs and such, they clarified that I should be able to improve the scraper without going that route.</p>
    <p>Had to take a couple of days off in between for unavoidable reasons.</p>
    <p>After that I took some calls with my mentors, clarifying details and trying to work things through together as I figured out what I should do next.
    All the scraper // dataretriever clients require two strings, <code>baseurl</code> and <code>pattern</code> and I figure out a way to merge them somehow.
    I looked into just what role the two of them had and found that <code>pattern</code> was used only to parse data.
    For example, When writing scraper clients, we require a baseurl and a pattern, an example from the NOAA Client:</p>
    <div class="highlight"><pre tabindex="0"><code class="language-python"><span style="display: flex;"><span>baseurl <span style="color: #f92672;">=</span> <span style="color: #e6db74;">r</span><span style="color: #e6db74;">'ftp://ftp.ngdc.noaa.gov/STP/swpc_products/daily_reports/solar_region_summaries/%Y/%m/%Y%m</span><span style="color: #e6db74;">%d</span><span style="color: #e6db74;">SRS.txt'</span>
    </span></span><span style="display: flex;"><span>pattern <span style="color: #f92672;">=</span> <span style="color: #e6db74;">'</span><span style="color: #e6db74;">{}</span><span style="color: #e6db74;">/</span><span style="color: #e6db74;">{year:4d}</span><span style="color: #e6db74;">/</span><span style="color: #e6db74;">{month:2d}</span><span style="color: #e6db74;">/</span><span style="color: #e6db74;">{year:4d}{month:2d}{day:2d}</span><span style="color: #e6db74;">SRS.txt'</span>
    </span></span></code></pre></div><p>Instead of passing both, we should be able to merge them into just one since the pattern string is conveying information that is already available in the baseurl.</p>
    <p>I figured it should be possible to transform <code>baseurl</code> to <code>pattern</code> and generate <code>pattern</code> that way but halfway through I realised that it&rsquo;d not be possible. However we should be able to convert a full <code>pattern</code> to it&rsquo;s <code>baseurl</code> formatted counterpart.</p>
    <p>I remember writing out loud what I thought as I approached that problem:</p>
    <h2 id="rubber-ducky-microblogging">rubber ducky microblogging?
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#rubber-ducky-microblogging">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h2><p>now how do we include this transformation in our code?
    we have mainly two places / files of concern.
    <code>dataretriever/client.py</code> and <code>scraper.py</code>
    at this point there are a couple of ways to go about it that come to my mind, all of them would however can be categorised as:
    a) include the transformation in dr/client.py
    b) include it in scraper.py</p>
    <p>before i get ahead of myself, it&rsquo;s better to arrive at a concrete decision here, if that&rsquo;s possible, to avoid having too much of overhead.</p>
    <p>case a:
    pattern transforms in client and is then sent to scraper. this means the scraper still operates on strftime baseurl.
    and when we want to call the parse function, instead of sending pattern as we do now, we can just send the original new format</p>
    <p>case b:
    pass the new format to scraper. scraper converts it into strftime to use in all of its functions, and</p>
    <p>the second approach makes more sense, yeah.</p>
    <p>NOW
    what&rsquo;d be a nice way to incorporate this transform in the scraper file?</p>
    <p>So there have to be Two strings/patterns, throughout this codebase.
    the strftime kind and the parse kind.
    what we input is the parse kind (since we can convert this to strftime, and the other way around wasn&rsquo;t possible)</p>
    <p>how to incorporate both strings? make them both private members of the Scraper class?</p>
    <p>some functions will be changed as a result of this</p>
    <p>like _URL_followsPattern</p>
    <p>okay so the plan of action is:
    go add a transform function, call it in init
    we&rsquo;ll have a variable for the time_pattern, update pattern -&gt; time_pattern wherever applicable.
    rewrite using parse wherever applicable</p>
    <p>but this would take away from having a standard system and we&rsquo;ll be defining our own set of names to name variables as.</p>
    <p>also a future plan can be to check for redundant functions / moving code.</p>
    <h2 id="in-conclusion">in conclusion
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#in-conclusion">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h2><p>So as of right now, I&rsquo;ve been working on <a href="https://github.com/sunpy/sunpy/issues/7073">#7073</a> and <a href="https://github.com/sunpy/sunpy/pull/7077">PR #7077</a>, more details on this issue and my proposed solution can be found in the issue description.</p>
    <p>This&rsquo;ll be all for now, will be posting more in the future.</p>

