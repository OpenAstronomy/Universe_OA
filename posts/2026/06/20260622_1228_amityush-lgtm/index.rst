.. title: GSoC 2026 – Weeks 3 & 4: Looking Beyond the Code
.. slug:
.. date: 2026-06-22 12:28:09 
.. tags: SunPy
.. author: Kumar Amityush
.. link: https://sunpy-radiospectra.blogspot.com/2026/06/gsoc-2026-weeks-3-4-looking-beyond-code.html
.. description:
.. category: gsoc2026


.. raw:: html

    <h2 style="text-align: left;">Understanding the Infrastructure</h2><p>The past two weeks have been quite different from the start of the coding period.</p>
    <p>Instead of spending most of my time implementing new functionality, I found myself exploring a part of open source development that I had very little experience with before: testing infrastructure, CI workflows and release tooling.</p>
    <p>One thing I've learned so far is that writing code is only part of maintaining a project. Making sure that code continues to work months or years later is an equally important challenge.</p>
    <!-- TEASER_END -->
    <h2>Bringing Figure Tests to Radiospectra</h2><p>The main focus of the last two weeks was introducing the initial figure testing infrastructure to radiospectra.</p>
    <p>Before this, I had never worked with figure tests. My understanding of testing was mostly limited to checking outputs and functionality. Testing plots turned out to be a completely different world.</p>
    <p>To understand how it worked, I spent time exploring the figure testing workflow used across the SunPy ecosystem. This involved learning about baseline images, hash generation, automated image comparisons, and the CI infrastructure that keeps everything running.</p>
    <p>After a lot of reading, experimenting, and asking questions, I was able to get the initial setup working for radiospectra and add the first figure tests using real WIND/WAVES data. Although only WAVES is covered for now, it provides a foundation for expanding figure test coverage across other spectrogram sources in the future.</p>
    <h2>Learning the CI Side of Open Source</h2><p>One of the most interesting parts of this work was understanding how figure tests interact with CI systems.</p>
    <p>What initially sounded like "just add some tests" quickly became a deep dive into CircleCI workflows, baseline image repositories. 😓</p>
    <p>I spent quite a bit of time comparing radiospectra's setup with other SunPy projects and understanding how these pieces fit together behind the scenes. It was one of those tasks where the amount of learning happening around the code was much larger than the amount of code being written.</p>
    <h2>Small Contributions Along the Way</h2><p>Alongside the figure testing work, I also contributed a couple of smaller fixes.</p>
    <p>One PR removed some remaining legacy scraper-related code that was no longer needed now that newer SunPy versions are required.</p>
    <p>Another fix addressed an issue where links in the generated changelog were pointing to incorrect GitHub URLs. While investigating it, I ended up learning more about how release notes and documentation are generated than I originally expected.</p>
    <p>Another exciting milestone during this period was the release of radiospectra 0.7. Being able to contribute while a new release was being prepared and published gave me a better understanding of the project's release process, documentation generation, and the work that goes into maintaining a scientific open-source package beyond feature development. Here is the link you can check it out:&nbsp;<a href="https://anaconda.org/channels/conda-forge/packages/radiospectra/overview">https://anaconda.org/channels/conda-forge/packages/radiospectra/overview</a></p>
    <h2>Looking Ahead</h2><p>The last two weeks reinforced something I've been learning throughout GSoC:</p>
    <blockquote><p>Understanding the system is often more important than changing the system.</p>
    </blockquote><p>A lot of progress during this period came from understanding existing workflows, asking questions, exploring project infrastructure, and learning how different parts of the ecosystem connect together.</p>
    <p>With the initial figure testing setup now in place, I'm looking forward to expanding the coverage further and continuing the NDCube-related work in the coming weeks.</p>
    <p>As always, many thanks to my mentors and the SunPy community for their guidance, patience, and feedback along the way. 🚀</p>

