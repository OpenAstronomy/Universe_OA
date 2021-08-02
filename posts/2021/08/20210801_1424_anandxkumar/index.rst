.. title: Chapter 4: The Other Side
.. slug:
.. date: 2021-08-01 14:24:32 
.. tags: radis
.. author: anandxkumar
.. link: https://anandkumar-blog.netlify.app/5/
.. description:
.. category: gsoc2021


.. raw:: html

    <p>A new month has started and I have started to see the light at the end of the tunnel. Good Morning and welcome back. Phase 2 has been rolling and let us look at the new findings.</p>
    <p>Earlier the complexity of Legacy method was determined. The complexity of LDM Voigt and LDM FFT was to be determined using similar approach. Upon executing several benchmarks based on Number of lines, Spectum range, wstep, broadening max width. Previously it was thought the complexity was: <br /></p>
    <div class="gatsby-highlight"><pre class="language-text"><code class="language-text">time(LDM_fft) ~ c2*Nlines + c3*(N_G*N_L + 1)*N_v*log(N_v) (where N_v =  Spectral Points)
    <!-- TEASER_END -->
    time(LDM_voigt) ~ c2*Nlines + c3'*(N_G*N_L + 1)*N_truncation*log(N_truncation) (where N_truncation = broadening width / wstep)</code></pre></div>
    <p>But in actual Re running all benchmarks for <strong>LDM>Voigt</strong> and <strong>LDM>FFT</strong> with a <code class="language-text">broadening max width = 300 cm-1</code>. All benchmarks and visualizations can be found <a href="https://anandxkumar.github.io/Benchmark_Visualization_GSoC_2021/">here</a> we were able to conclude the followings:<br /></p>
    <p><strong>FFT:</strong><br />
    •  Complexity doesn’t depend on Nlines but rather wL x wG ; check this benchmark: <a href="https://public.tableau.com/app/profile/anand.kumar4841/viz/LDMLinesvsCalculationTimeUpdatedCO2/Sheet1">link</a>, it certainly looks like Complexity ∝ Nlines but its actually dependent on wL and wG, and gives same result on (wL x wG+ 1) x Spectral<em>Points x Log(Spectral</em>Points).<br />
    •  Upon implementing multiple linear regression for <strong>c1 x Nlines + c2 x (wL x wG+ 1)*Spectral<em>Points x Log(Spectral</em>Points)</strong> gives <code class="language-text">c1=2.65e-07</code>, <code class="language-text">c2=4.48256e-08</code> but their <code class="language-text">p value = 0.648 and 0.00001</code>, and <code class="language-text">p&gt;0.05</code> are insignificant, thus Nlines is insignificant for determining the complexity.<br />
    •  Since FFT is independent of broadening max width; benchmark: <a href="https://public.tableau.com/app/profile/anand.kumar4841/viz/LDMVoigtandFFTBMW_NEW/Sheet1">link</a>, so on comparing it Spectral point gives us same same time. Thus Spectral Point =  (wavenum max - wavenum max)/wstep instead of (wavenum maxcalc - wavenum min calc)/wstep<br />
    •  <strong>Overall complexity =  4.48256897e-08 x (wL x wG+ 1) x Spectral<em>Points(without BMW) x Log(Spectral</em>Points(without BMW))</strong>  <a href="https://anandxkumar.github.io/Benchmark_Visualization_GSoC_2021/LDM/Complexity_FFT_Final/Complexity_FFT_Final.html">link</a> (with the help of multple linear regression using sklearn; is almost accurate)<br /></p>
    <p><strong>Voigt:</strong><br />
    •  Similar to 1st point of FFT.<br />
    •  Upon doing multiple linear regression for <strong>c1 x N lines + c2 x (wL x wG + 1) x SpectralPoints x BMW xLog(SpectralPoints x (BMW) )</strong> gives <code class="language-text">c1=-1.9392e-06, c2=1.28256e-09</code> but their <code class="language-text">p value = 0.848 and 0.00001</code>, and <code class="language-text">p&gt;0.05</code> are insignificant, thus N<em>lines is insignificant for determining the complexity.<br />
    •  Calculation time is dependent `Broadening</em>Max<em>width`, but upon inspections with Spectral Points, we have the exact same plot. So complexity is dependent only on Spectral Points but with broadening</em>max<em>width i.e. wavenum</em>calc, which causes the increase in computational time on increasing broadening<em>max</em>width.<br />
    •  <strong>Overall complexity = 5.26795e-07 * (wL x wG+ 1)*Spectral Points x Log(Spectral Points)</strong> <a href="https://anandxkumar.github.io/Benchmark_Visualization_GSoC_2021/LDM/Complexity_Voigt_Final/Complexity_Voigt_Final.html">link</a> (with the help of multple linear regression using sklearn; almost straight)<br /></p>
    <p><strong>Also:</strong> From all the above plots, it really clear if going with broadening<em>max</em>width=300cm-1 in wavespace, it will take alot more time than fft in all aspects.</p>
    <p>But upon replacing <code class="language-text">np.convolve</code> with <code class="language-text">scipy.signal.oaconvolve</code>, we were able to achieve <code class="language-text">2 to 30</code> times performance boost. So it will be interesting to re run benchmarks with the latest piece of code and see which method performs better. Also some benchmarks will be added to ASV benchmark too to see how its performance changes over time.</p>
    <p>Also profiler was modified to a tree like a stucture using <code class="language-text">OrderedDict</code> and <code class="language-text">YAML</code> has been used to print the profiler in a proper structued way using <strong>Spectrum.print_perf_profiler()</strong> or <strong>SpectrumFactory.print_perf_profiler()</strong>.</p>
    <p><strong>Example:</strong></p>
    <div class="gatsby-highlight"><pre class="language-text"><code class="language-text">s = calc_spectrum(1900, 2300,         # cm-1
    molecule='CO',
    isotope='1,2,3',
    pressure=1.01325,   # bar
    Tvib=1000,          # K
    Trot=300,           # K
    mole_fraction=0.1,
    verbose=3,
    )
    s.print_perf_profile()</code></pre></div>
    <p><strong>Gives the following output:</strong></p>
    <div class="gatsby-highlight"><pre class="language-text"><code class="language-text">&gt;&gt;&gt; spectrum_calculation:
    &gt;&gt;&gt;   applied_linestrength_cutoff: 0.0024361610412597656
    &gt;&gt;&gt;   calc_emission_integral: 0.006468772888183594
    &gt;&gt;&gt;   calc_hwhm: 0.006415128707885742
    &gt;&gt;&gt;   calc_line_broadening:
    &gt;&gt;&gt;     DLM_Distribute_lines: 0.0003898143768310547
    &gt;&gt;&gt;     DLM_Initialized_vectors: 9.775161743164062e-06
    &gt;&gt;&gt;     DLM_closest_matching_line: 0.0005028247833251953
    &gt;&gt;&gt;     DLM_convolve: 0.029767990112304688
    &gt;&gt;&gt;     precompute_DLM_lineshapes: 0.013132810592651367
    &gt;&gt;&gt;     value: 0.07619166374206543
    &gt;&gt;&gt;   calc_lineshift: 0.00074005126953125
    &gt;&gt;&gt;   calc_noneq_population:
    &gt;&gt;&gt;     part_function: 0.03405046463012695
    &gt;&gt;&gt;     population: 0.005669832229614258
    &gt;&gt;&gt;     value: 0.03983640670776367
    &gt;&gt;&gt;   calc_other_spectral_quan: 0.002928495407104492
    &gt;&gt;&gt;   calc_weight_trans: 0.008247852325439453
    &gt;&gt;&gt;   check_line_databank: 0.0002810955047607422
    &gt;&gt;&gt;   check_non_eq_param: 0.04109525680541992
    &gt;&gt;&gt;   fetch_energy_5: 0.014983654022216797
    &gt;&gt;&gt;   generate_spectrum_obj: 0.00032138824462890625
    &gt;&gt;&gt;   generate_wavenumber_arrays: 0.0010433197021484375
    &gt;&gt;&gt;   reinitialize:
    &gt;&gt;&gt;     copy_database: 2.1457672119140625e-06
    &gt;&gt;&gt;     memory_usage_warning: 0.0018389225006103516
    &gt;&gt;&gt;     reset_population: 2.6226043701171875e-05
    &gt;&gt;&gt;     value: 0.001964569091796875
    &gt;&gt;&gt;   scaled_non_eq_linestrength:
    &gt;&gt;&gt;     corrected_population_se: 0.002747774124145508
    &gt;&gt;&gt;     map_part_func: 0.0010590553283691406
    &gt;&gt;&gt;     value: 0.0038983821868896484
    &gt;&gt;&gt;   value: 0.1904621124267578</code></pre></div>
    <p>So at the end a productive week! Looking forward to conclude GSoC with a worthy ending :)</p>

