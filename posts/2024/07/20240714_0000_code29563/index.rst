.. title: Finishing up equilibrium spectra
.. slug:
.. date: 2024-07-14 00:00:00 
.. tags: radis
.. author: code29563
.. link: http://code29563.github.io/Finishing-up-equilibrium-spectra/
.. description:
.. category: gsoc2024


.. raw:: html

    <ul>
    <li>Tests have been added for the implementation of the Kurucz database and associated parts of the code</li>
    <li>Examples have been added relating to the Lorentzian broadening of atomic lines and partition functions.</li>
    <!-- TEASER_END -->
    <li>The function to parse Kurucz linelists has been re-written based on Pandas.</li>
    <li>The precision of some parts of the code has been improved by using <code class="language-plaintext highlighter-rouge">numpy.expm1</code> rather than <code class="language-plaintext highlighter-rouge">numpy.exp</code>, thereby showing weaker spectra that otherwise weren’t being seen</li>
    <li>Support has been added for loading existing databanks of atomic species without specifying the species initially.</li>
    <li>A greater range of formats are now accepted as input to specify the species for which to calculate a spectrum.</li>
    <li>Documentation for atomic spectra and the Kurucz database has been updated further</li>
    </ul>

