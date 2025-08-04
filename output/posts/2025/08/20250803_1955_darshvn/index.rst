.. title: We’re onto something.
.. slug:
.. date: 2025-08-03 19:55:57 
.. tags: radis
.. author: Darshan Patil
.. link: https://medium.com/@darshvn/were-onto-something-a8f681c13ca5?source=rss-33c64fc8aea8------2
.. description:
.. category: gsoc2025


.. raw:: html

    <p>I know I’m a bit late with this update, but I’ve been deep in the process of making everything work. The pieces we’ve been putting together since the beginning of the project are finally falling into place.</p>
    <p>Since my last blog post, I resolved the broken data flow during the parsing of the states file. Now, all the necessary data flows cleanly through to the spectrum calculation step.</p>
    <p>I also began getting some calculated values but something was off. Instead of showing normalized populations per electronic state, it was printing partition function values. Once corrected, the values made sense and were properly normalized.</p>
    <!-- TEASER_END -->
    <p><strong>Debug outputs:</strong><br />Electronic Population Fractions:</p>
    <pre>State: A²Σ⁺ | Fraction: 0.094942 (9.49%)<br />State: X²Π | Fraction: 0.905058 (90.51%)</pre><p>Rovibrational Population Normalization:</p>
    <pre>X²Π state: 932 rovibrational levels, sum = 1.0000000000000002<br />A²Σ⁺ state: 481 rovibrational levels, sum = 0.9999999999999999</pre><p>Population Products (elec. fraction × rovib. sum):</p>
    <pre>State: A²Σ⁺ | Product: 0.094942<br />State: X²Π | Product: 0.905058<br />Total Sum of Products: 1.0</pre><p>Next, I compared the generated spectrum with the reference one Nicolas had shared. It matched quite well except my plot showed too much population in the high vibrational states.</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*D5MHvgifJsOswOPmamv_pQ.png" /><figcaption><em>Reference vs Plotted Spectrum</em></figcaption></figure><p>The root cause turned out to be the default fallback values for vibrational quantum number (v) and degeneracy when parsing failed. That’s now fixed; the correct vibrational levels are being parsed properly.</p>
    <p>At this point, the code returns NaN for transitions with v&gt;10, so the output is restricted to those with v≤10. In this case, 714 transitions are excluded, and the resulting spectrum closely matches the reference.</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*YyaWzipkoDuDGys0OBf80Q.jpeg" /><figcaption>Spectrum after Filtering</figcaption></figure><p><strong>What’s causing the NaNs?</strong><br />The partition function was only being calculated up to vibrational level 10, while the line database includes levels like v = 11–13. When the code attempts to fetch partition function values for these higher levels, it receives None, which becomes NaN in the DataFrame. This breaks the nu (upper state population) calculation, which relies on a valid Qrotu.</p>
    <p>The vibrational quantum numbers in the partition function are generated in build_energy_levels_class1 using:</p>
    <pre>ElecState.Erovib(v, J=0, remove_ZPE=True)</pre><p>This method:</p>
    <ul><li>Starts at v = 0</li><li>Increments by 1</li><li>Computes energy from spectroscopic constants</li><li>Stops when energy exceeds the dissociation limit</li><li>Generates all levels up to that point</li></ul><p>This logic was already used for CO and CO₂ earlier in the codebase. I’m now awaiting feedback from mentors on whether we should sum the partition function only up to the dissociation limit or extend it to match all states available in the transition file.</p>
    <p>The next step, as suggested by Nicolas, is to generalize the implementation to support any molecule from ExoMol. We can then test it by comparing with CH(A–X), which is already available in our in-house code. I’ll also clean up some redundant code that was introduced while experimenting with different approaches.</p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=a8f681c13ca5" width="1" />

