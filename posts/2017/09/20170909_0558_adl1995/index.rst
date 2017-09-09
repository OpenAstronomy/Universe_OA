.. title: Parallel tile fetching and CPU-and-memory statistics
.. slug:
.. date: 2017-09-09 05:58:00 
.. tags: Astropy
.. author: Adeel Ahmad
.. link: https://adl1995.github.io/parallel-tile-fetching-and-cpu-and-memory-statistics.html
.. description:
.. category: gsoc2017

The hips package now supports parallel tile fetching. The user can achieve this either using urllib or aiohttp.
In case of aiohttp, the fetched tile data is coupled with HipsTileMeta to create a HipsTile object. This ensures there is no misalignment of tile data, otherwise, tiles could be swapped du `...READ MORE... <https://adl1995.github.io/parallel-tile-fetching-and-cpu-and-memory-statistics.html>`__

