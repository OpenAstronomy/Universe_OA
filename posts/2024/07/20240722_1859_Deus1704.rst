.. title: Blog 4: Testing the New Coalignment with a Catch
.. slug:
.. date: 2024-07-22 18:59:31 
.. tags: SunPy
.. author: Deus1704
.. link: https://deus1704.vercel.app/posts/blog_4/
.. description:
.. category: gsoc2024


.. raw:: html

    <p>Now that we&rsquo;ve agreed on the structure of the co-alignment API and also laid down its foundation, all that&rsquo;s left is to validate it through actual tests and generate some gallery examples.</p>
    <h2 id="first-try-with-coaligning-eis-raster-with-aia-map">First try with coaligning EIS raster with AIA map</h2>
    <p>Let&rsquo;s take a closer look at the EIS raster first. I found an AIA image close to the <code>date_average</code> of the raster.</p>
    <!-- TEASER_END -->
    <table>
    <thead>
    <tr>
    <th style="text-align: center;"><img alt="EIS raster" src="https://deus1704.vercel.app/images/original_eis.jpeg" /></th>
    <th style="text-align: center;"><img alt="AIA Full-disc image" src="https://deus1704.vercel.app/images/aia_near_raster_avg.jpeg" /></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: center;">EIS raster</td>
    <td style="text-align: center;">AIA Full-disc image</td>
    </tr>
    </tbody>
    </table>
    <table>
    <thead>
    <tr>
    <th style="text-align: center;"><img alt="Updated EIS" src="https://deus1704.vercel.app/images/updated_eis.png" /></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: center;">Updated EIS</td>
    </tr>
    </tbody>
    </table>
    <p>At first glance, the results seemed promising, but a more detailed analysis revealed some discrepancies.</p>
    <p>The updated WCS metadata looked fine at first, but on closer inspection, it wasn&rsquo;t entirely correct. We&rsquo;ll dive into the specifics later in this blog. For now, let&rsquo;s discuss why it might look correct at a glance. How does a common user check if the maps are aligned? By overlaying them and checking the overlaps!</p>
    <table>
    <thead>
    <tr>
    <th style="text-align: center;"><img alt="EIS overlaid on AIA" src="https://deus1704.vercel.app/images/eis_overlaid_aia.png" /></th>
    <th style="text-align: center;"><img alt="Zoomed" src="https://deus1704.vercel.app/images/eis_overlaid_aia_zoomed.png" /></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: center;">EIS overlaid on AIA</td>
    <td style="text-align: center;">Zoomed</td>
    </tr>
    </tbody>
    </table>
    <p>This visual inspection might convince some that the method works, but it’s far from accurate. We proved this by highlighting the bright regions and focusing on the actual overlaps.</p>
    <table>
    <thead>
    <tr>
    <th style="text-align: center;"><img alt="EIS contours overlaid on AIA" src="https://deus1704.vercel.app/images/old_contours.png" /></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: center;">EIS contours overlaid on AIA</td>
    </tr>
    </tbody>
    </table>
    <p>This showed us that something was wrong with either the way we were updating the metadata or the co-alignment method. While discussing this, we realized that an assumption in the match_template method was that the maps should have the same type of WCS.</p>
    <h2 id="the-celestial-fix">The Celestial Fix</h2>
    <p>In our initial approach, we focused on adjusting the CRPIX values instead of the CRVAL values. CRPIX specifies the position of the reference pixel in the image, shifting the image in pixel space without correcting the world coordinates directly. This method led to apparent alignment issues because it didn&rsquo;t address the celestial coordinate system. After consultation, we realized that adjusting CRVAL, which defines the world coordinates of the reference pixel, is essential. This adjustment ensures that the reference points align correctly in world coordinate space, maintaining consistent mapping between pixel and celestial coordinates.</p>
    <p>Furthermore, for accurate co-alignment, the observers (instruments) should be within a tolerable angular separation to minimize parallax effects. When observers are too far apart, solar features can appear differently due to relative positions, complicating alignment. By correcting CRVAL values and considering angular separation, we achieved precise co-alignment, as evidenced by the corrected overlay of EIS contours on the AIA image, allowing for reliable scientific analysis.</p>
    <table>
    <thead>
    <tr>
    <th style="text-align: center;"><img alt="EIS contours overlaid on AIA (corrected)" src="https://deus1704.vercel.app/images/fixed_eis.jpeg" /></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: center;">EIS contours overlaid on AIA (corrected)</td>
    </tr>
    </tbody>
    </table>

