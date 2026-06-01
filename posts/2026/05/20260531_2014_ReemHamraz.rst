.. title: Beyond the Abstraction
.. slug:
.. date: 2026-05-31 20:14:31 
.. tags: Astropy
.. author: Reem Hamraz
.. link: https://dev.to/reemhamraz/beyond-the-abstraction-17na
.. description:
.. category: gsoc2026


.. raw:: html

    <p>The glow of the screen hits different when you're reading an email that dictates your entire summer. Getting accepted into Google Summer of Code 2026 programme for Astropy, under the OpenAstronomy umbrella, was one of those really defining moments; all I could do was stare at the screen in disbelief (I'd done it). Then, the abstraction fades away, and suddenly, you need to get down to the real work.</p>
    
    <p>This post, is the first of many. I plan to keep these updates transparent and real—documenting, so it's really not just going to be about the code that ships, but rather the (not-so)basic commands I need to google, or the dumb mistakes, or the long hours spent scouring the internet for things that developers ought to know (but I don't), and the brutal reality of open-source development or at least the reality from the perspective of a first-timer (that would be me needing to google how to squash and rebase, haha fun times:| or not)</p>
    <!-- TEASER_END -->
    
    <h3>
    
    
    Let's break down my project
    </h3>
    
    <p>This summer, my life will revolve around Astropy's low-level test suite, or more formally speaking:</p>
    
    <blockquote>
    <p>"Hardening Astropy's Core Stability" </p>
    </blockquote>
    
    <p>I am skipping the wrappers and going straight for the raw C-extensions. Which, when you think about it, there is a kind of profound honesty in testing the core engine. It forces transparency. It demands technical accountability (excuse my philosophical analysis). What I meant to say is that no one can fake it you know? By the end of the day you really gotta understand what you're doing because otherwise you'll be lost as hell. So yeah, this is what I plan to do all summer and I can't wait for it! So totafreakingly excited!!</p>
    
    <h3>
    
    
    Speaking of being lost
    </h3>
    
    <p>My greatest advice to anyone starting would be to find your mentors, and I will swear upon this, that you really need to find your perfect organization and your perfect mentors! I wouldn't have even started down this path if it weren't for @neutrinoceros. It was a fateful email, and one that led to many many more and here I am. So, I'd really like to give a huge shoutout to my mentors for this project, @nstarman and @neutrinoceros. Open-source can be so intimidating, but having mentors who are just straight up transparent and value direct communication makes it all so much more manageable, and I'm pretty grateful that I have that experience. </p>
    
    <p>And moreover, I am not starting from absolute zero either. We actually got some real momentum going recently. I finally got PR #19458 merged! The one adding direct tests for join_inner in table/_np_utils Cython extension. IT GOT MERGED. Though, ideally this would've been my first PR right after the community bonding period, I tackled it before-hand and well it paid off (proof that I can actually write code that works, phew). </p>
    
    <p>A lil side note: I'm writing this post after the community bonding period but I'm starting from the very start so bear with me please. The next post will deep dive into my the coding details of my first and second set of test cases, mentor meetings, Astropy's dev telecon and all the wonderful stuff.</p>
    
    <h3>
    
    
    The next 2 weeks
    </h3>
    
    <p>Now that the official coding phase is here, my life for the next fortnight is basically going to be staring at architecture maps. I need get going with the test coverage for these Cython extensions. Plus, I really have to optimize my local setup so my laptop doesn't literally take off into orbit while running these low-level builds. Although @neutrinoceros did have a meeting with me, to help set me with the local setup, GitHub CLI and UV tools, plus a bunch of cool commands that have literally helped me a tonne.</p>
    
    <p>I know, that it is going to be a grind, but like, a really good grind. I'll be back here in, whenever I feel like it, (though most probably within the next 2 weeks) to let you all in on more cool things I learnt over the course of these weeks. Check back then for more raw updates and probably more stories of me overcomplicating basic git commands. </p>
    
    <p>Toodles!</p>

