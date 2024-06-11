.. title: The start
.. slug:
.. date: 2024-06-10 00:00:00 
.. tags: radis
.. author: code29563
.. link: http://code29563.github.io/the-start/
.. description:
.. category: gsoc2024


.. raw:: html

    <p>The first aim for this project is to add support for the atomic Kurucz database to RADIS. A <a href="https://github.com/radis/radis/pull/601">PR</a> containing previous work done on this provides a starting point. Much use had been made of code from the ExoJax project, which had already implemented support for the Kurucz database and with which RADIS is pursuing a common API.</p>
    
    <p>After examining the work done so far in that PR, I merged it onto the latest <code class="language-plaintext highlighter-rouge">develop</code> branch with few conflicts to resolve. There are a number of errors and/or placeholders in the previous code that are gradually being corrected.</p>
    <!-- TEASER_END -->
    
    <p>I began looking into an outstanding issue from the previous work which was implementing Lorentzian broadening for atomic lines, as RADIS has previously catered mainly for molecular databases. ExoJax provides <a href="https://github.com/HajimeKawahara/exojax/blob/78466cef0170ee1a2768b6a6f7b7c911d715c1bd/documents/userguide/atomll.rst#broadening-parameters">5 functions to choose from</a> for this, the results of which can <a href="https://github.com/HajimeKawahara/exojax/blob/920bce49e9bf30c33b5d349425dc9b837237974f/tests/endtoend/metals/opacity_Fe_test.py#L59">differ from each other by up to an order of magnitude</a>. The <code class="language-plaintext highlighter-rouge">gamma_vald3</code> function is the one regularly used in ExoJax and we chose to use it as a basis for the default function in RADIS. I have been reviewing its handling of Stark broadening in particular as some corrections were required.</p>
    
    <p>Considering the numerous different formulae that have been proposed for Lorentzian broadening of atomic lines, and the significantly different results they produce, I also added a parameter in the <code class="language-plaintext highlighter-rouge">SpectrumFactory</code> class for a user to specify their own function to use instead of <code class="language-plaintext highlighter-rouge">gamma_vald3</code>. I also added a similar parameter in <code class="language-plaintext highlighter-rouge">calc_spectrum</code> (a typical entry point for the end user) for a user to specify a class to use in place of <code class="language-plaintext highlighter-rouge">SpectrumFactory</code>, which allows them even more flexibility and control over other parts of the spectrum calculation too.</p>
    
    <p>I started a PR for this project to enquire about <a href="https://github.com/radis/radis/pull/652#issuecomment-2141212791">an issue</a> related to the <code class="language-plaintext highlighter-rouge">truncation</code> parameter used in calculating the lineshape and the differing results depending on the choice of <code class="language-plaintext highlighter-rouge">optimization</code> method.</p>
    
    <p>I’ve also been looking into third-party tools to generate plots of spectra for the same atoms for comparison with the results being generated in RADIS and to potentially indicate through any discrepancies whether there’s an error to be resolved.</p>

