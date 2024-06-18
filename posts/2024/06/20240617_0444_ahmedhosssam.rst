.. title: Finishing implementation and doc strings
.. slug:
.. date: 2024-06-17 04:44:45 
.. tags: SunPy
.. author: Ahmed Hossam
.. link: https://dev.to/ahmedhosssam/finishing-implementation-and-doc-strings-4c2a
.. description:
.. category: gsoc2024


.. raw:: html

    <p>The main implementation and documentation strings phase has been finished.</p>
    
    <p>One of the functions that have been deleted was <code>parse_unit</code>, it almost wasn't triggered by any event of HEK events, so I decided to delete it, and we will see in the future if it has any major effects on the code.</p>
    <!-- TEASER_END -->
    
    <p>Also <code>parse_columns_to_table</code> has been refactored by adding more variables to make the code more readable.</p>
    
    <p>This is the new implementation:<br />
    </p>
    
    <div class="highlight js-code-highlight">
    <pre class="highlight python"><code><span class="k">def</span> <span class="nf">parse_columns_to_table</span><span class="p">(</span><span class="n">table</span><span class="p">,</span> <span class="n">attributes</span><span class="p">,</span> <span class="n">is_coord_prop</span> <span class="o">=</span> <span class="bp">False</span><span class="p">):</span>
    <span class="sh">"""</span><span class="s">
    Parses the columns in an Astropy table and convert the values into Astropy objects.
    
    Parameters
    ----------
    table: astropy.table
    Astropy table.
    attributes: list
    A list of HEK unit attributes or coordinate attributes.
    is_coord_prop: bool
    To specify if `attributes` is a list of unit attributes or coordinate attributes.
    
    Returns
    -------
    `astropy.table`
    
    Raises
    ------
    TypeError
    If `table` is not an Astropy table.
    KeyError
    If any of the attribute dictionaries are missing required keys (i.e. </span><span class="sh">"</span><span class="s">name</span><span class="sh">"</span><span class="s">, </span><span class="sh">"</span><span class="s">unit_prop</span><span class="sh">"</span><span class="s">).
    </span><span class="sh">"""</span>
    <span class="k">for</span> <span class="n">attribute</span> <span class="ow">in</span> <span class="n">attributes</span><span class="p">:</span>
    <span class="k">if</span> <span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">name</span><span class="sh">"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">table</span><span class="p">.</span><span class="n">colnames</span> <span class="ow">and</span> <span class="p">(</span><span class="sh">"</span><span class="s">unit_prop</span><span class="sh">"</span> <span class="ow">in</span> <span class="n">attribute</span> <span class="ow">or</span> <span class="n">attribute</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="sh">"</span><span class="s">is_chaincode</span><span class="sh">"</span><span class="p">,</span> <span class="bp">False</span><span class="p">))</span> <span class="ow">and</span> <span class="n">attribute</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="sh">"</span><span class="s">is_unit_prop</span><span class="sh">"</span><span class="p">,</span> <span class="bp">True</span><span class="p">):</span>
    <span class="n">unit_attr</span> <span class="o">=</span> <span class="sh">""</span>
    <span class="k">if</span> <span class="n">is_coord_prop</span><span class="p">:</span>
    <span class="n">unit_attr</span> <span class="o">=</span> <span class="sh">"</span><span class="s">event_coordunit</span><span class="sh">"</span>
    <span class="k">else</span><span class="p">:</span>
    <span class="n">unit_attr</span> <span class="o">=</span> <span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">unit_prop</span><span class="sh">"</span><span class="p">]</span>
    
    <span class="n">new_column</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="nf">enumerate</span><span class="p">(</span><span class="n">table</span><span class="p">[</span><span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">name</span><span class="sh">"</span><span class="p">]]):</span>
    <span class="n">new_value</span> <span class="o">=</span> <span class="sh">""</span>
    <span class="k">if</span> <span class="n">value</span> <span class="ow">in</span> <span class="p">[</span><span class="sh">""</span><span class="p">,</span> <span class="bp">None</span><span class="p">]:</span>
    <span class="n">new_value</span> <span class="o">=</span> <span class="n">value</span>
    <span class="k">elif</span> <span class="n">attribute</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="sh">"</span><span class="s">is_chaincode</span><span class="sh">"</span><span class="p">,</span> <span class="bp">False</span><span class="p">):</span>
    <span class="n">new_value</span> <span class="o">=</span> <span class="nf">parse_chaincode</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">attribute</span><span class="p">,</span> <span class="n">table</span><span class="p">[</span><span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">unit_prop</span><span class="sh">"</span><span class="p">]][</span><span class="n">idx</span><span class="p">])</span>
    <span class="k">else</span><span class="p">:</span>
    <span class="n">unit</span> <span class="o">=</span> <span class="nf">get_unit</span><span class="p">(</span><span class="n">table</span><span class="p">[</span><span class="n">unit_attr</span><span class="p">][</span><span class="n">idx</span><span class="p">])</span>
    <span class="n">new_value</span> <span class="o">=</span> <span class="n">value</span> <span class="o">*</span> <span class="n">unit</span>
    <span class="n">new_column</span><span class="p">.</span><span class="nf">append</span><span class="p">(</span><span class="n">new_value</span><span class="p">)</span>
    
    <span class="n">table</span><span class="p">[</span><span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">name</span><span class="sh">"</span><span class="p">]]</span> <span class="o">=</span> <span class="n">new_column</span>
    
    <span class="k">for</span> <span class="n">attribute</span> <span class="ow">in</span> <span class="n">attributes</span><span class="p">:</span>
    <span class="k">if</span> <span class="n">attribute</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="sh">"</span><span class="s">is_unit_prop</span><span class="sh">"</span><span class="p">,</span> <span class="bp">False</span><span class="p">)</span> <span class="ow">and</span> <span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">name</span><span class="sh">"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">table</span><span class="p">.</span><span class="n">colnames</span><span class="p">:</span>
    <span class="k">del</span> <span class="n">table</span><span class="p">[</span><span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">name</span><span class="sh">"</span><span class="p">]]</span>
    <span class="k">return</span> <span class="n">table</span>
    
    </code></pre>
    
    </div>
    
    
    
    <p>Also a public interface <code>__all__</code> has been added to <code>util.py</code>, until now, the public "api" for <code>util.py</code> is:<br />
    </p>
    
    <div class="highlight js-code-highlight">
    <pre class="highlight python"><code><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span>
    <span class="sh">'</span><span class="s">freeze</span><span class="sh">'</span><span class="p">,</span>
    <span class="sh">'</span><span class="s">parse_times</span><span class="sh">'</span><span class="p">,</span>
    <span class="sh">'</span><span class="s">parse_values_to_quantities</span><span class="sh">'</span><span class="p">,</span>
    <span class="sh">'</span><span class="s">UNIT_FILE_PATH</span><span class="sh">'</span><span class="p">,</span>
    <span class="sh">'</span><span class="s">COORD_FILE_PATH</span><span class="sh">'</span>
    <span class="p">]</span>
    </code></pre>
    
    </div>
    
    
    
    <p><code>UNIT_FILE_PATH</code> and <code>COORD_FILE_PATH</code> are used in <code>test_hek.py</code></p>
    
    <p>There was a problem in <code>get_unit</code> because of some units that wasn't parsed correctly, one of them is <code>ergs per cubic centimeter</code>, because of the first implementation of <code>get_unit</code>:<br />
    </p>
    
    <div class="highlight js-code-highlight">
    <pre class="highlight python"><code><span class="k">with</span> <span class="n">u</span><span class="p">.</span><span class="nf">add_enabled_units</span><span class="p">([</span><span class="n">cm2</span><span class="p">,</span> <span class="n">m2</span><span class="p">,</span> <span class="n">m3</span><span class="p">]),</span> <span class="n">u</span><span class="p">.</span><span class="nf">set_enabled_aliases</span><span class="p">(</span><span class="n">aliases</span><span class="p">):</span>
    <span class="c1"># Units for coordinate frames have more than one unit, otherwise it will be just one unit.
    </span>        <span class="c1"># There is an assumption that coord1_unit, coord2_unit and coord3_unit are the same.
    </span>        <span class="n">units</span> <span class="o">=</span> <span class="n">re</span><span class="p">.</span><span class="nf">split</span><span class="p">(</span><span class="sa">r</span><span class="sh">'</span><span class="s">[, ]</span><span class="sh">'</span><span class="p">,</span> <span class="n">unit</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">u</span><span class="p">.</span><span class="nc">Unit</span><span class="p">(</span><span class="n">units</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="nf">lower</span><span class="p">())</span>
    </code></pre>
    
    </div>
    
    
    
    <p>The function was taking the first "word" of the input and returns the unit, obviously this will be wrong with <code>ergs per cubic centimeter</code> because it will take only <code>ergs</code> and returns <code>u.Unit('erg')</code>.<br />
    But this is the only case with HEK units, the other units works just fine.<br />
    This is the new implementation to correct this behavior:<br />
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
    <span class="n">erg_per_cm3</span> <span class="o">=</span> <span class="n">u</span><span class="p">.</span><span class="nf">def_unit</span><span class="p">(</span><span class="sh">"</span><span class="s">ergs/cm^3</span><span class="sh">"</span><span class="p">,</span> <span class="n">u</span><span class="p">.</span><span class="n">erg</span><span class="o">/</span><span class="n">u</span><span class="p">.</span><span class="n">ml</span><span class="p">)</span>
    
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
    <span class="sh">"</span><span class="s">ergs per cubic centimeter</span><span class="sh">"</span><span class="p">:</span> <span class="n">erg_per_cm3</span><span class="p">,</span>
    <span class="p">}</span>
    <span class="k">with</span> <span class="n">u</span><span class="p">.</span><span class="nf">add_enabled_units</span><span class="p">([</span><span class="n">cm2</span><span class="p">,</span> <span class="n">m2</span><span class="p">,</span> <span class="n">m3</span><span class="p">]),</span> <span class="n">u</span><span class="p">.</span><span class="nf">set_enabled_aliases</span><span class="p">(</span><span class="n">aliases</span><span class="p">),</span> <span class="n">warnings</span><span class="p">.</span><span class="nf">catch_warnings</span><span class="p">():</span>
    <span class="c1"># Units for coordinate frames have more than one unit, otherwise it will be just one unit.
    </span>        <span class="c1"># There is an assumption that coord1_unit, coord2_unit and coord3_unit are the same.
    </span>        <span class="n">warnings</span><span class="p">.</span><span class="nf">filterwarnings</span><span class="p">(</span><span class="sh">"</span><span class="s">ignore</span><span class="sh">"</span><span class="p">,</span> <span class="n">category</span><span class="o">=</span><span class="n">u</span><span class="p">.</span><span class="n">UnitsWarning</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">unit</span> <span class="ow">in</span> <span class="n">aliases</span><span class="p">:</span>
    <span class="n">unit</span> <span class="o">=</span> <span class="n">u</span><span class="p">.</span><span class="nc">Unit</span><span class="p">(</span><span class="n">aliases</span><span class="p">[</span><span class="n">unit</span><span class="p">])</span>
    <span class="k">else</span><span class="p">:</span>
    <span class="n">unit</span> <span class="o">=</span> <span class="n">u</span><span class="p">.</span><span class="nc">Unit</span><span class="p">(</span><span class="n">re</span><span class="p">.</span><span class="nf">split</span><span class="p">(</span><span class="sa">r</span><span class="sh">'</span><span class="s">[, ]</span><span class="sh">'</span><span class="p">,</span> <span class="n">unit</span><span class="p">)[</span><span class="mi">0</span><span class="p">].</span><span class="nf">lower</span><span class="p">())</span>
    <span class="k">return</span> <span class="n">unit</span>
    </code></pre>
    
    </div>
    
    
    
    <p>Also, the units warnings were ignored because it's irrelevant to the user of HEK.</p>
    
    <p>So, the next phase is testing, we will see if our assumptions about the unit parsing and the other refactoring were right or not.</p>

