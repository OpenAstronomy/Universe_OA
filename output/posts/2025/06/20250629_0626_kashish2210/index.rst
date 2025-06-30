.. title: ✨Good Time, Bad Time: GTI/BTI :)
.. slug:
.. date: 2025-06-29 06:26:00 
.. tags: JuliaAstro
.. author: kashish shrivastav
.. link: https://kashish2210.blogspot.com/2025/06/good-time-bad-time-gtibti.html
.. description:
.. category: gsoc2025


.. raw:: html

    <p>In my continued journey with <code>Stingray.jl</code> During GSoC 2025, this phase focused on a core aspect of high-energy astrophysics: time filtering using <strong>GTIs (Good Time Intervals)</strong> and <strong>BTIs (Bad Time Intervals)</strong>. After a productive discussion with my mentor <a class="" href="https://github.com/matteobachetti" rel="noopener" target="_new">@matteobachetti</a> during our meet, I dove into implementing and refining functionality around GTIs—an essential tool in the timing analysis of astrophysical data.</p><div class="flex basis-auto flex-col -mb-(--composer-overlap-px) [--composer-overlap-px:24px] grow overflow-hidden"><div class="relative h-full"><div class="flex h-full flex-col overflow-y-auto [scrollbar-gutter:stable_both-edges] @[84rem]/thread:pt-(--header-height)"><div class="@thread-xl/thread:pt-header-height flex flex-col text-sm pb-25"><article class="text-token-text-primary w-full" dir="auto"><div class="text-base my-auto mx-auto py-5 [--thread-content-margin:--spacing(4)] @[37rem]:[--thread-content-margin:--spacing(6)] @[72rem]:[--thread-content-margin:--spacing(16)] px-(--thread-content-margin)"><div class="[--thread-content-max-width:32rem] @[34rem]:[--thread-content-max-width:40rem] @[64rem]:[--thread-content-max-width:48rem] mx-auto flex max-w-(--thread-content-max-width) flex-1 text-base gap-4 md:gap-5 lg:gap-6 group/turn-messages focus-visible:outline-hidden" tabindex="-1"><div class="group/conversation-turn relative flex w-full min-w-0 flex-col agent-turn"><div class="relative flex-col gap-1 md:gap-3"><div class="flex max-w-full flex-col grow"><div class="min-h-8 text-message relative flex w-full flex-col items-end gap-2 text-start break-words whitespace-normal [.text-message+&amp;]:mt-5" dir="auto"><div class="flex w-full flex-col gap-1 empty:hidden first:pt-[3px]"><div class="markdown prose dark:prose-invert w-full break-words dark">
    <h3>What Are GTIs and BTIs?</h3>
    <ul>
    <!-- TEASER_END -->
    <li>
    <p><strong>GTIs</strong> define intervals during which the data is considered reliable—free of contamination, instrument artifacts, or observational interruptions.</p>
    </li>
    <li>
    <p><strong>BTIs</strong> are the complementary regions—gaps between GTIs that typically represent unusable or noisy time segments.</p>
    </li>
    </ul>
    <p>Correct handling of these intervals is critical, especially in <strong>X-ray timing</strong>, where even small artifacts can skew power spectra, light curves, and periodograms.</p>
    <hr />
    <h3>Worked on Features this week</h3>
    <p>I extended and validated the implementation of GTI filtering in both <code>EventList</code> and <code>LightCurve</code> structures:</p>
    <hr />
    <h4><code>apply_gtis(el::EventList, gtis::Matrix)</code></h4>
    <p>This function filters photon events using a list of GTIs:</p><pre class="overflow-visible!"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-julia">filtered_el = filter_time(t -&gt; gti_start ≤ t ≤ gti_stop, el)
    </code></div></div></pre>
    <p>Only events within the GTI boundaries are retained, and only non-empty segments are returned. This helps preserve valid data while preparing segments for further timing analysis.</p>
    <hr />
    <h4><code>apply_gtis(lc::LightCurve, gtis::Matrix)</code></h4>
    <p>For light curves, bins are included <strong>only if their centers fall entirely within a GTI</strong>:</p><pre class="overflow-visible!"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-julia">bin_mask = (lc.time .≥ gti_start) .&amp; (lc.time .≤ gti_stop)
    </code></div></div></pre>
    <p>This strict criterion ensures that bin integrity is preserved—especially important for Fourier-based methods like power spectral density and periodogram calculations. Each resulting segment includes full metadata and is well-formed for downstream analysis.</p>
    <hr />
    <h4><code>fill_bad_time_intervals!(el::EventList, gtis::Matrix)</code></h4>
    <p>I also implemented an <strong>experimental utility</strong> for BTI filling. Short gaps (BTIs shorter than a configurable threshold) can be optionally filled with <strong>synthetic events</strong> to maintain temporal continuity for methods sensitive to uneven sampling.</p>
    <p>Highlights:</p>
    <ul>
    <li>
    <p>BTIs are computed from GTIs and event time range.</p>
    </li>
    <li>
    <p>Short gaps can be filled with randomly spaced synthetic events.</p>
    </li>
    <li>
    <p>Synthetic events sample from the original energy distribution (if present).</p>
    </li>
    <li>
    <p>Metadata is updated to clearly tag synthetic data.</p>
    </li>
    </ul>
    <p>This feature is useful for methods like <strong>Bartlett periodograms</strong> or other analyses where continuity is required but small gaps might otherwise bias the results</p>
    <hr />
    <p>Stay tuned for the next dive into timing analysis tools in <code>Stingray.jl</code>. Until then—make your time intervals <em>good</em> :)</p></div></div></div></div></div></div></div></div></article></div></div></div></div><div class="isolate z-10 w-full basis-auto has-data-has-thread-error:pt-2 has-data-has-thread-error:[box-shadow:var(--sharp-edge-bottom-shadow)] md:border-transparent md:pt-0 dark:border-white/20 md:dark:border-transparent flex flex-col" id="thread-bottom-container"><div class="text-token-text-secondary relative mt-auto flex min-h-8 w-full items-center justify-center p-2 text-center text-xs md:px-[60px]"><div></div></div></div>

