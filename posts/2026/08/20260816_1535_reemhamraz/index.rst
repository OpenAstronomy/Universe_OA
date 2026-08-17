.. title: Learning to Speak C & Cython: My GSoC Summer with Astropy
.. slug:
.. date: 2026-08-16 15:35:15 
.. tags: Astropy
.. author: Reem Hamraz
.. link: https://dev.to/reemhamraz/learning-to-speak-c-cython-my-gsoc-summer-with-astropy-1fh0
.. description:
.. category: gsoc2026


.. raw:: html

    <p>The summer is officially over. I am staring at a remarkably clean Git branch, my laptop didn't literally take off into orbit (though the CPU fans certainly tried a few times during local CI builds), and I somehow know what <code>git rebase -i</code> does without having to Google it in a cold sweat.</p>
    
    <p>If you'd asked me back in May what I was going to be doing, I would have confidently told you I was going to "write tests for Astropy's C extensions." It sounded so neat. So contained. But open source doesn't really work like that. I came in thinking I was just going to write tests, and somewhere along the way, I ended up learning how the actual machinery underneath the Python abstraction works, how maintainers think about architecture, and how to safely catch C-level memory panics without taking down the entire interpreter.</p>
    <!-- TEASER_END -->
    
    <p>So, here is the real story of what I did for the last few months, what broke, how we fixed it, and where the project stands now.</p>
    
    <h2>
    
    
    So, what was I actually supposed to do?
    </h2>
    
    <p>Astropy is a beast of a library. The Python-facing API is incredibly robust and beautifully documented. But underneath all those pretty Python classes is a complex, mixed-language architecture. The library relies heavily on compiled C, and Cython extensions to handle the performance-critical hot-paths.</p>
    
    <p>The problem? That compiled layer was a massive testing blind spot. Before this summer, these performance-critical extensions were almost entirely tested indirectly, meaning they were only validated by calling the high-level Python wrappers. That is a risky abstraction. If a regression happens deep inside the C code, the Python layer sitting above it can accidentally mask it. You wouldn't know something was fundamentally broken until a downstream package started acting weird.</p>
    
    <p>My project goal was to build a dedicated, de novo test suite that bypassed the public API completely and exercised each compiled extension module directly. This wasn't just for code coverage. It was an absolute prerequisite for three massive Astropy milestones:</p>
    
    <ul>
    <li>
    <strong>The APE Split</strong>: Proving the extensions are stable enough to live in a completely separate package.</li>
    <li>
    <strong>Meson Migration</strong>: Having a safety net to catch silent regressions when the build system transitions.</li>
    <li>
    <strong>Python 3.15 Limited API</strong>: Safely testing internal C-refactors for the upcoming free-threaded builds.</li>
    </ul>
    
    <p>The mission was to harden Astropy's core stability. The reality was peeling away layers of Python abstractions until I was staring at raw memory buffers.</p>
    
    <h2>
    
    
    Turns out, "testing C extensions" is not quite as simple as it sounds
    </h2>
    
    <p>I started my summer in <code>astropy/table</code>, which my mentors flagged as a solid starting point. My first target was <code>test_np_utils.py</code>, writing a low-level suite for the <code>join_inner</code> Cython extension.</p>
    
    <p>The thing is, Cython engines don't want your high-level <code>Table</code> objects. They want raw data. I had to build a helper function, <code>_make_join_inputs</code>, which acted as a pre-processor. It took two arrays, concatenated them, sorted them with <code>argsort(kind="stable")</code>, and used a boolean <code>diffs</code> array to find the exact boundaries of unique keys. It output the exact <code>np.intp</code> bindings that Cython demanded.</p>
    
    <p>Once I could feed the raw engine, I built strictly typed dataclasses (<code>ArrayMaskPair</code> and <code>ExpectedResults</code>) to hold the outputs without making the pytest matrices unreadable with massive tuples. I tested standard overlaps, but the real fun was the Cartesian edge cases. I threw O(N²) expansions at the engine, where duplicate keys joined with duplicate keys, just to prove the C-engine could handle the explosive memory allocation without crashing. I also verified that it properly handles <code>np.nan</code> as a unique entity (since <code>nan != nan</code> in Python).</p>
    
    <p>And all this stands as proof that I can actually write code that works, phew!</p>
    
    <h3>
    
    
    The C-Slots
    </h3>
    
    <p>Things got significantly more complicated when I moved to <code>test_column_mixins.py</code>. The objective here was to test the Cython <code>__getitem__</code> routing in pure isolation.</p>
    
    <p>I couldn't just pass a standard array. I had to create a "Shim Strategy" (so fancy), so I wrote <code>MinimalColumn</code> and <code>MinimalMaskedColumn</code> classes that inherited directly from the Cython mixins (<code>_ColumnGetitemShim</code>, <code>_MaskedColumnGetitemShim</code>) and mapped them directly onto raw NumPy arrays using <code>.view()</code> casting. By overriding the <code>.data</code> property to return a pure ndarray view, I stopped the Cython engine from returning raw memoryview buffers, which would have hard-crashed the tests. We were hitting the <code>tp_as_mapping-&gt;mp_subscript</code> C-slot directly.</p>
    
    <p>But this is where I hit my first major hurdle.</p>
    
    <p>While I was writing a test for structured arrays, indexing it with a single string, the structured dtype suddenly just dropped, and it returned a 1D array of the underlying field's type. I spent hours going down this rabbit hole, utterly convinced my test was wrong. Eventually, I found the machinery underneath: a literal trapdoor in <code>base_getitem</code>.<br />
    </p>
    
    <div class="highlight js-code-highlight">
    <pre class="highlight python"><code><span class="k">if</span> <span class="n">dtype_kind</span> <span class="o">==</span> <span class="sh">'</span><span class="s">V</span><span class="sh">'</span> <span class="ow">and</span> <span class="nf">isinstance</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="n">STRING_TYPES</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="n">data</span><span class="p">[</span><span class="n">item</span><span class="p">]</span>
    </code></pre>
    
    </div>
    
    
    
    <p>Because it accessed the raw <code>.data</code> array, it inherited NumPy's default behavior and lost the structure. Rather than cementing this unintended behavior by writing a passing test for it, I dropped the test case and opened Issue <a href="https://github.com/astropy/astropy/issues/19827" rel="noopener noreferrer">#19827</a>.</p>
    
    <p>This was my first realization that tests aren't just a safety net; when written at this level, they act like a microscope.</p>
    
    <h2>
    
    
    And then things started breaking in interesting ways
    </h2>
    
    <p>Open source isn't just writing code, getting a green checkmark, and merging. The messy middle is where the actual work happens. I mean everyone knows that right? Yeah no sometimes people get a reality check; people is me, I am people.</p>
    
    <ul>
    <li>
    <strong>The Masked Array <code>isinstance</code> Trap</strong>: I proudly swapped <code>isinstance()</code> checks for strict <code>type(result) is ...</code> assertions, which instantly caused my masked array tests to fail. It turns out standard ndarray slicing strips subclasses, but <code>np.ma.MaskedArray.__getitem__</code> inherently preserves them. The C-slot was actively returning the <code>MinimalMaskedColumn</code> shim.</li>
    <li>
    <strong>The CI Gatekeeper</strong>: While working on the mixins, I used an <code>@override</code> decorator. Python 3.12 CI matrices immediately failed because <code>typing_extensions</code> wasn't in the base test environment. Instead of bloating <code>pyproject.toml</code> with a new dependency just for one test file, I made the architectural choice to drop the decorator completely. CI went green.</li>
    <li>
    <strong>Git History looking like a crime scene</strong>: At one point, a <code>.uv.lock</code> file triggered a <code>check-added-large-files</code> pre-commit hook failure. My branch had some incredibly messy commits. So I took a couple a deep breaths, paced around, and after a midly dramatic breakdown, I ran <code>git restore --staged</code>, and fired up a local interactive rebase (<code>git rebase -i HEAD~6</code>) via Nano to squash the chaos into a single, clean production commit (see told ya it was simple :) )</li>
    </ul>
    
    <h2>
    
    
    Somewhere along the way, I stopped just writing tests
    </h2>
    
    <p>As the summer progressed, the project evolved. The APE split required not just test coverage, but rigorous structural boundaries. I started writing <code>.pyi</code> type stubs to define the Python-facing boundaries of compiled extensions so static type checkers could understand them without executing the C-engine, not to forget the Proof of Concept, all in a days work (I'm lying, I almost cried trying the machete strategy).</p>
    
    <h3>
    
    
    The XML C-Extension Stubs (<code>iterparser_iterparser.pyi</code>)
    </h3>
    
    <p>When I looked at the C struct for the <code>_iterparser</code> extension, it looked like the parser accepted <code>fd</code>, <code>buffersize</code>, <code>file</code>, and <code>buffer</code>. But looking at the C struct is like looking at a map and realizing the map is wrong.</p>
    
    <p>By analyzing the C-API execution (<code>PyArg_ParseTupleAndKeywords</code>), I discovered that <code>file</code> and <code>buffer</code> were strictly internal C-state variables generated after crossing the Python boundary. The Python <code>__init__</code> only actually takes <code>fd</code> and <code>buffersize</code>. Because the C-engine didn't natively support keyword argument routing here, I had to enforce positional-only arguments using the PEP 570 <code>/</code> marker in Python.</p>
    
    <p>Even better, we had a friendly discussion about the <code>fd.read</code> callable. My mentor pointed out <code>read(self-&gt;file, self-&gt;buffer...)</code> in the C code. But tracing the Python C-API showed a <code>Py_BuildValue("(n)", buffersize)</code> call directly before <code>PyObject_CallObject</code>. The C-engine was packing a C <code>Py_ssize_t</code> into a 1-element Python tuple. We proved the Python callable only ever receives one integer, finalizing the strict protocol signature as <code>Callable[[int], bytes]</code>.</p>
    
    <h3>
    
    
    Dimensionality Locking in <code>_convolve</code>
    </h3>
    
    <p>For <code>_convolve.pyx</code>, we needed to ensure that arrays passed to the C engine matched perfectly before runtime. I used bounded <code>TypeVar</code> aliases (<code>_D1</code>, <code>_D2</code>, <code>_D3</code>) to enforce a strict mathematical rule at the static analysis level. The result, <code>array_to_convolve</code>, and kernel arrays can be 1D, 2D, or 3D, but the linter now mathematically locks them so all three must have the exact same dimensionality.</p>
    
    <h3>
    
    
    The <code>unit_list_proxy.c</code> Dependency Injection
    </h3>
    
    <p>This was easily one of the coolest things I worked on. <code>astropy/wcs/src/unit_list_proxy.c</code> had a massive circular dependency problem. It was relying on <code>astropy.units.UnitBase</code> via <code>PyImport_ImportModule</code> at runtime.</p>
    
    <p>We discovered that <code>cunit</code> wasn't a normal attribute; it was a C-level mutable proxy array. Standard Python <code>@property</code> wrappers broke the memory linkage, meaning the C-array never received updates.</p>
    
    <p>Following my mentor Clément's strategy, we scrapped the Python wrappers and built a Dependency Injection architecture. We implemented a <code>_setup_unit_class(PyObject* unit_class)</code> function, dynamically exposed to <code>_wcs</code>. It runs exactly once during Python initialization to cache the <code>Unit</code> class pointer in a static C variable, completely severing the heavy <code>PyImport</code> dependency. We updated the getitem C-slot to natively yield <code>Unit</code> objects (like <code>CompositeUnit</code>) back to Python, and made the setitem slot use duck-typing (<code>parse_strict="warn"</code>) so it gracefully emits a <code>UnitsWarning</code> for garbage FITS strings instead of hard-crashing. I was super elated when I finally succeeded and to see the CI checks green? Goodness was that rewarding, so I treated myself to an ice-cream sundae!</p>
    
    <h3>
    
    
    Numerical sanity and the "Grid Trap"
    </h3>
    
    <p>I also wrote isolated suites for the <code>astropy.timeseries</code> periodogram C-extensions. Bypassing the high-level <code>BoxLeastSquares</code> API, I fed raw <code>np.float64</code> memory buffers directly into the Cython boundary (<code>_impl.pyx</code>).</p>
    
    <p>I built a <code>SyntheticTransit</code> fixture to inject a perfect transit dip into a simulated light curve to prove the C-engine's <code>best_objective</code> algorithm peaked accurately.</p>
    
    <p>But math is cruel :(</p>
    
    <p>My tests were failing to recover a mathematically perfect period of 2.0. Why? Because I generated my frequency grid using <code>np.linspace(1.5, 2.5, 100)</code>. If you do the floating-point math, the step size is ~0.0101. The number 2.0 literally did not exist in the array (the closest it got was 2.005). I was stuck fighting my own numerical grid. I changed it to 101 steps, and voila it hit the target perfectly!</p>
    
    <p>We also dealt with a fascinating accuracy tradeoff. When using a coarse grid (1,000 points, <code>oversample=10</code>), the discrete phase-binning of the BLS algorithm caused the edges of the transit to smear, changing the recovered depth from a perfect 0.5 to 0.478. My mentor challenged the 5% tolerance. By fixing the <code>linspace</code> bug and adjusting the points, we tightened the mathematical accuracy to <code>1e-4</code> while balancing the matrix to keep the isolated test executing in under 300ms so we didn't anger the CI limits.</p>
    
    <p>I ran into a similar trapdoor testing the Lomb-Scargle Cython implementation (<code>cython_impl.pyx</code>). I tried to test the Cython-level <code>t.ndim != 1</code> error. But when I passed a 2D array for <code>t</code> and 1D arrays for <code>y</code>, <code>np.broadcast_arrays</code> panicked and raised a Python <code>ValueError</code> before the C-engine ever saw it. The fix? I deliberately passed identical 2D arrays for all parameters so it survived the Python broadcasting check and successfully crashed directly on the C-boundary. Hurrayy!</p>
    
    <h2>
    
    
    The parts that didn't go according to plan
    </h2>
    
    <p>Of course, not everything matched the original proposal. My initial timeline had me delivering tests for <code>astropy/erfa</code> and <code>astropy.coordinates</code> towards the end of the summer (Deliverables 5 and 6).</p>
    
    <p>The reality of open-source struck: <code>astropy/erfa</code> had already been spun out into the standalone <code>pyerfa</code> package, and <code>astropy.coordinates</code> was delegating its math to that external library. You can't write isolated C-extension tests for an architecture that doesn't live in your repository anymore.</p>
    
    <p>Rather than viewing this as a failure, I contacted my mentors, pivoted, and spent that time significantly deepening the coverage and architectural stability of the <code>.pyi</code> stubs and the XML parsers.</p>
    
    <h2>
    
    
    So, where did we end up? (Current State)
    </h2>
    
    <p>The goal was to make the compiled layer testable, and I am leaving behind an architecture to ensure it stays that way.</p>
    
    <h3>
    
    
    Merged work &amp; contributions
    </h3>
    
    <ul>
    <li>Table C-extensions: merged isolated tests for <code>join_inner</code> (PR <a href="https://github.com/astropy/astropy/pull/19458" rel="noopener noreferrer">#19458</a>), documented <code>jointype</code> integer mappings (PR #19468), and added direct C-slot tests for <code>_column_mixins</code> (PR <a href="https://github.com/astropy/astropy/pull/19806" rel="noopener noreferrer">#19806</a>).</li>
    <li>XML iterparser: built structural 4-tuple boundary tests for the <code>_iterparser</code> C-extension and caught memory buffer behaviors (PR <a href="https://github.com/astropy/astropy/pull/19922" rel="noopener noreferrer">#19922</a>).</li>
    <li>Type stubs: defined the static type boundaries for <code>_iterparser.pyi</code> (PR <a href="https://github.com/astropy/astropy/pull/20006" rel="noopener noreferrer">#20006</a>, positional-only) and <code>_convolve</code> (PR <a href="https://github.com/astropy/astropy/pull/20093" rel="noopener noreferrer">#20093</a>, dimensionality locking).</li>
    <li>Time parse extension: overhauled the <code>_parse_times.c</code> boundary test using strict <code>type(parser) is np.ufunc</code> assertions and byte arrays (<code>"S24"</code>) (PR <a href="https://github.com/astropy/astropy/pull/19875" rel="noopener noreferrer">#19875</a>).</li>
    <li>Quantity unit extraction: fixed unit extraction in <code>structured_to_unstructured</code> for <code>StructuredQuantity</code> (PR <a href="https://github.com/astropy/astropy/pull/19106" rel="noopener noreferrer">#19106</a>).</li>
    <li>APE split expansion: contributed to the proof of concept for the APE split, expanding the implementation section in Clement's fork (PR <a href="https://github.com/neutrinoceros/astropy-APEs/pull/3" rel="noopener noreferrer">#3</a>) to define what the low-level tests look like.</li>
    </ul>
    
    <h3>
    
    
    Still open, waiting on review
    </h3>
    
    <ul>
    <li>WCS dependency injection: refactored <code>unit_list_proxy.c</code> to cache the <code>Unit</code> class pointer, severing the <code>PyImport</code> overhead (PR <a href="https://github.com/astropy/astropy/pull/20072" rel="noopener noreferrer">#20072</a>).</li>
    <li>Timeseries math engines: built exact synthetic recovery matrices for Box Least Squares (<code>bls.c</code> / <code>_impl.pyx</code>, PR <a href="https://github.com/astropy/astropy/pull/20151" rel="noopener noreferrer">#20151</a>) and Lomb-Scargle (<code>cython_impl.pyx</code>, PR <a href="https://github.com/astropy/astropy/pull/20222" rel="noopener noreferrer">#20222</a>).</li>
    </ul>
    
    <h3>
    
    
    The Developer Guide
    </h3>
    
    <p>Perhaps the most lasting piece of work I did was writing and merging <code>testing_extensions.rst</code> (PR <a href="https://github.com/astropy/astropy/pull/20239" rel="noopener noreferrer">#20239</a>) into Astropy's core documentation. This document establishes the architectural standards for making low-level compiled modules testable. It outlines the rules for bypassing Python wrappers, strictly avoiding <code>isinstance()</code> at the compiled boundary, structural validation, safe exception handling using <code>pytest.raises</code> substring matching, and <code>.pyi</code> architecture. If anyone has any questions regarding the project I think this would serve as a good starting point (before the actual coding part of course).</p>
    
    <h2>
    
    
    What's left after I leave?
    </h2>
    
    <p>The work on <code>astropy/erfa</code> was pivoted to the external <code>pyerfa</code> repository, so testing that boundary remains a future task for whoever manages that standalone package.</p>
    
    <p>Beyond that, the primary future work is maintenance. When a new Cython extension is updated or a C-boundary changes, these isolated tests will immediately flag it. The <code>testing_extensions.rst</code> guide exists specifically so future contributors don't have to stumble through the same trapdoors I did. Future contributors can use this suite as a blueprint to expand coverage into newer subpackages.</p>
    
    <p>Sidenote: I plan on staying (long time). I'm not going to disappear just because GSoC is over but rather continue to contribute to this epic organization. I'll keep working, raising PRs, beefing with GitHub and most importantly, I'll help guide all those who stumble across Astropy just as Clément and Nathaniel were always there for me!!</p>
    
    <h2>
    
    
    What I actually took away from this
    </h2>
    
    <p>I came into GSoC thinking I was going to write tests. Somewhere along the way, I ended up learning how to actually reason about a mature codebase.</p>
    
    <p>I learned that you have to read the C code before writing the Python test. I learned to question unexpected behavior rather than blindly cementing it into a test. I learned that CI is a judgmental gatekeeper, Git history tells a story, and numerical tolerances matter a whole lot more than just getting the test to pass. I learned that maybe breaking a huge problem into separate sections wasn't such a bad idea after all and it's this lesson that I'll be applying to my life as well.</p>
    
    <p>Most importantly, I learned how maintainer-level review actually works. The feedback I got wasn't just "fix this bug," it was "let's structure this so it's statically typed, mathematically locked, and future-proof." And it really shaped my journey. I mean the Reem from January decided to open her very first PR and make huge changes in 4 different files, which ultimately was pretty overwhelming and she closed the PR. My point is that I have grown as a contributor and that makes me so very proud. </p>
    
    <h2>
    
    
    A HUGE thank you
    </h2>
    
    <p>All this is just because I had the BEST mentors EVER, Clément Robert (@neutrinoceros), and Nathaniel Starkman (@nstarman).</p>
    
    <p>Clément, thank you for never once making me feel dumb for asking the same question twice, and for having the patience to let me actually sit with a hard bug instead of just handing me the fix. For taking time out from your busy schedule every week, just so that I could ask you all the questions I saved, and to go through my code, suggest changes and help me understand all the whys. You didn't just correct my code, you really changed how I think about coding. I came into this summer knowing how to write Python and I'm ending it knowing how to reason about the machine underneath.</p>
    
    <p>Nathaniel, thank you for being just as generous with your time, and just as willing to slow down and explain something properly even when the answer must have felt obvious from where you were standing. </p>
    
    <p>Having two mentors who both cared this much about getting it right, and not just getting it merged, made all the difference. And I couldn't be more grateful!</p>
    
    <p>To the OpenAstronomy and Astropy community: thank you for letting me poke around the raw engine of your library.</p>
    
    <p>Until next time,<br />
    Reem &lt;3</p>

