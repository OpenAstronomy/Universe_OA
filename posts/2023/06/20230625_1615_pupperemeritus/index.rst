.. title: GSoC Week 2-3 Update
.. slug:
.. date: 2023-06-25 16:15:57 
.. tags: stingray
.. author: pupper emeritus
.. link: https://dev.to/pupperemeritus/gsoc-week-2-3-update-1b7l
.. description:
.. category: gsoc2023


.. raw:: html

    <h1>
    
    
    <!-- TEASER_END -->
    Brief
    </h1>
    
    <p>These weeks I refactored the <code>LombScargleCrossspectrum</code> and <code>LombScarglePowerspectrum</code> classes to accommodate the fast algorithm which went smoothly.<br />
    However when it comes to the fast algorithm. I had tunnel vision and unconsciously made the <code>lsft_fast</code> function compute the power spectrum instead of the fourier transform. Right now I am working towards isolating the algorithm to compute the fourier transform using the Press and Rybicki optimizations(<a href="https://ui.adsabs.harvard.edu/abs/1989ApJ...338..277P/abstract">https://ui.adsabs.harvard.edu/abs/1989ApJ...338..277P/abstract</a>).</p>
    <h1>
    
    
    Challenges Faced
    </h1>
    
    <p>Integrating the optimization to the existing slow algorithm is giving me a bit of trouble. I'm still figuring out how to add the optimizations. If this is done, I can move onto making the time lag, phase lag functions and then onto testing and documentation.</p>
    <h1>
    
    
    Details
    </h1>
    
    <p>Added the following parameters to both the classes in order to accommodate choice between the fast and slow algorithm.<br />
    </p>
    
    <div class="highlight js-code-highlight">
    <pre class="highlight plaintext"><code>method : str
    The method to be used by the Lomb-Scargle Fourier Transformation function. `fast`
    and `slow` are the allowed values. Default is `fast`. fast uses the optimized Press
    and Rybicki O(n*log(n))
    
    oversampling : float, optional, default: 5
    Interpolation Oversampling Factor (for the fast algorithm)
    </code></pre>
    
    </div>
    
    
    
    <p>For full code refer <a href="https://github.com/StingraySoftware/stingray/pull/737">https://github.com/StingraySoftware/stingray/pull/737</a></p>
    
    <p>Most important part of the process is the Lomb Scargle Fourier Transform.<br />
    The wrapper class is trivial, they only wrap the fast and slow lomb scargle fourier transform functions.</p>
    
    <h1>
    
    
    Results using the slow algorithm
    </h1>
    
    <h2>
    
    
    On synthetic data
    </h2>
    
    
    
    <div class="highlight js-code-highlight">
    <pre class="highlight plaintext"><code>rand = np.random.default_rng(42)
    n = 100
    t = np.sort(rand.random(n)) * n
    y = np.cos(2 * np.pi * 5 * t) + 0.01 * rand.standard_normal(n)
    y -= np.min(y)
    lc1 = Lightcurve(t, y, err_dist="poisson")
    y2 = np.cos(2 * np.pi * 5.0 * (t)) + 0.01 * rand.standard_normal(n)
    y2 -= np.min(y2)
    lc2 = Lightcurve(t, y2, err_dist="poisson")
    </code></pre>
    
    </div>
    
    
    
    <p><a class="article-body-image-wrapper" href="https://res.cloudinary.com/practicaldev/image/fetch/s--48Z7wHCy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xgf4z7yaxi81aoxj9dkx.png"><img alt="Image description" height="827" src="https://res.cloudinary.com/practicaldev/image/fetch/s--48Z7wHCy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xgf4z7yaxi81aoxj9dkx.png" width="800" /></a></p>
    
    <h2>
    
    
    On real data
    </h2>
    
    <h3>
    
    
    The lightcurve
    </h3>
    
    <p><a href="https://heasarc.gsfc.nasa.gov/FTP/nicer/data/obs/2018_03//1200120106/xti/event_cl/ni1200120106_0mpu7_cl.evt.gz">https://heasarc.gsfc.nasa.gov/FTP/nicer/data/obs/2018_03//1200120106/xti/event_cl/ni1200120106_0mpu7_cl.evt.gz</a></p>
    
    <p><a class="article-body-image-wrapper" href="https://res.cloudinary.com/practicaldev/image/fetch/s--2qWoGIUP--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/w3dz8zsjk2ika71ytlkx.png"><img alt="Image description" height="431" src="https://res.cloudinary.com/practicaldev/image/fetch/s--2qWoGIUP--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/w3dz8zsjk2ika71ytlkx.png" width="574" /></a></p>
    
    <p><a class="article-body-image-wrapper" href="https://res.cloudinary.com/practicaldev/image/fetch/s--F7NDO8dr--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/167buf3woin2hplbo89r.png"><img alt="Image description" height="417" src="https://res.cloudinary.com/practicaldev/image/fetch/s--F7NDO8dr--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/167buf3woin2hplbo89r.png" width="559" /></a></p>

