.. title: The problems in venv
.. slug:
.. date: 2024-05-24 08:56:00 
.. tags: stingray
.. author: Kartik Mandar
.. link: https://gsoc2024.kartikmandar.com/2024/05/the-problems-in-venv.html
.. description:
.. category: gsoc2024


.. raw:: html

    <p>&nbsp;So earlier during pre-gsoc period I had setup my environment in base itself and then just a few weeks back I shifted to python venv as the Hendrics dependencies were clashing with Stingray's.&nbsp;<br />After setting up the venv specifically for stingray so that I can test it's functions and API, I went on to explore the different libraries to plot the data we are generating. Holoviz seemed a good option and installation was a breeze but these packages were specifically in conda. As a result I was not able to access the packages from the venv at all, as it had its own conda environment to run from. Now I thought why not make a docker and work in base from there.&nbsp;</p>
    <p>But I came to the conclusion that it's an overkill solution and would be too much of a hassle. Later on,&nbsp; I went on to make a fresh conda environment for stingray too and currently am in this process.</p>
    <!-- TEASER_END -->

