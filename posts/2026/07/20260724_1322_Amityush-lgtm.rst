.. title: What Six Weeks of GSoC Have Taught Me
.. slug:
.. date: 2026-07-24 13:22:21 
.. tags: SunPy
.. author: Kumar Amityush
.. link: https://sunpy-radiospectra.blogspot.com/2026/07/what-six-weeks-of-gsoc-have-taught-me.html
.. description:
.. category: gsoc2026


.. raw:: html

    <div style="text-align: left;"><h2 style="text-align: left;">What Six Weeks of GSoC Have Taught Me 🚀</h2>
    <blockquote>
    <p><em>"I came into GSoC thinking I'd spend most of my time writing code. Six weeks later, I realized that's only a small part of the journey."</em></p>
    <!-- TEASER_END -->
    </blockquote>
    <p>A few days ago, I successfully passed my <strong>Google Summer of Code 2026 midterm evaluation</strong> 🎉 and it felt like the perfect time to look back on everything that's happened over the past six weeks.</p><p></p><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEgmhFPrMLPIt4ESIcx25xyy8XQSvGc4PznXnOuS8gha_rHGhQAurpmnWKRVWQOU2h9TrVZfc6YpDtSH0nfFHK8hnViKWJuBmoYQda5F3CQZ2EoM_UkXadCfSW46bR0wJoJBgBaBm3cpIv5yAVetVpCK1HDdVWhRs7ODGSIj1rgbRGvldQxbQsSIS8l-YUM" style="margin-left: 1em; margin-right: 1em;"><img alt="" height="193" src="https://blogger.googleusercontent.com/img/a/AVvXsEgmhFPrMLPIt4ESIcx25xyy8XQSvGc4PznXnOuS8gha_rHGhQAurpmnWKRVWQOU2h9TrVZfc6YpDtSH0nfFHK8hnViKWJuBmoYQda5F3CQZ2EoM_UkXadCfSW46bR0wJoJBgBaBm3cpIv5yAVetVpCK1HDdVWhRs7ODGSIj1rgbRGvldQxbQsSIS8l-YUM" width="320" /></a></div><div class="separator" style="clear: both; text-align: center;"><br /></div><p></p>
    <p>I've been working with the <strong>SunPy</strong> community on <strong>radiospectra</strong>&nbsp;and honestly, this experience has been very different from what I expected.</p>
    <p>Sure, I've written code, opened pull requests and fixed bugs - but that's only part of the story.</p>
    <p>The bigger lesson has been learning <strong>how</strong> an open-source project is built and how people from different parts of the world collaborate to make it better.</p>
    <p>So instead of another weekly update, I thought I'd share a few things this journey has taught me so far.</p>
    <hr />
    <h2 style="text-align: left;">Learning a Large Codebase Takes Time ⌚</h2>
    <p>When I opened the repository for the first time, it was... a lot.</p>
    <p>There were spectrograms, WCS, NDCube, plotting code, metadata classes, different instrument readers, tests and somehow everything depended on everything else.</p>
    <p>My first reaction was honestly,</p>
    <blockquote>
    <p><em>"Where do I even begin?"</em>&nbsp; 😅</p>
    </blockquote>
    <p>At first, I felt like I wasn't making much progress because I was spending more time reading code than writing it.</p>
    <p>I'd follow a single function into another file, then another and before I knew it, I had ten tabs open trying to understand how everything fit together.</p>
    <p>Looking back, that was probably the most important part of the journey.</p>
    <p>Once I understood <em>why</em> the code was written a certain way, making changes became much easier.</p>
    <p><strong>One thing I've learned is that understanding a project isn't time wasted - it's time invested.</strong></p>
    <hr />
    <h2 style="text-align: left;">Every Code Review Is a Learning Opportunity 💬</h2>
    <p>Before GSoC, I used to think code reviews were mainly about pointing out mistakes.</p>
    <p>Now I see them very differently.</p>
    <p>Some of my pull requests worked exactly as intended, but my mentors would still suggest changes - not because the code was wrong, but because there was a cleaner API, a simpler implementation, or a design that would be easier to maintain in the future.</p>
    <p>Those conversations completely changed how I think while writing code.</p>
    <p>Instead of asking myself,</p>
    <blockquote>
    <p><em>"Does this work?"</em></p>
    </blockquote>
    <p>I now find myself asking,</p>
    <ul>
    <li>
    Is this easy to understand?
    </li>
    <li>
    Does it fit naturally with the rest of the project?
    </li>
    <li>
    Will this still make sense a year from now?
    </li>
    <li>
    Can someone else build on top of this easily?
    </li>
    </ul>
    <p>Those are questions I rarely thought about before GSoC.</p>
    <hr />
    <h2 style="text-align: left;">Small Improvements Matter 😊</h2>
    <p>One thing I really appreciate about open source now is that every contribution doesn't have to be a huge feature.</p>
    <p>Sometimes, making something a little easier for users is enough.</p>
    <p>One of my recent pull requests focused on making spectrogram cropping more intuitive.</p><p class="PDq2pG_selectionAnchorContainer">I worked on making spectrogram cropping easier for users.<span class="PDq2pG_selectionAnchor"></span></p><p>Previously, users had to interact directly with the underlying NDCube&nbsp;API.</p><p>Now they can simply do this:</p><pre class="overflow-visible! px-0!"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16" dir="ltr" id="code-block-viewer"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><b><span class="ͼ11">spec</span><span class="ͼv">.</span>crop_time(<span class="ͼ11">start</span>, <span class="ͼ11">end</span>)</b></code></pre></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre><p>instead of</p><p>
    
    
    
    
    </p><pre class="overflow-visible! px-0!"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16" dir="ltr" id="code-block-viewer"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><b><span class="ͼ11">spec</span><span class="ͼv">.</span>crop((<span class="ͼ11">start</span>, <span class="ͼy">None</span>), (<span class="ͼ11">end</span>, <span class="ͼy">None</span>))</b></code></pre></div></div></div></div></div></div></div></div></div></div></div></div></div></div></pre>
    <p>Instead of interacting directly with the underlying NDCube API, users can now use simpler convenience methods.</p>
    <p>It isn't a massive feature.</p>
    <p>It probably won't make headlines.</p>
    <p>But if it makes someone's life a little easier, I'd call that a success.</p>
    <p>That's something GSoC has taught me - small improvements add up.</p>
    <hr />
    <h2 style="text-align: left;">Communication Is Part of Engineering 🤝</h2>
    <p>This was probably the most unexpected lesson.</p>
    <p>Writing code is only one part of contributing.</p>
    <p>The other part is explaining your ideas, asking questions, discussing different approaches and responding to reviews.</p>
    <p>At first, I was hesitant to ask questions because I thought I should already know the answers.</p>
    <p>Thankfully, my mentors were incredibly patient and always encouraged discussion.</p>
    <p>Over time, I realized that asking questions doesn't make you look inexperienced.</p>
    <p>If anything, it shows that you're trying to understand the problem before jumping to a solution.</p>
    <p>And more often than not, those conversations led to better ideas than I would have come up with on my own.</p>
    <hr />
    <h2 style="text-align: left;">Progress Isn't Always Visible 🧠</h2>
    <p>There were weeks when I didn't have a shiny new merged pull request to show.</p>
    <p>Earlier, that would've made me feel like I wasn't doing enough.</p>
    <p>But during those same weeks, I was reading architecture, understanding how different components worked together, experimenting with ideas and having discussions with my mentors.</p>
    <p>Those weeks were just as valuable.</p>
    <p>Maybe even more.</p>
    <p>One thing I've learned is that progress isn't always measured by commits or merged PRs.</p>
    <p>Sometimes progress is simply understanding something that confused you yesterday.</p>
    <hr />
    <h2 style="text-align: left;">Looking Back 📈</h2>
    <p>If someone had asked me six weeks ago what I'd learn during GSoC, I would've probably answered,</p>
    <blockquote>
    <p>"Python."</p>
    </blockquote>
    <p>Now my answer would be very different.</p>
    <p>I've learned how to approach a large codebase.</p>
    <p>I've learned how valuable thoughtful code reviews are.</p>
    <p>I've become more comfortable asking questions and discussing design decisions.</p>
    <p>Most importantly, I've learned that great software isn't built by one person writing perfect code.</p>
    <p>It's built by people sharing ideas, reviewing each other's work and learning together.</p>
    <hr />
    <h2 style="text-align: left;">What's Next? 🚀</h2>
    <p>Passing the midterm evaluation feels less like reaching the finish line and more like reaching the halfway point.</p>
    <p>There's still a lot I want to learn and I'm excited about the work ahead.</p>
    <p>Over the next few weeks, I'll be diving deeper into the architecture of <b>radiospectra</b>, working on larger improvements and hopefully contributing even more to the project.</p>
    <p>I'm looking forward to sharing that journey in my next blog.</p>
    <hr />
    <h2 style="text-align: left;">Thank You ❤️</h2>
    <p>Before wrapping up, I'd like to thank my mentors, <strong><a href="https://github.com/samaloney" target="_blank">Shane Maloney</a></strong> and <strong><a href="https://github.com/hayesla" target="_blank">Laura Hayes</a></strong>, for all their guidance, thoughtful feedback and encouragement throughout these six weeks.</p>
    <p>Every review comment, every discussion and every suggestion has helped me grow, not just as an open-source contributor, but as a developer.</p>
    <p>I'm excited to see what the second half of GSoC has in store.</p>
    <p>See you in the next blog!</p></div>

