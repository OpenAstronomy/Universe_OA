.. title: GSoC 2020: Blog 2 - Parameters and incompatible units
.. slug:
.. date: 2020-06-30 09:54:19 
.. tags: EinsteinPy
.. author: Jyotirmaya Shivottam
.. link: https://dev.to/jes24/gsoc-2020-blog-2-parameters-and-incompatible-units-fb5
.. description:
.. category: gsoc2020


.. raw:: html

    <h2>
    <a href="#progress-so-far" class="anchor">
    </a>
    <!-- TEASER_END -->
    Progress so far...
    </h2>
    
    <p>Over the last two weeks, PR <a href="https://github.com/einsteinpy/einsteinpy/pull/512">#512</a> was finalized and merged into EinsteinPy. With it, the big refactor of the <code>metric</code> module is over. As I had mentioned in my last blog, this PR adds a core structure to the <code>metric</code> module, with the <code>metric.BaseMetric</code> class, and adds some new functionalities, like support for Kerr-Schild Perturbations. Also, 7 issues, big and small, were fixed in this PR, ranging from purely semantic issues to mathematical inaccuracies. One of the important ones was Issue <a href="https://github.com/einsteinpy/einsteinpy/issues/514">#514</a>, the distinction between Rotational Length Parameter,
    
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">α\alpha </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">α</span></span></span></span>
    </span>
    and Dimensionless Spin Parameter,
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">aa </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">a</span></span></span></span>
    </span>
    , which has had a cascade effect across the codebase. It is worth a discussion, as it has led to many changes across the numerical side of EinsteinPy.</p>
    
    
    
    
    <h2>
    <a href="#whats-all-the-fuss-about" class="anchor">
    </a>
    What's all the fuss about?
    </h2>
    
    <p>The expressions for the Rotational Length Parameter,
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">α\alpha </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">α</span></span></span></span>
    </span>
    , and Spin Parameter,
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">aa </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">a</span></span></span></span>
    </span>
    , are as follows:<br>
    
    </p>
    <div class="katex-element">
    <span class="katex-display"><span class="katex"><span class="katex-mathml">α=JMc
    \alpha = \frac{J}{Mc}
    </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">α</span><span class="mspace"></span><span class="mrel">=</span><span class="mspace"></span></span><span class="base"><span class="strut"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="mord"><span class="mord mathdefault">M</span><span class="mord mathdefault">c</span></span></span><span><span class="pstrut"></span><span class="frac-line"></span></span><span><span class="pstrut"></span><span class="mord"><span class="mord mathdefault">J</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span></span>
    </div>
    <br>
    
    <div class="katex-element">
    <span class="katex-display"><span class="katex"><span class="katex-mathml">a=JJMax=JcGM2
    a = \frac{J}{J_{Max}} = \frac{Jc}{GM^2}
    </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">a</span><span class="mspace"></span><span class="mrel">=</span><span class="mspace"></span></span><span class="base"><span class="strut"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="mord"><span class="mord"><span class="mord mathdefault">J</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathdefault mtight">M</span><span class="mord mathdefault mtight">a</span><span class="mord mathdefault mtight">x</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span></span></span></span><span><span class="pstrut"></span><span class="frac-line"></span></span><span><span class="pstrut"></span><span class="mord"><span class="mord mathdefault">J</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace"></span><span class="mrel">=</span><span class="mspace"></span></span><span class="base"><span class="strut"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="mord"><span class="mord mathdefault">G</span><span class="mord"><span class="mord mathdefault">M</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span><span><span class="pstrut"></span><span class="frac-line"></span></span><span><span class="pstrut"></span><span class="mord"><span class="mord mathdefault">J</span><span class="mord mathdefault">c</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span></span>
    </div>
    <br>
    which give us:<br>
    
    <div class="katex-element">
    <span class="katex-display"><span class="katex"><span class="katex-mathml">α=GMc2a
    \boxed{
    \alpha = \frac{GM}{c^2}a
    }
    </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="boxpad"><span class="mord"><span class="mord"><span class="mord mathdefault">α</span><span class="mspace"></span><span class="mrel">=</span><span class="mspace"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="mord"><span class="mord"><span class="mord mathdefault">c</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span><span><span class="pstrut"></span><span class="frac-line"></span></span><span><span class="pstrut"></span><span class="mord"><span class="mord mathdefault">G</span><span class="mord mathdefault">M</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mord mathdefault">a</span></span></span></span></span><span><span class="pstrut"></span><span class="stretchy fbox"></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span></span></span></span></span>
    </div>
    <br>
    Here,
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">J,MJ, M </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">J</span><span class="mpunct">,</span><span class="mspace"></span><span class="mord mathdefault">M</span></span></span></span>
    </span>
    denote the angular momentum and mass of the gravitating body (for example, black holes), respectively, while
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">G,cG, c </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">G</span><span class="mpunct">,</span><span class="mspace"></span><span class="mord mathdefault">c</span></span></span></span>
    </span>
    denote the Gravitational Constant and speed of light in vacuum, respectively. As the expression for
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">aa </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">a</span></span></span></span>
    </span>
    tells us, it is a constraint on the body's angular momentum. It might seem arbitrary at first, as in classical physics, we do not bother with such constraints and
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">JJ </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">J</span></span></span></span>
    </span>
    is not limited. However, in General Relativity, especially in the context of how black holes are formed, or more appropriately, how we hypothesize their formation, we find that, for certain solutions to the Einstein Field Equations, like the Kerr solutions (rotating black hole), a maximum limit needs to be placed on the black hole angular momentum. This is a direct consequence of the efforts to contain the causality-breaking nature of black hole singularities, especially a naked singularity. As the name suggests, naked singularities are not covered by an Event Horizon and so, they would be observable from outside the black hole. This breaks the framework of GR, as no deterministic predictions about the future evolution of spacetime can be made near a singularity. Note that, GR breaks for covered singularities as well, but causality remains intact, because the spacetime within the event horizon is not viewable or approachable from outside. To complicate things further, GR, as is, does not preclude the existence of naked singularities. All of this led to much deliberation on this issue and ultimately, in 1969, Sir Roger Penrose postulated the (Weak) Cosmic Censorship Hypothesis. This hypothesis aims to alleviate the issue with physical singularities by claiming that naked or observable singularities cannot exist in the universe, as the deterministic nature of general relativity will fall apart otherwise. It is worth mentioning that, while this is still a conjecture, we are yet to detect naked singularities through astronomical observations. Also, in order to work in the theoretical framework of GR and make physical predictions using GR, one needs to circumvent the problem of naked singularities and this is where
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">aa </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">a</span></span></span></span>
    </span>
    comes in for rotating black holes, like in the Kerr solution. To ensure that, the black hole singularity has an event horizon, we must constrain
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">JJ </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">J</span></span></span></span>
    </span>
    and this is done by the spin parameter,
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">aa </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">a</span></span></span></span>
    </span>
    . Here, for
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">∣J∣≤GM2c|J| \leq \frac{GM^2}{c} </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord">∣</span><span class="mord mathdefault">J</span><span class="mord">∣</span><span class="mspace"></span><span class="mrel">≤</span><span class="mspace"></span></span><span class="base"><span class="strut"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathdefault mtight">c</span></span></span></span><span><span class="pstrut"></span><span class="frac-line"></span></span><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathdefault mtight">G</span><span class="mord mtight"><span class="mord mathdefault mtight">M</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span>
    </span>
    , the solution has an event horizon, while for
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">∣J∣&gt;GM2c|J| &gt; \frac{GM^2}{c} </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord">∣</span><span class="mord mathdefault">J</span><span class="mord">∣</span><span class="mspace"></span><span class="mrel">&gt;</span><span class="mspace"></span></span><span class="base"><span class="strut"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathdefault mtight">c</span></span></span></span><span><span class="pstrut"></span><span class="frac-line"></span></span><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathdefault mtight">G</span><span class="mord mtight"><span class="mord mathdefault mtight">M</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span>
    </span>
    , the solution possesses naked singularities, which we must exclude, due to reasons discussed above. This condition is obtained by solving for singularities in the Kerr solutions.
    
    <p>As for
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">α\alpha </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">α</span></span></span></span>
    </span>
    , it is a convenient length parameter, that helps in making equations shorter to write.</p>
    
    <p>Physics aside, the issue, as mentioned in <a href="https://github.com/einsteinpy/einsteinpy/issues/514">#514</a>, was that the modules in EinsteinPy do not differentiate between
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">α\alpha </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">α</span></span></span></span>
    </span>
    and
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">aa </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">a</span></span></span></span>
    </span>
    . This is due to the intermixing of Geometrized quantities with that in SI units. In geometrized units,
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">G=c=1G = c = 1 </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">G</span><span class="mspace"></span><span class="mrel">=</span><span class="mspace"></span></span><span class="base"><span class="strut"></span><span class="mord mathdefault">c</span><span class="mspace"></span><span class="mrel">=</span><span class="mspace"></span></span><span class="base"><span class="strut"></span><span class="mord">1</span></span></span></span>
    </span>
    , making
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">α=a=JM\alpha = a = \frac{J}{M} </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">α</span><span class="mspace"></span><span class="mrel">=</span><span class="mspace"></span></span><span class="base"><span class="strut"></span><span class="mord mathdefault">a</span><span class="mspace"></span><span class="mrel">=</span><span class="mspace"></span></span><span class="base"><span class="strut"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathdefault mtight">M</span></span></span></span><span><span class="pstrut"></span><span class="frac-line"></span></span><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathdefault mtight">J</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span>
    </span>
    . However, in SI, this is not the case. EinsteinPy works purely in SI and this issue is an artifact from the changes around unit conversions. This issue has been fixed now, after <a href="https://github.com/einsteinpy/einsteinpy/pull/512">#512</a>, with
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">aa </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">a</span></span></span></span>
    </span>
    being one of the defining parameters in rotating spacetimes, while
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">α\alpha </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">α</span></span></span></span>
    </span>
    is calculated using
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">aa </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">a</span></span></span></span>
    </span>
    .</p>
    
    <p>As I mentioned earlier, this issue has caused a ripple effect across the numerical side of EinsteinPy. It has highlighted some problems, around systems of unit, in the definition of a few core methods in the <code>metric</code> classes, as well as the <code>coordinates</code> module.</p>
    
    <h2>
    <a href="#until-next-time" class="anchor">
    </a>
    Until next time...
    </h2>
    
    <p>I am currently working on fixing the aforementioned issues, as well as refactoring the <code>coordinates</code> module. To be specific, I am working on adding support for 4-Vector calculations and Kerr-Schild coordinates to the <code>coordinates</code> module. The latter would make use of the Kerr-Schild perturbation functionality of the <code>metric</code> module and help in modularizing the definition of new metric classes. I will discuss Kerr-Schild perturbations and the so-called Kerr-Schild form of the metric tensor in my next blog. </p>
    
    
    
    
    <p>In the meantime, here's a piece of trivia, related to the Cosmic Censorship Hypothesis.</p>
    
    <blockquote>
    <p>In 1991, John Preskill and Kip Thorne bet against Stephen Hawking that the hypothesis was false. Hawking conceded the bet in 1997, due to the discovery of some special situations, that violated the hypothesis, which he characterized as "technicalities". Hawking later reformulated the bet to exclude those technicalities. The revised bet is still open, with the prize being "clothing to cover the winner's nakedness".</p>
    </blockquote>
    
    <p>The description of the original bet can be found <a href="http://www.theory.caltech.edu/people/preskill/old_naked_bet.html">here</a>, while that of the new bet can be found <a href="http://www.theory.caltech.edu/people/preskill/new_naked_bet.html">here</a>.</p>

