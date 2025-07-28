.. title: Bench-marking Partial Decompression
.. slug:
.. date: 2025-07-27 12:24:19 
.. tags: radis
.. author: Pratham
.. link: https://medium.com/@prathamhole/bench-marking-partial-decompression-a0aed143eef0?source=rss-edb3c1b90bf0------2
.. description:
.. category: gsoc2025


.. raw:: html

    <p>Hello everyone, and welcome back to another episode of my Google Summer of Code project series! In my previous post, I introduced a clever partial decompression mechanism. If you haven’t had a chance to read it yet, check it out <a href="https://medium.com/@prathamhole/seeking-fast-at-any-point-in-a-bz2-compressed-file-5ee78f20670f">here</a>. I promise it’s worth your time. In this post, I’ll share the benchmarks and findings for the new functionality.</p>
    <p>Both the previous and new implementations require downloading the full 6 GB file before processing, so download time is excluded from all benchmarks below. In the original approach, after downloading, the entire file is parsed into a DataFrame and stored in <em>HDF5/H5 format</em>. As expected, this process is painfully slow when you only need to extract, say 2.5 GB out of 50 GB worth of data from the decompressed stream. This is where my partial decompression logic shines.</p>
    <h4>Parsing 2.5 GB Without Cache</h4><p>Below is the comparison of parsing 2.5 GB of data (without cache) using the old mechanism versus my new solution:</p>
    <!-- TEASER_END -->
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/976/1*KvmMfiPT2PnhIZOAHqSkrw.png" /></figure><h4>Parsing 2.5 GB With Vectorized Optimizations</h4><p>In the above benchmark, parsing 2.5 GB of data with new implementation using the original regex-based slicing parsing took around 6.5 minutes. By replacing these expensive regex operations with a more efficient index-based slicing approach, I was able to bring that time down to just 4.55 minutes. This change resulted in a performance boost nearly a 30% improvement.</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/976/1*VDT6zzRssngN9YCv1U42MQ.png" /></figure><h4>Parsing 2.5 GB With Cache</h4><p>Next, I measured the performance of parsing 2.5 GB of data when reusing the cached files generated during the initial parse. Thanks to caching, subsequent reads avoid decompressing and re‑indexing the same regions, yielding dramatically faster turnaround for typical query sizes. In our tests, parsing 2.5 GB from the cache dropped from 4.55 minutes down to just 1.2 minutes an almost 75 % improvement over the original uncached workflow. Of course, if users workload involves scanning the entire 50 GB dataset in a single pass, the relative gains from caching diminish significantly; I’ll cover end‑to‑end file performance in my next post.</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/976/1*ujEQDoZJl_hy4sUZI4KQQQ.png" /></figure><p>The next major update will leverage <em>C++ SIMD intrinsics</em> (Single Instruction, Multiple Data) to accelerate parsing at the assembly level. That optimization will push performance even further, and I’ll share the details and code examples in my next blog post. As always, thank you for reading, and stay tuned!</p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=a0aed143eef0" width="1" />

