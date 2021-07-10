.. title: astropy@GSoC Blog Post #3, Week 3
.. slug:
.. date: 2021-06-23 22:23:00 
.. tags: Astropy
.. author: Suyog Garg
.. link: https://suyog20.blogspot.com/2021/06/astropygsoc-blog-post-3-week-3.html
.. description:
.. category: gsoc2021


.. raw:: html

    So, it's the start of the 3rd week now. I will be virtually meeting Aarya and Moritz again Tom.<br /><br />For the past few weeks now, I have been pushing commits to a Draft PR&nbsp;<a href="https://github.com/astropy/astropy/pull/11835">https://github.com/astropy/astropy/pull/11835</a>&nbsp;on GitHub. I wanted to have something working quite early in the project, in order to be able to pinpoint accurately when something doesn't work. This is why I started with directly adding the <b>cdspyreadme</b> code within Astropy. Afterwards, I am also writing the code from scratch. As more of the required features from <b>cdspyreadme</b> get integrated into <i>cds.py</i>, those files and codes added earlier will be removed.<br /><br />About the reading/writing to Machine Readable Table format, in fact I wrote about it briefly in my GSoC Proposal that I could attempt it as an extension. I don't have an opinion on whether or not it should have it's own format classes etc. However, since the title of my GSoC project is to <b>Add a CDS format writer to Astropy</b>, I would prefer to work on the CDS format writer first and then on the MRT format. The MRT header anyway appears to be a bit simpler than the CDS header, so there shouldn't be much difficulty in the extension.<br /><br />So, in a nutshell, this is my workflow:<br /><ul style="text-align: left;"><li>Try out directly using <b>cdspyreadme</b> from within Astropy.</li><li>Add CdsData.write method.</li><li>Add a ByteByByte writer.</li><li>Write features to add complete ReadMe to the Header, starting off with having both ReadMe and Data in a single file.</li><li>Have features for writing separate CDS ReadMe and Data file.</li><li>Further work on some specific table columns, for instance, those containing Units and Coordinates.</li><li>Add appropriate tests along the way.</li><li>Resolve other issues that come up.</li><li>MRT format reader/writer.</li></ul><br />I have completed the first three tasks and will now work on the fourth. I think by the time this finishes, a separate <i>CDSColumn.py</i> won't be required. I can open another PR which adds the Data writer, in the meantime.<div><br /></div><div>Let's see how it goes!</div>
    <!-- TEASER_END -->

