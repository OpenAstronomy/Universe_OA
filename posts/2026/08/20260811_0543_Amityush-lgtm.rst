.. title: Weeks 9 & 10: Slicing, Profiles and a New Factory
.. slug:
.. date: 2026-08-11 05:43:29 
.. tags: SunPy
.. author: Kumar Amityush
.. link: https://sunpy-radiospectra.blogspot.com/2026/08/weeks-9-10-slicing-profiles-and-new.html
.. description:
.. category: gsoc2026


.. raw:: html

    <h2 style="text-align: left;">&nbsp;Slicing, Profiles and a New Factory 🚀</h2>
    <p class="">The last two weeks have been a pretty interesting mix of working on spectrogram slicing and starting to look at one of the bigger architectural changes in <code><b>radiospectra</b></code>.</p>
    <p>A lot of the work this time was about understanding how the different pieces fit together and figuring out how to make things easier for users and contributors.</p>
    <!-- TEASER_END -->
    <h2>Exploring Slicing and Profiles 🔍</h2>
    <p>After the <code><b>ndcube</b></code> refactor, I started looking more closely at how users could work with individual parts of a spectrogram.</p>
    <p>One thing I wanted to make easier was getting a <strong>time profile at a particular frequency</strong> or a <strong>frequency profile at a particular time</strong>.</p>
    <p>Initially, I worked on adding <code><b><i>time_profile()</i></b></code> and <code><b><i>line_profile()</i></b></code> methods to <code><b>GenericSpectrogram</b></code>.</p>
    <p>To make this work, I had to deal with something I hadn't worked with much before—converting physical coordinates into the actual array indices behind the spectrogram.</p>
    <p>I added a couple of internal helpers to handle this conversion, so users could provide things like an <code><b>astropy.time.Time</b></code> or a frequency with units without having to figure out the corresponding array index themselves.</p>
    <p>I also added tests to make sure these conversions work correctly across different cases.</p>
    <p>This was a nice learning experience for me because it made me look much more closely at how the WCS and the actual data array are connected.</p>
    <hr />
    <h2>Starting the SpectrogramFactory Migration 🔧</h2>
    <p>The other major thing I've been working on is the <code><b>SpectrogramFactory</b></code> migration.</p>
    <p>This is definitely one of the bigger changes I've worked on so far.</p>
    <p>The existing factory would basically parse the entire file first and create the data and metadata before checking which instrument the file belonged to.</p>
    <p>That means quite a lot of work could happen before we even knew which instrument was supposed to handle the file.</p>
    <p>The idea behind the new approach is to keep this much lighter.</p>
    <p>Instead of fully parsing the file first, the factory can get the basic information needed to identify the instrument. Once the correct instrument is found, that instrument can handle the actual parsing through a new <code><b><i>from_raw()</i></b></code> method.</p>
    <p>So the basic idea becomes:</p>
    <p><strong>Old:</strong></p>
    <p><code><i>Read everything → Identify instrument → Create spectrogram</i></code></p>
    <p><strong>New:</strong></p>
    <p><code><i>Read basic information → Identify instrument → Let the instrument parse the data</i></code></p>
    <p>I've started implementing this approach and have migrated the first two sources:</p>
    <ul>
    <li>
    <strong>WAVES</strong>
    </li>
    <li>
    <strong>e-CALLISTO</strong>
    </li>
    </ul>
    <p>There's still a lot to migrate, but getting these two working has given me a much better idea of how the rest of the factory can be moved over.</p>
    <hr />
    <h2>What's Next? 👀</h2>
    <p>For the next couple of weeks, I'll be working through the feedback on the slicing and profiling work and continuing the <code><b>SpectrogramFactory</b></code> migration.</p>
    <p>There are still several instruments to move to the new <code>from_raw()</code> pattern, so I'm looking forward to seeing how the factory looks once the migration is complete.</p>
    <p>It's been really interesting moving from smaller API improvements to working on the bigger architecture of <code><b>radiospectra</b></code>, and I'm excited to keep going!</p>
    <p>Until next time! 🚀</p>

