.. title: Implementing the NIST database
.. slug:
.. date: 2024-08-12 00:00:00 
.. tags: radis
.. author: code29563
.. link: http://code29563.github.io/Implementing-the-NIST-database/
.. description:
.. category: gsoc2024


.. raw:: html

    <ul>
    <li>The Einstein A coefficient is now used directly for calculating the non-equilibrium linestrength, given that it is calculated anyway for non-equilibrium spectra where it isn’t already present, rather than removing the temperature-dependent component of the reference linestrength, which was found to result in some atomic spectra not appearing. This also removes the need to calculate the reference linestrength for databanks where it’s not already present.</li>
    <li>Removed some redundnant code and miscellaneous fixes and improvements.</li>
    <!-- TEASER_END -->
    <li>Fixed the documentation for many parts of the new code for atomic spectra so the formatting appears correct on Read the Docs.</li>
    <li>The pull request for the implementation of the Kurucz database has been merged</li>
    <li>Work has started on adding support for the NIST atomic database and it is currently at a stage where it produces working spectra.</li>
    </ul>

