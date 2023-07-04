.. title: GSoC Week 4 Update
.. slug:
.. date: 2023-07-03 19:17:26 
.. tags: stingray
.. author: pupper emeritus
.. link: https://dev.to/pupperemeritus/gsoc-week-4-update-2g4a
.. description:
.. category: gsoc2023


.. raw:: html

    <h1>
    
    
    <!-- TEASER_END -->
    Brief
    </h1>
    
    <p>This week I successfully finished implementing the fast algorithm. Now my <code>LombScargleCrossspectrum</code> and <code>LombScarglePowerspectrum</code> are that much closer to completion. Only things left to sort out/implement are time lags and phase lag functions and checking the phase of the output.</p>
    
    <h1>
    
    
    Details
    </h1>
    
    <p>Testing on the following synthetic data has been conducted to compare the outputs with the existing cross spectrum and power spectrum for evenly spaced data first then checking the outputs of the lomb scargle variants on unevenly sampled data<br />
    </p>
    
    <div class="highlight js-code-highlight">
    <pre class="highlight plaintext"><code>rand = np.random.default_rng(42)
    n = 1000
    t = np.linspace(0, 10, n)
    y = np.sin(2 * np.pi * 3.0 * t) + 0.1 * rand.standard_normal(n)
    y2 = np.sin(2 * np.pi * 3.0 * t) + 0.1 * rand.standard_normal(n)
    y -= np.min(y)
    y2 -= np.min(y2)
    </code></pre>
    
    </div>
    
    <h2>
    
    
    The Cross spectra for evenly sampled data
    </h2>
    
    <p><a class="article-body-image-wrapper" href="https://res.cloudinary.com/practicaldev/image/fetch/s--HDSGExDP--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ldcxxcpq760ym5yph7jv.png"><img alt="Image description" height="417" src="https://res.cloudinary.com/practicaldev/image/fetch/s--HDSGExDP--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ldcxxcpq760ym5yph7jv.png" width="558" /></a></p>
    <h2>
    
    
    The time lags for evenly sampled data
    </h2>
    
    <p>As it is evident the time lags need work.</p>
    
    <p><a class="article-body-image-wrapper" href="https://res.cloudinary.com/practicaldev/image/fetch/s--5_uNnIpc--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/sknrib3nkos5tcnojlng.png"><img alt="Image description" height="413" src="https://res.cloudinary.com/practicaldev/image/fetch/s--5_uNnIpc--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/sknrib3nkos5tcnojlng.png" width="559" /></a></p>
    <h2>
    
    
    The power spectra for evenly sampled data
    </h2>
    
    <p>One quirk is that the power spectrum class is returning the power spectrum with a negative sign. This is a known bug. The values otherwise are within margin of error.</p>
    
    <p><a class="article-body-image-wrapper" href="https://res.cloudinary.com/practicaldev/image/fetch/s--njHhZDEY--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vtf835ktnxo9dn83iy55.png"><img alt="Image description" height="417" src="https://res.cloudinary.com/practicaldev/image/fetch/s--njHhZDEY--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vtf835ktnxo9dn83iy55.png" width="559" /></a></p>
    <h2>
    
    
    The Lomb Scargle cross spectrum and power spectrum when data is unevenly sampled
    </h2>
    
    <p><code>t = np.sort(rand.random(n))*10</code></p>
    <h3>
    
    
    The cross spectrum
    </h3>
    
    <p><a class="article-body-image-wrapper" href="https://res.cloudinary.com/practicaldev/image/fetch/s--LeUsZL3d--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/bzddaq7u9naiskry0x7i.png"><img alt="Image description" height="417" src="https://res.cloudinary.com/practicaldev/image/fetch/s--LeUsZL3d--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/bzddaq7u9naiskry0x7i.png" width="558" /></a></p>
    <h3>
    
    
    The power spectrum
    </h3>
    
    <p><a class="article-body-image-wrapper" href="https://res.cloudinary.com/practicaldev/image/fetch/s--mFs4vcWd--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/yfz6sav17mw51yas49he.png"><img alt="Image description" height="417" src="https://res.cloudinary.com/practicaldev/image/fetch/s--mFs4vcWd--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/yfz6sav17mw51yas49he.png" width="559" /></a></p>
    <h3>
    
    
    The time lags
    </h3>
    
    <p><a class="article-body-image-wrapper" href="https://res.cloudinary.com/practicaldev/image/fetch/s--bAp6Nw-1--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qkyr5to5lbkxm2s2xbi9.png"><img alt="Image description" height="413" src="https://res.cloudinary.com/practicaldev/image/fetch/s--bAp6Nw-1--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qkyr5to5lbkxm2s2xbi9.png" width="559" /></a></p>
    
    <p>They are off here too. Which will be fixed in the coming week.</p>
    
    <p>For exhaustive testing code refer<br />
    </p>
    <div class="ltag_gist-liquid-tag">
    
    </div>

