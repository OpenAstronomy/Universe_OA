.. title: astropy@GSoC Blog Post #5, Week 6&7
.. slug:
.. date: 2021-07-21 20:00:00 
.. tags: Astropy
.. author: Suyog Garg
.. link: https://suyog20.blogspot.com/2021/07/astropygsoc-blog-post-5-week-6.html
.. description:
.. category: gsoc2021


.. raw:: html

    <p>Hi,</p>
    <p>How are you?</p>
    <p>My dear mentors and I have decided to have the MRT (Machine Readable Table) format writing first. The same CDS code as been used now will be used, just the template of the written table will be in the MRT format.</p>
    <!-- TEASER_END -->
    <p>Points to be noted regarding this and the immediate things that have been and will done are as follows:</p>
    <p></p>
    <ul style="text-align: left;"><li>Leave out writing all the optional CDS ReadMe fields as of now. These can be dealt with individual PRs later.</li><li>Some tests fail because <span style="font-family: courier;">start_line = None</span> doesn't work. It has been introduced once again within <span style="font-family: courier;">CdsData.write</span> function in addition to been defined in the main <span style="font-family: courier;">Cds</span> class. The test failure occurs because CdsData now inherits from <span style="font-family: courier;">FixedWidthData</span> which itself inherits <span style="font-family: courier;">basic.BasicReader</span> instead of BaseReader. I should make sure that all tests pass properly.</li><li>Have a template for MRT tables and write them first. <b>Title</b>, <b>Authors</b>, <b>Date</b>, <b>Caption</b> and <b>Notes</b> sections, i.e. all sections except the Byte-By-Byte and the Data itself, will be left blank in the template, with warning for the user to put them in manually afterwards.</li><li>Documentation for the CDS/MRT format writer.</li><li>At present issue a warning note for tables with two or more mix-in columns (<span style="font-family: courier;">SkyCoord</span> cols primarily). If ways to correctly work out such situations is thought of, add that feature in a separate PR.</li><li>Work with a copy of the original table, so that&nbsp; the copy is modified and not the original table, when component coordinate columns are written. The modified copy of the table is written to a file, while the user retains access to the columns of the original table.</li><li>Need to have features to recognise non Spherical coordinates, like the Cartesian coordinates, and either skip them or write them as Single column string values. Add test for such other coordinates. Also for cases when coordinates are in a <span style="font-family: courier;">SkyCoord</span> object but the frame is not Spherical.</li><li>Have two other templates, one for CDS in which the user fills values of optional fields manually later and another in which filling optional fields can be done from within Astropy, via a <span style="font-family: courier;">cdsdict</span>. In separate PRs. Here too write only the required fields in the ReadMe first, like <b>Abstract</b>.</li><li>Have features for Time columns later within the original PR or much later.</li><li>Simplify how column format is obtained for float columns. The current manner of string formatting is too complicated. <span style="font-family: courier;">col.width</span> value can be directly used in some cases. The <span style="font-family: courier;">Outputter</span> class will also know the column format since it writes out the table.</li><li>Other minor/major edits and modifications as suggested by others.</li></ul><div>With this PR for the MRT format table writing getting eventually merged to Astropy, the main goal of my astropy@GSoC project will be completed. The support for other extra features essentially serves as appendages to the primary task been done by this PR.</div><div>Let's see how it goes.</div><div><br /></div><div>Oh! On another note, a few days back I received the GSoC First Evaluations payment! 😁</div><div><br /></div><div>Adious!</div><p></p>

