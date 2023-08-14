.. title: GSoC Week 9-10
.. slug:
.. date: 2023-08-13 10:23:47 
.. tags: stingray
.. author: pupper emeritus
.. link: https://dev.to/pupperemeritus/gsoc-week-9-10-17mo
.. description:
.. category: gsoc2023


.. raw:: html

    <p>Big progress on the front of algorithm working. Turns out there wasn't that much of a problem in the algorithm. I just had to subtract the mean from the data before taking the fourier transform. The Lomb Scargle seems to work on data that has mean subtracted from it. Furthermore they dont seem to work that well or at all in full spectrum. <br />
    The LSFT also is highly sensitive to the time intervals that are input to it. I have found some more clues as to how to make it even better. I will expound upon this further within 2 weeks since my final exams are going on and I have limited time.</p>
    
    <!-- TEASER_END -->
    <p>Minimum Working Code Example<br />
    </p>
    
    <div class="highlight js-code-highlight">
    <pre class="highlight plaintext"><code>def data_func(time, freq=1.2324235252):
    return  2 * np.sin(2 * np.pi * time * freq)
    
    t0 = 0
    t1 = 100
    dt = 0.1
    
    np.random.seed(43)
    time_uniform = np.arange(t0, t1, dt)
    time_nonuniform = np.sort(np.random.uniform(t0, t1, time_uniform.size))
    
    npft = np.fft.fft(data_func(time_uniform))
    npfreqs = np.fft.fftfreq(npft.size, dt)
    npft = npft[npfreqs&gt;=0]
    npfreqs = npfreqs[npfreqs&gt;=0]
    lsfreqs = np.linspace(np.min(npfreqs), np.max(npfreqs), npfreqs.size * 8)
    lsfreqs = lsfreqs[lsfreqs&gt;=0]
    np.random.seed(43)
    lsft_slow_arr = lsft_slow(data_func(time_nonuniform), time_nonuniform, lsfreqs,sign=-1, fullspec=False)
    lsft_fast_arr = lsft_fast(data_func(time_nonuniform), time_nonuniform, lsfreqs,sign=-1, fullspec=False,oversampling=10)
    plt.plot(time_nonuniform,lsft_slow_inv(lsft_slow_arr,freqs=time_nonuniform, t=lsfreqs).real ,alpha=0.5,label="Slow")
    plt.plot(time_nonuniform,lsft_fast_inv(lsft_fast_arr,freqs=time_nonuniform, t=lsfreqs).real,alpha=0.5,label="Fast")
    plt.plot(time_nonuniform,data_func(time_nonuniform),label="Original Data")
    plt.legend()
    plt.xlim(0,10)
    plt.ylim(-3,3)
    </code></pre>
    
    </div>
    
    
    
    <p><a class="article-body-image-wrapper" href="https://res.cloudinary.com/practicaldev/image/fetch/s--v8B0QIbQ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/g10l11a0u36xzhtkq5n5.png"><img alt="Image description" height="418" src="https://res.cloudinary.com/practicaldev/image/fetch/s--v8B0QIbQ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/g10l11a0u36xzhtkq5n5.png" width="555" /></a></p>

