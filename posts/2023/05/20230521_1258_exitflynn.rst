.. title: Getting Selected As A GSoC student at SunPy
.. slug:
.. date: 2023-05-21 12:58:10 
.. tags: SunPy
.. author: exitflynn
.. link: https://exitflynn.github.io/blog/posts/gsoc-acceptance-speech/
.. description:
.. category: gsoc2023


.. raw:: html

    <h1 id="what-is-the-google-summer-of-code">What is The Google Summer of Code?
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#what-is-the-google-summer-of-code">
    <!-- TEASER_END -->
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h1><p>It is a program by Google for promoting students to contribute to open-source communities.
    It is also a  G R E A T  opportunity for us to work on projects with such big impact. I&rsquo;m so glad I came to know about it. I loved that I could get this opportunity to work with people involved in developing software that is used by many.
    Now one could argue that that&rsquo;s the opportunity Open-Source provides in general, which is true. It&rsquo;s difficult to admit but I did need that initial push, some motivating factor to <em>truly</em> make the effort and get my hands wet with contributing to an open-source project. However it&rsquo;s as they say, the beginning&rsquo;s the hardest part and that once you start contributing it becomes so much more easy to keep going. I think they&rsquo;ve done a great job at incentivising Open-Source contributions.</p>
    <h1 id="choosing-an-org">Choosing an Org
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#choosing-an-org">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h1><p>A lot of Organisations participate in GSoC. I had worked on a couple of #good-first-issues on a few projects before this period and had achieved that level of confidence where the language / tech-stack wasn&rsquo;t the deciding factor for me anymore but it was now the project idea / the community.
    I <strong>love</strong> Astronomy and feel quite strongly about it. I am super-curious about how I can use my skills / to-be skills in tech in the field of Astronomy, some sort of an intersection of the two would actually be one of the most meaningful and enjoyable work I could find for myself.
    Naturally, I looked into <strong>OpenAstronomy</strong> as a GSoC org.
    I&rsquo;ve seen a lot of people prioritising those organisations which make for nicer addition to a resume from a product-based tech companies pov and it indeed <em>is</em> a very smart way to go about it to be honest but I decided that I didn&rsquo;t want to miss this unique opportunity to work on something I had wanted to do since a long time.
    Under the sub-orgs for OpenAstronomy, I found <strong>SunPy</strong>.</p>
    <h1 id="first-experience-with-sunpy">First Experience with SunPy
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#first-experience-with-sunpy">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h1><p>Now, SunPy is a python library relating to solar physics. Though heliophysics wasn&rsquo;t exactly something that I thought of when thinking of astrophysics or space-stuff, I was <em>really</em> impressed by how active and supportive the community is. Besides, I found myself interested in the networking side of things more than the solar-physics stuff anyways as for now.</p>
    <p>While first going through the issues I came across one which included <a href="https://github.com/sunpy/sunpy/issues/6692">detecting gzipped files from more than just the extension</a> (via file-signatures / magic-bytes). I love when my familairity with using linux-based systems comes into play during development and I felt the issue to be quite approachable. During the PR Review, I remember going through the documentation for python&rsquo;s <code>gzip</code> module to verify that it doesn&rsquo;t need to decompress a whole gzipped file and that we could decompress just enough to get the first couple of bits which include the file-signature (since otherwise it&rsquo;d mean way too much overhead for the solution to be practical) and information on that is <em>not</em> as easily available on the web as I&rsquo;d like.</p>
    <h1 id="subsequent-experience">Subsequent Experience
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#subsequent-experience">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h1><p>I kept on making code-contributions which I felt approachable for some parts of January and February. And then I got a bit busy due to some health-reasons and college and organsing OSDHack &lsquo;23 (I&rsquo;ll totally write a blog-post on that later, it was such a nice success). I was a bit apprehensive because I was also looking forward to participate in the Google Summer of Code as a SunPy contributor and I didn&rsquo;t want to give off the wrong impression so I wrote a (not)brief text to <a href="https://github.com/Nabobalis">Nabil</a> who was super-supportive. When the proposal submission period came around, it wasn&rsquo;t the most ideal process since I ended up having to make the proposal in the last 2 days. Thankfully again, the community is super responsive and I reached out to both Nabil and <a href="https://github.com/wtbarnes">Will</a> for some feedback on my proposal and they both replied immediately.</p>
    <h1 id="contributing-to-open-source-is-goated">Contributing to Open-Source is GOATed
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#contributing-to-open-source-is-goated">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h1><p>People in tech / software development should actually be talking about this so much more than they are. Some of the things that come to my mind right now are:</p>
    <h2 id="its-a-great-way-to-learn-stuff">It&rsquo;s a great way to learn stuff
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#its-a-great-way-to-learn-stuff">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h2><p>One of the main factors why I think people have a hard time contributing is that they think &ldquo;I can&rsquo;t contribute here because I don&rsquo;t know nearly enough tech to do stuff&rdquo;. The thing with being involved in this form of software development is that it gets you used to learning on the fly which is central to software development and doing well in any field, tbh.</p>
    <p>Contributing to big open-source projects helped me gained TREMENDOUS self-confidence. I could look at any issue on any repo now, and never think that it&rsquo;s un-doable. No matter what domain or what language the project is in, it&rsquo;s only a question of how much time it&rsquo;d take to get through the relevant documentation and concepts. This is certainly a long way from &ldquo;I can&rsquo;t do $#!+ in this codebase if my life depended on it, it scares me&rdquo; and I&rsquo;m very much glad I could have this experience.</p>
    <h2 id="the-best-practices-ever">The best practices ever
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#the-best-practices-ever">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h2><p>You get to learn how to write well-tested, well-documented and maintainable Production-Ready code following the best software development practices.</p>
    <h2 id="you-get-to-choose-what-you-want-to-work-on">You get to choose what you <em>want</em> to work on
    <span>
    <a href="https://exitflynn.github.io/blog/tags/gsoc/index.xml#you-get-to-choose-what-you-want-to-work-on">
    <svg height="100%" viewBox="0 0 28 23" width="19" xmlns="http://www.w3.org/2000/svg"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" fill="none" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2"></svg>
    </a>
    </span>
    </h2><p>YEP! And most of the communities would love to have you work on it, that&rsquo;s such an exciting thing if you ask me.</p>
    <p>(this post is a bit rough around the edges, I definitely want to add stuff to it but owing to my exams right now I&rsquo;ll get to it at some later point of time, thanks for reading!)</p>

