.. title: During GSoC 2024, I made several key contributions to the sunpy-soar project:
.. slug:
.. date: 2024-08-23 17:10:53 
.. tags: SunPy
.. author: Manit Singh
.. link: https://medium.com/@manitsingh018/during-gsoc-2024-i-made-several-key-contributions-to-the-sunpy-soar-project-6fe71e4df084?source=rss-472b9ac5a505------2
.. description:
.. category: gsoc2024


.. raw:: html

    <ol><li><strong>Initial Implementation of Metadata for Remote Sensing Instrument(merged):</strong></li></ol><ul><li><a href="https://github.com/sunpy/sunpy-soar/pull/118">PR #118</a>: This was my initial pull request where I established join operations for tables and implemented metadata for wavelength and detector for remote sensing instruments.</li></ul><p><strong>2. Gallery Examples and How-to Guide for recent implementations(merged):</strong></p>
    <ul><li><a href="https://github.com/sunpy/sunpy-soar/pull/127">PR #127</a>: In this pull request, I added gallery examples and a how-to guide showcasing the newly implemented wavelength and detector metadata.</li></ul><p><strong>3. Error Handling for SOAR Server Downtime(merged):</strong></p>
    <ul><li><a href="https://github.com/sunpy/sunpy-soar/pull/135">PR #135</a>: This update involved catching server errors thrown by SOAR when it’s down, enhancing the robustness of the system.</li></ul><p><strong>4. Distance Filtering Query Support(merged):</strong></p>
    <!-- TEASER_END -->
    <ul><li><a href="https://github.com/sunpy/sunpy-soar/pull/137">PR #137</a>: I added support for a new query method, REQUEST=&quot;doQueryFilteredByDistance&quot;, enabling distance-based filtering for queries.</li></ul><p><strong>5. Observation Mode Metadata (Not Yet Merged):</strong></p>
    <ul><li><a href="https://github.com/sunpy/sunpy-soar/pull/140">PR #140</a>: This pull request introduced Observation Mode as a new metadata. After discussions with my mentors, we decided not to merge this feature for now.</li></ul><p><strong>6. Field of View (FoV) Values Extraction(Not yet merged):</strong></p>
    <ul><li><a href="https://github.com/sunpy/sunpy-soar/pull/143">PR #143</a>: I added a third join table to extract Field of View (FoV) values with “earth” and “sun” references, allowing users to plot these on a SunPy map.</li></ul><p><strong>7. Developer Guides for Future Development(Not yet merged)</strong></p>
    <ul><li><a href="https://github.com/sunpy/sunpy-soar/pull/147">PR #147</a>: This pull request added a section of developer guides designed to assist future contributors in developing sunpy-soar.</li></ul><p><strong>8. External Method for URL Construction (closed):</strong></p>
    <ul><li><a href="https://github.com/sunpy/sunpy-soar/pull/129">PR #129</a>: This pull request proposed using an external method for making URL calls instead of manually constructing them. However, after further discussion with my mentors, we realized this approach could limit our ability to add future functionality, so we decided not to close it.</li></ul><img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=6fe71e4df084" width="1" />

