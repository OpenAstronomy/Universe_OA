.. title: My GSoC Journey - Part 1
.. slug:
.. date: 2022-05-29 00:00:00 
.. tags: gnuastro
.. author: Jash Shah
.. link: https://jash_shah.github.io/Blogs/2022/05/29/GSoC-What_Why_How.html
.. description:
.. category: gsoc2022


.. raw:: html

    <h2 id="what-is-google-summer-of-code-gsoc">What Is Google Summer of Code (GSoC)</h2>
    <p><code class="language-plaintext highlighter-rouge">Google Summer of Code</code>(shortly known as GSoC) is a global, online program(organized by…..you guessed it! Google) focused on bringing new contributors into open source software development. GSoC Contributors work with an open source organization on a 12+ week programming project under the guidance of mentors. You can think of GSoC as an incubator for nurturing future open source developers.</p>
    
    <!-- TEASER_END -->
    <h3 id="why-is-open-source-important">Why is Open Source important?</h3>
    <p>Open source software is code that is designed to be publicly accessible—<strong>anyone can see, modify, and distribute the code</strong> as they see fit. This makes it ideal for developers who want to contribute towards making a <em>small but significant change</em> in the world of softwares, but might lack the credentials, time, resources or just plain will to go through the grueling process of first getting employed by a software firm. Open source organiztions, are genrally helmed by engineers, who are <em>extremely practical</em>(even to a fault sometimes ;) ). Thus, Open Source slices through all the social constructs and procedural beuracracy invovled in getting a job in a software firm, by giving anyone with an idea and the will+ability to bring that idea to fruition, a chance to contribute to these softwares, thus working towards making it a better software for everyone.
    <img alt="Matrix Open Source Software Meme" src="https://images-cdn.9gag.com/photo/aM4jpy6_700b.jpg" /></p>
    
    <h2 id="why-did-i-participate-in-gsoc">Why did I participate in GSoC?</h2>
    <p>Well…there a bunch of reasons for this:</p>
    <ul>
    <li>It seemed like <code class="language-plaintext highlighter-rouge">the natural next step</code> in my journey as a Computer Engineer. I have just finished my IV Semester, got a few good projects under my belt, taken part(&amp; won) in a few competitions, ad GSoC feels like the right way to now start getting into the world of free software!</li>
    <li><code class="language-plaintext highlighter-rouge">Peer Pressure 🙃 : The Good Kind</code><br />
    My college (<a href="https://vjti.ac.in/">VJTI, Matunga</a>) had a staggering <strong>24 GSoC’ers in 2022</strong>. 21 of these were from <a href="https://github.com/SRA-VJTI">SRA(Society of Robotics and Automation)</a> a club that I’ve been a very active part of. Hence, being surrounded by people who were also working towards getting accepted in GSoC definetly helped me in doing the same.</li>
    <li>I felt the <code class="language-plaintext highlighter-rouge">need(nay obligation) to contribute to the open source softwares that had helped ME</code> in my few budding years of being a Computer Engineer. When you get to use and interact with the communities of something as good as Linux, OpenCV, ROS, VLC, React for free; you will feel the same way, trust me ;)</li>
    <li>The prospect of <code class="language-plaintext highlighter-rouge">being mentored</code> by someone, <em>much much more</em> proficient than me at such an early stage, while also getting paid to do so !!</li>
    <li><code class="language-plaintext highlighter-rouge">College Work just doesn't seem enough</code><br />
    This might be exclusive to just me, but I was not satisfied with the challenge offered by the assignments and projects in my college curriculum. Hence, GSoC also fills that gap of trying out something outside of the normal confines of my college,</li>
    </ul>
    
    <h2 id="how-to-start-with-gsoc">How to start with GSoC?</h2>
    
    <ol>
    <li>
    <p><strong>Find an Organization:</strong><br />
    According to the <a href="https://developers.google.com/open-source/gsoc/timeline">timeline of GSoC 22’</a>, the organizations were announced on <em>7th March, 2022</em>. However, there are a few legacy organiztions (like CERN-HSF, Red Hat, OpenCV, Julia, etc.) that have been participating in GSoC for long, hence aiming for one of these orgs(if you like them!) and starting even as early as Januaray (i.e ~4 months before the application period) is a good idea. It will also give you time to browse various orgs and settle into their communities. Although because of some other commitments, I was not able to start properly working on GSoC till April (i.e. a month before the application period :0 ). So, <em>don’t do as I do but do as I say</em>.<br />
    The org which I chose was <a href="https://www.gnu.org/savannah-checkouts/gnu/gnuastro/gnuastro.html">Gnuastro</a> which is part of the umbrella org <a href="https://openastronomy.org/">openastronomy</a></p>
    </li>
    <li>
    <p><strong>Finding a Project:</strong><br />
    Every org participating in GSoC will have an ideas page with many prospect ideas, also some unfinished ideas(or ideas requiring enhancement) from previous GSoC’s. I combed through the <a href="https://openastronomy.org/gsoc/gsoc2022/#/projects">ideas page of openastronomy</a> and found a project that piqued my interest called <a href="https://openastronomy.org/gsoc/gsoc2022/#/projects?project=gnuastro_library_in_python">GNUAstro Library in Python</a>.</p>
    </li>
    <li>
    <p><strong>Finding my Mentor:</strong><br />
    I followed the links to the Element(Matrix) channel of my org, where I introduced myself and was greeted warmly by my mentor with help regarding the <a href="https://savannah.gnu.org/support/index.php?110613#comment0">GSoC Checklist</a> that Gnuastro had. This step might be different for different orgs. Some may have you commit some code my creating a Pull Request(PR), some have you solve tasks, some may have no <em>necessary</em> criteria except for a proposal. The aspect common to all orgs/mentors is <code class="language-plaintext highlighter-rouge">showing your enthusiasm for the project, and to learn</code>. Also <strong>having a few(or even one in my case) commits to the org before submitting the proposal</strong> will go a long way!</p>
    </li>
    <li>
    <p><strong>Making the right proposal</strong><br />
    The proposal submission deadline in GSoC 22’ was <strong>19th April</strong>. So I had less than a month post joining my org to submit a proposal. To be frank, this was a tough and hectic period(amplified more by all my friends also being in the same state). This is where the helpfulness of my mentor and the push from my college seniors really pushed me. I built my proposal by first carefully studying previous year proposals, while these are not publicly available (and some GSoCers even refuse to share them), there are many great resources maintained by GSoCers to help the new aspirants. I used the <a href="https://github.com/Google-Summer-of-Code-Archive/gsoc-proposals-archive">Proposal Archive</a> to study different proposals, for varied orgs, theor structure, content, concisivness and balance between technical and theoretical language.</p>
    </li>
    </ol>
    
    <h2 id="conclusion">Conclusion</h2>
    <p>Luckily, I must’ve done something right, as I did get selected for Gnuastro(openastronomy) in GSoC. And will now be spending my summer(12 weeks) contributing to the same under the guidance of my mentor!</p>

