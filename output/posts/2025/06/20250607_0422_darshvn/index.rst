.. title: Starting My GSoC Journey with RADIS
.. slug:
.. date: 2025-06-07 04:22:57 
.. tags: radis
.. author: Darshan Patil
.. link: https://medium.com/@darshvn/starting-my-gsoc-journey-with-radis-14b98a245c55?source=rss-33c64fc8aea8------2
.. description:
.. category: gsoc2025


.. raw:: html

    <h3>Getting Started</h3><p>A month has passed since the GSoC results came out, and honestly, and the excitement still hasn’t quite settled. That announcement day was pretty intense, my mind was racing, second-guessing everything. But wow, things worked out even better than I’d hoped.</p>
    <p>The community bonding period hit right during my final exams, which was tricky timing. So I focused on what mattered most, getting to know my mentors, joining the weekly calls, and really wrapping my head around the project from a theoretical standpoint.</p>
    <h3>What I’m Working On</h3><p>I’m working on something called “<strong>Electronic Spectra for RADIS.</strong>” Basically, RADIS is this awesome library for modeling rovibrational spectra, but it’s missing one key piece; electronic transitions. That’s where I come in! I want to add that missing functionality and make RADIS even more powerful.</p>
    <!-- TEASER_END -->
    <p>Even though I already knew RADIS pretty well, I spent time going through everything again to make sure I really understood what needed to be done. No point in reinventing the wheel, right? My mentor Nicolas helped me put together a solid plan that actually makes sense.</p>
    <h3>Breaking It Down</h3><p>Here’s how I’m breaking it down into four main chunks:</p>
    <p>First up is <strong>OH Electronic Spectra Calculation</strong> — I’m starting with OH molecules as my test case and building the ability to manually tweak electronic band intensities when things are not in equilibrium as suggested by Nicolas in the project idea, “<em>starting with non-equilibrium spectra of atomic species makes sense since the physics is slightly easier than for molecules</em>.”</p>
    <p>Then comes <strong>Electronic Temperature Support</strong> — this is where I’ll add calculations for electronic state populations, assuming the electronic temperature is different from the other temperatures.</p>
    <p>Third is <strong>Equilibrium OH Spectrum</strong> — putting together everything from the earlier steps to calculate OH spectra when things are in equilibrium.</p>
    <p>Finally, <strong>Extension to ExoMol Molecules</strong> — taking what I’ve built and making it work for all ExoMol molecules.</p>
    <p>This approach builds on what RADIS already does well while systematically adding the electronic transition stuff, all within the GSoC timeline.</p>
    <h3>The Technical Stuff</h3><h3>Working with Data Files</h3><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*pTN3jp3K2szObHXmSYp3gw.png" /><figcaption>Sample of the OH .states file format showing electronic state information and quantum numbers.</figcaption></figure><p>To kick off the first milestone, I’m using the .states file from ExoMol for OH molecules, which has all the electronic state info and quantum numbers. RADIS already has a read_states() function in exomolapi.py that can parse this format, but right now it only extracts:</p>
    <ul><li>i: State counting number</li><li>E: State energy</li><li>g: State degeneracy</li><li>J: Total angular momentum</li></ul><p>I’ll modify this to additionally extract the electronic-specific parameters:</p>
    <ul><li>State: Electronic state label (e.g., X(²Π))</li><li>Λ: Electronic angular momentum quantum number</li><li>Σ: Spin angular momentum quantum number</li><li>Ω: Total electronic angular momentum quantum number</li><li>Type: State type (e.g., Ma for main)</li></ul><p>This will be the foundation for getting electronic transitions working in RADIS.</p>
    <h3>Making the Calculations Work</h3><p>For the population calculations, I’ll be working with the existing partfunc.py file. I'm planning to create a new ElectronicPartitionFunction class and implement the Boltzmann distribution for electronic states. Nicolas referenced a formula from his <a href="https://theses.fr/2020UPAST052">thesis (Chapter 1, Section 1.1)</a> that’s relevant to what I’m implementing.</p>
    <figure><img alt="Boltzmann distribution" src="https://cdn-images-1.medium.com/max/1024/1*bEtk5kQGqpD5kbzwgmLeCQ.png" /><figcaption>Boltzmann distribution</figcaption></figure><p>All of this will eventually get integrated into SpectrumFactory to compute electronic spectra in SpectrumFactory.non_eq_spectrum(). I'll be adding an electronic temperature (Telec) parameter and thinking about using the overpopulation parameter for manually adjusting electronic band intensities.</p>
    <h3>What’s Next</h3><p>I’m planning to work on all this over the next few weeks to nail the first milestone. I’m genuinely excited to be part of this project and can’t wait to learn tons and build something really cool. This is going to be an amazing journey!</p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=14b98a245c55" width="1" />

