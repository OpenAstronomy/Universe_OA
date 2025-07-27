.. title: RECIPES RECIPES WHAT KIND OF RECIPES? :)
.. slug:
.. date: 2025-07-26 06:07:00 
.. tags: JuliaAstro
.. author: kashish shrivastav
.. link: https://kashish2210.blogspot.com/2025/07/recipes-recipes-what-kind-of-recipes.html
.. description:
.. category: gsoc2025


.. raw:: html

    <p>&nbsp;</p><h1><strong>Exploring Light Curve Plotting in Stingray.jl: Recipes and Examples:</strong></h1>
    <p>In my continued work with <strong><a href="https://github.com/StingraySoftware/Stingray.jl">Stingray.jl</a>, </strong><span>so hello everyone, let's learns about plotting my favorite topic:)</span></p><p>Light curves are essential in high-energy astrophysics, as they represent the brightness of an astronomical object as a function of time. Precise visualization and filtering of these curves help astronomers perform accurate timing analysis, detect variability, and identify astrophysical phenomena.</p>
    <p>This post demonstrates how to generate and customize light curve plots using <strong>Stingray.jl</strong>, leveraging real NICER datasets.</p>
    <!-- TEASER_END -->
    <hr />
    <h2><strong>Dataset and Setup:</strong></h2>
    <p>For this demonstration, I used a dataset from <a href="https://heasarc.gsfc.nasa.gov/FTP/nicer/data/obs/2018_03/1200120104/xti/event_cl/"><strong>NICER-HESRAC-CL.EVT</strong>.</a> The first step is to load the event data into an <code>EventList</code> object:</p>
    <pre class="overflow-visible!"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary select-none rounded-t-2xl">julia</div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-julia">using Plots
    events = readevents("ni1200120104_0mpu7_cl.evt", load_gti=true, sort=true)
    </code></div></div></pre>
    <p><strong>Output:</strong></p>
    <pre class="overflow-visible!"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary select-none rounded-t-2xl">pgsql</div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span class="hljs-built_in">Found</span> GTI data: <span class="hljs-number">16</span> intervals
    GTI <span class="hljs-type">time</span> range: <span class="hljs-number">1.3253976595089495e8</span> <span class="hljs-keyword">to</span> <span class="hljs-number">1.3261337476368216e8</span>
    EventList <span class="hljs-keyword">with</span> <span class="hljs-number">21244574</span> times <span class="hljs-keyword">and</span> energies
    </code></div></div></pre>
    <hr />
    <h2><strong>Basic Light Curve Plotting</strong></h2>
    <p>The simplest way to visualize the event list is:</p>
    <pre class="overflow-visible!"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary select-none rounded-t-2xl">julia</div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-julia">plot(events)
    </code></div></div></pre>
    <p><strong>Output:</strong><br />
    <em></em></p><div class="separator" style="clear: both; text-align: left;"><em><a href="https://blogger.googleusercontent.com/img/a/AVvXsEihP4ymjuB-9gfZJBpcSKGMrSfBlKAQ3O0pFr2mPxvcX6E9W2I2SEzCQiIDZXybLZ4dXxUgcfmxP53BmMJKC3nb9A-J96r_HuGjra-xEbzh1KYk7-nfz66i3lVLOqOJLKqP4WH14k7XkD04tDW8fBGkLm1YWKX5tg1OgbjnCD04ETkZy2Cwxum7nMEmN7TM" style="margin-left: 1em; margin-right: 1em;"><img alt="" height="324" src="https://blogger.googleusercontent.com/img/a/AVvXsEihP4ymjuB-9gfZJBpcSKGMrSfBlKAQ3O0pFr2mPxvcX6E9W2I2SEzCQiIDZXybLZ4dXxUgcfmxP53BmMJKC3nb9A-J96r_HuGjra-xEbzh1KYk7-nfz66i3lVLOqOJLKqP4WH14k7XkD04tDW8fBGkLm1YWKX5tg1OgbjnCD04ETkZy2Cwxum7nMEmN7TM=w540-h324" width="540" /></a></em></div><em><br /></em><p></p>
    <hr />
    <h2><strong>Energy Filtering</strong></h2>
    <p>To restrict the light curve to specific energy ranges, use <code>energy_filter</code>:</p>
    <pre class="overflow-visible!"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary select-none rounded-t-2xl">julia</div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-julia">plot(events, energy_filter=(0, 5e3))
    </code></div></div></pre>
    <p><strong>Output:</strong><br />
    <em></em></p><div class="separator" style="clear: both; text-align: left;"><em><a href="https://blogger.googleusercontent.com/img/a/AVvXsEjMnzrAcQ1MM7beCneFyvvO-YXPUK9qisHBbeqeBjxr-JcjRX5vmh1eWlKyCUOjYNjvHdhs117oNLc1PzK4lB0A6p0DshL6G6CwrXNL_mTvHkyTshYn0937tUEq7HZaShBHGAp_agFQRUOgatFWzbB276M7oNryLnVNkD-_Lvx-T3R4l5xjEx2I2zGHsuQw" style="margin-left: 1em; margin-right: 1em;"><img alt="" height="336" src="https://blogger.googleusercontent.com/img/a/AVvXsEjMnzrAcQ1MM7beCneFyvvO-YXPUK9qisHBbeqeBjxr-JcjRX5vmh1eWlKyCUOjYNjvHdhs117oNLc1PzK4lB0A6p0DshL6G6CwrXNL_mTvHkyTshYn0937tUEq7HZaShBHGAp_agFQRUOgatFWzbB276M7oNryLnVNkD-_Lvx-T3R4l5xjEx2I2zGHsuQw=w533-h336" width="533" /></a></em></div><em><br /></em><p></p>
    <hr />
    <h2><strong>Time Range Filtering</strong></h2>
    <p>For a specific time interval, provide <code>tstart</code> and <code>tstop</code>:</p>
    <pre class="overflow-visible!"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary select-none rounded-t-2xl">julia</div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-julia">plot(events, tstart=1.32540e8, tstop=1.32546e8)
    </code></div></div></pre>
    <p><strong>Output:</strong><br />
    <em></em></p><div class="separator" style="clear: both; text-align: left;"><em><a href="https://blogger.googleusercontent.com/img/a/AVvXsEg7aQdd6nY8LM_FCf5XvTKY2tx-81yGHiL-UGRDPQTP8ssSaC-42O1kTVIDdtsrmVcaLCIL_Yb8UHVxkxLREViVIzWBGjtjQo4Qw6FoI-xb6nk6S4gEMuFe32JeGWc45T3MfxRcQ9wmZz_y-ILAd7BsQzwzAtq2phfxxIgmlCwsEIonNz1jx9kyTAP8LRep" style="margin-left: 1em; margin-right: 1em;"><img alt="" height="352" src="https://blogger.googleusercontent.com/img/a/AVvXsEg7aQdd6nY8LM_FCf5XvTKY2tx-81yGHiL-UGRDPQTP8ssSaC-42O1kTVIDdtsrmVcaLCIL_Yb8UHVxkxLREViVIzWBGjtjQo4Qw6FoI-xb6nk6S4gEMuFe32JeGWc45T3MfxRcQ9wmZz_y-ILAd7BsQzwzAtq2phfxxIgmlCwsEIonNz1jx9kyTAP8LRep=w536-h352" width="536" /></a></em></div><em><br /></em><p></p>
    <hr />
    <h2><strong>Axis Limits and GTI/BTI Visualization</strong></h2>
    <p>You can highlight <strong>Good Time Intervals (GTIs)</strong> and <strong>Bad Time Intervals (BTIs)</strong>:</p>
    <pre class="overflow-visible!"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary select-none rounded-t-2xl">julia</div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-julia">plot(events, 5, axis_limits=[1.32540e8, 1.32546e8, 5e3, 2e4], show_gtis=true, show_btis=true)
    </code></div></div></pre>
    <p>Adjust transparency with <code>gti_alpha</code> and <code>bti_alpha</code>:</p>
    <pre class="overflow-visible!"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary select-none rounded-t-2xl">julia</div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-julia">plot(events, show_btis=true, bti_alpha=0.4, show_gtis=true, gti_alpha=0.3)
    </code></div></div></pre>
    <p><strong>Output:</strong><br />
    <em></em></p><div class="separator" style="clear: both; text-align: left;"><em><a href="https://blogger.googleusercontent.com/img/a/AVvXsEhTsXV3EHoUbJ3IC-XnZ8VShdN0FhV-dtHeH4K_0kMOZ--aLVp7uDwOUr-MuvMpVPUIyJZNIO2MU9SaupizdYMR1K175zdOD9YKV73JSNhE-E3jC9zRnFl3eVhHpr4R1tPa-UF8WKHl-u2FJ6lp9w0d5ATS3h5Fv8zNatdyX1UvTm_RvU8riZLug8euFQUw" style="margin-left: 1em; margin-right: 1em;"><img alt="" height="342" src="https://blogger.googleusercontent.com/img/a/AVvXsEhTsXV3EHoUbJ3IC-XnZ8VShdN0FhV-dtHeH4K_0kMOZ--aLVp7uDwOUr-MuvMpVPUIyJZNIO2MU9SaupizdYMR1K175zdOD9YKV73JSNhE-E3jC9zRnFl3eVhHpr4R1tPa-UF8WKHl-u2FJ6lp9w0d5ATS3h5Fv8zNatdyX1UvTm_RvU8riZLug8euFQUw=w537-h342" width="537" /></a></em></div><div class="separator" style="clear: both; text-align: center;"><div class="separator" style="clear: both; text-align: left;"><em><a href="https://blogger.googleusercontent.com/img/a/AVvXsEhttPrsMvIN-UQjWTWdziqT_arISCdVnmBTT2KOpjqe65-OzlplG9wkcdl3tgjaivyRQHA2zIl6Zh6WivdlqEt-LqwQi7OaK65ZM2wPB3evb93twB8NlrfekhZTRv_oiJE1zOBJfbCH_QQO3sYCI9s8L3H-ooVKp6oy7MdCeEWepMuaMRKk-Shteh1V1-vp" style="margin-left: 1em; margin-right: 1em;"><img alt="" height="378" src="https://blogger.googleusercontent.com/img/a/AVvXsEhttPrsMvIN-UQjWTWdziqT_arISCdVnmBTT2KOpjqe65-OzlplG9wkcdl3tgjaivyRQHA2zIl6Zh6WivdlqEt-LqwQi7OaK65ZM2wPB3evb93twB8NlrfekhZTRv_oiJE1zOBJfbCH_QQO3sYCI9s8L3H-ooVKp6oy7MdCeEWepMuaMRKk-Shteh1V1-vp=w538-h378" width="538" /></a></em></div><em><br /><br /></em></div><em><br /></em><p></p>
    <p>You can also plot using a custom GTI matrix or file:</p>
    <pre class="overflow-visible!"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary select-none rounded-t-2xl">julia</div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-julia">gti1 = [1.32540e8 1.32580e8]
    plot(events, gtis=gti1, show_gtis=true, gap_threshold=100)
    # Or use a GTI file:
    # plot(events, gti_file="gti.fits", show_gtis=true)
    </code></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-julia"><br /></code></div><div class="overflow-y-auto p-4" dir="ltr"><strong>Output:</strong></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-julia"><div class="separator" style="clear: both; text-align: left;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEhR43Tz_RXbWZYUGFy9MbrOjGWZNa6blI2RFrdkyCIpRLHJEnrpL7PDxZ6g5LQrI1EhZ9uJHLobssyNNn6vfrWrazJeFaPFlQ3exjDSWd0cyx--aZXHOwEMyGO3Sb8jWC6xq6Y7JCHENtNFXN75pxsZdfOVQrAuqOBN3A53g-WfoyT2PTEevWjWzhpYGXRE" style="margin-left: 1em; margin-right: 1em;"><img alt="" height="379" src="https://blogger.googleusercontent.com/img/a/AVvXsEhR43Tz_RXbWZYUGFy9MbrOjGWZNa6blI2RFrdkyCIpRLHJEnrpL7PDxZ6g5LQrI1EhZ9uJHLobssyNNn6vfrWrazJeFaPFlQ3exjDSWd0cyx--aZXHOwEMyGO3Sb8jWC6xq6Y7JCHENtNFXN75pxsZdfOVQrAuqOBN3A53g-WfoyT2PTEevWjWzhpYGXRE=w539-h379" width="539" /></a></div><br /><br /></code></div></div></pre>
    <hr />
    <h2><strong>Rebinning Light Curves</strong></h2>
    <p>Rebinning improves visualization and helps in reducing noise:</p>
    <pre class="overflow-visible!"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary select-none rounded-t-2xl">julia</div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-julia">eventlist = readevents("ni1200120104_0mpu7_cl.evt")
    lc = create_lightcurve(eventlist, 800)
    plot(lc, 1000, show_original=true, original_alpha=1)
    </code></div></div></pre>
    <p><strong>Output:</strong><br />
    <em></em></p><div class="separator" style="clear: both; text-align: left;"><em><a href="https://blogger.googleusercontent.com/img/a/AVvXsEjXJZ4UyLdgpISvzhmrQKiGGw04kdtgnG7RbVo3hmNCgXOt-4UyjrPgdMqxAo2Ft0t1fKGyBFYB0xer1bYO6wTDNhrYdrYGFrzjXvAwjntgWK6EjrXSyw_D7iuoZFRhnYDxM6bhw01PVvAoJUsCX079Yflt0n6VLj6IYizFjkwWlOCqs3QbOe77XQUTJrZg" style="margin-left: 1em; margin-right: 1em;"><img alt="" height="348" src="https://blogger.googleusercontent.com/img/a/AVvXsEjXJZ4UyLdgpISvzhmrQKiGGw04kdtgnG7RbVo3hmNCgXOt-4UyjrPgdMqxAo2Ft0t1fKGyBFYB0xer1bYO6wTDNhrYdrYGFrzjXvAwjntgWK6EjrXSyw_D7iuoZFRhnYDxM6bhw01PVvAoJUsCX079Yflt0n6VLj6IYizFjkwWlOCqs3QbOe77XQUTJrZg=w552-h348" width="552" /></a></em></div><em><br /></em><p></p>
    <hr />
    <h2><strong>Adding Poisson Errors</strong></h2>
    <pre class="overflow-visible!"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary select-none rounded-t-2xl">julia</div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-julia">lc = create_lightcurve(events, 10)
    plot(lc, show_errors=true)
    </code></div></div></pre>
    <p><strong>Output:</strong><br />
    <em></em></p><div class="separator" style="clear: both; text-align: left;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEh6-Fio9dE4cR5z46SorUNTVfwZ3a3cGuBRSAV6XOvK-rsog1QUHHdYLuzGZ_X2EHhmC8Oj_6hVUuax8Oz85hoFqs4QsicpliNFI84Vuaw-xR3f4Hp6g78caKlEb6EORTs3vcxruk_rPUZolBQDI4mZqXpOJFJQkijJC1YGNv168bSGRFQz3zgsjZKYi0BG" style="margin-left: 1em; margin-right: 1em;"><img alt="" height="363" src="https://blogger.googleusercontent.com/img/a/AVvXsEh6-Fio9dE4cR5z46SorUNTVfwZ3a3cGuBRSAV6XOvK-rsog1QUHHdYLuzGZ_X2EHhmC8Oj_6hVUuax8Oz85hoFqs4QsicpliNFI84Vuaw-xR3f4Hp6g78caKlEb6EORTs3vcxruk_rPUZolBQDI4mZqXpOJFJQkijJC1YGNv168bSGRFQz3zgsjZKYi0BG=w567-h363" width="567" /></a></div><div class="separator" style="clear: both; text-align: left;"><h3 dir="auto"><span style="background-color: white;">Now with <a href="https://github.com/StingraySoftware/Stingray.jl/blob/main/test/data/monol_testA.evt" target="_blank">monal_testA</a> :</span></h3><div><span style="background-color: white;"><div class="separator" style="clear: both; text-align: center;"><div class="separator" style="clear: both; text-align: left;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEiUGSFO7XFRWxZgQipdeyzCVIJ969PNbvjTX2Vrdgolz6PfEA0YoNSV7cwWjaElGmkTZB6DbEAZ78wFIcHukoL5TspjaLl-Bdz7aygVbdtMOj2kW--VTCZRjK0KWEtOcxC_UyneDUx8whQB1tEl_HVlRy8bW9efNzw32ZdBvGw6ButoU2LFidYyG-stG-Gv" style="margin-left: 1em; margin-right: 1em;"><img alt="" height="388" src="https://blogger.googleusercontent.com/img/a/AVvXsEiUGSFO7XFRWxZgQipdeyzCVIJ969PNbvjTX2Vrdgolz6PfEA0YoNSV7cwWjaElGmkTZB6DbEAZ78wFIcHukoL5TspjaLl-Bdz7aygVbdtMOj2kW--VTCZRjK0KWEtOcxC_UyneDUx8whQB1tEl_HVlRy8bW9efNzw32ZdBvGw6ButoU2LFidYyG-stG-Gv=w589-h388" width="589" /></a></div><br /><br /></div><br /></span></div></div><div class="separator" style="clear: both; text-align: center;"><br /></div><h2><strong>Gaussian Confidence Bands:[this one is just for testing, like what we can do next, I will work on <a href="https://docs.astropy.org/en/stable/api/astropy.stats.bayesian_blocks.html">bayesian_block</a>]</strong></h2><h2><span style="font-size: small;"><strong>(</strong><span style="font-weight: normal;">hehe, u got next blog hint</span><strong>)</strong></span></h2>
    <p>For smoother visualization with statistical confidence intervals:[focus "<span style="font-family: monospace; white-space: pre;">smoothed_counts</span>" a small function to smoothing the lightcurve:)]</p>
    <pre class="overflow-visible!"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary select-none rounded-t-2xl">julia</div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-julia">using StatsBase
    
    lc = create_lightcurve(events, 1)
    lc_times = lc.time
    lc_counts = lc.counts
    
    # Apply smoothing (moving average)
    window_size = 1000
    smoothed_counts = [mean(lc_counts[max(1, i-window_size):min(end, i+window_size)]) for i in 1:length(lc_counts)]
    
    # Compute confidence intervals
    σ = sqrt.(max.(smoothed_counts, 1))
    upper_1σ = smoothed_counts .+ σ
    lower_1σ = smoothed_counts .- σ
    upper_2σ = smoothed_counts .+ 2 .* σ
    lower_2σ = smoothed_counts .- 2 .* σ
    upper_3σ = smoothed_counts .+ 3 .* σ
    lower_3σ = smoothed_counts .- 3 .* σ
    
    # Plot with confidence bands
    p = plot(lc_times, smoothed_counts, seriestype=:line, linewidth=2, color=:blue,
    label="Data", xlabel="Time (s)", ylabel="Counts", title="Gaussian Confidence Bands")
    
    plot!(lc_times, [upper_3σ lower_3σ], fillrange=[lower_3σ upper_3σ], fillalpha=0.2, fillcolor=:gray, label="3σ")
    plot!(lc_times, [upper_2σ lower_2σ], fillrange=[lower_2σ upper_2σ], fillalpha=0.3, fillcolor=:orange, label="2σ")
    plot!(lc_times, [upper_1σ lower_1σ], fillrange=[lower_1σ upper_1σ], fillalpha=0.4, fillcolor=:lightblue, label="1σ")
    
    display(p)
    </code></div></div></pre>
    <p><strong>Output:</strong><br /><a href="https://blogger.googleusercontent.com/img/a/AVvXsEh0xblxI4PNP-R0BWWbgQWUGaDJg2FcUbbUxwUfdrxyv4YX0MSI26yNiltUkyu7kprzNU_pEisEpHBMqTrV2rs2jH91Ecce7yFNz_V4fpQ2YkVsx_Hyxe6JT5XF1H0fnZCZ8nTeo3E4zCSAaNMR43pFCgUtEPLcK0rcBxFSVA-LwPG0cIYd751Vv2Yvr2uH" style="font-style: italic; margin-left: 1em; margin-right: 1em;"><img alt="" height="348" src="https://blogger.googleusercontent.com/img/a/AVvXsEh0xblxI4PNP-R0BWWbgQWUGaDJg2FcUbbUxwUfdrxyv4YX0MSI26yNiltUkyu7kprzNU_pEisEpHBMqTrV2rs2jH91Ecce7yFNz_V4fpQ2YkVsx_Hyxe6JT5XF1H0fnZCZ8nTeo3E4zCSAaNMR43pFCgUtEPLcK0rcBxFSVA-LwPG0cIYd751Vv2Yvr2uH=w497-h348" width="497" /></a></p>
    <hr />
    <h2><strong>Segmenting Light Curves</strong></h2>
    <p>For dividing data into segments:</p>
    <pre class="overflow-visible!"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary select-none rounded-t-2xl">julia</div><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary select-none rounded-t-2xl">segments = create_segments(events, 10000.0)</div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-julia">plot(segments, show_errors=false, show_segment_boundaries=true,
    segment_colors=[:blue, :red, :green, :orange, :purple])
    </code></div></div></pre>
    <p><strong>Output:</strong><br />
    <em></em></p><div class="separator" style="clear: both; text-align: left;"><em><a href="https://blogger.googleusercontent.com/img/a/AVvXsEjmY42-_fCw1Dr1QmIp7gtvV3VxcRkekL9aCh-eaOXviqlzyEexJA1_EcouAj9enxG8srUQKDZMoD2LHZuOkZLcYPXXXjcQlGCiHANkHLvMg9E5DZaMi8xxDDlEvq2TV27cPlOKZpzmuDqDdVyBv3sqD5ZFTc2q2UzXEaZsXXj-gDxQt2MM0MYm8_IGe6Lw" style="margin-left: 1em; margin-right: 1em;"><img alt="" height="326" src="https://blogger.googleusercontent.com/img/a/AVvXsEjmY42-_fCw1Dr1QmIp7gtvV3VxcRkekL9aCh-eaOXviqlzyEexJA1_EcouAj9enxG8srUQKDZMoD2LHZuOkZLcYPXXXjcQlGCiHANkHLvMg9E5DZaMi8xxDDlEvq2TV27cPlOKZpzmuDqDdVyBv3sqD5ZFTc2q2UzXEaZsXXj-gDxQt2MM0MYm8_IGe6Lw=w517-h326" width="517" /></a></em></div><em><br /><br /><br /></em><p></p>
    <hr />
    <h2><strong>GitHub Reference</strong></h2>
    <p>For detailed code and implementation, check out my PR:<br /><a class="" href="https://github.com/StingraySoftware/Stingray.jl/pull/54#issue-3242463035" rel="noopener" target="_new">GitHub PR #54 – Stingray.jl</a></p>
    <hr />
    <h3><span style="font-weight: normal;"><span style="font-size: small;">These plotting recipes make it easier to visualize event lists and light curves with GTIs, BTIs, and advanced error handling in <a href="https://github.com/StingraySoftware/Stingray.jl"><span>Stingray.jl</span>.</a> They serve as a foundation for advanced timing analysis techniques, such as power spectral density, periodograms, and others.</span></span></h3>
    <p>Stay tuned for my next post:) find hint for my next post ::}</p>

