.. title: Improving time efficiency of Vaex Implementation
.. slug:
.. date: 2023-07-06 00:00:00 
.. tags: radis
.. author: Somesh Verma
.. link: https://1someshverma.github.io/improvingTimeEfficieny/
.. description:
.. category: gsoc2023


.. raw:: html

    <p>Though Vaex reduced memory use by RADIS to compute specturm but it is slow for smaller databank and in our case when the number of lines in the databank is very less . The slow performance of Vaex for smaller dataframes is due to three main reasons for our implementation of RADIS</p>
    
    <ul>
    <!-- TEASER_END -->
    <li>First vaex is optimized for larger databank and doesn’t focus that much for smaller dataframe .</li>
    <li>Vaex uses virtual columns to reduce memory and only compute the virutal column when it is required it saves memory space but in case when virtual column
    is required multiple times then it is computed multiple times and it costs time . For Pandas it only compute the column only once and saves it for further calculations and in-memory compute of Pandas are faster than Vaex for smaller dataframes.</li>
    <li>Vaex is based on Apache Arrow and uses Expression class for column while for Pandas which stores column as numpy no conversion is required to use library functions of numpy but for vaex some operations require explict conversion to numpy array and it costs time.</li>
    </ul>
    
    <p>Apart from this there was issue it the implementation of vaex which are now optimized by better alternatives.
    Intially the time graph for Vaex and Pandas in terms of time comparison was as given below-</p>
    
    <p>Total Time  which is the sum of loading time and computation time for calculating spectrum .
    Plot of Total Time vs Number of lines Graph</p>
    
    <p><img alt="Vaex Comparison" src="https://1someshverma.github.io/images/earlierTotal.png" /></p>
    
    <p>Computation time , it is time required to compute the spectrum using Vaex or Implementation
    Plot of Compuation Time vs Number of lines Graph</p>
    
    <p><img alt="Vaex Comparison" src="https://1someshverma.github.io/images/earlierCom.png" /></p>
    
    <p>##Optimizations</p>
    
    <ul>
    <li>Calculating Sum</li>
    </ul>
    
    <p>At first we were computing the sum as</p>
    
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code> error = df[b].S.sum() / df.S.sum() * 100
    </code></pre></div></div>
    <p>but later changed it to</p>
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>error_cutoff = df[b].sum(df[b].S) / df.sum(df.S) * 100
    </code></pre></div></div>
    
    <p>The time taken to calculate 25 spectra decreased from 6.0 s to 5.4 s</p>
    
    <p>Code used was</p>
    
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>from radis import calc_spectrum
    import time
    
    t0 = time.time()
    for i in range(25):
    s = calc_spectrum(2000, 2010,         # cm-1
    molecule='CO',
    isotope='1,2,3',
    pressure=1.01325,   # bar
    Tgas=1000,
    mole_fraction=0.1,
    databank='hitemp',  # or 'hitemp'
    diluent = "air",
    verbose = 0,
    engine = "vaex"
    )
    t1 = time.time()
    print(t1 -t0)
    </code></pre></div></div>
    
    <ul>
    <li>Not using df.extract()
    After masking some of the rows, that is filtering some of the rows based on some conditions . Then I was using df.extract(), later i found it was using a lot of time .So i commented that and refactored code to work without it .
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>df = df.extract() # later commented it .
    </code></pre></div>    </div>
    </li>
    </ul>
    
    <p>Improvements after this was quite impressive as i found out running below codes</p>
    
    <p>It reduced calculation time for the code below by 10 seconds</p>
    
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>from radis import calc_spectrum
    
    import time
    t0=time.time()
    
    s = calc_spectrum(1500, 2500,         # cm-1
    molecule='H2O',
    isotope='1,2,3',
    pressure=1.01325,   # bar
    Tgas=700,           # K
    mole_fraction=0.1,
    wstep='auto',
    path_length=1,      # cm
    databank='hitemp',  # or 'hitemp', 'geisa', 'exomol'
    engine='vaex',
    )
    
    s.apply_slit(0.5, 'nm')       # simulate an experimental slit
    
    t1=time.time()
    
    print('Time taken : '+str(t1 - t0))
    
    </code></pre></div></div>
    
    <p>And reduced 0.5 seconds calculation time for the code</p>
    
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>from radis import calc_spectrum
    import time
    t0=time.time()
    s = calc_spectrum(2000, 2010,         # cm-1
    molecule='CO',
    isotope='1,2,3',
    pressure=1.01325,   # bar
    Tgas=1000,
    mole_fraction=0.1,
    databank='hitran',  # or 'hitemp'
    diluent = "air",
    verbose = 3,
    engine = "vaex"
    )
    t1=time.time()
    
    
    print('Time taken : '+str(t1-t0))
    </code></pre></div></div>
    
    <p>After all of this updated time graph were as below
    <img alt="Vaex Comparison" src="https://1someshverma.github.io/images/updatedCom.png" /></p>
    
    <p><img alt="Vaex Comparison" src="https://1someshverma.github.io/images/updatedTotal.png" /></p>
    
    <p>I significant improvement can be observed from it .</p>
    
    <p>Now to smaller time performance of smaller dataframe , I converted the vaex dataframes to pandas for smaller databases. And overall improvemets are as</p>
    <ul>
    <li>Memory performance is improved for all dataframes.</li>
    <li>Time performance is same for smaller dataframes , and for larger dataframes time performance of vaex is quite better than Pandas.</li>
    </ul>

