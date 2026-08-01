.. title: Weeks 7 & 8: Making Spectrograms a Little Easier to Work With
.. slug:
.. date: 2026-07-31 07:03:03 
.. tags: SunPy
.. author: Kumar Amityush
.. link: https://sunpy-radiospectra.blogspot.com/2026/07/weeks-7-8-making-spectrograms-little.html
.. description:
.. category: gsoc2026


.. raw:: html

    <h2 style="text-align: left;">Making Spectrograms a Little Easier to Work With</h2>
    <p>Another couple of weeks have gone by and it's been a mix of writing code, responding to reviews and learning more about the <code><b>radiospectra</b></code> codebase.</p>
    <p>Compared to the first few weeks, I spent less time figuring out <em>where</em> things lived and more time thinking about <em>how</em> people actually use the library. That shift has been really fun because even small improvements can make a noticeable difference for users.</p>
    <!-- TEASER_END -->
    <h2><span><a name="more"></a></span>Cropping, but Simpler</h2>
    <p>One of the things I worked on was making it easier to crop spectrograms.</p>
    <p>The functionality already existed through <code>ndcube</code>, but it wasn't something you could immediately discover if you were new to the library. So I added two convenience methods:</p>
    <ul>
    <li>
    <b><code>crop_time()</code>
    </b></li>
    <li>
    <code><b>crop_freq()</b></code>
    </li>
    </ul>
    <p>They're fairly small additions, but they make common workflows much nicer.</p>
    <p>Instead of digging into the underlying API, you can now crop directly using the quantities you already have.</p>
    <div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCzPb5YrFGlO5VutMwWM17KywyGMsCHm4ysQm2ycK3uet-n0p-kJracFOgDwru12pcHDPcTIWyfEwFxtflLrfrbFCVkcVFAj-8FijjjR5remwmCMv65cxqSHTtan0B2WoZdxz113JuIM1PuZLDUnoWWu9ZLn822sRmjBWQp4sjokNkoE0ATxZV0kuKYh8/s1400/spectrogram_time_crop.png" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="261" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCzPb5YrFGlO5VutMwWM17KywyGMsCHm4ysQm2ycK3uet-n0p-kJracFOgDwru12pcHDPcTIWyfEwFxtflLrfrbFCVkcVFAj-8FijjjR5remwmCMv65cxqSHTtan0B2WoZdxz113JuIM1PuZLDUnoWWu9ZLn822sRmjBWQp4sjokNkoE0ATxZV0kuKYh8/w609-h261/spectrogram_time_crop.png" width="609" /></a></div><p style="text-align: center;"><b>Time Cropping</b></p><p style="text-align: left;"><br /></p>
    <div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg0Eo3Axqivbdh4W5DyXiJy3OYBhkabdjIZxtjG02AlXuR5SbDAWG2xJGJkOfK_bj8B7jTQEmqa_bh530mF0jJ6EY_xLz5ISd4cUyfmsmwYQ8SHYnPXmlr6V1Wet56aA03ynMoYSJ93B5IpCw0w4zSmxAT__L1KXJaJfovmZS5W8qSyuNWD96u4ugKIQNM/s1400/spectrogram_freq_crop.png" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="232" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg0Eo3Axqivbdh4W5DyXiJy3OYBhkabdjIZxtjG02AlXuR5SbDAWG2xJGJkOfK_bj8B7jTQEmqa_bh530mF0jJ6EY_xLz5ISd4cUyfmsmwYQ8SHYnPXmlr6V1Wet56aA03ynMoYSJ93B5IpCw0w4zSmxAT__L1KXJaJfovmZS5W8qSyuNWD96u4ugKIQNM/w610-h232/spectrogram_freq_crop.png" width="610" /></a></div><div style="text-align: center;"><br /></div><div style="text-align: center;"><b>Frequency Cropping</b></div><div style="text-align: center;"><b><br /></b></div><div style="text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhvvmUGxmicyqbi627amQ_T3pLmEpJ0koNSnvRS_ReIcyxLhg0gcnf_-zq-2SAdTZlGjCUUA_xcR3qPUooPedk57ZqGUb7j9pZpDg6aDrXOtn_9I0MtrPAbqeuQdtdNvnN-T2D2RdUn1-wuU6-pZtDsVH_0nHdYlVrHZUH0W15IzXhqc325W6wv6QXZWWg/s1400/spectrogram_both_crop.png" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="265" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhvvmUGxmicyqbi627amQ_T3pLmEpJ0koNSnvRS_ReIcyxLhg0gcnf_-zq-2SAdTZlGjCUUA_xcR3qPUooPedk57ZqGUb7j9pZpDg6aDrXOtn_9I0MtrPAbqeuQdtdNvnN-T2D2RdUn1-wuU6-pZtDsVH_0nHdYlVrHZUH0W15IzXhqc325W6wv6QXZWWg/w623-h265/spectrogram_both_crop.png" width="623" /></a></div><div style="text-align: center;"><b>Frequency + Time Cropping</b></div><p><br /></p>
    <hr />
    <h2>Playing Around with Slicing</h2>
    <p>After finishing the cropping work, I started experimenting with slicing.</p>
    <p>Since <code><b>GenericSpectrogram</b></code> inherits from <code><b>ndcube</b></code>, slicing "just works", but what I found really cool is that it keeps all the coordinate information intact.</p>
    <p>That means extracting useful data becomes surprisingly simple.</p>
    <p>Want to see how the intensity changes over time at a particular frequency? That's just a time profile.</p>
    <p>Or maybe you want to look at the spectrum at a specific instant? That's a line profile.</p>
    <p>It was one of those moments where I stopped thinking <em>"this is another feature"</em> and started thinking <em>"this is actually really nice to use."</em></p>
    <div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIfSA7wdPFHEoEXDE1yGIAr-CVDCXRINRUUiECvKNLbznVUwE4kQscmXO-pQdiRNT3yTl-lEhnCOIp7UHraKxfvALl9oXIRx_9MIbR5XqpZ5EbB3NnJ9HnbV8hiRyk5itvDKIf6BxhjqxrS1VWwdWjLBE2QYILxk0_rRjEhHUfFyLyO4dNjA1JssU-W10/s1400/spectrogram_profiles.png" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="256" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIfSA7wdPFHEoEXDE1yGIAr-CVDCXRINRUUiECvKNLbznVUwE4kQscmXO-pQdiRNT3yTl-lEhnCOIp7UHraKxfvALl9oXIRx_9MIbR5XqpZ5EbB3NnJ9HnbV8hiRyk5itvDKIf6BxhjqxrS1VWwdWjLBE2QYILxk0_rRjEhHUfFyLyO4dNjA1JssU-W10/w598-h256/spectrogram_profiles.png" width="598" /></a></div><br /><p><br /></p>
    <hr />
    <h2>Reviews, Reviews... and More Reviews 😄</h2>
    <p>A good chunk of these two weeks was spent going through review comments.</p>
    <p>At first, I used to think reviews were mostly about fixing mistakes. Now I realize they're often about finding cleaner ways to solve the same problem.</p>
    <p>Some comments were tiny, others led to bigger discussions about API design and a few even made me rethink parts of the implementation altogether.</p>
    <p>It's probably been one of the most valuable parts of GSoC so far.</p>
    <hr />
    <h2>What's Next?</h2>
    <p>I'm now starting to look at some of the bigger architectural changes in <code><b>radiospectra</b></code>, especially around the metadata factory and how instruments parse their data.</p>
    <p>There's still quite a bit to explore, but I'm excited to keep building on the work from the past few weeks.</p>
    <hr />
    <p>That's all for this update!</p>
    <p>Thanks to my mentors for all the helpful feedback and discussions. Every review teaches me something new and I'm looking forward to sharing more progress in the next blog post.</p>

