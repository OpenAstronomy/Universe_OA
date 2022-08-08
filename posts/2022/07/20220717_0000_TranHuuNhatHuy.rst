.. title: Fifth week - Major updates on literally everything, and non-LTE benchmarking
.. slug:
.. date: 2022-07-17 00:00:00 
.. tags: radis
.. author: TranHuuNhatHuy
.. link: https://https://gsoc2022tranhuunhathuy.gatsbyjs.io/6. 5th-week/
.. description:
.. category: gsoc2022


.. raw:: html

    <p><a href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/b6a43fd435ed51da926a7346d2f66de9/JSON_sample.json">JSON sample</a></p>
    <h3>1. Fitting method benchmarking</h3>
    <p>The ideal of benchmarking result is to test and assess under what conditions, such as fitting method, pipeline, refinement, etc., the fitting process can achieve a stable and robust result. Firstly, I want to test the fitting method and see which ones are the best to put into the module as the default method. As we use LMFIT.Minimizer, we have 23 fitting methods in total:</p>
    <!-- TEASER_END -->
    <ul>
    <li><code class="language-text">leastsq</code>: Levenberg-Marquardt (default).</li>
    <li><code class="language-text">least_squares</code>: Least-Squares minimization, using Trust Region Reflective method.</li>
    <li><code class="language-text">differential_evolution</code>: differential evolution.</li>
    <li><code class="language-text">brute</code>: brute force method.</li>
    <li><code class="language-text">basinhopping</code>: Basin-hopping method.</li>
    <li><code class="language-text">ampgo</code>: Adaptive Memory Programming for Global Optimization.</li>
    <li><code class="language-text">nelder</code>: Nelder-Mead.</li>
    <li><code class="language-text">lbfgsb</code>: Limited-memory Broyden–Fletcher–Goldfarb–Shanno (L-BFGS-B).</li>
    <li><code class="language-text">powell</code>: Powell’s method.</li>
    <li><code class="language-text">cg</code>: Conjugate-Gradient.</li>
    <li><code class="language-text">newton</code>: Newton-Conjugate-Gradient.</li>
    <li><code class="language-text">cobyla</code>: Cobyla.</li>
    <li><code class="language-text">bfgs</code>: Broyden–Fletcher–Goldfarb–Shanno (BFGS).</li>
    <li><code class="language-text">tnc</code>: Truncated Newton.</li>
    <li><code class="language-text">trust-ncg</code>: Newton-Conjugate-Gradient trust-region.</li>
    <li><code class="language-text">trust-exact</code>: nearly exact trust-region.</li>
    <li><code class="language-text">trust-krylov</code>: Newton’s Generalized Lanczos Trust-Region (GLTR).</li>
    <li><code class="language-text">trust-constr</code>: trust-region for constrained optimization.</li>
    <li><code class="language-text">dogleg</code>: Dog-leg trust-region.</li>
    <li><code class="language-text">slsqp</code>: Sequential Linear Squares Programming.</li>
    <li><code class="language-text">emcee</code>: Maximum likelihood via Monte-Carlo Markov Chain.</li>
    <li><code class="language-text">shgo</code>: Simplicial Homology Global Optimization.</li>
    <li><code class="language-text">dual_annealing</code>: Dual Annealing optimization.</li>
    </ul>
    <p>In this list, there are 5 methods - <code class="language-text">newton</code>, <code class="language-text">trust-ncg</code>, <code class="language-text">trust_exact</code>, <code class="language-text">trust-krylov</code> and <code class="language-text">dogleg</code> - that require Jacobian function to work, which adds more complexity into our fitting process and codebase, hence I remove them from the benchmark and never use them again. There are also <code class="language-text">emcee</code> method that, for some unknown reasons, the fitting procedure never stops even after passing the loop limit, thus I have to remove it. Now we have 17 methods left that are stable enough to compare. Additionally, I set the max number of fitting loops as 200, so this means that any method that have equal of higher than 200 loops means that they are most likely unable to stop. I will conduct benchmarking process on the <code class="language-text">CO2_measured_spectrum_4-5um.spec</code> first.</p>
    <p>The result for this method-comparing benchmark can be found in <a href="https://gsoc2022tranhuunhathuy.gatsbyjs.io/method_comparison.txt">this JSON file</a>.</p>
    <table>
    <thead>
    <tr>
    <th align="left">Method</th>
    <th align="center">Last residual</th>
    <th align="center">Number of loops</th>
    <th align="center">Processing time (s)</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td align="left">leastsq</td>
    <td align="center">0.0027299042272</td>
    <td align="center">17</td>
    <td align="center">6.128568887710571</td>
    </tr>
    <tr>
    <td align="left">least_squares</td>
    <td align="center">0.0027299046347</td>
    <td align="center">14</td>
    <td align="center">3.8792104721069336</td>
    </tr>
    <tr>
    <td align="left">differential_evolution</td>
    <td align="center">0.0027299042330</td>
    <td align="center">48</td>
    <td align="center">7.211840629577637</td>
    </tr>
    <tr>
    <td align="left">brute</td>
    <td align="center">0.0027847218345</td>
    <td align="center">20</td>
    <td align="center">3.13600492477417</td>
    </tr>
    <tr>
    <td align="left">basinhopping</td>
    <td align="center">0.0030471725482</td>
    <td align="center">201</td>
    <td align="center">31.650216579437256</td>
    </tr>
    <tr>
    <td align="left">ampgo</td>
    <td align="center">0.0027301332094</td>
    <td align="center">201</td>
    <td align="center">36.60996413230896</td>
    </tr>
    <tr>
    <td align="left">nelder</td>
    <td align="center">0.0027299042330</td>
    <td align="center">48</td>
    <td align="center">7.532714605331421</td>
    </tr>
    <tr>
    <td align="left">lbfgsb</td>
    <td align="center">0.0027299043815</td>
    <td align="center">12</td>
    <td align="center">1.8955962657928467</td>
    </tr>
    <tr>
    <td align="left">powell</td>
    <td align="center">0.0027299042271</td>
    <td align="center">38</td>
    <td align="center">6.310025691986084</td>
    </tr>
    <tr>
    <td align="left">cg</td>
    <td align="center">0.0027299046922</td>
    <td align="center">34</td>
    <td align="center">5.223567724227905</td>
    </tr>
    <tr>
    <td align="left">cobyla</td>
    <td align="center">0.0027299044752</td>
    <td align="center">22</td>
    <td align="center">3.028048515319824</td>
    </tr>
    <tr>
    <td align="left">bfgs</td>
    <td align="center">0.0027299042351</td>
    <td align="center">20</td>
    <td align="center">2.9560532569885254</td>
    </tr>
    <tr>
    <td align="left">tnc</td>
    <td align="center">0.0027299042284</td>
    <td align="center">36</td>
    <td align="center">5.905533313751221</td>
    </tr>
    <tr>
    <td align="left">trust-constr</td>
    <td align="center">0.0027299042271</td>
    <td align="center">16</td>
    <td align="center">2.3700413703918457</td>
    </tr>
    <tr>
    <td align="left">slsqp</td>
    <td align="center">0.0027299969016</td>
    <td align="center">18</td>
    <td align="center">3.160074472427368</td>
    </tr>
    <tr>
    <td align="left">shgo</td>
    <td align="center">0.0027299042272</td>
    <td align="center">32</td>
    <td align="center">6.185185194015503</td>
    </tr>
    <tr>
    <td align="left">dual_annealing</td>
    <td align="center">0.0221619241989</td>
    <td align="center">201</td>
    <td align="center">32.40411591529846</td>
    </tr>
    </tbody>
    </table>
    <p><em>(It is important to remember that this result might differ for each run, but rest assure the common trend is unchanged)</em></p>
    <p>As you can see from the data above, we have <code class="language-text">basinhopping</code>, <code class="language-text">ampgo</code> and <code class="language-text">dual_annealing</code> jumping out of the loop limit of 200, and it’s totally not a good thing, which I would like to exclude them out for the sake of better visualization. Then, in order to compare the rest of 14 methods, I have a scatter plot below in which I focus on analyzing the <code class="language-text">last_residual</code> - indicator of accuracy - on the horizontal axis, and <code class="language-text">loops</code> - indicator of fitting iterations needed - on the vertical axis. As <code class="language-text">time</code> is heavily influenced by the computational capacity of each device, I don’t prioritize it than other two criteria in the result assessment, and thus it is indicated by color code.</p>
    <p><img alt="Scatter plot of the result." src="https://gsoc2022tranhuunhathuy.gatsbyjs.io/result_plot.png" /></p>
    <p>If we zoom in the best 8 cases marked by the red rectangle above:</p>
    <p><img alt="Best 8" src="https://gsoc2022tranhuunhathuy.gatsbyjs.io/result_zoomed.png" /></p>
    <p>In the zoomed figure, the result is quite satisfying as I expected. When we talk about the most famous curve-fitting algorithms, we can mention either <code class="language-text">leastsq</code>/<code class="language-text">least_squares</code> or <code class="language-text">bfgs</code>/<code class="language-text">lbfgsb</code>, and now we can see them taking 4 out of top 5. Now let’s focus on the two competitors: <code class="language-text">lbfgsb</code> and <code class="language-text">least_squares</code> and get some observations:</p>
    <ul>
    <li><code class="language-text">lbfgsb</code> has a little lower residual and so a little bit better in accuracy than <code class="language-text">least_squares</code>.</li>
    <li>Although approximately same fitting loops (12 and 14), the time required for <code class="language-text">lbfgsb</code> is 1.895596s, significantly lower than <code class="language-text">least_squares</code> of 3.879210s. We can also see this behavior in their neighbors: <code class="language-text">bfgs</code> (2.956053s) &#x3c; <code class="language-text">leastsq</code> (6.128569s).</li>
    </ul>
    <p>This is explainable. While <code class="language-text">least_squares</code> simply calculating and minimizing the sum of the residuals of points from the comparative curves, <code class="language-text">lbfgsb</code> - Limited-memory BFGS uses a limited amount of computer memory to conduct <a href="https://en.wikipedia.org/wiki/Broyden%E2%80%93Fletcher%E2%80%93Goldfarb%E2%80%93Shanno_algorithm">Broyden-Fletcher-Goldfarb-Shanno algorithm</a> for the minimization.</p>
    <p>So for now, I have initial assumption that <code class="language-text">lbfgsb</code> performs slightly better than <code class="language-text">leastsq</code>. After conducting fitting process on other spectra, the <code class="language-text">lbfgsb</code> and <code class="language-text">leastsq</code> are seem to be dominant in terms of speed (based on number of loops and time elapsed) and accuracy (this depends a little bit on pipeline combination, which will be addressed in next part) compared to other methods. However, more benchmarks are needed to confirm my initla assumption.</p>
    <h3>2. Fitting pipeline comparison</h3>
    <p>Next is the benchmarking process focusing on pipeline comparison. A fitting pipeline comprises of several options, from spectrum refinement methods such as which spectral quantity to take, whether applying normalization on both spectra or not, or simply just fitting process preferences such as maxinum number of fitting loops allowed, or fitting method, or max fitting tolerance. While in the new JSON structure the users are free to adjust all of them, through this benchmarking process I would like acquire more understandings about how these pipeline might affect the quality of a fitting work.</p>
    <p>In order to assess a fitting’s quality, I use the synthetic spectra that I generated on week 1. Although they are heavily convoluted with noises and offsets, since they are software-generated, we can know what are the experimental properties (such as <code class="language-text">path_length</code>, <code class="language-text">slit</code>, etc.). Meanwhile, regarding the experimental spectrum <code class="language-text">CO2_measured_spectrum_4-5um</code>, we are definitely not sure those parameters (in fact, we don’t even know whether it is LTE or non-LTE). So, I decided to test on 7 synthetic spectra:</p>
    <ol>
    <li><code class="language-text">synth-CO-1-1800-2300-cm-1-P3-t1500-v-r-mf0.1-p1-sl1nm.spec</code></li>
    <li><code class="language-text">synth-CO2-1-500-1100-cm-1-P2-t900-v-r-mf0.5-p1-sl1nm.spec</code></li>
    <li><code class="language-text">synth-CO2-1-500-3000-cm-1-P93-t740-v-r-mf0.96-p1-sl1nm.spec</code></li>
    <li><code class="language-text">synth-CO2-1-3300-3700-cm-1-P0.005-t3000-v-r-mf0.01-p1-sl1.4nm.spec</code></li>
    <li><code class="language-text">synth-H2O-1-1000-2500-cm-1-P0.5-t1500-v-r-mf0.5-p1-sl1nm.spec</code></li>
    <li><code class="language-text">synth-NH3-1-500-2000-cm-1-P10-t1000-v-r-mf0.01-p1-sl1nm.spec</code></li>
    <li><code class="language-text">synth-O2-1-7500-8000-cm-1-P1.01325-t298.15-v-r-mf0.21-p1-sl1nm.spec</code></li>
    </ol>
    <p>For each spectra, I will modify the pipeline’s <code class="language-text">method</code> and <code class="language-text">normalize</code> properties, until the best possible fitting result is achieved - least fitting loops, and closest to the ground-truth (GT) temperature (this is why I prefer synthetic over experimental spectra, as I explained above). Here is the result:</p>
    <table>
    <thead>
    <tr>
    <th align="center">Spec No.</th>
    <th align="center">GT Temp</th>
    <th align="center">Start Temp</th>
    <th align="center">Best Temp</th>
    <th align="center">Method</th>
    <th align="center">Normalize</th>
    <th align="center">Diff</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td align="center">1</td>
    <td align="center">1500</td>
    <td align="center">1300</td>
    <td align="center">1468.97</td>
    <td align="center"><code class="language-text">lbfgsb</code></td>
    <td align="center">false</td>
    <td align="center"><a href="https://raw.githubusercontent.com/TranHuuNhatHuy/my-2022-gsoc-journey/master/content/blog/5.%204th-week/1.png">1</a></td>
    </tr>
    <tr>
    <td align="center">2</td>
    <td align="center">900</td>
    <td align="center">1300</td>
    <td align="center">898.84</td>
    <td align="center"><code class="language-text">lbfgsb</code></td>
    <td align="center">false</td>
    <td align="center"><a href="https://raw.githubusercontent.com/TranHuuNhatHuy/my-2022-gsoc-journey/master/content/blog/5.%204th-week/2.png">2</a></td>
    </tr>
    <tr>
    <td align="center">3</td>
    <td align="center">740</td>
    <td align="center">1000</td>
    <td align="center">~740</td>
    <td align="center">both</td>
    <td align="center">false</td>
    <td align="center"><a href="https://raw.githubusercontent.com/TranHuuNhatHuy/my-2022-gsoc-journey/master/content/blog/5.%204th-week/3.png">3</a></td>
    </tr>
    <tr>
    <td align="center">4</td>
    <td align="center">3000</td>
    <td align="center">2850</td>
    <td align="center">3003.52</td>
    <td align="center"><code class="language-text">leastsq</code></td>
    <td align="center">false</td>
    <td align="center"><a href="https://raw.githubusercontent.com/TranHuuNhatHuy/my-2022-gsoc-journey/master/content/blog/5.%204th-week/4.png">4</a></td>
    </tr>
    <tr>
    <td align="center">5</td>
    <td align="center">1500</td>
    <td align="center">2000</td>
    <td align="center">1507.25</td>
    <td align="center"><code class="language-text">leastsq</code></td>
    <td align="center">true</td>
    <td align="center"><a href="https://raw.githubusercontent.com/TranHuuNhatHuy/my-2022-gsoc-journey/master/content/blog/5.%204th-week/5.png">5</a></td>
    </tr>
    <tr>
    <td align="center">6</td>
    <td align="center">1000</td>
    <td align="center">2250</td>
    <td align="center">994.90</td>
    <td align="center"><code class="language-text">leastsq</code></td>
    <td align="center">false</td>
    <td align="center"><a href="https://raw.githubusercontent.com/TranHuuNhatHuy/my-2022-gsoc-journey/master/content/blog/5.%204th-week/6.png">6</a></td>
    </tr>
    <tr>
    <td align="center">7</td>
    <td align="center">298.15</td>
    <td align="center">660</td>
    <td align="center">297.86</td>
    <td align="center"><code class="language-text">leastsq</code></td>
    <td align="center">false</td>
    <td align="center"><a href="https://raw.githubusercontent.com/TranHuuNhatHuy/my-2022-gsoc-journey/master/content/blog/5.%204th-week/7.png">7</a></td>
    </tr>
    </tbody>
    </table>
    <p>As we can see from the table above:</p>
    <ul>
    <li>All spectra achieve near-perfect best fit results. This is because we have perfect ground-truth conditions. In real-life circumstances, such accurate ground-truth is virtually impossible to achieve, but this is the job of fitting users to measure and set them.</li>
    <li><code class="language-text">leastsq</code> performs quite good in most case. This is quite surprising after the result from <code class="language-text">CO2_measured_spectrum_4-5um.spec</code>, but it can be explained as most likely we didn’t use the correct ground-truth conditions for it since we don’t know (seriously, who created that spectrum?). However, there is a small observation from me that, those cases where <code class="language-text">lbfgsb</code> lost agains <code class="language-text">leastsq</code> were primarily because of number of loops. Still, it’s a win for <code class="language-text">leastsq</code>.</li>
    <li>Their neighbors, <code class="language-text">least_squares</code> and <code class="language-text">bfgs</code>, are completely underdogs. We don’t even need to mention other methods.</li>
    <li>In nearly all the best cases, <code class="language-text">normalize = false</code> is set. This is quite explainable, the more originality the better.</li>
    </ul>
    <h3>3. Summary</h3>
    <p>After all the benchmarking works above, I have decided to set the <code class="language-text">leastsq</code> as the default fitting method, in case users don’t state the method explicitly in JSON file. Later on, in the fitting tutorial, I will add some suggestions about using <code class="language-text">lbfgsb</code> and trying to switch the <code class="language-text">normalize</code> in case their fitting work is not quite good.</p>
    <p>Nevertheless, these benchmarks helped me gain more insights about the performance of my fitting module, and most importantly, let me experience the feeling of a spectroscopist trying to fit his spectra - playing around the parameters, adjusting parameters and praying for a good result to come. Quite a physically and mentally exhausting work to be honest, since whenever the result went wrong, I didn’t know whether the error came from ground-truth conditions, or from my fitting module. There have been days and nights I sat in front of my laptop adjusting the JSON files and codebase continuously. But finally, the benchmarking process for LTE spectra is good now, and I am quite confident in my fitting module. Now let’s move on to the non-LTE spectra!</p>
    <p><img alt="A footage of me turning parameters up and down like a DJ" src="https://gsoc2022tranhuunhathuy.gatsbyjs.io/meme.jpg" /></p>

