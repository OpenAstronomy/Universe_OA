.. title: A Great Start to GSoC with SunPy
.. slug:
.. date: 2024-06-02 09:15:15 
.. tags: SunPy
.. author: Manit Singh
.. link: https://medium.com/@manitsingh018/a-great-start-to-gsoc-with-sunpy-c0fa3bca6157?source=rss-472b9ac5a505------2
.. description:
.. category: gsoc2024


.. raw:: html

    <p>Hello, everyone! My name is Manit Singh, and I’m thrilled to share my journey as a participant in Google Summer of Code (GSoC) with SunPy. Getting selected for this prestigious program has been a significant milestone in my career, and I am excited to contribute to the Enhancing SOAR Metadata project.</p>
    <h3>Community Bonding Period</h3><h3>Introduction to the Community Bonding Period</h3><p>The community bonding period was an essential phase where I got to know my mentors, understand the project’s goals in-depth, and prepare for the coding period.</p>
    <h3>Meetings and Discussions</h3><p>During this period, I had several meetings and discussions with my mentors and community members. These interactions were crucial for:</p>
    <!-- TEASER_END -->
    <ul><li>Understanding the Project Goals: The project aims to increase the scope of SOAR data in sunpy-soar.</li><li>Clarifying Initial Approaches: My initial approach was to implement wavelength and detector first, and then discuss the implementation of the next set of metadata.</li></ul><p>From these initial discussions, we concluded that the Detector should be implemented first, after creating methods to support the joining of instrument and data tables (i.e., v_&lt;instrument&gt;_&lt;ll/sc&gt;_fits and v_&lt;ll/sc&gt;_data_item).</p>
    <h3>First Coding Week: Implementing the Detector in the SOAR Project</h3><h3>Objectives</h3><p>The primary objective for the first week was to add methods to support querying data involving instrument and data tables both and implement the detector component in the SOAR project. Although the detector is part of the SOAR product, my mentors suggested that there are many people who might still want to query over the detector.</p>
    <h3>Implementation Details</h3><p>As discussed in the meetings held during the community bonding period, I worked on constructing methods to enable joining two different tables. Initially, it all looked very messy, but with time and refactoring, a quite simple join constructing method was created.</p>
    <ul><li>Implementing Detector: Similar to how other metadata in the sunpy.net attribute system was implemented, I implemented the Detector. The only major difference was taking data from two tables and joining them.</li><li>Testing: I added tests to ensure that the construct method designed for joining tables could give the desired query outputs and that the detector was working fine for instruments with multiple dimensional data. (which depends on the dimensional index).</li></ul><h3>Challenges and Solutions</h3><h4>Different Dimension Index for instruments:</h4><p>Instruments collect a wide variety of data types that can be multidimensional. For example, for SPICE, there are 4 dimensions, resulting in 4 similar rows of data, one for each dimension. This could be confusing for the user unless the dimension index is also shown in a column. For the STIX instrument, there are 0 dimensions, meaning it does not have any detector column in its instrument fits table. For other remote sensing instruments, there are 2 dimensions.</p>
    <p>Solution:</p>
    <pre># As there are no dimensions in STIX, the dimension index need not be included in the query for STIX.<br />if &quot;stx&quot; not in instrument_table:<br /># To avoid duplicate rows in the output table, the dimension index is set to 1.<br />final_query += &quot;h2.dimension_index='1'+AND+&quot;</pre><p>In the construct methods of the ADQL query I added dimension_index to be taken 1 by default for all instruments other than STIX, this results in no repetition of data.<br />For STIX instrument, since there are no dimension it just works simply okay without taking any dimension in the join query constructed after construct methods</p>
    <h3>Outcomes</h3><p>code:</p>
    <pre>instrument = a.Instrument(&quot;METIS&quot;)<br />time = a.Time(&quot;2022-06-02 0:00&quot;,&quot;2022-06-02 1:00&quot;)<br />level = a.Level(2)<br />detector=a.Detector(&quot;VLD&quot;)</pre><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*ek6niIkxBvp0a6AqSrAivw.png" /></figure><p>By the end of the first week, the detector component was successfully implemented in sunpy-soar. The pull request is currently awaiting review from all the mentors to ensure any discrepancies in the implementation are addressed and to gather additional insights. :)</p>
    <h3>Conclusion</h3><p>The journey so far has been incredibly enriching. The support from my mentors and the community has been invaluable. I am looking forward to the upcoming weeks and continuing to contribute to the SOAR project.</p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=c0fa3bca6157" width="1" />

