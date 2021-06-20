.. title: Chapter 0: Prologue
.. slug:
.. date: 2021-06-06 22:40:32 
.. tags: radis
.. author: anandxkumar
.. link: https://anandkumar-blog.netlify.app/1/
.. description:
.. category: gsoc2021


.. raw:: html

    <p>Hi There and Namaste! This is going to be the second blog and first blog related to GSoC where I will be sharing my experience Community Bonding Period Experience with <b>Radis</b>. Before moving ahead lets learn about GSoC and my perspective about it.</p>
    <h2>Google Summer of Code</h2>
    <p>GSoC or the way I like to say it <strong>(Great Summer Opportunity to Code ;)</strong> is a program conducted and funded by Google to promote college students around the world to engage with Open Source Community and contribute to the organization for a tenure of 3 months. In the process, code is created and released for the world to see and use. But the main aim of GSoC is to promote students to stick to the organizations and help to grow the Open Source Community. This is a great initiative by Google that brings thousands of students every year and help them get an opportunity to peek into the world of open source development, learn new skills and also get compensated for the work, quite generously.</p>
    <!-- TEASER_END -->
    <p>I remember during second year of my college, it was around end of March and my roommate was applying for GSoC and I was like what is this program? There I got to know about it but since the deadline was near I was afraid of doing all the stuffs in a week of time, so I didn’t apply for it. Fast forwarding to next year, I was prepared enough this time and I feel priviledged to be a part of GSoC as part of OpenAstronomy. </p>
    <h2>My GSoC Project</h2>
    <p>I’m part of <b><a href="https://github.com/radis/radis">Radis</a></b> organization which is a sub-org of <a href="https://github.com/OpenAstronomy">OpenAstronomy</a>. Radis is a fast line-by-line code used to synthesize high-resolution infrared molecular
    spectra and a post-processing library to analyze spectral lines. It can synthesize absorption
    and emission spectrum for multiple molecular species at both equilibrium and
    non-equilibrium conditions.<br />
    Radis computes every spectral line (absorption/emission) from the molecule considering
    the effect of parameters like Temperature, Pressure. Due to these parameters, we don’t get
    a discrete line but rather a shape with a width. This is called line broadening and for any spectral synthesis code, this is the bottleneck step. Ok let us C what my GSoC project is all about! <br /></p>
    <p>Radis has 2 methods to calculate the lineshape of lines.<br />
    ● Legacy Method<br />
    ● DLM Method<br /></p>
    <p>The goal of this project is to derive an equation comprising all parameters that affect the
    performance for calculating Voigt broadening by running several benchmarks for different
    parameters involved in the calculation of lineshapes to check their significance in
    computation time. Then we need to find the critical value for the derived equation (<code class="language-text">Rc</code>)
    which will tell us which optimization technique to select based on the computed <code class="language-text">R</code> value in
    <b>calc_spectrum()</b>. An <code class="language-text">optimization = &quot;auto&quot;</code> will be added that will choose the best method based on the parameters provided.</p>
    <h2>Community Bonding Period</h2>
    <p>The first phase of GSoC is the <b>Community Bonding Period</b> which is a 3 weeks long period. Its main aim is allow the student to get familiar with the community and the codebase. It serves as a warm-up period before the coding period. The first thing I did was that I went though the original Radis <a href="https://www.sciencedirect.com/science/article/abs/pii/S0022407318305867?via%3Dihub">paper</a> and also the DLM implementation <a href="https://ui.adsabs.harvard.edu/abs/2021JQSRT.26107476V/abstract">paper</a> because our project objective is based on these 2 implementations. It helped me understand the main purpose of RADIS, its architecture and the science behind different steps of both equilibrium and non-equilibrium spectrum, though I have to accept these papers are way too technical for me :p (Complex Spectroscopy related formulas).<br /> I believed inorder to get myself ready for the coding period, I shall focus on solving some related issues to make me more familiar with the codebase.<br /></p>
    <p>In order to compute any spectrum we need to determine several parameters like: minimum-maximum wavenumber, molecule, Temperature of gas, mole fraction, wstep, etc.<br />
    <code class="language-text">wstep</code> determines the wavenumber grid’s resolution. Smaller the value, higher the resolution and vice-versa. By default radis uses <code class="language-text">wstep=0.01</code>. You can manually set the wstep value in <b>calc_spectrum()</b> and <strong>SpectrumFactory</strong>. To get more accurate result you can further reduce the value, and to increase the performance you can increase the value.</p>
    <p>Based on wstep, it will determine the number of gridpoints per linewidth. To make sure that there are enough gridpoints, Radis will raise an <strong>Accuracy Warning</strong>. If number of gridpoints are less than <code class="language-text">GRIDPOINTS_PER_LINEWIDTH_WARN_THRESHOLD</code> and raises an <strong>Accuracy Error</strong> if number of gridpoints are less than <code class="language-text">GRIDPOINTS_PER_LINEWIDTH_ERROR_THRESHOLD</code>.</p>
    <p>So inorder to select the optimum value of <code class="language-text">wstep</code> I had to refactor the codebase such that we could compute the minimum FWHM (<code class="language-text">min_width</code>) value after calculating the HWHM of all lines and and set <code class="language-text">wstep = min_width / GRIDPOINTS_PER_LINEWIDTH_WARN_THRESHOLD</code>. All <code class="language-text">wstep</code> dependent parameters had to be refactored to make sure they are not being called before the calculating <code class="language-text">min_width</code>. At the end this feature was successfully merged in the develop branch of Radis and now users can use <code class="language-text">wstep = &quot;auto&quot;</code> to automatically get the optimal value of <code class="language-text">wstep</code>. This feature will be available from version <b>0.9.30</b>. Here is the <a href="https://github.com/radis/radis/pull/271">link</a> of the merged PR.</p>
    <p>In short, the Community Bonding Period has been great and I have learned alot about Radis during this time. In the next 2 weeks I will be focussing on building a benchmarking framework and run various benchmarks for both Legacy and DLM method and determine the most influential paramters for performance.</p>
    <p>I’m very excited for the upcoming months. I know that this summer is going to be a life long experience and I’m really looking forward to do amazing things for the community and want to thank Google, OpenAstronomy, Radis and my mentors <a href="https://github.com/erwanp">Erwan Pannier</a>, <a href="https://github.com/dcmvdbekerom">Dirk van den Bekerom</a> and <a href="https://github.com/pkj-m">Pankaj Mishra</a> for this opportunity.
    I’m ready for this amazing adventure.</p>
    <p align="center">
    <b>LETS DO THIS</b><br />
    <img src="https://anandkumar-blog.netlify.app/2b4e6a4b663f4bc49d559484b8dd37b1/Start.gif" /><br />
    ps: Am a huge Spiderman Fan :p
    </p>

