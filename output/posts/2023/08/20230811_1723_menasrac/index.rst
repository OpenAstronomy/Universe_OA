.. title: Progress on Kurucz and NIST databases
.. slug:
.. date: 2023-08-11 17:23:24 
.. tags: radis
.. author: Racim MENASRIA
.. link: https://medium.com/@menasrac/progress-on-kurucz-and-nist-databases-e955d61c1591?source=rss-e63f6bf6735b------2
.. description:
.. category: gsoc2023


.. raw:: html

    <p>Since the last article, I received a lot of feedback and comments about the Kurucz PR.</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/952/1*iyB8Ya_dKD5OIkQ8gbcovg.png" /></figure><p>Here is and example of a Fe_I spectrum I can obtain with these conditions.</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*alxgHx0L0Bg54hyUcp8h0Q.png" /></figure><h3>The main remarks where that :</h3><p>I needed to adjust the code to make it more general and user friendly. I introduced a specie argument to SpectrumFactory and calc_spectrum to replace atom and molecule and gather them under a same name.</p>
    <!-- TEASER_END -->
    <p>I made sure to respect the Radis structure by mooving files where I needed to and adding a new Partfunc class for Kurucz. <br />Then I added a few tests and removed old tests that were not needed any longer.</p>
    <p>I also cleaned my PR : removed all the unused methods from the Kurucz API,added references, moved hardcoded arrays to proper files.</p>
    <p>We asked the Exojax team for more help about the broadening parameters. For the moment, there are some approximations and placeholders about the airbrd (air broadening which is required in the Radis format) by computing it thanks to the Kurucz parameters.<br />A simplified version of the broadening allows to plot spectra for now but there are still values to adjust for the various species.</p>
    <p>I also started to work on the NIST database by fixing a parsers developed last year. Though I can plot NIST spectra for some wavelength, there still are issues particularly about the FWHM to deal with.</p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=e955d61c1591" width="1" />

