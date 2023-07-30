.. title: Adapting Kurucz to SpectrumFactory and what is next ?
.. slug:
.. date: 2023-07-29 23:43:53 
.. tags: radis
.. author: Racim MENASRIA
.. link: https://medium.com/@menasrac/adapting-kurucz-to-spectrumfactory-and-what-is-next-d3453292daf1?source=rss-e63f6bf6735b------2
.. description:
.. category: gsoc2023


.. raw:: html

    <h3><strong>Adapting Kurucz to SpectrumFactory and what is next ?</strong></h3><p>After my first pull request I received some feedback.<br />Optional and major changes were requested. The most important changes were that my code should <strong>better integrate the existing Radis code</strong>. Indeed, though I added a new database with Kurucz, its API remained distinct which is something which will make Radis progress toward a common API.</p>
    <p>Another key remark was that my code didn’t take into account the <strong>Broadening effects</strong> that modify the lineshapes.<br />This is why I had a Team meeeting with my mentors to discuss the physics behind the code. It helped me a lot to understand what was expected.</p>
    <p>After this I worked on adding broadening and merging the new AdB Kurucz with SpectrumFactory. In order to do so, I worked on an example which allows to plot a spectrum using the Kurucz atomic data and <strong>SpectrumFactory.</strong> My first attempt was to use one of the existing Radis formats for databanks named <strong>hdf5-radisdb</strong> since I worked with hdf5 files in my Class.<br />This attempt happened to be too difficult because the formats were made for molecules and too many columns of my dataframe were different from the expected columns.<br />This is why I eventually decided to add <strong>a new format named “kurucz” </strong>to the load_databank method which allows to load the kurucz data with the proper form.</p>
    <!-- TEASER_END -->
    <p>Then, I worked on the <strong>eq_spectrum</strong> method to adjust it to this newformat.<br />I added some methods and adapted methods from Exojax to handle linestrength computation, broadening,convolution,pressure layers and create a Spectrum Object. It took me a lot of efforts and I modified many files as Broadening.py, Base.by,Factory.py or loader.py.<br />However, the results of the Spectrum I obtained were not convincing and some parameters and units didn’t fit properly.</p>
    <p>Moreover, by the time I wrote this spectrocopy code, I fell behind in my project, that’s why we organized a long meeting with one of my supervisors in order to take stock, we adjusted the objectives of the project.</p>
    <h3>We gave up the last one about adding the CIA database and agreed on the following timeline :</h3><ul><li>finishing with SpectrumFactory for Kurucz ASAP</li><li>Moving to NIST</li><li>Then working on the DatabaseManager Class architecture and adapting to AdB and MdB manager subclasses</li><li>Moving to the TheoreTS ( it will require to reach people in Reims to fix the db that I still cannot access).</li><li>Working on developing an example during the last week to show what applications the atomic spectra physics brings.</li></ul><p>We also noticed that I had written my Spectrum Factory example from the beginning rather than using the existing radis methods which is why I lost time and it was unaccurate. However, the meeting brought me the right guidelines and working on this code allowed me to getting a better understanding of the architecture and adapting the example to the existing structure of the code should be easier now. We also discussed about a few existing codes which could be a could starting point for adding NIST to Kurucz.</p>
    <h3><strong>Conclusion</strong></h3><p>The next weeeks will take me a lot of time and effort to complete the objectives but in the end, I am happy that we had this meeting because it unblocked me when I was kinda stuck with Kurucz for a while.</p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=d3453292daf1" width="1" />

