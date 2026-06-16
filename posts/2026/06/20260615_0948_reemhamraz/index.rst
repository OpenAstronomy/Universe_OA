.. title: Biting Into It: My Astropy Summer (Weeks 1-3)
.. slug:
.. date: 2026-06-15 09:48:44 
.. tags: Astropy
.. author: Reem Hamraz
.. link: https://dev.to/reemhamraz/biting-into-it-my-astropy-summer-weeks-1-3-5g2l
.. description:
.. category: gsoc2026


.. raw:: html

    <blockquote>
    <p>"I really want to be something in life. I don't want to be forgotten."</p>
    </blockquote>
    <!-- TEASER_END -->
    
    <p>It's a heavy thought for a Tuesday night, but it's been bouncing around my head a lot lately. I read this Sartre quote recently about living a "toothless life", just waiting around, reserving yourself for later, and then suddenly realizing your teeth are gone. I decided a while ago that I'm not doing that. If I'm going to leave something behind, it has to be through work that actually matters.</p>
    
    <p>Right now, that work looks like deliberately bypassing high-level Python APIs to aggressively test raw, compiled C-engines for Astropy.</p>
    
    
    
    
    <h2>
    
    
    The Weekly Grind
    </h2>
    
    <p>Juggling CS coursework while trying to wrangle Cython for Google Summer of Code is a lot. But honestly? I've been loving every damn second of it. Reading documentation in a vacuum is one thing, actually hashing out C-level memory bindings is where the reality sets in. My mentors don't just let me write code; they force me to hold my work to strict architectural standards, which honestly gives me an immense sense of accomplishment once I clear them.</p>
    
    
    
    
    <h2>
    
    
    <code>test_np_utils.py</code>: First Blood
    </h2>
    
    <p>Getting this merged was my first real bite into the codebase. Instead of playing it safe with high-level Astropy <code>Table</code> objects, I stripped away the Python wrapper to test the raw C-engine underneath. I threw every Cartesian edge case at the <code>join_inner</code> function just to see if the explosive $O(N^2)$ memory allocations would break it.</p>
    
    <p>They didn't.</p>
    
    
    
    
    <h2>
    
    
    <code>test_column_mixins.py</code>: The Beast
    </h2>
    
    <p>Absolute beast of a PR. I had to write <code>MinimalColumn</code> shims and cast them directly onto raw NumPy arrays just to isolate the Cython <code>__getitem__</code> routing. Somewhere in there I found a legitimate C-level trapdoor — indexing a structured array with a single string was silently dropping the dtype entirely. That became Issue #19827, which I later learned was actually expected behavior, so I closed it. End of story.</p>
    
    <p>But the real boss fight wasn't even the code (funny, right?!). It was Git. I ran a terrifying interactive rebase in Nano to squash six messy commits before force-pushing to my branch. Truly character-building.</p>
    
    <p>If it isn't clear by now, let me spell it out:</p>
    
    <blockquote>
    <p>"I absolutely despise GitHub squash and rebase. Actually, I don't think we (me and GitHub) can ever be on amicable terms."</p>
    </blockquote>
    
    
    
    
    <h2>
    
    
    APE Split &amp; <code>_parse_times.c</code>: Standing on Shoulders
    </h2>
    
    <p>Lately I've been laying the tracks for the APE split, writing isolated tests for the <code>_parse_times.c</code> extension. This was mostly building on another contributor's accepted PR, but it was enlightening to understand how other brains work. I'll be honest, I spent a good chunk of time just deciphering the existing test cases before touching anything, making sure I didn't alter their original essence.</p>
    
    
    
    
    <p>That's weeks 1–3, folks.</p>
    
    <p>It's a blur of memory buffers, strict type checking, and fighting CI matrices. But when those green checkmarks come in, and especially when I see those purple merged PRs, I know I'm actually building something.</p>
    
    <p>I'm biting into it. I'm not waiting anymore.</p>

