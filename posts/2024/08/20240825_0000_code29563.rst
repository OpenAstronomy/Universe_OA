.. title: A summary
.. slug:
.. date: 2024-08-25 00:00:00 
.. tags: radis
.. author: code29563
.. link: http://code29563.github.io/A-summary/
.. description:
.. category: gsoc2024


.. raw:: html

    <p>RADIS describes itself as <a href="https://radis.readthedocs.io/en/latest/">‘a fast line-by-line code for high resolution infrared molecular spectra’</a>. My project focussed on adding support for atomic line databases to RADIS, which has up till now catered only for molecular databases. Atomic lines differ significantly from molecular lines in how they are affected by Lorentzian broadening and how non-equilibrium spectra are handled.</p>
    
    <p>The main goal was <a href="https://github.com/radis/radis/pull/652">adding support for the Kurucz atomic database</a>, which is now complete. This laid the basic structure for adding new atomic databases, and <a href="https://github.com/radis/radis/pull/689">a PR is now open for adding NIST</a>.</p>
    <!-- TEASER_END -->
    
    <p>A number of side issues have arisen throughout the course of the project and been tended to within those PRs, whereas independent issues and PRs have been opened for other issues:</p>
    <ul>
    <li>The non-equilibrium linestrength calculation for both atoms and molecules now <a href="https://github.com/radis/radis/pull/676">uses the Einstein Coefficient instead of the reference linestrength</a>, thereby allowing weaker spectra to be seen</li>
    <li><a href="https://github.com/radis/radis/issues/661">The issue was also raised</a> as to whether RADIS should be automatically modifying the user config file, and if so then how. That has been tended to in the Kurucz and NIST implementation so far and could be expanded to the molecular databases too.</li>
    <li><a href="https://github.com/radis/radis/pull/675">fixing the removal of ‘object’ type columns from the line dataframe</a></li>
    <li><a href="https://github.com/radis/radis/issues/666">Debugging a docstring example that didn’t actually work</a></li>
    </ul>
    
    <p>Prior to the project starting, <a href="https://github.com/radis/radis/pull/646">a PR</a> was also opened to allow users to specify the minimum linestrength at which to cut off weaker lines by specifying them as the weakest x% of lines.</p>

