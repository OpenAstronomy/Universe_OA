.. title: Moving towards the right approach
.. slug:
.. date: 2025-07-03 11:15:00 
.. tags: stingray
.. author: Mohammad Adnan
.. link: https://sejifukishima.blogspot.com/2025/07/moving-towards-right-approach.html
.. description:
.. category: gsoc2025


.. raw:: html

    <h3><br /></h3><p></p>
    <p>&nbsp;The last few weeks have been a whirlwind of ideas, coding, and rethinking as we figured out the best way to build my dashboard project.</p>
    <p><b>Our First Idea:</b></p>
    <!-- TEASER_END -->
    <p>My initial plan seemed pretty logical. I was going to download all the raw data (the "event files"), process them into lightweight <code>h5&nbsp;</code>files full of handy PNGs, and stick them all in an S3 bucket. The dashboard would just grab these pre-made files.</p>
    <p>It was a neat and tidy plan, but the more we thought about it, a static, deployed app . We decided to make something that a user could clone and run right on their own local machine.</p>
    <p><b>The Next Step:&nbsp;</b></p>
    <p>So, that's what we did. The new idea was to build a dashboard that anyone could just grab from a repository and run on their own computer. No big deployment , In this version, the user would download the source data they were interested in, and my dashboard would help them create the plots and data products right there on their machine.</p>
    <p>But that created a whole new problem: asking people to download gigabytes of data and clog up their own hard drives. That didn't feel very user-friendly, and it was a major headache waiting to happen.</p>
    <p><b>The "Aha!" Moment: Why Not Go Where the Data Already Lives?</b></p>
    <p>This is when we had the real breakthrough. It was a total game-changer. Instead of moving massive datasets around, we realized we could just move our little dashboard <i>to the data</i>.</p>
    <p>By running everything on SciServer, where all the telescope data already lives, the user doesn't have to download a single thing. Suddenly, the headache of huge downloads and local storage just... vanished. All the complex processing happens on SciServer's temporary "scratch" storage. It's faster, way more efficient, and saves everyone a lot of trouble. The only time we spend now is on the actual science—the calibration and corrections.</p>
    <p><b>So, Where Are We Now?</b></p>
    <p>I'm really happy to say that I have a working version of the dashboard running with this new, much smarter approach! All the major functions are in place.</p>
    <p>To be honest, the user interface is still a bit basic—it looks like an engineer built it (which, well, I did). So my next big task is to clean it up and make it look more polished.</p>
    <p>To give you a little peek, here’s what the initial draft looks like:</p>
    <div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgqRuuwud2lD3OPYDA98yZsgfyxEnaEpJ-NATxEF1f1RcSVfJmDslHtcuF5wXuGK20adNNEtYe2e8pbikYPuBHEUY2auZen722r_s-ipQhFxuunj9_Eet7K21aPqAeKbblKpK0nRGcoMGwaN2eYfYvUqxTazTCCVgrn8EfkDy9lcsRMZ1YuEi1lam8pb08/s1906/Screenshot%202025-06-30%20100541.png" style="margin-left: 1em; margin-right: 1em; text-align: center;"><img border="0" height="237" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgqRuuwud2lD3OPYDA98yZsgfyxEnaEpJ-NATxEF1f1RcSVfJmDslHtcuF5wXuGK20adNNEtYe2e8pbikYPuBHEUY2auZen722r_s-ipQhFxuunj9_Eet7K21aPqAeKbblKpK0nRGcoMGwaN2eYfYvUqxTazTCCVgrn8EfkDy9lcsRMZ1YuEi1lam8pb08/w423-h237/Screenshot%202025-06-30%20100541.png" width="423" /></a></div><p></p>
    <p>As we get closer to the mid-term evaluations, my goals are coming into focus. First up, I'll be syncing with my mentors, @matteobachetti &amp; @Gullo, to make sure we're all on the same page with going all-in on SciServer. After that, I'm excited to start making the UI more dynamic and adding some cool new features.</p>
    <p><br /></p>
    <p></p>
    <br /><br /><p></p>

