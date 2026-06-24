.. title: Community Bonding and week 1 & 2
.. slug:
.. date: 2026-06-09 03:27:42 
.. tags: lincc-fw
.. author: Om Biradar
.. link: https://imporving-pyarrow-for-nested-structures.hashnode.dev/community-bonding-and-week-1-2
.. description:
.. category: gsoc2026


.. raw:: html

    <p>The start was amazing! The community bonding was really great. I got to meet the mentors, get to know the whole organization structure of OpenAstronomy and LINCC frameworks, the work they do, the people and facilities associated with it, the ways PyArrow and nested-pandas was being used in astronomy and the expectations they had form the internship. They offered to help me through tasks if I could not do it on my own along with some content to look through to get a deeper understanding of the project. I attended the Apache Arrow community meeting with my mentor to introduce the project them and get their views on it. They were really helpful and even suggested certain thing to do to improve the final PR.</p>
    <p>Week 1 and 2 were spent on improving the parallel reading of parquet files, which was successfully implemented by me. The benchmarking of these performance changes proved quite hard, as this would require the following, starting with the main arrow branch:</p>
    <ol>
    <!-- TEASER_END -->
    <li><p>Building arrow C++ from source</p>
    </li>
    <li><p>Building PyArrow from source</p>
    </li>
    <li><p>Running benchmarking scripts</p>
    </li>
    <li><p>Switching the branch from the main branch and repeating steps 1-3</p>
    </li>
    </ol>
    <p>The time taken to benchmark the changes for all order of magnitude of files proved to be very long, approximately ~140 hours or 6 days. I could speed this up using parallel jobs in github which needed to be configured separately using config settings and matrix github runners. This needed to be done because github sets a timeout of 6 hours on each github action with at max 20 concurrent jobs and a 24 hour auto cancel timeout on jobs in queue. Based on these constraints I had to figure out a way to orchestrate different runners and combine their results for which I used sqlite3.</p>

