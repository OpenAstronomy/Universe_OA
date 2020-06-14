.. title: GSoC 2020: Blog 1 - Beginning of Coding Period
.. slug:
.. date: 2020-06-13 18:20:19 
.. tags: EinsteinPy
.. author: Jyotirmaya Shivottam
.. link: https://dev.to/jes24/gsoc-2020-blog-1-beginning-of-coding-period-4338
.. description:
.. category: gsoc2020


.. raw:: html

    <p>So the community bonding period of GSoC has ended and the coding period is officially underway. In my last blogpost, I had outlined the basic principles of General Relativity that go into my project. I had also mentioned, that the next blog will have details about the coding process. However, things had to be slowed down considerably, due to the announcement of closure of my academic session and some logistical issues. This has also affected my blog schedule, as I could not work on a blog, that was supposed to be up 2 weeks ago. However, I am pleased to inform that all the issues are sorted out now, leaving the rest of the summer free for me to delve into the project. Whew. I am also exceedingly grateful to my mentors, who have been understanding throughout. As for details on the code implementation for my project, I have decided to break it up across the blogs, as "Progress Reports" (bland, I know), in order to provide a better understanding of both what I am working on and my approach to it. So, read on.</p>
    
    <h2>
    <!-- TEASER_END -->
    <a href="#progress-so-far" class="anchor">
    </a>
    Progress so far...
    </h2>
    
    <p>Over the last few discussions with my GSoC mentors, we have discovered some logical bottlenecks in some of the EinsteinPy modules, especially the way the <code>metric</code> &amp; <code>utils</code> modules work at the moment. Currently, the <code>utils</code> module stores most of the necessary functions required to form a <code>metric</code> class, while the <code>metric</code> module lacks support for user-defined metrics. It also handles the calculation of particle trajectory, which logically belongs inside a <code>geodesic</code> module. Since my project is on Null Geodesics, these issues are major obstacles, that must be overcome, before the work on adding support for Null Geodesic calculation begins.</p>
    
    <p>As such, I am refactoring these modules, so that we have logical cohesion across EinsteinPy, whilst also adding some new features, like a brand new <code>metric</code> class, that supports defining arbitrary metrics and also adding first order linear perturbations to the metric, written in Kerr-Schild form. I have also grouped together the utility functions present in <code>utils</code> in <code>metric</code> itself. These changes can be followed at the PR link, <a href="https://github.com/einsteinpy/einsteinpy/pull/512">here</a>. At the moment, I am reusing some of the old tests and writing some new ones for the new features. I hope to see this PR clear all tests and be merged soon.</p>
    
    <h2>
    <a href="#until-next-time" class="anchor">
    </a>
    Until next time...
    </h2>
    
    <p>After <code>metric</code>, comes the <code>coordinates</code> module, which will see some changes and code rearrangements too, albeit not as much as <code>metric</code> and <code>utils</code>. The basic work on this has already started and after the first PR is merged, I will open another PR with these changes.</p>
    
    <p>We have lost around 2 weeks, due to the aforementioned issues on my side. Therefore, it is contingent on me to accelerate the pace of development now. Over the next few weeks, we should see some cool new feature additions to EinsteinPy. I will be detailing them here, as we proceed with the project.</p>

