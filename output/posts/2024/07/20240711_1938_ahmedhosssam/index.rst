.. title: The project is almost finished
.. slug:
.. date: 2024-07-11 19:38:21 
.. tags: SunPy
.. author: Ahmed Hossam
.. link: https://dev.to/ahmedhosssam/the-project-is-almost-finished-1hfb
.. description:
.. category: gsoc2024


.. raw:: html

    <p>So, after I finished the main refactoring and the documentation strings, I started the testing phase.<br />
    I started with the smallest functions that don't call any non-tested function, and then went to the bigger functions.</p>
    
    <!-- TEASER_END -->
    <p>After finishing the main unit tests, I had a problem, the columns in the input data from the hek have different units, for example, for <code>event_coord1</code> we have some rows with degrees and others with arcsecond, and the result would be a column with one unit, the degrees are converted into arcseconds or vice versa. So me and my mentor decided to:</p>
    
    <ol>
    <li>Merge <code>event_coord1</code> and <code>event_coord2</code> and <code>event_coord3</code> into one <code>SkyCoord</code> object for every row.
    </li>
    </ol>
    <div class="highlight js-code-highlight">
    <pre class="highlight python"><code><span class="k">if</span> <span class="n">is_coord_prop</span><span class="p">:</span>
    <span class="n">event_coord_col</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">idx</span> <span class="ow">in</span> <span class="nf">range</span><span class="p">(</span><span class="nf">len</span><span class="p">(</span><span class="n">table</span><span class="p">[</span><span class="sh">'</span><span class="s">event_coord1</span><span class="sh">'</span><span class="p">])):</span>
    <span class="n">unit</span> <span class="o">=</span> <span class="nf">get_unit</span><span class="p">(</span><span class="n">table</span><span class="p">[</span><span class="sh">'</span><span class="s">event_coordunit</span><span class="sh">'</span><span class="p">][</span><span class="n">idx</span><span class="p">])</span>
    <span class="n">coord1</span> <span class="o">=</span> <span class="n">table</span><span class="p">[</span><span class="sh">'</span><span class="s">event_coord1</span><span class="sh">'</span><span class="p">][</span><span class="n">idx</span><span class="p">]</span>
    <span class="n">coord2</span> <span class="o">=</span> <span class="n">table</span><span class="p">[</span><span class="sh">'</span><span class="s">event_coord2</span><span class="sh">'</span><span class="p">][</span><span class="n">idx</span><span class="p">]</span>
    <span class="n">coord3</span> <span class="o">=</span> <span class="n">table</span><span class="p">[</span><span class="sh">'</span><span class="s">event_coord3</span><span class="sh">'</span><span class="p">][</span><span class="n">idx</span><span class="p">]</span>
    <span class="n">frame</span> <span class="o">=</span> <span class="sh">'</span><span class="s">helioprojective</span><span class="sh">'</span> <span class="k">if</span> <span class="n">unit</span><span class="o">==</span><span class="n">u</span><span class="p">.</span><span class="n">arcsec</span> <span class="k">else</span> <span class="sh">'</span><span class="s">icrs</span><span class="sh">'</span>
    <span class="k">if</span> <span class="n">coord3</span><span class="p">:</span>
    <span class="n">event_coord</span> <span class="o">=</span> <span class="nc">SkyCoord</span><span class="p">(</span><span class="n">coord1</span><span class="o">*</span><span class="n">unit</span><span class="p">,</span> <span class="n">coord2</span><span class="o">*</span><span class="n">unit</span><span class="p">,</span> <span class="n">coord3</span><span class="o">*</span><span class="n">unit</span><span class="p">,</span> <span class="n">frame</span><span class="o">=</span><span class="n">frame</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
    <span class="n">event_coord</span> <span class="o">=</span> <span class="nc">SkyCoord</span><span class="p">(</span><span class="n">coord1</span><span class="o">*</span><span class="n">unit</span><span class="p">,</span> <span class="n">coord2</span><span class="o">*</span><span class="n">unit</span><span class="p">,</span> <span class="n">frame</span><span class="o">=</span><span class="n">frame</span><span class="p">)</span>
    <span class="n">event_coord_col</span><span class="p">.</span><span class="nf">append</span><span class="p">(</span><span class="n">event_coord</span><span class="p">)</span>
    <span class="n">event_coord_col</span> <span class="o">=</span> <span class="nc">Column</span><span class="p">(</span><span class="n">event_coord_col</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="sh">'</span><span class="s">event_coord</span><span class="sh">'</span><span class="p">)</span>
    <span class="k">del</span> <span class="n">table</span><span class="p">[</span><span class="sh">'</span><span class="s">event_coord1</span><span class="sh">'</span><span class="p">]</span>
    <span class="k">del</span> <span class="n">table</span><span class="p">[</span><span class="sh">'</span><span class="s">event_coord2</span><span class="sh">'</span><span class="p">]</span>
    <span class="k">del</span> <span class="n">table</span><span class="p">[</span><span class="sh">'</span><span class="s">event_coord3</span><span class="sh">'</span><span class="p">]</span>
    <span class="n">table</span><span class="p">.</span><span class="nf">add_column</span><span class="p">(</span><span class="n">event_coord_col</span><span class="p">)</span>
    </code></pre>
    
    </div>
    
    
    <ol>
    <li>The other columns that has multiple units would be converted into astropy column first and then added to the table
    </li>
    </ol>
    <div class="highlight js-code-highlight">
    <pre class="highlight python"><code><span class="k">if</span> <span class="ow">not</span> <span class="n">attribute</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="sh">"</span><span class="s">is_chaincode</span><span class="sh">"</span><span class="p">):</span>
    <span class="n">new_column</span> <span class="o">=</span> <span class="nc">Column</span><span class="p">(</span><span class="n">new_column</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">table</span><span class="p">[</span><span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">name</span><span class="sh">"</span><span class="p">]],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">u</span><span class="p">.</span><span class="n">Quantity</span><span class="p">)</span>
    </code></pre>
    
    </div>
    
    
    <p>After this, I started a mission of checking the resulting columns and comparing them to the input and also to the expected results. And here I saw some surprises:<br />
    There are columns that don't even exist in the <a href="https://www.lmsal.com/hek/VOEvent_Spec.html" rel="noopener noreferrer">HEK Feature/Event Types definitions<br />
    </a>:</p>
    
    <ul>
    <li>hgc_coord</li>
    <li>hpc_coord</li>
    <li>hgs_coord</li>
    <li>hrc_coord</li>
    <li>hgc_boundcc</li>
    <li>hpc_boundcc</li>
    <li>hgs_boundcc</li>
    <li>hrc_boundcc</li>
    </ul>
    
    <p>So I had to add them into <code>coord_properties.json</code> file with double-checking the frames.</p>
    
    <p>hgc_coord, hpc_coord, hgs_coord, hrc_coord are points, so they had to be converted into <code>PointSkyRegion</code>.<br />
    And they were supported in <code>parse_chaincode</code>:<br />
    </p>
    
    <div class="highlight js-code-highlight">
    <pre class="highlight python"><code><span class="k">def</span> <span class="nf">parse_chaincode</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">attribute</span><span class="p">,</span> <span class="n">unit</span><span class="p">,</span> <span class="n">time</span><span class="p">):</span>
    <span class="p">.</span>
    <span class="p">.</span>
    <span class="p">.</span>
    <span class="k">if</span> <span class="n">attribute</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="sh">"</span><span class="s">is_point</span><span class="sh">"</span><span class="p">):</span>
    <span class="n">coordinates</span> <span class="o">=</span> <span class="n">value</span><span class="p">.</span><span class="nf">replace</span><span class="p">(</span><span class="sh">"</span><span class="s">POINT(</span><span class="sh">"</span><span class="p">,</span> <span class="sh">""</span><span class="p">).</span><span class="nf">replace</span><span class="p">(</span><span class="sh">"</span><span class="s">)</span><span class="sh">"</span><span class="p">,</span> <span class="sh">""</span><span class="p">).</span><span class="nf">split</span><span class="p">()</span>
    <span class="n">coord_list</span> <span class="o">=</span> <span class="p">[</span><span class="nf">float</span><span class="p">(</span><span class="n">coordinate</span><span class="p">)</span> <span class="k">for</span> <span class="n">coordinate</span> <span class="ow">in</span> <span class="n">coordinates</span><span class="p">]</span>
    <span class="n">coord_list</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*=</span> <span class="n">coord1_unit</span>
    <span class="n">coord_list</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">*=</span> <span class="n">coord2_unit</span>
    <span class="k">if</span> <span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">frame</span><span class="sh">"</span><span class="p">]</span> <span class="o">==</span> <span class="sh">"</span><span class="s">heliocentric</span><span class="sh">"</span><span class="p">:</span>
    <span class="n">center_sky</span> <span class="o">=</span> <span class="nc">SkyCoord</span><span class="p">(</span><span class="n">coord_list</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">coord_list</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">*</span> <span class="nf">len</span><span class="p">(</span><span class="n">coord_list</span><span class="p">)</span> <span class="o">*</span> <span class="n">u</span><span class="p">.</span><span class="n">AU</span><span class="p">,</span> <span class="n">obstime</span><span class="o">=</span><span class="n">time</span><span class="p">,</span> <span class="n">observer</span><span class="o">=</span><span class="n">observer</span><span class="p">,</span> <span class="n">representation_type</span><span class="o">=</span><span class="sh">"</span><span class="s">cylindrical</span><span class="sh">"</span><span class="p">,</span> <span class="n">frame</span><span class="o">=</span><span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">frame</span><span class="sh">"</span><span class="p">])</span>
    <span class="k">return</span> <span class="nc">PolygonSkyRegion</span><span class="p">(</span><span class="n">vertices</span><span class="o">=</span><span class="n">center_sky</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
    <span class="n">center_sky</span> <span class="o">=</span> <span class="nc">SkyCoord</span><span class="p">(</span><span class="n">coord_list</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">coord_list</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="n">obstime</span><span class="o">=</span><span class="n">time</span><span class="p">,</span> <span class="n">observer</span><span class="o">=</span><span class="n">observer</span><span class="p">,</span> <span class="n">frame</span><span class="o">=</span><span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">frame</span><span class="sh">"</span><span class="p">])</span>
    <span class="k">return</span> <span class="nc">PointSkyRegion</span><span class="p">(</span><span class="n">center</span><span class="o">=</span><span class="n">center_sky</span><span class="p">)</span>
    <span class="p">.</span>
    <span class="p">.</span>
    <span class="p">.</span>
    </code></pre>
    
    </div>
    
    
    
    <p>So far so good.</p>
    
    <p>Also, some tests in <code>test_hek</code> were simplified, instead of checking if the object is instance of PolygonSkyRegion or PointSkyRegion, we can just check if it's instance of SkyRegion which is the base class for all regions defined in celestial coordinates.</p>
    
    <p>Also, another update to <code>parse_chaincode</code>, the observation time were added to the parameter to be added to all the region objects. We used the column <code>event_starttime</code> to specify the obstime of the event. And we also I added the observer as <code>earth</code>, I still don't know if this would be correct for the different conditions and different queries of the hek, but we will see, and also I wrote a comment to highlight the assumption.</p>
    
    <p>Here is the complete implementation of <code>parse_chaincode</code>:<br />
    </p>
    
    <div class="highlight js-code-highlight">
    <pre class="highlight python"><code><span class="k">def</span> <span class="nf">parse_chaincode</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">attribute</span><span class="p">,</span> <span class="n">unit</span><span class="p">,</span> <span class="n">time</span><span class="p">):</span>
    <span class="sh">"""</span><span class="s">
    Parses a string representation of coordinates and convert them into a PolygonSkyRegion object
    using units based on the specified coordinate frame.
    
    Parameters
    ----------
    value : str
    A polygon defined using vertices in sky coordinates.
    attribute : dict
    An object from </span><span class="sh">"</span><span class="s">coord_properties.json</span><span class="sh">"</span><span class="s">
    unit : str
    The unit of the coordinates
    time : `~astropy.time.core.Time`
    An event_starttime row parsed into astropy time.
    
    Returns
    -------
    `PolygonSkyRegion`
    A polygon defined using vertices in sky coordinates.
    
    Raises
    ------
    IndexError
    Because ``value`` does not contain the expected </span><span class="sh">'</span><span class="s">((</span><span class="sh">'</span><span class="s"> and </span><span class="sh">'</span><span class="s">))</span><span class="sh">'</span><span class="s"> substrings.
    UnitConversionError
    Because the units set by ``coord1_unit`` or ``coord2_unit`` are incompatible with the values being assigned.
    </span><span class="sh">"""</span>
    <span class="n">observer</span> <span class="o">=</span> <span class="sh">'</span><span class="s">earth</span><span class="sh">'</span> <span class="c1"># There is an assumption that earth is the observer.
    </span>    <span class="n">coord1_unit</span> <span class="o">=</span> <span class="n">u</span><span class="p">.</span><span class="n">deg</span>
    <span class="n">coord2_unit</span> <span class="o">=</span> <span class="n">u</span><span class="p">.</span><span class="n">deg</span>
    <span class="k">if</span> <span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">frame</span><span class="sh">"</span><span class="p">]</span> <span class="o">==</span> <span class="sh">"</span><span class="s">helioprojective</span><span class="sh">"</span><span class="p">:</span>
    <span class="n">coord1_unit</span> <span class="o">=</span> <span class="n">u</span><span class="p">.</span><span class="n">arcsec</span>
    <span class="n">coord2_unit</span> <span class="o">=</span> <span class="n">u</span><span class="p">.</span><span class="n">arcsec</span>
    <span class="k">elif</span> <span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">frame</span><span class="sh">"</span><span class="p">]</span> <span class="o">==</span> <span class="sh">"</span><span class="s">heliocentric</span><span class="sh">"</span><span class="p">:</span>
    <span class="n">coord1_unit</span> <span class="o">=</span> <span class="n">u</span><span class="p">.</span><span class="n">R_sun</span> <span class="c1"># Nominal solar radius
    </span>    <span class="k">elif</span> <span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">frame</span><span class="sh">"</span><span class="p">]</span> <span class="o">==</span> <span class="sh">"</span><span class="s">icrs</span><span class="sh">"</span><span class="p">:</span>
    <span class="n">coord1_unit</span> <span class="o">=</span> <span class="nf">get_unit</span><span class="p">(</span><span class="n">unit</span><span class="p">)</span>
    <span class="n">coord2_unit</span> <span class="o">=</span> <span class="nf">get_unit</span><span class="p">(</span><span class="n">unit</span><span class="p">)</span>
    
    <span class="k">if</span> <span class="n">attribute</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="sh">"</span><span class="s">is_point</span><span class="sh">"</span><span class="p">):</span>
    <span class="n">coordinates</span> <span class="o">=</span> <span class="n">value</span><span class="p">.</span><span class="nf">replace</span><span class="p">(</span><span class="sh">"</span><span class="s">POINT(</span><span class="sh">"</span><span class="p">,</span> <span class="sh">""</span><span class="p">).</span><span class="nf">replace</span><span class="p">(</span><span class="sh">"</span><span class="s">)</span><span class="sh">"</span><span class="p">,</span> <span class="sh">""</span><span class="p">).</span><span class="nf">split</span><span class="p">()</span>
    <span class="n">coord_list</span> <span class="o">=</span> <span class="p">[</span><span class="nf">float</span><span class="p">(</span><span class="n">coordinate</span><span class="p">)</span> <span class="k">for</span> <span class="n">coordinate</span> <span class="ow">in</span> <span class="n">coordinates</span><span class="p">]</span>
    <span class="n">coord_list</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*=</span> <span class="n">coord1_unit</span>
    <span class="n">coord_list</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">*=</span> <span class="n">coord2_unit</span>
    <span class="k">if</span> <span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">frame</span><span class="sh">"</span><span class="p">]</span> <span class="o">==</span> <span class="sh">"</span><span class="s">heliocentric</span><span class="sh">"</span><span class="p">:</span>
    <span class="n">center_sky</span> <span class="o">=</span> <span class="nc">SkyCoord</span><span class="p">(</span><span class="n">coord_list</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">coord_list</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">*</span> <span class="nf">len</span><span class="p">(</span><span class="n">coord_list</span><span class="p">)</span> <span class="o">*</span> <span class="n">u</span><span class="p">.</span><span class="n">AU</span><span class="p">,</span> <span class="n">obstime</span><span class="o">=</span><span class="n">time</span><span class="p">,</span> <span class="n">observer</span><span class="o">=</span><span class="n">observer</span><span class="p">,</span> <span class="n">representation_type</span><span class="o">=</span><span class="sh">"</span><span class="s">cylindrical</span><span class="sh">"</span><span class="p">,</span> <span class="n">frame</span><span class="o">=</span><span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">frame</span><span class="sh">"</span><span class="p">])</span>
    <span class="k">return</span> <span class="nc">PolygonSkyRegion</span><span class="p">(</span><span class="n">vertices</span><span class="o">=</span><span class="n">center_sky</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
    <span class="n">center_sky</span> <span class="o">=</span> <span class="nc">SkyCoord</span><span class="p">(</span><span class="n">coord_list</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">coord_list</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="n">obstime</span><span class="o">=</span><span class="n">time</span><span class="p">,</span> <span class="n">observer</span><span class="o">=</span><span class="n">observer</span><span class="p">,</span> <span class="n">frame</span><span class="o">=</span><span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">frame</span><span class="sh">"</span><span class="p">])</span>
    <span class="k">return</span> <span class="nc">PointSkyRegion</span><span class="p">(</span><span class="n">center</span><span class="o">=</span><span class="n">center_sky</span><span class="p">)</span>
    <span class="n">coordinates_str</span> <span class="o">=</span> <span class="n">value</span><span class="p">.</span><span class="nf">split</span><span class="p">(</span><span class="sh">'</span><span class="s">((</span><span class="sh">'</span><span class="p">)[</span><span class="mi">1</span><span class="p">].</span><span class="nf">split</span><span class="p">(</span><span class="sh">'</span><span class="s">))</span><span class="sh">'</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
    <span class="n">coord1_list</span> <span class="o">=</span> <span class="p">[</span><span class="nf">float</span><span class="p">(</span><span class="n">coord</span><span class="p">.</span><span class="nf">split</span><span class="p">()[</span><span class="mi">0</span><span class="p">])</span> <span class="k">for</span> <span class="n">coord</span> <span class="ow">in</span> <span class="n">coordinates_str</span><span class="p">.</span><span class="nf">split</span><span class="p">(</span><span class="sh">'</span><span class="s">,</span><span class="sh">'</span><span class="p">)]</span> <span class="o">*</span> <span class="n">coord1_unit</span>
    <span class="n">coord2_list</span> <span class="o">=</span> <span class="p">[</span><span class="nf">float</span><span class="p">(</span><span class="n">coord</span><span class="p">.</span><span class="nf">split</span><span class="p">()[</span><span class="mi">1</span><span class="p">])</span> <span class="k">for</span> <span class="n">coord</span> <span class="ow">in</span> <span class="n">coordinates_str</span><span class="p">.</span><span class="nf">split</span><span class="p">(</span><span class="sh">'</span><span class="s">,</span><span class="sh">'</span><span class="p">)]</span> <span class="o">*</span> <span class="n">coord2_unit</span>
    <span class="n">vertices</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">if</span> <span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">frame</span><span class="sh">"</span><span class="p">]</span> <span class="o">==</span> <span class="sh">"</span><span class="s">heliocentric</span><span class="sh">"</span><span class="p">:</span>
    <span class="n">vertices</span> <span class="o">=</span> <span class="nc">SkyCoord</span><span class="p">(</span><span class="n">coord1_list</span><span class="p">,</span> <span class="n">coord2_list</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">*</span> <span class="nf">len</span><span class="p">(</span><span class="n">coord1_list</span><span class="p">)</span> <span class="o">*</span> <span class="n">u</span><span class="p">.</span><span class="n">AU</span><span class="p">,</span> <span class="n">obstime</span><span class="o">=</span><span class="n">time</span><span class="p">,</span> <span class="n">observer</span><span class="o">=</span><span class="n">observer</span><span class="p">,</span> <span class="n">representation_type</span><span class="o">=</span><span class="sh">"</span><span class="s">cylindrical</span><span class="sh">"</span><span class="p">,</span> <span class="n">frame</span><span class="o">=</span><span class="sh">"</span><span class="s">heliocentric</span><span class="sh">"</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
    <span class="n">vertices</span> <span class="o">=</span> <span class="nc">SkyCoord</span><span class="p">(</span><span class="n">coord1_list</span><span class="p">,</span> <span class="n">coord2_list</span><span class="p">,</span> <span class="n">obstime</span><span class="o">=</span><span class="n">time</span><span class="p">,</span> <span class="n">observer</span><span class="o">=</span><span class="n">observer</span><span class="p">,</span> <span class="n">frame</span><span class="o">=</span><span class="n">attribute</span><span class="p">[</span><span class="sh">"</span><span class="s">frame</span><span class="sh">"</span><span class="p">])</span>
    
    <span class="k">return</span> <span class="nc">PolygonSkyRegion</span><span class="p">(</span><span class="n">vertices</span><span class="o">=</span><span class="n">vertices</span><span class="p">)</span>
    </code></pre>
    
    </div>
    
    
    
    <p>One major outcome of this project was to make using hek and acquiring data from it easy, and this happened when I saw some errors from the CI and when I checked it I saw that one example of <code>overplot_hek_polygon.py</code> should be modified due to the interface changing and the returned data types.<br />
    This was the initial using of hek in this example:<br />
    </p>
    
    <div class="highlight js-code-highlight">
    <pre class="highlight python"><code><span class="n">ch</span> <span class="o">=</span> <span class="n">responses</span><span class="p">[</span><span class="n">response_index</span><span class="p">]</span>
    <span class="n">p1</span> <span class="o">=</span> <span class="n">ch</span><span class="p">[</span><span class="sh">"</span><span class="s">hpc_boundcc</span><span class="sh">"</span><span class="p">][</span><span class="mi">9</span><span class="p">:</span><span class="o">-</span><span class="mi">2</span><span class="p">]</span>
    <span class="n">p2</span> <span class="o">=</span> <span class="n">p1</span><span class="p">.</span><span class="nf">split</span><span class="p">(</span><span class="sh">'</span><span class="s">,</span><span class="sh">'</span><span class="p">)</span>
    <span class="n">p3</span> <span class="o">=</span> <span class="p">[</span><span class="n">v</span><span class="p">.</span><span class="nf">split</span><span class="p">(</span><span class="sh">"</span><span class="s"> </span><span class="sh">"</span><span class="p">)</span> <span class="k">for</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">p2</span><span class="p">]</span>
    <span class="n">ch_date</span> <span class="o">=</span> <span class="nf">parse_time</span><span class="p">(</span><span class="n">ch</span><span class="p">[</span><span class="sh">'</span><span class="s">event_starttime</span><span class="sh">'</span><span class="p">])</span>
    <span class="n">ch_boundary</span> <span class="o">=</span> <span class="n">responses</span><span class="p">[</span><span class="n">response_index</span><span class="p">][</span><span class="sh">"</span><span class="s">hpc_boundcc</span><span class="sh">"</span><span class="p">]</span>
    
    <span class="c1">##############################################################################
    # The coronal hole was detected at different time than the AIA image was
    # taken so we need to rotate it to the map observation time.
    </span>
    <span class="n">ch_boundary</span> <span class="o">=</span> <span class="nc">SkyCoord</span><span class="p">(</span>
    <span class="p">[(</span><span class="nf">float</span><span class="p">(</span><span class="n">v</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span> <span class="nf">float</span><span class="p">(</span><span class="n">v</span><span class="p">[</span><span class="mi">1</span><span class="p">]))</span> <span class="o">*</span> <span class="n">u</span><span class="p">.</span><span class="n">arcsec</span> <span class="k">for</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">p3</span><span class="p">],</span>
    <span class="n">obstime</span><span class="o">=</span><span class="n">ch_date</span><span class="p">,</span> <span class="n">observer</span><span class="o">=</span><span class="sh">"</span><span class="s">earth</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">frame</span><span class="o">=</span><span class="n">frames</span><span class="p">.</span><span class="n">Helioprojective</span><span class="p">)</span>
    <span class="n">rotated_ch_boundary</span> <span class="o">=</span> <span class="nf">solar_rotate_coordinate</span><span class="p">(</span><span class="n">ch_boundary</span><span class="p">,</span> <span class="n">time</span><span class="o">=</span><span class="n">aia_map</span><span class="p">.</span><span class="n">date</span><span class="p">)</span>
    </code></pre>
    
    </div>
    
    
    
    <p>And now it became this:<br />
    </p>
    
    <div class="highlight js-code-highlight">
    <pre class="highlight python"><code><span class="n">ch</span> <span class="o">=</span> <span class="n">responses</span><span class="p">[</span><span class="n">response_index</span><span class="p">]</span>
    <span class="n">ch_boundary</span> <span class="o">=</span> <span class="n">responses</span><span class="p">[</span><span class="n">response_index</span><span class="p">][</span><span class="sh">"</span><span class="s">hpc_boundcc</span><span class="sh">"</span><span class="p">].</span><span class="n">vertices</span>
    
    <span class="c1"># The coronal hole was detected at different time than the AIA image was
    # taken so we need to rotate it to the map observation time.
    </span>
    <span class="n">rotated_ch_boundary</span> <span class="o">=</span> <span class="nf">solar_rotate_coordinate</span><span class="p">(</span><span class="n">ch_boundary</span><span class="p">,</span> <span class="n">time</span><span class="o">=</span><span class="n">aia_map</span><span class="p">.</span><span class="n">date</span><span class="p">)</span>
    </code></pre>
    
    </div>
    
    
    
    <p>Yeah, and that's it.<br />
    The remaining parts are writing the user documentation, and double-checking the returned data from different events and different queries.</p>

