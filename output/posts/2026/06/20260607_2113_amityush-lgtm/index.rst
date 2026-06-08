.. title: GSoC 2026 - Weeks 1 & 2: Understanding Before Implementing
.. slug:
.. date: 2026-06-07 21:13:15 
.. tags: SunPy
.. author: Kumar Amityush
.. link: https://sunpy-radiospectra.blogspot.com/2026/06/gsoc-2026-weeks-1-2-understanding.html
.. description:
.. category: gsoc2026


.. raw:: html

    <h2 style="text-align: left;">The Journey Begins 💪</h2><p>The first two weeks of the coding period have been a mixture of excitement, confusion, debugging, learning and the occasional moment of staring at a terminal wondering why something that worked five minutes ago suddenly doesn't.</p>
    <p>As someone once said:</p>
    <p><em>"The expert in anything was once a beginner who refused to give up."</em></p>
    <!-- TEASER_END -->
    <p>That quote has felt surprisingly relevant over the past couple of weeks.</p>
    <h2>Building the Foundation with NDCube 💻</h2><p>A major part of my work focused on integrating radiospectra with NDCube. This involved migrating the core <b><i>GenericSpectrogram</i></b>&nbsp;class, understanding how coordinate-aware data is represented and diving deeper into World Coordinate Systems (WCS) than I ever expected.</p>
    <p>At first glance it sounded simple: "just integrate NDCube."</p>
    <p>It was not.</p>
    <p>Along the way, I had to understand how time and frequency coordinates interact, how plotting components work and spend a fair amount of time convincing Git that my branches and commits were actually where they were supposed to be. I also spent a lot of time exploring how plotting should work in an NDCube-backed architecture and understanding how radiospectra's existing functionality can be adapted to the new design.</p>
    <p>The good news? The migration is moving forward and has already helped me understand the architecture of radiospectra much better.</p>
    <h2>Testing with Real Data 🤔</h2><p>One thing I've quickly learned is that real-world data likes to surprise you.</p>
    <p>I worked on expanding online integration tests for several instruments and data sources including <i><b>PSP</b></i>, <i><b>RSTN</b></i>, <i><b>e-Callisto</b></i> and <b><i>ILOFAR</i></b>. These tests fetch actual data from remote observatories and help ensure that radiospectra continues to work reliably beyond local test files.</p>
    <p>Naturally, this also meant discovering metadata, parsing issues and a few "why is this file formatted like this?" moments. There were several occasions where a test would fail only after downloading real data, leading me down an unexpected debugging rabbit hole.</p>
    <p>Fortunately, most of those mysteries have now been solved and the testing infrastructure is in a much better place than it was when I started.</p>
    <h2>Making Documentation More Interactive 😃</h2><p>Good documentation can save hours of confusion, so another task was introducing a Sphinx example gallery similar to the one used in SunPy.</p>
    <p>I added the gallery infrastructure and wrote the first end-to-end example demonstrating how users can search, download and plot <b><i>WIND/WAVES</i></b> data using <code><span style="font-family: inherit;"><b><i>sunpy.net.Fido</i></b></span></code> and <b><i>radiospectra</i></b>.</p>
    <p>Seeing the example render successfully for the first time was one of those small but satisfying wins that make debugging worth it. The process also involved several rounds of feedback and refinement, helping me better understand how to build documentation that is both useful and easy to follow.</p>
    <h2>Looking Ahead 🚀</h2><p class="isSelectedEnd">The first two weeks have taught me that open-source development is about much more than just writing code.</p>
    <p class="isSelectedEnd">Some of the most valuable progress happens before a single line of code is written while understanding the architecture, exploring unfamiliar datasets, discussing ideas with mentors, reviewing feedback and figuring out how different pieces of a project fit together.</p>
    <p>Looking back, I spent as much time learning and understanding as I did coding. And honestly, that's what has made this experience so rewarding so far.</p>
    <p>There were plenty of moments where a five-minute change turned into an hour-long debugging session and a few moments where Git seemed determined to test my patience. But every challenge taught me something new about the codebase and the broader scientific Python ecosystem.</p>
    <p>I'm grateful to my mentors and the community for their guidance so far and I'm excited to continue pushing the project forward in the weeks ahead.</p>
    <p><em>"Success is the sum of small efforts, repeated day in and day out."</em>&nbsp; ~ Robert Collier</p>
    <p>On to the next challenge 🚀</p>

