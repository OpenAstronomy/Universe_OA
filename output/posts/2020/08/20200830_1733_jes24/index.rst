.. title: GSoC 2020: Blog 5 - Adding Kerr Null Geodesics functionality to EinsteinPy
.. slug:
.. date: 2020-08-30 17:33:57 
.. tags: EinsteinPy
.. author: Jyotirmaya Shivottam
.. link: https://dev.to/jes24/gsoc-2020-blog-5-adding-kerr-null-geodesics-functionality-to-einsteinpy-2ocj
.. description:
.. category: gsoc2020


.. raw:: html

    <p>Null Geodesics functionality has been implemented into EinsteinPy, with PR<a href="https://github.com/einsteinpy/einsteinpy/pull/527">#527</a>, having been merged 🎉🎉. I apologize for no blogs in the past 3 weeks. There was a COVID situation here, that required multiple tests and isolation and all that it entails. This led to me foregoing an entire week. And, when that had settled, I had to take the call on abandoning the plan of numerically integrating the Geodesics equations, due to the massive error accumulation, as discussed in my last blog. A confusing fact about that, was that <em>Mathematica</em> could still keep the error build-up to a minimum, while <em>Python</em> simply could not, even with adaptive and symplectic schemes. But the symplectic schemes did bring the error down, by around 2 orders of magnitude, which gave me the idea to take a Hamiltonian approach, which would increase the number of ODEs to solve, but drop the order by 1. And, as it turns out, the Kerr Hamiltonian is separable (Carter, 1968a [1]), which makes the implementation even simpler. In this blog, I will be discussing this approach, which has finally led to proper geodesic calculations. I have also included some plots (and a cool animation) for Kerr &amp; Schwarzschild Null-like (and Time-like) geodesics.</p>
    
    <h2>
    <!-- TEASER_END -->
    <a href="#some-physics" class="anchor">
    </a>
    Some Physics...
    </h2>
    
    <p>In Chapter 33 of <em>Gravitation</em> [2], the authors expound on Carter's seminal paper from 1968, titled, "<em>Global Structure of the Kerr Family of Gravitational Fields</em>", and present some nice results from it, one of which is a derivation of the Kerr (super-)Hamiltonian, which can be written as follows (in the <em>M</em>-Unit system (
    
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">G=c=M=1G = c = M = 1</span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">G</span><span class="mspace"></span><span class="mrel">=</span><span class="mspace"></span></span><span class="base"><span class="strut"></span><span class="mord mathdefault">c</span><span class="mspace"></span><span class="mrel">=</span><span class="mspace"></span></span><span class="base"><span class="strut"></span><span class="mord mathdefault">M</span><span class="mspace"></span><span class="mrel">=</span><span class="mspace"></span></span><span class="base"><span class="strut"></span><span class="mord">1</span></span></span></span>
    </span>
    ):<br>
    
    </p>
    <div class="katex-element">
    <span class="katex-display"><span class="katex"><span class="katex-mathml">H=−(a4(E2−2pr2)−8aELr−2r(pθ2(−2+r)+pr2(−2+r)2r−E2r3)+a2(2L2−2pθ2−4pr2(−2+r)r+E2r(2+3r))+(a2+(−2+r)r)(a2E2cos⁡2θ−2L2csc⁡θ2)4(a2+(−2+r)r)(r2+a2cos⁡θ2))
    \mathcal{H} = -\frac{(a^4 (E^2 - 2 p_r^2) - 8 a E L r - 2 r (p_\theta^2 (-2 + r) + p_r^2 (-2 + r)^2 r - E^2 r^3) + a^2 (2 L^2 - 2 p_\theta^2 - 4 p_r^2 (-2 + r) r + E^2 r (2 + 3 r)) + (a^2 + (-2 + r) r) (a^2 E^2 \cos 2\theta - 2 L^2 \csc\theta^2)}{4 (a^2 + (-2 + r) r) (r^2 + a^2 \cos\theta^2))}
    </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord"><span class="mord mathcal">H</span></span><span class="mspace"></span><span class="mrel">=</span><span class="mspace"></span></span><span class="base"><span class="strut"></span><span class="mord">−</span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="mord"><span class="mord">4</span><span class="mopen">(</span><span class="mord"><span class="mord mathdefault">a</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mspace"></span><span class="mbin">+</span><span class="mspace"></span><span class="mopen">(</span><span class="mord">−</span><span class="mord">2</span><span class="mspace"></span><span class="mbin">+</span><span class="mspace"></span><span class="mord mathdefault">r</span><span class="mclose">)</span><span class="mord mathdefault">r</span><span class="mclose">)</span><span class="mopen">(</span><span class="mord"><span class="mord mathdefault">r</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mspace"></span><span class="mbin">+</span><span class="mspace"></span><span class="mord"><span class="mord mathdefault">a</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mspace"></span><span class="mop">cos</span><span class="mspace"></span><span class="mord"><span class="mord mathdefault">θ</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mclose">)</span><span class="mclose">)</span></span></span><span><span class="pstrut"></span><span class="frac-line"></span></span><span><span class="pstrut"></span><span class="mord"><span class="mopen">(</span><span class="mord"><span class="mord mathdefault">a</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">4</span></span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord"><span class="mord mathdefault">E</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mspace"></span><span class="mbin">−</span><span class="mspace"></span><span class="mord">2</span><span class="mord"><span class="mord mathdefault">p</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">r</span></span></span><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span></span><span class="mclose">)</span><span class="mspace"></span><span class="mbin">−</span><span class="mspace"></span><span class="mord">8</span><span class="mord mathdefault">a</span><span class="mord mathdefault">E</span><span class="mord mathdefault">L</span><span class="mord mathdefault">r</span><span class="mspace"></span><span class="mbin">−</span><span class="mspace"></span><span class="mord">2</span><span class="mord mathdefault">r</span><span class="mopen">(</span><span class="mord"><span class="mord mathdefault">p</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">θ</span></span></span><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord">−</span><span class="mord">2</span><span class="mspace"></span><span class="mbin">+</span><span class="mspace"></span><span class="mord mathdefault">r</span><span class="mclose">)</span><span class="mspace"></span><span class="mbin">+</span><span class="mspace"></span><span class="mord"><span class="mord mathdefault">p</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">r</span></span></span><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord">−</span><span class="mord">2</span><span class="mspace"></span><span class="mbin">+</span><span class="mspace"></span><span class="mord mathdefault">r</span><span class="mclose"><span class="mclose">)</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mord mathdefault">r</span><span class="mspace"></span><span class="mbin">−</span><span class="mspace"></span><span class="mord"><span class="mord mathdefault">E</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mord"><span class="mord mathdefault">r</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span></span></span></span></span><span class="mclose">)</span><span class="mspace"></span><span class="mbin">+</span><span class="mspace"></span><span class="mord"><span class="mord mathdefault">a</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord">2</span><span class="mord"><span class="mord mathdefault">L</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mspace"></span><span class="mbin">−</span><span class="mspace"></span><span class="mord">2</span><span class="mord"><span class="mord mathdefault">p</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">θ</span></span></span><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span></span><span class="mspace"></span><span class="mbin">−</span><span class="mspace"></span><span class="mord">4</span><span class="mord"><span class="mord mathdefault">p</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">r</span></span></span><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord">−</span><span class="mord">2</span><span class="mspace"></span><span class="mbin">+</span><span class="mspace"></span><span class="mord mathdefault">r</span><span class="mclose">)</span><span class="mord mathdefault">r</span><span class="mspace"></span><span class="mbin">+</span><span class="mspace"></span><span class="mord"><span class="mord mathdefault">E</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mord mathdefault">r</span><span class="mopen">(</span><span class="mord">2</span><span class="mspace"></span><span class="mbin">+</span><span class="mspace"></span><span class="mord">3</span><span class="mord mathdefault">r</span><span class="mclose">)</span><span class="mclose">)</span><span class="mspace"></span><span class="mbin">+</span><span class="mspace"></span><span class="mopen">(</span><span class="mord"><span class="mord mathdefault">a</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mspace"></span><span class="mbin">+</span><span class="mspace"></span><span class="mopen">(</span><span class="mord">−</span><span class="mord">2</span><span class="mspace"></span><span class="mbin">+</span><span class="mspace"></span><span class="mord mathdefault">r</span><span class="mclose">)</span><span class="mord mathdefault">r</span><span class="mclose">)</span><span class="mopen">(</span><span class="mord"><span class="mord mathdefault">a</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mord"><span class="mord mathdefault">E</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mspace"></span><span class="mop">cos</span><span class="mspace"></span><span class="mord">2</span><span class="mord mathdefault">θ</span><span class="mspace"></span><span class="mbin">−</span><span class="mspace"></span><span class="mord">2</span><span class="mord"><span class="mord mathdefault">L</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mspace"></span><span class="mop">csc</span><span class="mspace"></span><span class="mord"><span class="mord mathdefault">θ</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span></span>
    </div>
    <br>
    where,
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">E=−ptE = -p_t </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">E</span><span class="mspace"></span><span class="mrel">=</span><span class="mspace"></span></span><span class="base"><span class="strut"></span><span class="mord">−</span><span class="mord"><span class="mord mathdefault">p</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">t</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span></span></span></span></span>
    </span>
    and
    <span class="katex-element">
    <span class="katex"><span class="katex-mathml">L=pϕL = p_\phi </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord mathdefault">L</span><span class="mspace"></span><span class="mrel">=</span><span class="mspace"></span></span><span class="base"><span class="strut"></span><span class="mord"><span class="mord mathdefault">p</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">ϕ</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span></span></span></span></span>
    </span>
    are the energy and orbital angular momentum of the test particle, respectively. Note that, this Hamiltonian is for a general test particle, i.e., it can be massive or massless. Then, the dynamical equations of motion can be derived easily, using Hamilton's principle, i.e.:<br>
    
    <div class="katex-element">
    <span class="katex-display"><span class="katex"><span class="katex-mathml">dqidλ=∂H∂pidpidλ=−∂H∂qi
    \frac{\mathrm{d}q_i}{\mathrm{d}\lambda} = \frac{\partial\mathcal{H}}{\partial p_i} \quad
    \frac{\mathrm{d}p_i}{\mathrm{d}\lambda} = -\frac{\partial\mathcal{H}}{\partial q_i}
    </span><span class="katex-html"><span class="base"><span class="strut"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="mord"><span class="mord"><span class="mord mathrm">d</span></span><span class="mord mathdefault">λ</span></span></span><span><span class="pstrut"></span><span class="frac-line"></span></span><span><span class="pstrut"></span><span class="mord"><span class="mord"><span class="mord mathrm">d</span></span><span class="mord"><span class="mord mathdefault">q</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace"></span><span class="mrel">=</span><span class="mspace"></span></span><span class="base"><span class="strut"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="mord"><span class="mord">∂</span><span class="mord"><span class="mord mathdefault">p</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span></span></span></span><span><span class="pstrut"></span><span class="frac-line"></span></span><span><span class="pstrut"></span><span class="mord"><span class="mord">∂</span><span class="mord"><span class="mord mathcal">H</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="mord"><span class="mord"><span class="mord mathrm">d</span></span><span class="mord mathdefault">λ</span></span></span><span><span class="pstrut"></span><span class="frac-line"></span></span><span><span class="pstrut"></span><span class="mord"><span class="mord"><span class="mord mathrm">d</span></span><span class="mord"><span class="mord mathdefault">p</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace"></span><span class="mrel">=</span><span class="mspace"></span></span><span class="base"><span class="strut"></span><span class="mord">−</span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="mord"><span class="mord">∂</span><span class="mord"><span class="mord mathdefault">q</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathdefault mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span></span></span></span><span><span class="pstrut"></span><span class="frac-line"></span></span><span><span class="pstrut"></span><span class="mord"><span class="mord">∂</span><span class="mord"><span class="mord mathcal">H</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span></span>
    </div>
    <br>
    I calculated these in <em>Mathematica</em>, and the corresponding notebooks and the Python code, making use of these, can be accessed <a href="https://github.com/einsteinpy/GSoC-2020/tree/master/Code">here</a>.
    <h2>
    <a href="#and-some-plots" class="anchor">
    </a>
    ...and some plots
    </h2>
    
    <p>Unfortunately, even with these first order ODEs, the error accumulation issue in Python persisted, as can be observed in the plots below. Note that, these results were obtained with a symplectic leapfrog solver, which should, in principal keep the error build-up to a minimum.</p>
    
    <p>
    
    <a href="https://res.cloudinary.com/practicaldev/image/fetch/s--vO8CNKzj--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/bb7nxgooagbji7pd99ho.png" class="article-body-image-wrapper"><img src="https://res.cloudinary.com/practicaldev/image/fetch/s--vO8CNKzj--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/bb7nxgooagbji7pd99ho.png" alt="Python 1"></a>Kerr Null-like Escape
    
    
    <br>
    Although, for shorter integration durations, the results were good.
    
    </p>
    
    
    <img src="https://res.cloudinary.com/practicaldev/image/fetch/s--dfQOcrwn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/o6czz4tal0iteqtjjgsz.png" alt="Python 2">Kerr Null-like Capture
    
    
    
    
    <p>After discussions with my mentors, I looked into other languages, that could help and we chose Julia, due to its excellent <a href="https://diffeq.sciml.ai/stable/">DifferentialEquations.jl</a> suite and "closeness" with Python. Another key bit is that, the <em>HamiltonianProblem</em> type, offered by <a href="https://github.com/SciML/DiffEqPhysics.jl"><em>DiffEqPhysics</em></a>, immensely simplifies the process of solving the system, as it uses Forward Mode Automatic Differentiation to automatically calculate the partial derivatives from the Hamiltonian. The separable nature of the Hamiltonian helps here. Considering all this, I implemented a module in Julia and voilà, the results are accurate, even for some quirky geodesics.</p>
    
    <p>
    
    <a href="https://res.cloudinary.com/practicaldev/image/fetch/s--u-loUOA9--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/nnl1x4g39gtzesaw1467.png" class="article-body-image-wrapper"><img src="https://res.cloudinary.com/practicaldev/image/fetch/s--u-loUOA9--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/nnl1x4g39gtzesaw1467.png" alt="Python 1"></a>Kerr Null-like Capture (Plotted using `Plots.jl`)
    
    
    <br>
    
    <a href="https://res.cloudinary.com/practicaldev/image/fetch/s--4oaFkUBn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/oc2qagahf0htkhr1w5pr.png" class="article-body-image-wrapper"><img src="https://res.cloudinary.com/practicaldev/image/fetch/s--4oaFkUBn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/oc2qagahf0htkhr1w5pr.png" alt="Python 2"></a>Schwarzschild Whirl (Plotted using `Plots.jl`)
    
    
    </p>
    
    <p>Now came the problem of integrating the Julia code with EinsteinPy, for which I looked towards <em>PyJulia</em>. However, it has some issues with <a href="https://pyjulia.readthedocs.io/en/latest/troubleshooting.html">installation on *nix systems</a>. So, I opted to write my own wrapper, using Python's <code>subprocess</code>. and, with the help of my GSoC mentor, Shreyas, packaged the Julia module and the Python wrapper into what is now <a href="https://github.com/einsteinpy/einsteinpy-geodesics"><code>einsteinpy_geodesics</code></a>, an add-on module to EinsteinPy. </p>
    
    
    <div class="ltag-github-readme-tag">
    <div class="readme-overview">
    <h2>
    <img src="https://res.cloudinary.com/practicaldev/image/fetch/s--vJ70wriM--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://practicaldev-herokuapp-com.freetls.fastly.net/assets/github-logo-ba8488d21cd8ee1fee097b8410db9deaa41d0ca30b004c0c63de0a479114156f.svg" alt="GitHub logo">
    <a href="https://github.com/einsteinpy">
    einsteinpy
    </a> / <a href="https://github.com/einsteinpy/einsteinpy-geodesics">
    einsteinpy-geodesics
    </a>
    </h2>
    <h3>
    Python wrapper for a Julia solver for geodesics in the Kerr family of spacetimes. Maintainer : <a class="comment-mentioned-user" href="https://dev.to/jes24">@jes24</a>
    
    </h3>
    </div>
    <div class="ltag-github-body">
    
    <div id="readme" class="rst">
    <a href="https://einsteinpy.org/" rel="nofollow"><img alt="EinsteinPy Logo" src="https://camo.githubusercontent.com/fa1ddad33fe74cb5404a0a7e4d1520c905fe001e/68747470733a2f2f626c6f672e65696e737465696e70792e6f72672f696d672f6c6f676f2e706e67"></a>
    <div class="table-wrapper-paragraph"><table>
    <tbody>
    <tr>
    <th>Name:</th>
    <td>EinsteinPy Geodesics</td>
    </tr>
    <tr>
    <th>Website:</th>
    <td><a href="https://docs.geodesics.einsteinpy.org/en/latest/" rel="nofollow">https://docs.geodesics.einsteinpy.org/en/latest/</a></td>
    </tr>
    <tr>
    <th>Version:</th>
    <td>0.2.dev0</td>
    </tr>
    </tbody>
    </table></div>
    <p><a href="https://groups.io/g/einsteinpy-dev" rel="nofollow"><img alt="mailing" src="https://camo.githubusercontent.com/d2a43e78ff011f2098aa9d07daf700dcdac6a0d2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6d61696c696e672532306c6973742d67726f7570732e696f2d3863626364312e7376673f7374796c653d666c61742d737175617265"></a> <a href="https://gitter.im/EinsteinPy-Project/EinsteinPy?utm_source=badge&amp;utm_medium=badge&amp;utm_campaign=pr-badge&amp;utm_content=badge" rel="nofollow"><img alt="Join the chat at https://gitter.im/EinsteinPy-Project/EinsteinPy" src="https://camo.githubusercontent.com/679ce20047cd21814c1f6b30c9e2837a298e8a86/68747470733a2f2f696d672e736869656c64732e696f2f6769747465722f726f6f6d2f45696e737465696e50792d50726f6a6563742f45696e737465696e50792e7376673f6c6f676f3d676974746572267374796c653d666c61742d737175617265"></a> <a href="https://riot.im/app/#/room/#einsteinpy:matrix.org" rel="nofollow"><img alt="riotchat" src="https://camo.githubusercontent.com/785902ae1e56239d1c3c9de820f88701f095ab2d/68747470733a2f2f696d672e736869656c64732e696f2f6d61747269782f65696e737465696e70793a6d61747269782e6f72672e7376673f6c6f676f3d72696f74267374796c653d666c61742d737175617265"></a> <a href="https://github.com/einsteinpy/einsteinpy-geodesics/blob/master/COPYING"><img alt="license" src="https://camo.githubusercontent.com/4b5966a2a252ee0f241a1e03b13417178eb4964f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d626c75652e7376673f7374796c653d666c61742d737175617265"></a> <a href="https://docs.geodesics.einsteinpy.org/en/latest/" rel="nofollow"><img alt="docs" src="https://camo.githubusercontent.com/dcb95bea2239d0bafb19511c244e34a567619e66/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f63732d6c61746573742d627269676874677265656e2e7376673f7374796c653d666c61742d737175617265"></a></p>
    <p>EinsteinPy Geodesics is an addon package for EinsteinPy, that wraps over Julia's
    excellent <a href="https://diffeq.sciml.ai/stable/" rel="nofollow">DifferentialEquations.jl</a>
    suite and provides a python interface to solve for geodesics in Kerr &amp; Schwarzschild spacetime
    <a href="https://einsteinpy.org/" rel="nofollow">EinsteinPy</a> is an open source pure Python package, dedicated to problems arising
    in General Relativity and Gravitational Physics
    As with EinsteinPy, EinsteinPy Geodesics is released under the MIT license.</p>
    
    <h2>
    Documentation</h2>
    <p><a href="https://docs.geodesics.einsteinpy.org/en/latest/" rel="nofollow"><img alt="docs" src="https://camo.githubusercontent.com/dcb95bea2239d0bafb19511c244e34a567619e66/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f63732d6c61746573742d627269676874677265656e2e7376673f7374796c653d666c61742d737175617265"></a></p>
    <p>Complete documentation for this module can be accessed at <a href="https://docs.geodesics.einsteinpy.org/en/latest/" rel="nofollow">https://docs.geodesics.einsteinpy.org/en/latest/</a> (Courtesy: <a href="https://readthedocs.org/" rel="nofollow">Read the Docs</a>).</p>
    
    <h2>
    Requirements</h2>
    <p>EinsteinPy Geodesics requires Python &gt;= 3.7, Julia &gt;= 1.5 and the following Julia packages:</p>
    <ul>
    <li>
    <dl>
    <dt>Julia</dt>
    <dd>
    <ul>
    <li>DifferentialEquations.jl &gt;= 6.15</li>
    <li>ODEInterfaceDiffEq.jl &gt;= 3.7</li>
    </ul>
    </dd>
    </dl>
    </li>
    </ul>
    
    <h2>
    Installation</h2>
    <p>First, ensure that, Julia is installed in your system and added to PATH. See <a href="https://julialang.org/downloads/platform/" rel="nofollow">https://julialang.org/downloads/platform/</a>
    for platform specific binaries and installation instructions. einsteinpy_geodesics also requires DifferentialEquations.jl
    and ODEInterfaceDiffEq.jl. You can add them, like so:</p>
    <pre>$ julia
    julia&gt; using Pkg
    julia&gt; Pkg.add("DifferentialEquations")
    julia&gt; Pkg.add("ODEInterfaceDiffEq")
    </pre>
    <p>Finally, einsteinpy_geodesics can…</p>
    </div>
    </div>
    <div class="gh-btn-container"><a class="gh-btn" href="https://github.com/einsteinpy/einsteinpy-geodesics">View on GitHub</a></div>
    </div>
    
    
    <p>On top of this, I also overhauled the geodesic plotting module and added support for 3D animations, parametric plots and choice of spatial coordinates in 2D plots, in both <code>Static</code> and <code>Interactive</code> modes (that use <code>matplotlib</code> and <code>plotly</code> respectively). I present some of the plots, produced through the final API, below. The plots shown here, have a mix of both <code>Static</code> and <code>Interactive</code> back-ends, as well as time-like and null-like geodesics.</p>
    
    <p>
    <br>
    
    <a href="https://res.cloudinary.com/practicaldev/image/fetch/s--p70PRpe2--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/vlr7wo51pmrv55xhxdx8.png" class="article-body-image-wrapper"><img src="https://res.cloudinary.com/practicaldev/image/fetch/s--p70PRpe2--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/vlr7wo51pmrv55xhxdx8.png" alt="Interactive"></a>Kerr Null-like Geodesic
    
    
    <br>
    
    <a href="https://res.cloudinary.com/practicaldev/image/fetch/s--Q4nv3DEX--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/8xxuz4iem796p7ofoifw.png" class="article-body-image-wrapper"><img src="https://res.cloudinary.com/practicaldev/image/fetch/s--Q4nv3DEX--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/8xxuz4iem796p7ofoifw.png" alt="Interactive"></a>Kerr Time-like Geodesic
    
    
    <br>
    
    <a href="https://res.cloudinary.com/practicaldev/image/fetch/s--LCBpOP4x--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/aifjnm4ggk59qiur48be.png" class="article-body-image-wrapper"><img src="https://res.cloudinary.com/practicaldev/image/fetch/s--LCBpOP4x--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/aifjnm4ggk59qiur48be.png" alt="2D"></a>Kerr Frame Dragging
    
    
    <br>
    
    <a href="https://res.cloudinary.com/practicaldev/image/fetch/s--6ID4SoXf--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/ntdoyu208csz252k2qeo.png" class="article-body-image-wrapper"><img src="https://res.cloudinary.com/practicaldev/image/fetch/s--6ID4SoXf--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/ntdoyu208csz252k2qeo.png" alt="2D"></a>Schwarzschild Precession
    
    
    <br>
    
    <a href="https://res.cloudinary.com/practicaldev/image/fetch/s--e1fXZqA_--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/oul7ierbcepq76ehb7l8.png" class="article-body-image-wrapper"><img src="https://res.cloudinary.com/practicaldev/image/fetch/s--e1fXZqA_--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/oul7ierbcepq76ehb7l8.png" alt="Closed"></a>Schwarzschild Time-like Closed Orbit
    
    
    <br>
    
    <a href="https://res.cloudinary.com/practicaldev/image/fetch/s--CFxLb1V7--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/kf1yn7z44090gf18itab.png" class="article-body-image-wrapper"><img src="https://res.cloudinary.com/practicaldev/image/fetch/s--CFxLb1V7--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/kf1yn7z44090gf18itab.png" alt="Closed"></a>Schwarzschild Time-like Closed Orbit Parametric Plot
    
    
    </p>
    
    <h2>
    <a href="#until-next-time" class="anchor">
    </a>
    Until next time...
    </h2>
    
    <p>The EinsteinPy geodesics API currently provides a choice of solvers, between a python back-end and a julia back-end, through the optional <code>einsteinpy_geodesics</code> add-on. I will continue to work on improving the python back-end, but for now, <code>einsteinpy_geodesics</code> adds proper &amp; accurate geodesic calculations to EinsteinPy, in the Kerr family of spacetimes (that includes Schwarzschild). Also, a notable aspect of the <code>HamiltonianProblem</code> approach is that, in principle, it should be easily extensible to Kerr-Newman geodesics, which is something, I'd like to explore, as soon as my GSoC commitment is over. I have another short blog coming up, that explains how to use the API (and has more cool plots), that will probably also be the last GSoC blog. Till then, I leave you with a nice animation, created entirely with EinsteinPy.</p>
    
    <p>
    
    <a href="https://res.cloudinary.com/practicaldev/image/fetch/s--hF0GF8ch--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/e47cv7qh0xejnmuaz0qb.gif" class="article-body-image-wrapper"><img src="https://res.cloudinary.com/practicaldev/image/fetch/s--hF0GF8ch--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/e47cv7qh0xejnmuaz0qb.gif" alt="Python 2"></a>(Extremal) Kerr Time-like Constant Orbit
    
    
    </p>
    
    
    
    
    <h4>
    <a href="#references" class="anchor">
    </a>
    References:
    </h4>
    
    <p>[1]: Carter, Brandon; <a href="https://link.aps.org/doi/10.1103/PhysRev.174.1559"><em>Global Structure of the Kerr Family of Gravitational Fields</em></a>, 1968 , Physical Review, 174(5), pp. 1559-1571</p>
    
    <p>[2]: Misner, Charles W. and Thorne, K.S. and Wheeler, J.A; <em>Gravitation</em>, 1973, W. H. Freeman, ISBN: 978-0-7167-0344-0, 978-0-691-17779-3</p>

