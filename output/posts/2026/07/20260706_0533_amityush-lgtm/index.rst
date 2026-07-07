.. title: Week 5 & 6 - The Work You Don't See 👀
.. slug:
.. date: 2026-07-06 05:33:30 
.. tags: SunPy
.. author: Kumar Amityush
.. link: https://sunpy-radiospectra.blogspot.com/2026/07/week-5-6-work-you-dont-see.html
.. description:
.. category: gsoc2026


.. raw:: html

    <h2 style="text-align: left;">🔍 Behind the Scenes</h2>
    <blockquote>
    <p><em>Users probably won't notice most of the work from these past two weeks... and that's completely okay.</em></p>
    <!-- TEASER_END -->
    </blockquote>
    <p>When people think about open source, it's easy to imagine exciting new features, shiny visual changes, or new capabilities.</p>
    <p>This wasn't one of those weeks.</p>
    <p>Instead, I spent the last two weeks working on something that's much less visible but just as important - making <strong>radiospectra</strong> easier to maintain, easier to extend and hopefully a little easier for future contributors to understand.</p>
    <hr />
    <h2>🏗️ Building a Better Metadata System</h2>
    <p>The biggest piece of work was redesigning how metadata is handled across the package.</p>
    <p>Instead of relying on plain dictionaries everywhere, I introduced a proper metadata architecture using <code><b>SpectrogramMetaABC</b></code> and <code><b>SpectrogramMeta</b></code>, backed by NDCube's <code><b>NDMeta</b></code>.</p>
    <p>Once the foundation was in place, I gradually added dedicated metadata classes for each supported instrument, moving instrument-specific logic out of the spectrogram classes into their own homes.</p>
    <p>This ended up covering instruments like <b>CALLISTO</b>, <b>WAVES</b>,<b> EOVSA</b>, <b>PSP RFS</b>, <b>Solar Orbiter RPW</b>, <b>SWAVES</b>, <b>RSTN</b> and<b> ILOFAR</b>.</p>
    <div class="separator" style="clear: both; text-align: center;"><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjAAQvfq_O4czxw5qWZKeWOqJmUCfltHk24S-Q7frE8nd_kfpYrMMsw37e6LlS1Hq_stsB9UdmxGVZ2cQOAEveiZj5izeZwzPjcUxP5ySA1IX-qAm84hFBoN8M77b8Zu8y9xESVkqMUJ7pFcqWY3WUtHLcc2zUoCODAstEEwCc2gNnx7zx9Yk3cYkz9Bjs/s4730/class_heirarchy_diagram.png" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="640" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjAAQvfq_O4czxw5qWZKeWOqJmUCfltHk24S-Q7frE8nd_kfpYrMMsw37e6LlS1Hq_stsB9UdmxGVZ2cQOAEveiZj5izeZwzPjcUxP5ySA1IX-qAm84hFBoN8M77b8Zu8y9xESVkqMUJ7pFcqWY3WUtHLcc2zUoCODAstEEwCc2gNnx7zx9Yk3cYkz9Bjs/w446-h640/class_heirarchy_diagram.png" width="446" /></a></div><br /></div><p></p>
    <hr />
    <h2>💬 The Best Part? Code Reviews&nbsp;</h2>
    <p>One thing I've started appreciating more during GSoC is how much learning happens <strong>after</strong> opening a pull request.</p>
    <p>Several rounds of review helped improve the implementation through better type hints, cleaner property definitions, improved documentation and a simpler overall API.</p>
    <p>Every review felt less like someone pointing out mistakes and more like someone helping shape a better design.</p>
    <p>That has honestly been one of my favourite parts of this project.</p><ul>
    </ul>
    <hr />
    <h2>🔧 The Unexpected Detour</h2>
    <p>No GSoC week is complete without a surprise.</p>
    <p>While working on the project, I noticed that the Read the Docs builds were failing. After a bit of digging, I traced the issue back to the deprecation of <code>mambaforge</code>.</p>
    <p>That small investigation ended up leading to fixes not only for <strong>radiospectra</strong>, but also for the upstream <strong>SunPy package template</strong>, helping future projects using the template as well.</p>
    <p>Definitely not something I expected to be working on... but that's part of the fun of open source.</p><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhn1EA6TiDq1xP2k0PtYhycX5EamSONe7QGmdFQaQ9xKKGL8GwCiCfrVYpRVs1V5x8ktL7WhUsWJ9Gcucm_AvSGU0x38jIF4wJNXgg9AoWT7Rk3rPCtpOg0cVWfmUeHEe-3u-pW7pTgkg1I975lN6a4wT_aqZlwfhydNuugnKUTYSPr1ZOadq1cgDWSSnA/s498/investigate.gif" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="211" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhn1EA6TiDq1xP2k0PtYhycX5EamSONe7QGmdFQaQ9xKKGL8GwCiCfrVYpRVs1V5x8ktL7WhUsWJ9Gcucm_AvSGU0x38jIF4wJNXgg9AoWT7Rk3rPCtpOg0cVWfmUeHEe-3u-pW7pTgkg1I975lN6a4wT_aqZlwfhydNuugnKUTYSPr1ZOadq1cgDWSSnA/s320/investigate.gif" width="320" /></a></div><div class="separator" style="clear: both; text-align: center;"><br /></div>
    <hr />
    <h2>🌱 A Small Reflection</h2>
    <p>These past two weeks reminded me that some of the most valuable contributions aren't the ones users immediately notice.</p>
    <p>Sometimes progress looks like cleaner architecture.</p>
    <p>Sometimes it looks like better tests.</p>
    <p>Sometimes it's fixing CI.</p><p>Sometimes it's learning from your mistakes.</p>
    <p>Sometimes it's simply making the next contributor's job a little easier.</p>
    <p>And honestly, I think that's one of the things I'm enjoying most about GSoC.</p>
    <hr />
    <p>Looking forward to the next chapter! 🚀</p>

