.. title: GSoC - 4
.. slug:
.. date: 2021-08-23 03:00:06 
.. tags: radis
.. author: Gagan Aryan
.. link: https://gagan-aryan.netlify.app/posts/gsoc-4/
.. description:
.. category: gsoc2021


.. raw:: html

    <p><img alt="Radis" src="https://gagan-aryan.netlify.app/images/gsoc-4/Radis.png" /></p>
    <p>Today is the last day of GSoC-21. The entire journey was a rollercoaster ride and I learnt a lot of new things along the way. I started out with hardly knowing any of the shortcomings of pandas and as we dug in, I was surprised to see so many loopholes it contains. This will be the final blogpost of my gsoc journey and I hope you like it.</p>
    <h2 id="pandas-and-vaex">Pandas and Vaex</h2>
    <!-- TEASER_END -->
    <h3 id="why-do-people-use-pandas-">Why do people use Pandas ?</h3>
    <p>Pandas is an open source Python package that is most widely used for data science/data analysis and machine learning tasks. It is built on top of another package named Numpy, which provides support for multi-dimensional arrays.</p>
    <p>Pandas makes it simple to do many of the time consuming, repetitive tasks associated with working with data, including:</p>
    <ul>
    <li>Data visualization</li>
    <li>Statistical analysis</li>
    <li>Data inspection</li>
    <li>Loading and saving data</li>
    <li>Data cleansing</li>
    <li>Data fill</li>
    <li>Data normalization</li>
    <li>Merges and joins</li>
    </ul>
    <p>As of the time I this blog was written pandas is arguably the most popular dataframe library that data scientists use. While pandas works smoothly while dealing with smaller data, it becomes very slow and inefficient when there are huge datasets.</p>
    <h3 id="why-use-vaex-">Why use Vaex ?</h3>
    <p>Vaex is a python library that is closely similar to Pandas. Vaex is a library especially for lazy Out-of-Core DataFrames, helps to visualize and explore big tabular datasets. It is a high performance library and can solve many of the shortcomings of pandas. As the API is similar to pandas, users do not face difficulty in shifting.</p>
    <p>Vaex is capable to calculate statistics such as mean, standard deviation etc, on an N-dimensional grid up to a billion (109109) objects/rows per second.</p>
    <h2 id="pandas-or-vaex-">Pandas or Vaex ?</h2>
    <p>Here at Radis the underlying algorithm was not able to perform to its maximum capacity due to usage of pandas which consumes way too much of memory. So we tried to see how vaex can help improve the performance.</p>
    <p>Below we are using <a href="https://hitran.org/hitemp/">HITEMP-N2O Database</a> for all checking the performance. It is to be noted that there is a difference between the pytables that pandas use and vaex friendly HDF5. The former is row-based whereas vaex friendly HDF5 files are column based.</p>
    <h3 id="loading-time">Loading time</h3>
    <p>In the code below we -</p>
    <ol>
    <li>load the the vaex HFD5 file and then convert it to pandas dataframe</li>
    <li>directly load the pandas hdf5 file</li>
    </ol>
    <div class="highlight"><div class="chroma">
    <table class="lntable"><tr><td class="lntd">
    <pre class="chroma"><code><span class="lnt"> 1
    </span><span class="lnt"> 2
    </span><span class="lnt"> 3
    </span><span class="lnt"> 4
    </span><span class="lnt"> 5
    </span><span class="lnt"> 6
    </span><span class="lnt"> 7
    </span><span class="lnt"> 8
    </span><span class="lnt"> 9
    </span><span class="lnt">10
    </span><span class="lnt">11
    </span><span class="lnt">12
    </span><span class="lnt">13
    </span><span class="lnt">14
    </span></code></pre></td>
    <td class="lntd">
    <pre class="chroma"><code class="language-python"><span class="o">&gt;</span> <span class="kn">from</span> <span class="nn">time</span> <span class="kn">import</span> <span class="n">time</span>
    <span class="o">&gt;</span> <span class="kn">import</span> <span class="nn">vaex</span>
    <span class="o">&gt;</span> <span class="n">t0</span> <span class="o">=</span> <span class="n">time</span><span class="p">()</span>
    <span class="o">&gt;</span> <span class="n">df</span> <span class="o">=</span> <span class="n">vaex</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">"~/.radisdb/N2O-04_HITEMP2019.hdf5"</span><span class="p">)</span>
    <span class="o">&gt;</span> <span class="n">df_pandas</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">to_pandas_df</span><span class="p">()</span>
    <span class="o">&gt;</span> <span class="k">print</span><span class="p">(</span><span class="n">time</span><span class="p">()</span><span class="o">-</span><span class="n">t0</span><span class="p">)</span>
    <span class="mf">7.833287477493286</span>
    <span class="o">&gt;</span> <span class="n">t0</span> <span class="o">=</span> <span class="n">time</span><span class="p">()</span>
    <span class="o">&gt;</span> <span class="kn">import</span> <span class="nn">pandas</span> <span class="kn">as</span> <span class="nn">pd</span>
    <span class="o">&gt;</span> <span class="n">df_pandas2</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_hdf</span><span class="p">(</span><span class="s2">"~/.radisdb/N2O-04_HITEMP2019.h5"</span><span class="p">)</span>
    <span class="o">&gt;</span> <span class="k">print</span><span class="p">(</span><span class="n">time</span><span class="p">()</span><span class="o">-</span><span class="n">t0</span><span class="p">)</span>
    <span class="mf">28.142656087875366</span>
    </code></pre></td></tr></table>
    </div>
    </div><p>Clearly the first appraoch is almost 4 times faster than the second one.</p>
    <h3 id="load-specific-columns">Load specific columns</h3>
    <p>As already stated, vaex hdf5 files are column based so loading only specific columns from vaex hdf5 file should be able give much better results than loading only specific columns in pandas. Lets check this and see the time taken to do both of these -</p>
    <div class="highlight"><div class="chroma">
    <table class="lntable"><tr><td class="lntd">
    <pre class="chroma"><code><span class="lnt"> 1
    </span><span class="lnt"> 2
    </span><span class="lnt"> 3
    </span><span class="lnt"> 4
    </span><span class="lnt"> 5
    </span><span class="lnt"> 6
    </span><span class="lnt"> 7
    </span><span class="lnt"> 8
    </span><span class="lnt"> 9
    </span><span class="lnt">10
    </span><span class="lnt">11
    </span></code></pre></td>
    <td class="lntd">
    <pre class="chroma"><code class="language-python"><span class="o">&gt;</span> <span class="n">t0</span> <span class="o">=</span> <span class="n">time</span><span class="p">()</span>
    <span class="o">&gt;</span> <span class="n">df</span> <span class="o">=</span> <span class="n">vaex</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">"~/.radisdb/N2O-04_HITEMP2019.hdf5"</span><span class="p">)</span>
    <span class="o">&gt;</span> <span class="n">df_pandas</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">to_pandas_df</span><span class="p">(</span><span class="n">column_names</span><span class="o">=</span><span class="p">[</span><span class="s2">"iso"</span><span class="p">,</span> <span class="s2">"wav"</span><span class="p">,</span> <span class="s2">"int"</span><span class="p">,</span> <span class="s2">"El"</span><span class="p">])</span>
    <span class="o">&gt;</span> <span class="k">print</span><span class="p">(</span><span class="n">time</span><span class="p">()</span><span class="o">-</span><span class="n">t0</span><span class="p">)</span>
    <span class="mf">0.1795198917388916</span>
    <span class="o">&gt;</span> <span class="n">t0</span> <span class="o">=</span> <span class="n">time</span><span class="p">()</span>
    <span class="o">&gt;</span> <span class="kn">import</span> <span class="nn">pandas</span> <span class="kn">as</span> <span class="nn">pd</span>
    <span class="o">&gt;</span> <span class="n">df_pandas2</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_hdf</span><span class="p">(</span><span class="s2">"~/.radisdb/N2O-04_HITEMP2019.h5"</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="p">[</span><span class="s2">"iso"</span><span class="p">,</span> <span class="s2">"wav"</span><span class="p">,</span> <span class="s2">"int"</span><span class="p">,</span> <span class="s2">"El"</span><span class="p">])</span>
    <span class="o">&gt;</span> <span class="k">print</span><span class="p">(</span><span class="n">time</span><span class="p">()</span><span class="o">-</span><span class="n">t0</span><span class="p">)</span>
    <span class="mf">22.85481858253479</span>
    </code></pre></td></tr></table>
    </div>
    </div><p>In comparison, loading 4 out of 19 columns is about 70% as slow with Pandas.</p>
    <h3 id="load-specific-rows">Load specific rows</h3>
    <p>To be fair to the pytables let&rsquo;s try to load specific rows and check if pandas can now provide better performance with its row indexed HDF5s.</p>
    <div class="highlight"><div class="chroma">
    <table class="lntable"><tr><td class="lntd">
    <pre class="chroma"><code><span class="lnt"> 1
    </span><span class="lnt"> 2
    </span><span class="lnt"> 3
    </span><span class="lnt"> 4
    </span><span class="lnt"> 5
    </span><span class="lnt"> 6
    </span><span class="lnt"> 7
    </span><span class="lnt"> 8
    </span><span class="lnt"> 9
    </span><span class="lnt">10
    </span><span class="lnt">11
    </span><span class="lnt">12
    </span></code></pre></td>
    <td class="lntd">
    <pre class="chroma"><code class="language-python"><span class="o">&gt;</span> <span class="n">t0</span> <span class="o">=</span> <span class="n">time</span><span class="p">()</span>
    <span class="o">&gt;</span> <span class="kn">import</span> <span class="nn">pandas</span> <span class="kn">as</span> <span class="nn">pd</span>
    <span class="o">&gt;</span> <span class="n">df_pandas2</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_hdf</span><span class="p">(</span><span class="s2">"~/.radisdb/N2O-04_HITEMP2019.h5"</span><span class="p">,</span> <span class="n">where</span><span class="o">=</span><span class="s2">"iso==1"</span><span class="p">)</span>
    <span class="o">&gt;</span> <span class="k">print</span><span class="p">(</span><span class="n">time</span><span class="p">()</span><span class="o">-</span><span class="n">t0</span><span class="p">)</span>
    <span class="mf">30.680099725723267</span>
    <span class="o">&gt;</span> <span class="n">t0</span> <span class="o">=</span> <span class="n">time</span><span class="p">()</span>
    <span class="o">&gt;</span> <span class="n">df</span> <span class="o">=</span> <span class="n">vaex</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">"~/.radisdb/N2O-04_HITEMP2019.hdf5"</span><span class="p">)</span>
    <span class="o">&gt;</span> <span class="n">df</span><span class="o">.</span><span class="n">select</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">iso</span> <span class="o">==</span> <span class="mi">1</span><span class="p">)</span>
    <span class="o">&gt;</span> <span class="n">df_pandas</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">to_pandas_df</span><span class="p">(</span><span class="n">selection</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
    <span class="o">&gt;</span> <span class="k">print</span><span class="p">(</span><span class="n">time</span><span class="p">()</span><span class="o">-</span><span class="n">t0</span><span class="p">)</span>
    <span class="mf">7.043155670166016</span>
    </code></pre></td></tr></table>
    </div>
    </div><p>Even in this case vaex provides better performance. So the idea was to harness this memory efficiency of vaex for all the I/O operations on the dataset in Radis. In order to do this I have written down a HDF5 writer that fetches <code>bz2</code> file and parses it into a column-major HDF5. The complete code to the HDF5 writer can be found <a href="https://gist.github.com/gagan-aryan/8ed5ba1f69074bbc72d081c31d43fcbd">in this gist</a>.</p>
    <p>That is it for GSoC21 from my side. Even though the second phase of my project got affected due to schools, I had an exciting summer as a whole. I am looking forward to be in touch with Radis and will try to contribute to it whenever I get a chance.</p>

