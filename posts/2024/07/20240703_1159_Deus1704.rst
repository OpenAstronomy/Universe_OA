.. title: Blog 3: Side Quests Week
.. slug:
.. date: 2024-07-03 11:59:31 
.. tags: SunPy
.. author: Deus1704
.. link: https://deus1704.vercel.app/posts/blog_3/
.. description:
.. category: gsoc2024


.. raw:: html

    <p>While the mentors are waiting for community reviews on the new coalignment API, I&rsquo;ve been diving into some fun side quests.</p>
    <h2 id="side-quest-1-asda-examplehttpsgithubcomsunpysunkit-imagepull218">Side Quest 1: <a href="https://github.com/sunpy/sunkit-image/pull/218">ASDA Example</a></h2>
    <p>The long-needed <a href="https://doi.org/10.3847/1538-4357/aabd34">Automated Swirl Detection Algorithm (ASDA)</a> example gallery in the sunkit-image is now ready. The ASDA module is for identifying the swirls or vortices in the 2D flow field of the solar atmosphere. ASDA offers a robust tool for detecting and analyzing the vortices in the solar atmosphere.</p>
    <!-- TEASER_END -->
    <p>Swirls in the solar atmosphere provide insights into dynamic solar processes such as solar flares and coronal mass ejections. Detecting and analyzing these swirls helps understand the mechanisms driving these solar activities.</p>
    <p>The Gamma(Γ1 &amp; Γ2) values are used for identifying the vortex center and the vortex edges respectively.</p>
    <ul>
    <li>Gamma1 (Γ1): Identifies vortex centers by quantifying rotational motion.</li>
    <li>Gamma2 (Γ2): Detects vortex edges by measuring the coherence of swirling motion.</li>
    </ul>
    <p>These can be visualised as;</p>
    <table>
    <thead>
    <tr>
    <th style="text-align: center;"><img alt="Gamma Visualization" src="https://deus1704.vercel.app/images/gammas.png" /></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: center;">Gamma values (Γ1 &amp; Γ2)</td>
    </tr>
    </tbody>
    </table>
    <p>Using these, the final map with the swirls identified looks like:</p>
    <table>
    <thead>
    <tr>
    <th style="text-align: center;"><img alt="Swirl Map " src="https://deus1704.vercel.app/images/detected_swirls.png" /></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: center;">Swirl Map with Velocity Field</td>
    </tr>
    </tbody>
    </table>
    <p>The swirl map is crucial for visualizing fluid flow dynamics in the solar atmosphere, helping to identify the distribution, size, and characteristics of vortices.</p>
    <p>Magnifying a particular section of these for better understanding of the streamlines:</p>
    <table>
    <thead>
    <tr>
    <th style="text-align: center;"><img alt="Magnified Swirl Map " src="https://deus1704.vercel.app/images/magnified_swirls.png" /></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: center;">Magnified Swirl Map Region with Streamlines</td>
    </tr>
    </tbody>
    </table>
    <p>Magnifying a specific region and overlaying streamlines allows for detailed analysis of flow patterns around swirls, aiding in understanding solar atmospheric dynamics and the interactions between different vortices.</p>
    <h2 id="side-quest-2-rotation-matrixhttpsgithubcomsunpysunpypull7452">Side Quest 2: <a href="https://github.com/sunpy/sunpy/pull/7452">Rotation Matrix</a></h2>
    <p>One of my very first pull requests in SunPy received reviews after a long hiatus. The feedback highlighted some implementation issues with the way the SpicePy API was being used. For instance, the sxform function only accepts a single ephemeris time, which required a workaround to obtain the correct state transformation matrix.
    With the invaluable help of Albert, these issues have been resolved and the test cases have been updated accordingly.</p>

