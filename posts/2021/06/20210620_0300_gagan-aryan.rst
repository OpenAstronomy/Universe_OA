.. title: GSoC - 1
.. slug:
.. date: 2021-06-20 03:00:06 
.. tags: radis
.. author: Gagan Aryan
.. link: https://gagan-aryan.netlify.app/posts/gsoc-1/
.. description:
.. category: gsoc2021


.. raw:: html

    <p>This is the first blog that documents the coding period of my GSoC21 journey. I learnt a few interesting things in these two weeks, as I expected I would. So, let&rsquo;s dive in and see if you knew few of these stuff I learnt.</p>
    <h2 id="starting-off-">Starting off !!!</h2>
    <p>I started off by getting a brief idea of the scope of the changes that could be done to the dataframe. This was the task I had decided on for the first week. Whenever we are involved in a project that runs for a period of anywhere between 2-4 months it is important to have a timeline or a roadmap of sorts to be able to look back to. This doesn&rsquo;t really have to be something rigid. We can chose to deviate from it and infact deviations are bound to happen due to multiple reasons. It can happen because of an unexpected bug in between, or because you came across some alternative that you did not consider at the start or simply because it is one of those projects that gives better insights as you dwell into it.</p>
    <!-- TEASER_END -->
    <p>Every good GSoC proposal consists of a tentative timeline that depicts the work we plan on doing as the weeks progress. Here is the timeline I had submitted in my proposal.</p>
    <p><img alt="Timeline1" src="https://gagan-aryan.netlify.app/images/gsoc-1/timeline1.png" /><br />
    <img alt="Timeline2" src="https://gagan-aryan.netlify.app/images/gsoc-1/timeline2.png" /></p>
    <p>So as per this I was supposed to finish off the refactors to the dataframe and also finish setting up the benchamarks. But I was unable to complete these. I had underestimated the work it would take to complete them. Nonetheless, I also did have some time to look up at the things I am supposed to do in the second half of the coding period.</p>
    <h2 id="memory-and-time-performance-benchmarks---tic-tok">Memory and Time performance benchmarks - Tic-Tok</h2>
    <p>Before making any changes to the codebase Erwan suggested me to have the benchmarks setup. So what do I mean by this? To make sure that the changes I am making to the code are indeed reducing the memory consumption of the computations we use a few tools that help us track the memory consumption for various calculations as a function of git commits. There are multiple tools that help us do this. Radis already used a tool developed by <a href="https://github.com/airspeed-velocity/asv">airspeed velocity</a> to track the memory computions. I ran into a lot of troubles in setting these up and a lost a lot of valuable time in the process ultimately Erwan fixed it and I was able to run the benchmarks on my machine.</p>
    <p>The benchmarks still seem to take a lot of time to run though and for them to be feasible to be used a tool through which I can check the performance regularly there are a few things I need to learn. I hope to pick these up in the next few days.</p>
    <p><img alt="Performance" src="https://gagan-aryan.netlify.app/images/gsoc-1/brace-yourselves.png" /></p>
    <p>We are also trying to look at a few other alternatives that can be used instead of asv. I will update the you guys regarding this in the next blog post.</p>
    <h2 id="oh-pandas-here-i-deal-with-you-">Oh Pandas here I deal with you !</h2>
    <h3 id="lets-ditch-a-few-columns">Let&rsquo;s ditch a few columns</h3>
    <p>We can reduce the memory usage of pandas by using one really simple trick - avoid giving loading the columns that are not required for computation. Below I demostrate how just dropping a few columns can provide significant improvement in the memory consumption. I am using <code>HITEMP-CH4</code> database for demonstration.</p>
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
    </span></code></pre></td>
    <td class="lntd">
    <pre class="chroma"><code class="language-python"><span class="o">&gt;&gt;&gt;</span> <span class="kn">from</span> <span class="nn">radis.io.hitran</span> <span class="kn">import</span> <span class="n">hit2df</span>
    <span class="o">&gt;&gt;&gt;</span> <span class="n">df</span> <span class="o">=</span> <span class="n">hit2df</span><span class="p">(</span><span class="s2">"06_HITEMP2020_2000.0-2500.0.par"</span><span class="p">)</span>
    <span class="o">...</span>
    <span class="o">&gt;&gt;&gt;</span> <span class="n">df</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="n">verbose</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">memory_usage</span><span class="o">=</span><span class="s2">"deep"</span><span class="p">)</span>
    <span class="o">...</span>
    <span class="n">memory</span> <span class="n">usage</span><span class="p">:</span> <span class="mf">30.5</span> <span class="n">MB</span>
    <span class="o">&gt;&gt;&gt;</span> <span class="n">df</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="s2">"id"</span><span class="p">,</span> <span class="s2">"iso"</span><span class="p">],</span> <span class="n">inplace</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
    <span class="o">&gt;&gt;&gt;</span> <span class="n">df</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="n">verbose</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">memory_usage</span><span class="o">=</span><span class="s2">"deep"</span><span class="p">)</span>
    <span class="o">...</span>
    <span class="n">memory</span> <span class="n">usage</span><span class="p">:</span> <span class="mf">25.4</span> <span class="n">MB</span>
    </code></pre></td></tr></table>
    </div>
    </div><p>The peak memory usage before dropping the columns was 30.5 MB and once I remove a few columns the peak memory usage becomes 25.4 MB. I have already implemented the dropping of id column and handled the case of single isotope as well by dropping the column and istead just storing the information of the isotope as a meta attribute. We have also finalised on the discarding of the other columns by considering the physics of these quantities. Let&rsquo;s check out a few of them. Since I haven&rsquo;t already implemented the optimisations that follow I will save the implementation details for the next blog.</p>
    <h3 id="einsteins-coeffecients-and-linestrengths">Einstein&rsquo;s Coeffecients and Linestrengths</h3>
    <p>There are four parameters of interest to describe the intensity of a line : Linestrength $(int)$, Einstein emission coefficient $(A)$ and Einstein absorption coefificent $(B_{lu})$, Einstein induced emission coefficient $(B_{ul})$. All of them are somehow linked to the Squared Transition Dipole Moment $(R)$. <sup id="fnref:1"><a class="footnote-ref" href="https://gagan-aryan.netlify.app/tags/gsoc21//index.xml#fn:1">1</a></sup></p>
    <p>$$ B_{lu}=10^{-36}\cdot\frac{8{\pi}^3}{3h^2} R_s^2 \cdot 10^{-7} $$<br />
    $$ B_{ul}=10^{-36}\cdot\frac{8{\pi}^3}{3h^2} \frac{gl}{gu} R_s^2 \cdot 10^{-7} $$<br />
    $$ A_{ul}=10^{-36}\cdot\frac{\frac{64{\pi}^4}{3h} {\nu}^3 gl}{gu} R_s^2 $$</p>
    <p>So now the idea would be to drop the $int$ column and use $A_{ul}$ to calculate the value of $int$ from it. The reason to drop $int$ and not $A_{ul}$ some databases like <code>ExoMol</code> databases only provide the value of $A_{ul}$.</p>
    <h3 id="concat-better">Concat better</h3>
    <p>For anyone who wants concate multiple datafiles pandas tends to become useless as the memory scales up. I started out experimenting concat operations inorder to cluster the isotopes of each type, run computations on them and later concat them. But I later learnt that since this data is already in the form of a single dataframe, indexing is a better parameter to track the memory consumption. Nonetheless there are a few other places in Radis where we process multiple files and concat them, hence this experiment would help us decide how we can chose to replace the current approach with a better one. I tried out three methods. I was using some random dummy datafiles of around 780 MBs.</p>
    <ul>
    <li>Normal <code>pandas.concat</code></li>
    <li>Concat with a doubly ended queue</li>
    <li>Concat with parquet</li>
    </ul>
    <p>Here are the results of each of these methods -</p>
    <div class="tab" id="cbbfde2b70afc7e2">
    <div class="tab__links">
    <button class="tab__link">pandas.concat</button>
    <button class="tab__link">deque</button>
    <button class="tab__link">parquet</button>
    </div>
    <div class="tab__content" id="c6b1e010ed52c9f8">
    <h3 id="pandasconcat">pandas.concat</h3>
    <pre><code>CPU Time - 0:02:43.797588
    Peak Memory Usage - 4.1050 GB
    </code></pre>
    </div>
    <div class="tab__content" id="a412292f0cf68165">
    <h3 id="pandasconcat-with-a-doubly-queue">pandas.concat with a doubly queue</h3>
    <pre><code>CPU Time - 0:02:34.484612
    Peak Memory Usage - 3.7725 GB
    </code></pre>
    </div>
    <div class="tab__content" id="c655ff276a8106d7">
    <h3 id="concat-with-parquet">Concat with parquet</h3>
    <pre><code>CPU Time - 0:01:37.984875
    Peak Memory Usage - 1.6829 GB
    </code></pre>
    </div>
    </div>
    
    <p>Looking at the results, parquet seems like a really good option to me. But we will run for a few more examples and later check which one suits the best.</p>
    <h2 id="the-next-two-weeks">The next two weeks</h2>
    <p>The project is making progress in all fronts. I feel I need to reorganize my thoughts a bit. My main work for now would be to complete the task list of <a href="https://github.com/radis/radis/pull/287">this pr</a>. And then look at other stuff.</p>
    <div class="footnotes">
    <hr />
    <ol>
    <li id="fn:1">
    <p><a href="https://www.sciencedirect.com/science/article/pii/S0022407398000788?via%3Dihub">Rothmann Paper (Eqs.(A7), (A8), (A9)</a> <a class="footnote-backref" href="https://gagan-aryan.netlify.app/tags/gsoc21//index.xml#fnref:1">&#x21a9;&#xfe0e;</a></p>
    </li>
    </ol>
    </div>

