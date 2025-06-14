.. title: 🌟 Things Are Getting Interesting!!
.. slug:
.. date: 2025-06-13 07:32:00 
.. tags: JuliaAstro
.. author: kashish shrivastav
.. link: https://kashish2210.blogspot.com/2025/06/things-are-getting-interesting.html
.. description:
.. category: gsoc2025


.. raw:: html

    <p>Hey everyone!</p>
    <p>If you’ve read my <a href="https://kashish2210.blogspot.com/2025/05/begining-of-gsoc2025.html" rel="noopener">first blog</a>, you already know how this journey started — with nervous excitement, inspiring mentors, and my deep love for astronomy. Since then, <strong>things have only gotten more interesting</strong> — and yes, more challenging, but in the best way possible!</p>
    <h2>Developing, Debugging, and Growing</h2>
    <!-- TEASER_END -->
    <p>These past few weeks have felt like a whirlwind of beauty. I’ve found myself diving deeper into spectral analysis, implementing windowing techniques, exploring real research articles, and most excitingly, contributing to the actual development of functions inside Stingray.jl!</p>
    <h2>A New Adventure: EventList and GTI Handling</h2>
    <p>Now comes the exciting part — I’ve been working on <strong>mission support</strong>,&nbsp;<a href="https://github.com/StingraySoftware/Stingray.jl/pull/49" rel="noopener" target="_new">PR #49</a>, where I got to play around with <code>EventList</code> structures.</p>
    <p>I made a minimal version&nbsp;&nbsp;<code>EventList</code> that could read test files, handle metadata smartly, and even filter events using GTIs (Good Time Intervals). My mentor @fergus and I created a&nbsp;&nbsp;<code>filter_time!&nbsp;</code>function that makes it super easy to slice time windows and work with just the needed data.</p>
    <p>It felt awesome to write something like this:</p>
    <pre class="overflow-visible!"><div class="contain-inline-size rounded-2xl border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none rounded-t-2xl">julia</div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-julia">filter_energy!(&lt;(10u"keV"), filter_time!(&gt;(min_time * u"s"), event_list))
    </code></div></div></pre>
    <p>Elegant, right?</p>
    <p>Also, a quick lesson: <strong>GTIs</strong> are just two columns — <code>START</code> and <code>STOP</code> — telling us when the telescope was actually collecting good data. Handling them properly means our analysis gets cleaner, smarter, and more accurate. I plan to extend my implementation soon to include full GTI support in <code>EventList</code> directly. Small step, big improvement!</p>
    <h2>Tests, Tests, and More Tests</h2>
    <p>One cool thing I picked up from looking at simpler implementations was <strong>writing smaller, more flexible test cases</strong>. I’ve started structuring my tests to be interactive and IDE-friendly — so I can quickly check and fix stuff without wrapping everything in big test blocks. It makes debugging <em>way</em> less stressful. suggested by @fergus</p>
    <h2>What's Next?</h2>
    <p>Right now, I’m:</p>
    <ul>
    <li>
    <p>Tweaking the <code>recipbase</code> functions to make them more modular.</p>
    </li>
    <li>
    <p>Exploring how to use metadata more flexibly in different missions.</p>
    </li>
    <li>
    <p>Working on improving event filtering and data handling inside <code>EventList</code>.</p>
    </li>
    <li>
    <p>Thinking about ways to contribute test utilities that let us simulate dummy FITS files and test logic <em>without</em> needing real data every time.</p>
    </li>
    </ul>
    <h2>✨ Final Thoughts</h2>
    <p>Honestly, it still feels surreal to be working with real tools and contributing code that could one day help researchers uncover deeper insights about the universe. Every commit I make, every tiny improvement I push, and even the bugs I chase down — they’re all helping me grow. Not just as a coder, but as a thinker, a problem solver, and someone who genuinely enjoys the process of learning.</p><p>
    </p><p>What started as an exciting journey has now become something even more thrilling — it feels like I’m leveling up with each challenge I face (yes, just like in my favorite anime, <em>Solo Leveling</em> 😄). And the best part? This is only the beginning.</p>

