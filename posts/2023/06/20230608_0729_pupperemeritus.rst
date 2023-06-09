.. title: GSoC Week 1 Progress Update
.. slug:
.. date: 2023-06-08 07:29:01 
.. tags: stingray
.. author: pupper emeritus
.. link: https://dev.to/pupperemeritus/gsoc-week-1-progress-update-17pp
.. description:
.. category: gsoc2023


.. raw:: html

    <h1>
    
    
    <!-- TEASER_END -->
    Brief
    </h1>
    
    <p>Week 1 has been quite eventful with me creating a Lomb Scargle Fourier Transform function and get a working class for Lomb Scargle Cross Spectrum and Power Spectrum.</p>
    
    <p>I inherited my LS cross spectrum from the regular cross spectrum class. Had to rewrite the <code>constructor</code>, <code>initial_checks</code> , <code>make_crossspectrum</code>, <code>_make_auxil_pds</code> and <code>_initialize_empty</code>. And also wrote a new <code>_ls_cross</code> method which just returns the frequencies and cross spectra for given light curves and it is an internal function only to be used by the class.</p>
    
    <p>The original slow implementation has been completed. I am still working on the fast version.</p>
    
    <p>As this is not a project that can be completed in a bunch of small PRs, I will push to a single PR which will be merged after completion of the project. The following draft PR is the one to which I will be pushing to. </p>
    
    <p><a href="https://github.com/StingraySoftware/stingray/pull/737/">https://github.com/StingraySoftware/stingray/pull/737/</a></p>
    
    <h1>
    
    
    Details
    </h1>
    
    <p>The following are the APIs for the classes</p>
    
    <h2>
    
    
    Cross Spectrum
    </h2>
    
    
    
    <div class="highlight js-code-highlight">
    <pre class="highlight plaintext"><code>Make a cross spectrum from an unevenly sampled light curve.
    You can also make an empty :class:`Crossspectrum` object to populate with your
    own Fourier-transformed data (this can sometimes be useful when making
    binned power spectra).
    
    Parameters
    ----------
    data1: :class:`stingray.Lightcurve` or :class:`stingray.events.EventList`, optional, default ``None``
    The dataset for the first channel/band of interest.
    
    data2: :class:`stingray.Lightcurve` or :class:`stingray.events.EventList`, optional, default ``None``
    The dataset for the second, or "reference", band.
    
    norm: {``frac``, ``abs``, ``leahy``, ``none``}, default ``none``
    The normalization of the (real part of the) cross spectrum.
    
    power_type: string, optional, default ``real``
    Parameter to choose among complete, real part and magnitude of the cross spectrum.
    
    fullspec: boolean, optional, default ``False``
    If False, keep only the positive frequencies, or if True, keep all of them .
    
    Other Parameters
    ----------------
    dt: float
    The time resolution of the light curve. Only needed when constructing
    light curves in the case where ``data1``, ``data2`` are
    :class:`EventList` objects
    
    skip_checks: bool
    Skip initial checks, for speed or other reasons (you need to trust your
    inputs!)
    
    min_freq : float
    Minimum frequency to take the Lomb-Scargle Fourier Transform
    
    max_freq: float
    Maximum frequency to take the Lomb-Scargle Fourier Transform
    
    df : float
    The time resolution of the light curve. Only needed where ``data1``, ``data2`` are
    
    method : str
    The method to be used by the Lomb-Scargle Fourier Transformation function. `fast`
    and `slow` are the alloowed values. Default is `fast`. fast uses the optimized Press
    and Rybicki O(n*log(n))
    
    Attributes
    ----------
    freq: numpy.ndarray
    The array of mid-bin frequencies that the Fourier transform samples
    
    power: numpy.ndarray
    The array of cross spectra (complex numbers)
    
    power_err: numpy.ndarray
    The uncertainties of ``power``.
    An approximation for each bin given by ``power_err= power/sqrt(m)``.
    Where ``m`` is the number of power averaged in each bin (by frequency
    binning, or averaging more than one spectra). Note that for a single
    realization (``m=1``) the error is equal to the power.
    
    df: float
    The frequency resolution
    
    m: int
    The number of averaged cross-spectra amplitudes in each bin.
    
    n: int
    The number of data points/time bins in one segment of the light
    curves.
    
    k: array of int
    The rebinning scheme if the object has been rebinned otherwise is set to 1.
    
    nphots1: float
    The total number of photons in light curve 1
    
    nphots2: float
    The total number of photons in light curve 2
    </code></pre>
    
    </div>
    
    
    
    <h2>
    
    
    Power Spectrum
    </h2>
    
    
    
    <div class="highlight js-code-highlight">
    <pre class="highlight plaintext"><code>Make a :class:`LombScarglePowerspectrum` (also called periodogram) from a unevenly sampled (binned)
    light curve. Periodograms can be normalized by either Leahy normalization,
    fractional rms normalization, absolute rms normalization, or not at all.
    
    You can also make an empty :class:`LombScarglePowerspectrum` object to populate with
    your own fourier-transformed data (this can sometimes be useful when making
    binned power spectra).
    
    Parameters
    ----------
    data: :class:`stingray.lightcurve.Lightcurve` or :class:`stingray.events.EventList` object, optional, default ``None``
    The light curve data to be Fourier-transformed.
    
    norm: {"leahy" | "frac" | "abs" | "none" }, optional, default "frac"
    The normaliation of the power spectrum to be used. Options are
    "leahy", "frac", "abs" and "none", default is "frac".
    
    Other Parameters
    ----------------
    dt: float
    The time resolution of the light curve. Only needed when constructing
    light curves in the case where ``data`` is a
    :class:`EventList` object
    
    skip_checks: bool
    Skip initial checks, for speed or other reasons (you need to trust your
    inputs!).
    
    min_freq : float
    Minimum frequency to take the Lomb-Scargle Fourier Transform
    
    max_freq: float
    Maximum frequency to take the Lomb-Scargle Fourier Transform
    
    df : float
    The time resolution of the light curve. Only needed where ``data`` is a :class`stingray.Eventlist` object
    
    method : str
    The method to be used by the Lomb-Scargle Fourier Transformation function. `fast`
    and `slow` are the alloowed values. Default is `fast`. fast uses the optimized Press
    and Rybicki O(n*log(n))
    
    Attributes
    ----------
    norm: {"leahy" | "frac" | "abs" | "none" }
    The normalization of the power spectrum.
    
    freq: numpy.ndarray
    The array of mid-bin frequencies that the Fourier transform samples.
    
    power: numpy.ndarray
    The array of normalized squared absolute values of Fourier
    amplitudes.
    
    power_err: numpy.ndarray
    The uncertainties of ``power``.
    An approximation for each bin given by ``power_err= power/sqrt(m)``.
    Where ``m`` is the number of power averaged in each bin (by frequency
    binning, or averaging power spectra of segments of a light curve).
    Note that for a single realization (``m=1``) the error is equal to the
    power.
    
    df: float
    The frequency resolution.
    
    m: int
    The number of averaged powers in each bin.
    
    n: int
    The number of data points in the light curve.
    
    nphots: float
    The total number of photons in the light curve.
    </code></pre>
    
    </div>

