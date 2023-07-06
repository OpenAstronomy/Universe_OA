.. title: Scraper Things
.. slug:
.. date: 2023-06-30 01:33:30 
.. tags: SunPy
.. author: exitflynn
.. link: https://exitflynn.github.io/blog/posts/gsoc-post-the-third/
.. description:
.. category: gsoc2023


.. raw:: html

    <p>Most of the week was spent rewriting the Scraper functions to go with the new parse-pattern and then looking for edge cases in the new implementations, fixing bugs and updating tests.</p>
    <h1 id="catching-up">{{Catching up}}
    <span>
    <!-- TEASER_END -->
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#catching-up">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h1><p>In the scraper, while trying to merge <code>baseurl</code> (an strftime formatted pattern i.e.<code> %Y%m</code> etc) and <code>pattern</code> (parse formatted pattern i.e. <code>{year:4d}{month:2d}</code> etc), I faced two choices, we could either:</p>
    <ul>
    <li>
    <p>Make the input all parse-style formatted. generate the datetime-compatible string from here wherever it is required, however the problem i was running into here is parse-stuff like <code>{year:2d}</code> will collide with <code>{instrument}</code> like placeholders on which we mean to call <code>.format(**kwargs)</code> on. All the ways I could think of pulling it off included adding a large no. of lines of code in the really early part of <code>__init__()</code>.</p>
    </li>
    <li>
    <p>Make the input all datetime formatted and generate the parse pattern from here. The problem with this is there are edge-cases when sometimes users define variables like <code>{Level:1d}</code> which we have no way of knowing beforehand. One way to go about this could&rsquo;ve been that we tell the user to define a pattern string in addition to baseurl whenever they have any new variables like that.</p>
    </li>
    </ul>
    <p>We ended up going with the first. My mentor, <a href="https://github.com/Nabobalis">Nabil</a> introduced me to how there&rsquo;s a prevalence of using double-curly brackets in places where we need to escape / use them with single curly brackets, and sure enough, the <code>parse</code> module supports that. So that took care of the problem there, I was mostly a bit concerned that I&rsquo;ll have to go back to the second way even though I had started with it before pivoting to the first one.</p>
    <h1 id="communication">Communication
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#communication">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h1><p>Nabil pointed out that we weren&rsquo;t being very good at communicating and that has a negative effect on the project which lead me to change how I was approaching it.</p>
    <p>A lot of times I was debugging things by including print statements here and there, and since my project now involves changing API it had me updating tests and a lot of these times the problem would just be in my understanding on how to convert the patterns and just how the new input should look like. Previously, I would only send a message on the matrix room when I had a question. And most of the times I&rsquo;d still hold out hope for solving something by myself when I have the strength to pick it up later. But it also makes sense because there&rsquo;d be no way to differentiate that from me not doing anything. Also around 75% of the time I&rsquo;ve drafted out questions, I found out an answer along the way. From now on I realise instead of just asking questions, I should think of it as a logging / progress-updating activity first which sounds obvious in hindsight.</p>
    <h1 id="to-regex-or-not-to-regex">To regex or not to regex
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#to-regex-or-not-to-regex">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h1><p>The next part where I was stuck at was in converting a pattern that involved custom placeholders like <code>{{CAR_ROT:4d}}</code> or <code>{{:3d}}</code> to their regex counterparts like  <code>(\d){3}</code>, <code>(\d){16}</code> etc without using like a l o t of regex, any less complex method than using a conversion function etc. However, after a quick conversation with the mentors and I realised that I had been mistakenly assuming that strftime required regex patterns. Earlier I thought that regex would no longer be part of the end-user experience but still somehow exist in the codebase but this is when I realised that we can entirely do away with it.</p>
    <h1 id="rewrite-then-remove-">Rewrite then Remove? 💀
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#rewrite-then-remove-">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h1><p>I also realised that the <code>_extractDateURL()</code> function was made redundant <em>after</em> rewriting it since I found out later that it was only called at one place and that part of the code was no longer required thanks to the existence of a parse-pattern. That&rsquo;s a nice message to keep in mind for the future.</p>
    <h1 id="modern-day-cain">Modern Day Cain
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#modern-day-cain">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h1><p>Another question I encountered was if we could assume that any {year:2d} or %y type 2-digit year xx to be interpreted to be in the 21st century like 20xx or not.</p>
    <h1 id="issue-found">Issue found
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#issue-found">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h1><p>I also found this bug in the codebase:
    In the current <code>scraper._check_timerange()</code>, it takes the simpler way <code>if</code> we provide it with an extractor // parse-pattern and a more complex way if we don&rsquo;t, however as it is implemented right now</p>
    <div class="highlight"><pre tabindex="0"><code class="language-python"><span style="display: flex;"><span><span style="color: #f92672;">from</span> sunpy.net.scraper <span style="color: #f92672;">import</span> Scraper
    </span></span><span style="display: flex;"><span><span style="color: #f92672;">from</span> sunpy.time <span style="color: #f92672;">import</span> TimeRange
    </span></span><span style="display: flex;"><span>s <span style="color: #f92672;">=</span> Scraper(<span style="color: #e6db74;">'%Y.fits'</span>)
    </span></span><span style="display: flex;"><span>s<span style="color: #f92672;">.</span>_check_timerange(<span style="color: #e6db74;">'2014.fits'</span>, TimeRange(<span style="color: #e6db74;">"2015-01-01"</span>, <span style="color: #e6db74;">"2015-01-02"</span>))
    </span></span></code></pre></div><p>would return True and it is intended that way in the tests but if we passed it an extractor // parse pattern</p>
    <div class="highlight"><pre tabindex="0"><code class="language-python"><span style="display: flex;"><span>s<span style="color: #f92672;">.</span>extractor <span style="color: #f92672;">=</span> <span style="color: #e6db74;">"</span><span style="color: #e6db74;">{year:4d}</span><span style="color: #e6db74;">.fits"</span>
    </span></span><span style="display: flex;"><span>s<span style="color: #f92672;">.</span>_check_timerange(<span style="color: #e6db74;">'2014.fits'</span>, TimeRange(<span style="color: #e6db74;">"2015-01-01"</span>, <span style="color: #e6db74;">"2015-01-02"</span>))
    </span></span></code></pre></div><p>it&rsquo;d return False.</p>
    <h1 id="inclusivity-is-important">Inclusivity is important
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#inclusivity-is-important">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h1><p>Failing tests required me to inqure if we want closed-intervals in the package or open, which concluded with closed. I also found other instances in the codebase where we endorse closed intervals.</p>
    <h1 id="future-steps">Future steps
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#future-steps">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h1><p>Cover why the rest of tests are breaking and fix em.
    Ask for review once everything works.
    Try to come up with a way to write parse-patterns so as the length remains less by trying to minimize repeated values.
    Also fix my Hugo setup before the night -_-</p>

