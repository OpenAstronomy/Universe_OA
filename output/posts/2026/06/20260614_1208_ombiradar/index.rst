.. title: Results are out!!!
.. slug:
.. date: 2026-06-14 12:08:19 
.. tags: lincc-fw
.. author: Om Biradar
.. link: https://imporving-pyarrow-for-nested-structures.hashnode.dev/results-are-out
.. description:
.. category: gsoc2026


.. raw:: html

    <p>My GSoC project's main goals includes parallelizing the reading of structs in parquet files. This is very beneficial to the community as astronomical data involves data stored in structs and other nested structures.</p>
    <img alt="" src="https://cdn.hashnode.com/uploads/covers/69cbd2f4c1e86567d73c63eb/79712cfd-bfff-44aa-b909-7dd5cb572175.png" style="display: block; margin: 0 auto;" />
    
    <!-- TEASER_END -->
    <p>This figure shows the performance increase/decrease the optimized parquet reader (which I made) has over the baseline main branch of apache/arrow when run on a standard free GitHub runner and the file in loaded into the RAM to remove the I/O overhead which is not relevant here.</p>
    <p>For smaller files, the overhead of multi threading causes it to be slower, but for real life cases when the file sizes are large, the optimized reader now provides 25%-30%+ faster reading times.</p>
    <img alt="" src="https://cdn.hashnode.com/uploads/covers/69cbd2f4c1e86567d73c63eb/8f49160a-b4ca-43a5-810f-b5bfa82d9766.png" style="display: block; margin: 0 auto;" />
    
    <p>When compared to flat parquet files, the nested struct now offer similar read speeds with multi threading enabled!!</p>
    <p>Overally, the project is going at a great pace with verifiable results. I hope this integrates with the upstream apache arrow library soon so that this performance boost can help the people working with PyArrow on astronomy datasets.</p>
    <p>The link to the PR - <a href="https://github.com/apache/arrow/pull/50158">https://github.com/apache/arrow/pull/50158</a></p>
    <p>Link to the results colab notebook - <a href="https://colab.research.google.com/drive/1TsxFkBSI_Iq0hfXEwNDs_D24acr3yxdC?usp=sharing">https://colab.research.google.com/drive/1TsxFkBSI_Iq0hfXEwNDs_D24acr3yxdC?usp=sharing</a></p>
    <p>Orchestrating and benchmarking repo - <a href="https://github.com/OmBiradar/pyarrow-lincc-fw-openastronomy-gsoc26">https://github.com/OmBiradar/pyarrow-lincc-fw-openastronomy-gsoc26</a></p>

