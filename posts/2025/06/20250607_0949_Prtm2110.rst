.. title: Yeah! I have a GSoC project with Radis
.. slug:
.. date: 2025-06-07 09:49:18 
.. tags: radis
.. author: Pratham
.. link: https://medium.com/@prathamhole/yeah-i-have-a-gsoc-project-with-radis-113900105c46?source=rss-edb3c1b90bf0------2
.. description:
.. category: gsoc2025


.. raw:: html

    <p>Finally, I have been contributing to scientific open source for about a year now and it has taught me a lot I mean a lot, I still remember searching for a simple documentation issue so I could get it merged and call myself a “contributor” haha, and that got me started in scientific open source. Since then, I have been able to make some truly meaningful contributions to many projects, and here I am writing a blog for GSoC with Radis which is a pythonic library for fast line-by-line code for high resolution infrared molecular spectra, under the OpenAstronomy umbrella.</p>
    <p>So my project is cool ngl, and it is titled “Fast Parsing of Large Databases and Execution Bottlenecks” basically there exists a large highly compressed CO₂ spectroscopic database of size 6 GB file that decompresses to about 50 GB and takes at least 2.5 hours to parse and convert into a DataFrame. As you might expect, my project is about significantly reducing the parsing time and finding a workaround for storing only the “necessary” parts of the decompressed file.</p>
    <p>Radis is pythonic and sometimes python gets real slow if not used the way it is meant to be used, so my initial thought was to first clean up the existing code and use vectorised operations and with numba we should be able to see some real optimisation. But then I realized the current implementation already has the right vectorized operations on DataFrames, and Pandas’ vectorized methods are already implemented in optimized C/Cython loops. So there isn’t much more to do here other than replace a few overheads with other operations. After that, as discussed with my mentors I can use a C++ Single Instruction Multiple Data (SIMD) mechanism to parse the file and create a python interface on top of that with pybind11 or cython and other option but this will cost us portability as compilation will be a thing that is to considered. Other approach which is using vulkan API in python as it supports CPU as well GPU parallelism and its cross platform as it will works on all CPU architectures.</p>
    <!-- TEASER_END -->
    <p>The first thing I did was profile the hit2df function for the NO₂ molecule, which is much smaller compared to CO₂ but uses the same operations. That gave a good idea of the actual bottlenecks and where I need to work.</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*9OApPZeVUuVw2vAwSCqGQg.png" /><figcaption>Profiling of `hit2df` function for NO₂ molecule</figcaption></figure><p>As you can see, most of the time is spent in post_process_hitran_data and which is expected because this function calls parse_local_quanta and parse_global_quanta both applies regex across multiple string columns, which is slow at scale, so I switced to fixed‐width slicing to avoid that per-row overhead, of course this was possible as the dataset is consistent and doesn’t require regex at all (I really hope).</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/0*4T1gkGX-4N4_CzO3" /></figure><p>This resulted in a clean improvement of about 38%, which will serve as the default option, along with the Vulkan-API mechanism, which I expect will yield a huge optimization compared to the default. That’s something we will see that in the next episode, stay tuned ;)</p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=113900105c46" width="1" />

