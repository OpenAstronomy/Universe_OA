.. title: GSoC Blog #0
.. slug:
.. date: 2022-06-14 17:14:10 
.. tags: stingray
.. author: AMAN PANDEY
.. link: https://medium.com/@aman_p/gsoc-blog-0-8f65bf844cd8?source=rss-1bafed5b4c37------2
.. description:
.. category: gsoc2022


.. raw:: html

    <p>With the end of the community bonding period, my GSoC 2022 project has officially started. It will be an exciting journey, and I will be documenting my experience and work in a series of blogs in the future.</p>
    <p>I’m <strong>Aman Pandey, </strong>and this blog is about my introduction to open source and learning Julia that lead me to take part in the Google Summer of Code for Open Astronomy, juliaAstro and Stingray to be specific. I also enlist my community bonding period work and what I intend to do next week.</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/680/1*dfjiDfMcY8h9eEOySAnxbA.jpeg" /></figure><p><strong>My journey to Open Source</strong></p>
    <!-- TEASER_END -->
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/310/1*6cUCFKPtaiyl4vQ3Q1YkLA.jpeg" /></figure><p>My intro to the open-source world was through a game called TwilioQuest. It had a level where I had to configure git and GitHub and then contribute to their Open Pixel Art repo by changing a JSON file. It was fun, but I wasn’t fully aware of the open-source community until I started understanding the Godot engine ( A 3D game engine in C++). I followed the instructions for compiling it on Windows using VSCode, but I met an issue. I couldn’t reproduce the instructions of the doc and created a pull request to change the docs when I found the solution. The community was very helpful, and after some suggestions, I could finally merge my first PR!</p>
    <p>Through the internet, I learned about GSoC as a program to foster an open-source culture among students, especially to guide newcomers to contribute code and engage with the community. I started searching for organizations that interested me and found OpenAstronomy (I was fascinated by the different projects going on in the organization). A thorough search made me sure to start learning Julia to contribute to the “Spectral Timing in Julia” project. While trying to contribute, I was fascinated by the structure of a Julia program and its excellent features like multiple dispatch and Abstract and Concrete Type System. Part of it was due to the incredible guidance by one of the project’s mentors, <strong>Mosè Giordano, </strong>which shows the role of community while developing open-source software. I was thrilled when my project was announced as selected; it will be a great summer this year!</p>
    <p><strong>Community Bonding Period</strong></p>
    <p>My project involves porting the Stingray package of python to Julia, which consists of different time series analysis methods to deal with periodicities in X-Ray signals coming from massive celestial objects. I started the period by learning about different methods implemented in the python package like creating periodograms, normalizing them, and using them for data types like NumPy iterables or custom objects like LightCurves and EventLists. At the same time, I focused on learning about Julia and its best practices and understanding how to write clean, high-performance, and documented code.</p>
    <p>I committed my first PR for the project by initializing the package and adding documentation and continuous integration (CI) support. I then looked forward to porting the fourier.py file and implementing tests alongside it and was reasonably successful in it. In my opinion, it was a significant period; I discussed many exciting things with the mentors, like using DataFrames and generating distribution to test the periodograms with array inputs. I myself worked on writing type-stable code (which I was introduced to while working on a PR for another juliaAstro package, AstroLib) and diving deep into topics like dispatch and type systems, which are the testament that open source contribution can enhance your developer skills multi-folds as these topics are not restricted to any specific programming language.</p>
    <p>An example of type-unstable function :</p>
    <pre>function foo()<br />    x = 1<br />    for i = 1:10<br />        x /= rand()<br />    end<br />    return x<br />end</pre><p><strong>Upcoming Week</strong></p>
    <p>I intend to implement the utility functions and fourier.py file of Stingray in Julia to create periodograms and cross spectra from tables. Then, I will move on to implement the light curves and event lists, through which, in the future, I will be able to create full-fledged periodograms and cross-spectra. Proper Testing and performance-related aspects will be sincerely followed throughout the project.</p>
    <p>I am excited about this summer and expect to learn much about software development, open-source, and the programming community throughout this journey. Thanks to Google, Open Astronomy, juliaAstro, Stingray, and my mentors <a href="https://github.com/matteobachetti">Matteo Bachetti</a> and <a href="https://github.com/giordano">Mosè Giordano</a> for providing me this opportunity. Let the coding phase start!</p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=8f65bf844cd8" width="1" />

