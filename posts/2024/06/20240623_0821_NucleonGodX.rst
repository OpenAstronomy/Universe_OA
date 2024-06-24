.. title: It’s going good.
.. slug:
.. date: 2024-06-23 08:21:59 
.. tags: SunPy
.. author: Manit Singh
.. link: https://medium.com/@manitsingh018/its-going-good-160df7122684?source=rss-472b9ac5a505------2
.. description:
.. category: gsoc2024


.. raw:: html

    <p>It’s going good.</p>
    <p>The past two weeks were dedicated to the implementation of wavelength functionality. Now, wavelength has been successfully implemented for the applicable instruments. Along with that, a how-to guide has been created to assist users in navigating querying over wavelength for different instruments. Additionally, a gallery example for wavelength and detector has been added.</p>
    <h3>What’s the direction of implementation:</h3><p>The implementation of wavelength can be divided into two parts:</p>
    <!-- TEASER_END -->
    <ol><li><strong>Instruments with a “wavelength” column in SOAR</strong>: These remote sensing instruments are EUI, SOLOHI, and METIS. For these instruments, we query on the basis of wavelength.</li></ol><pre> instrument = a.Instrument(&quot;EUI&quot;)<br /> time = a.Time(&quot;2023-04-03 15:00&quot;, &quot;2023-04-03 16:00&quot;)<br /> level = a.Level(1)<br /> wavelength = a.Wavelength(304 * u.AA)<br /> res = Fido.search(instrument &amp; time &amp; level &amp; wavelength)</pre><p>Result:</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*Ty2aSvBet-8KYDf6iE729w.png" /></figure><p>A range of wavelength can also be passed, which will be considered wavemin and wavemax for these three instruments.</p>
    <pre>wavelength = a.Wavelength(171 * u.AA, 185 * u.AA)</pre><p>Result:</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*oUBJwth5UcL9IegFG5LjaA.png" /></figure><p>2. For the instruments PHI and SPICE, we don’t have a “wavelength” column in their instrument table, so we use wavemin and wavemax for querying.</p>
    <p>However, there is a problem with SPICE. Since the range of wavelength is only given for the first spectral window of the data, to ensure the data is not misleading to the user, we do not return any wavelength values.</p>
    <pre> instrument = a.Instrument(&quot;PHI&quot;)<br /> time = a.Time(&quot;2023-02-01&quot;, &quot;2023-02-02&quot;)<br /> level = a.Level(2)<br /> wavelength = a.Wavelength(6173.065 * u.AA, 6173.501 * u.AA)<br /> res = Fido.search(instrument &amp; time &amp; level &amp; wavelength)</pre><p>Result:</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*fxkPK8p3KR6xMEv7zIkTXQ.png" /></figure><p>Although passing a range of wavelengths is preferred for PHI, if only one value is passed, it will be taken as wavemin, and filtering will be done based on it. Additionally, the corresponding wavemax will be provided in the output table.</p>
    <pre>wavelength = a.Wavelength(6173.065 * u.AA)</pre><p>Result:</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*O-pETZd8HZi9qVt9NQGa-w.png" /></figure><h3>Challenges that still needs working:</h3><p>There is an issue with PHI’s wavelength data as well. The wavelengths returned are sometimes in the order of 6173 and sometimes 617.3, which are essentially just different units of similar wavelength data, but this is not specified in SOAR.</p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=160df7122684" width="1" />

