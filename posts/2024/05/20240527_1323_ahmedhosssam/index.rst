.. title: Good start for the project
.. slug:
.. date: 2024-05-27 13:23:44 
.. tags: SunPy
.. author: Ahmed Hossam
.. link: https://dev.to/ahmedhosssam/good-start-for-the-project-131n
.. description:
.. category: gsoc2024


.. raw:: html

    <h2>
    
    
    <!-- TEASER_END -->
    First 2 weeks summarize:
    </h2>
    
    <p>This week I began working on refactoring <code>hek.py</code> functions.<br />
    I started by migrating the finished work in <a href="https://github.com/sunpy/sunpy/pull/7059">GSoC2023</a> to a new <a href="https://github.com/sunpy/sunpy/pull/7619">PR</a> to start working on it.<br />
    My first contribution was creating <code>util.py</code> file to include all utility functions needed for <code>hek.py</code>, a lot of functions that was added in HEKClient at first didn't make sense to remain there.</p>
    
    <p>Now the new <code>util.py</code> file includes:<br />
    </p>
    
    <div class="highlight js-code-highlight">
    <pre class="highlight python"><code><span class="k">def</span> <span class="nf">parse_times</span><span class="p">(</span><span class="n">table</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">parse_values_to_quantities</span><span class="p">(</span><span class="n">table</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">parse_columns_to_table</span><span class="p">(</span><span class="n">table</span><span class="p">,</span> <span class="n">attributes</span><span class="p">,</span> <span class="n">is_coord_prop</span> <span class="o">=</span> <span class="bp">False</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">parse_unit</span><span class="p">(</span><span class="n">table</span><span class="p">,</span> <span class="n">attribute</span><span class="p">,</span> <span class="n">is_coord_prop</span> <span class="o">=</span> <span class="bp">False</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">parse_chaincode</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">attribute</span><span class="p">,</span> <span class="n">unit</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">get_unit</span><span class="p">(</span><span class="n">unit</span><span class="p">)</span>
    
    </code></pre>
    
    </div>
    
    
    
    <p><code>get_unit</code> has been simplified in terms of implementation and interface, this was the first version:<br />
    </p>
    
    <div class="highlight js-code-highlight">
    <pre class="highlight python"><code>    <span class="k">def</span> <span class="nf">get_unit</span><span class="p">(</span><span class="n">attribute</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">is_coord_prop</span><span class="sh">"</span><span class="p">]:</span>
    <span class="n">coord1_unit</span><span class="p">,</span> <span class="n">coord2_unit</span><span class="p">,</span> <span class="n">coord3_unit</span> <span class="o">=</span> <span class="bp">None</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="bp">None</span>
    <span class="n">coord_units</span> <span class="o">=</span> <span class="n">re</span><span class="p">.</span><span class="nf">split</span><span class="p">(</span><span class="sa">r</span><span class="sh">'</span><span class="s">[, ]</span><span class="sh">'</span><span class="p">,</span> <span class="nb">str</span><span class="p">)</span>
    <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">coord_units</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span> <span class="c1"># deg
    </span>               <span class="n">coord1_unit</span> <span class="o">=</span> <span class="n">coord2_unit</span> <span class="o">=</span> <span class="n">u</span><span class="p">.</span><span class="nc">Unit</span><span class="p">(</span><span class="n">coord_units</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
    <span class="k">elif</span> <span class="nf">len</span><span class="p">(</span><span class="n">coord_units</span><span class="p">)</span> <span class="o">==</span> <span class="mi">2</span><span class="p">:</span>
    <span class="n">coord1_unit</span> <span class="o">=</span> <span class="n">u</span><span class="p">.</span><span class="nc">Unit</span><span class="p">(</span><span class="n">coord_units</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
    <span class="n">coord2_unit</span> <span class="o">=</span> <span class="n">u</span><span class="p">.</span><span class="nc">Unit</span><span class="p">(</span><span class="n">coord_units</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
    <span class="k">else</span><span class="p">:</span>
    <span class="n">coord1_unit</span> <span class="o">=</span> <span class="n">u</span><span class="p">.</span><span class="nc">Unit</span><span class="p">(</span><span class="n">coord_units</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
    <span class="n">coord2_unit</span> <span class="o">=</span> <span class="n">u</span><span class="p">.</span><span class="nc">Unit</span><span class="p">(</span><span class="n">coord_units</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
    <span class="n">coord3_unit</span> <span class="o">=</span> <span class="n">u</span><span class="p">.</span><span class="nc">Unit</span><span class="p">(</span><span class="n">coord_units</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span>
    <span class="k">return</span> <span class="nf">locals</span><span class="p">()[</span><span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">unit_prop</span><span class="sh">"</span><span class="p">]]</span>
    <span class="k">else</span><span class="p">:</span>
    <span class="k">return</span> <span class="n">u</span><span class="p">.</span><span class="nc">Unit</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span>
    </code></pre>
    
    </div>
    
    
    
    <p>The first thing that has been done is to use unit aliases inside the function using context manager instead of putting the aliases globally.</p>
    
    <p>The whole goal of this function is to parse a string into an astropy unit, but the big part of the function was splitting the string into more than one unit if the input was coordinate units, and then returning the unit assigned to <code>unit_prop</code>. I decided to just remove all of this and convert the unit into an array and return the first index, like this:<br />
    </p>
    
    <div class="highlight js-code-highlight">
    <pre class="highlight python"><code>   <span class="n">units</span> <span class="o">=</span> <span class="n">re</span><span class="p">.</span><span class="nf">split</span><span class="p">(</span><span class="sa">r</span><span class="sh">'</span><span class="s">[, ]</span><span class="sh">'</span><span class="p">,</span> <span class="n">unit</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">u</span><span class="p">.</span><span class="nc">Unit</span><span class="p">(</span><span class="n">units</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="nf">lower</span><span class="p">())</span>
    </code></pre>
    
    </div>
    
    
    
    <p>And actually it works just fine with all HEK features and events, so I will keep it like this until some strange error appears.<br />
    And also the interface has been simplified to just take the string of the targeted unit.</p>
    
    <p>This is the current version of <code>get_unit</code>:<br />
    </p>
    
    <div class="highlight js-code-highlight">
    <pre class="highlight python"><code><span class="k">def</span> <span class="nf">get_unit</span><span class="p">(</span><span class="n">unit</span><span class="p">):</span>
    <span class="sh">"""</span><span class="s">
    Converts string into astropy unit.
    
    Parameters
    ----------
    unit: str
    The targeted unit
    
    Returns
    -------
    unit
    Astropy unit object (e.g. &lt;class </span><span class="sh">'</span><span class="s">astropy.units.core.Unit</span><span class="sh">'</span><span class="s">&gt; or &lt;class </span><span class="sh">'</span><span class="s">astropy.units.core.CompositeUnit</span><span class="sh">'</span><span class="s">&gt;)
    
    Raises
    ------
    ValueError
    Because `unit` did not parse as unit.
    
    Notes
    ----
    For the complete list of HEK parameters: https://www.lmsal.com/hek/VOEvent_Spec.html
    
    </span><span class="sh">"""</span>
    <span class="n">cm2</span> <span class="o">=</span> <span class="n">u</span><span class="p">.</span><span class="nf">def_unit</span><span class="p">(</span><span class="sh">"</span><span class="s">cm2</span><span class="sh">"</span><span class="p">,</span> <span class="n">u</span><span class="p">.</span><span class="n">cm</span><span class="o">**</span><span class="mi">3</span><span class="p">)</span>
    <span class="n">m2</span> <span class="o">=</span> <span class="n">u</span><span class="p">.</span><span class="nf">def_unit</span><span class="p">(</span><span class="sh">"</span><span class="s">m2</span><span class="sh">"</span><span class="p">,</span> <span class="n">u</span><span class="p">.</span><span class="n">m</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span>
    <span class="n">m3</span> <span class="o">=</span> <span class="n">u</span><span class="p">.</span><span class="nf">def_unit</span><span class="p">(</span><span class="sh">"</span><span class="s">m3</span><span class="sh">"</span><span class="p">,</span> <span class="n">u</span><span class="p">.</span><span class="n">m</span><span class="o">**</span><span class="mi">3</span><span class="p">)</span>
    
    <span class="n">aliases</span> <span class="o">=</span> <span class="p">{</span>
    <span class="sh">"</span><span class="s">steradian</span><span class="sh">"</span><span class="p">:</span> <span class="n">u</span><span class="p">.</span><span class="n">sr</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">arcseconds</span><span class="sh">"</span><span class="p">:</span> <span class="n">u</span><span class="p">.</span><span class="n">arcsec</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">degrees</span><span class="sh">"</span><span class="p">:</span> <span class="n">u</span><span class="p">.</span><span class="n">deg</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">sec</span><span class="sh">"</span><span class="p">:</span> <span class="n">u</span><span class="p">.</span><span class="n">s</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">emx</span><span class="sh">"</span><span class="p">:</span> <span class="n">u</span><span class="p">.</span><span class="n">Mx</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">amperes</span><span class="sh">"</span><span class="p">:</span> <span class="n">u</span><span class="p">.</span><span class="n">A</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">ergs</span><span class="sh">"</span><span class="p">:</span> <span class="n">u</span><span class="p">.</span><span class="n">erg</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">cubic centimeter</span><span class="sh">"</span><span class="p">:</span> <span class="n">u</span><span class="p">.</span><span class="n">ml</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">square centimeter</span><span class="sh">"</span><span class="p">:</span> <span class="n">cm2</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">cubic meter</span><span class="sh">"</span><span class="p">:</span> <span class="n">m3</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">square meter</span><span class="sh">"</span><span class="p">:</span> <span class="n">m2</span><span class="p">,</span>
    <span class="p">}</span>
    
    <span class="k">with</span> <span class="n">u</span><span class="p">.</span><span class="nf">add_enabled_units</span><span class="p">([</span><span class="n">cm2</span><span class="p">,</span> <span class="n">m2</span><span class="p">,</span> <span class="n">m3</span><span class="p">]),</span> <span class="n">u</span><span class="p">.</span><span class="nf">set_enabled_aliases</span><span class="p">(</span><span class="n">aliases</span><span class="p">):</span>
    <span class="c1"># If they are units of coordinates, it will have more than one unit,
    </span>        <span class="c1"># otherwise it will be just one unit.
    </span>        <span class="c1"># NOTE: There is an assumption that coord1_unit, coord2_unit and coord3_unit will be the same.
    </span>        <span class="n">units</span> <span class="o">=</span> <span class="n">re</span><span class="p">.</span><span class="nf">split</span><span class="p">(</span><span class="sa">r</span><span class="sh">'</span><span class="s">[, ]</span><span class="sh">'</span><span class="p">,</span> <span class="n">unit</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">u</span><span class="p">.</span><span class="nc">Unit</span><span class="p">(</span><span class="n">units</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="nf">lower</span><span class="p">())</span>
    
    </code></pre>
    
    </div>
    
    
    
    <p>Another thing that has been done was adding a documentation string for <code>parse_chaincode</code> function.<br />
    </p>
    
    <div class="highlight js-code-highlight">
    <pre class="highlight python"><code><span class="k">def</span> <span class="nf">parse_chaincode</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">attribute</span><span class="p">,</span> <span class="n">unit</span><span class="p">):</span>
    <span class="sh">"""</span><span class="s">
    Parses a string representation of coordinates and convert them into a PolygonSkyRegion object
    using units based on the specified coordinate frame.
    
    Parameters
    ----------
    value: PolygonSkyRegion
    A polygon defined using vertices in sky coordinates.
    attribute: dict
    An object from coord_properties.json
    unit: str
    The unit of the coordinates
    
    Returns
    -------
    PolygonSkyRegion
    A polygon defined using vertices in sky coordinates.
    
    Raises
    ------
    IndexError
    Because `value` does not contain the expected </span><span class="sh">'</span><span class="s">((</span><span class="sh">'</span><span class="s"> and </span><span class="sh">'</span><span class="s">))</span><span class="sh">'</span><span class="s"> substrings.
    UnitConversionError
    Because the units set by `coord1_unit` or `coord2_unit` are incompatible with the values being assigned.
    
    </span><span class="sh">"""</span>
    <span class="n">coord1_unit</span> <span class="o">=</span> <span class="n">u</span><span class="p">.</span><span class="n">deg</span>
    <span class="n">coord2_unit</span> <span class="o">=</span> <span class="n">u</span><span class="p">.</span><span class="n">deg</span>
    <span class="k">if</span> <span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">frame</span><span class="sh">"</span><span class="p">]</span> <span class="o">==</span> <span class="sh">"</span><span class="s">helioprojective</span><span class="sh">"</span><span class="p">:</span>
    <span class="n">coord1_unit</span> <span class="o">=</span> <span class="n">u</span><span class="p">.</span><span class="n">arcsec</span>
    <span class="n">coord2_unit</span> <span class="o">=</span> <span class="n">u</span><span class="p">.</span><span class="n">arcsec</span>
    <span class="k">elif</span> <span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">frame</span><span class="sh">"</span><span class="p">]</span> <span class="o">==</span> <span class="sh">"</span><span class="s">heliocentric</span><span class="sh">"</span><span class="p">:</span>
    <span class="n">coord1_unit</span> <span class="o">=</span> <span class="n">u</span><span class="p">.</span><span class="n">R_sun</span> <span class="c1"># Nominal solar radius
    </span>    <span class="k">elif</span> <span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">frame</span><span class="sh">"</span><span class="p">]</span> <span class="o">==</span> <span class="sh">"</span><span class="s">icrs</span><span class="sh">"</span><span class="p">:</span>
    <span class="n">coord1_unit</span> <span class="o">=</span> <span class="nf">get_unit</span><span class="p">(</span><span class="n">unit</span><span class="p">)</span>
    <span class="n">coord2_unit</span> <span class="o">=</span> <span class="nf">get_unit</span><span class="p">(</span><span class="n">unit</span><span class="p">)</span>
    
    <span class="n">coordinates_str</span> <span class="o">=</span> <span class="n">value</span><span class="p">.</span><span class="nf">split</span><span class="p">(</span><span class="sh">'</span><span class="s">((</span><span class="sh">'</span><span class="p">)[</span><span class="mi">1</span><span class="p">].</span><span class="nf">split</span><span class="p">(</span><span class="sh">'</span><span class="s">))</span><span class="sh">'</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
    <span class="n">coord1_list</span> <span class="o">=</span> <span class="p">[</span><span class="nf">float</span><span class="p">(</span><span class="n">coord</span><span class="p">.</span><span class="nf">split</span><span class="p">()[</span><span class="mi">0</span><span class="p">])</span> <span class="k">for</span> <span class="n">coord</span> <span class="ow">in</span> <span class="n">coordinates_str</span><span class="p">.</span><span class="nf">split</span><span class="p">(</span><span class="sh">'</span><span class="s">,</span><span class="sh">'</span><span class="p">)]</span> <span class="o">*</span> <span class="n">coord1_unit</span>
    <span class="n">coord2_list</span> <span class="o">=</span> <span class="p">[</span><span class="nf">float</span><span class="p">(</span><span class="n">coord</span><span class="p">.</span><span class="nf">split</span><span class="p">()[</span><span class="mi">1</span><span class="p">])</span> <span class="k">for</span> <span class="n">coord</span> <span class="ow">in</span> <span class="n">coordinates_str</span><span class="p">.</span><span class="nf">split</span><span class="p">(</span><span class="sh">'</span><span class="s">,</span><span class="sh">'</span><span class="p">)]</span> <span class="o">*</span> <span class="n">coord2_unit</span>
    <span class="n">vertices</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">if</span> <span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">frame</span><span class="sh">"</span><span class="p">]</span> <span class="o">==</span> <span class="sh">"</span><span class="s">heliocentric</span><span class="sh">"</span><span class="p">:</span>
    <span class="n">vertices</span> <span class="o">=</span> <span class="nc">SkyCoord</span><span class="p">(</span><span class="n">coord1_list</span><span class="p">,</span> <span class="n">coord2_list</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">*</span> <span class="nf">len</span><span class="p">(</span><span class="n">coord1_list</span><span class="p">)</span> <span class="o">*</span> <span class="n">u</span><span class="p">.</span><span class="n">AU</span><span class="p">,</span> <span class="n">representation_type</span><span class="o">=</span><span class="sh">"</span><span class="s">cylindrical</span><span class="sh">"</span><span class="p">,</span> <span class="n">frame</span><span class="o">=</span><span class="sh">"</span><span class="s">heliocentric</span><span class="sh">"</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
    <span class="n">vertices</span> <span class="o">=</span> <span class="nc">SkyCoord</span><span class="p">(</span><span class="n">coord1_list</span><span class="p">,</span> <span class="n">coord2_list</span><span class="p">,</span> <span class="n">frame</span><span class="o">=</span><span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">frame</span><span class="sh">"</span><span class="p">])</span>
    
    <span class="k">return</span> <span class="nc">PolygonSkyRegion</span><span class="p">(</span><span class="n">vertices</span> <span class="o">=</span> <span class="n">vertices</span><span class="p">)</span>
    </code></pre>
    
    </div>

