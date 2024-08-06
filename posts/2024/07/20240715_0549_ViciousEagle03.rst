.. title: GSoC [Week 04-05] Progress
.. slug:
.. date: 2024-07-15 05:49:00 
.. tags: SunPy
.. author: ViciousEagle03
.. link: https://viciouseagle03.github.io/post/week-04-05-progress/
.. description:
.. category: gsoc2024


.. raw:: html

    <p><img alt="img" src="https://viciouseagle03.github.io/images/test_img.png" /></p>
    <blockquote>
    <p>This blog post covers all the work done in the fourth and fifth week of Google Summer of Code.</p>
    <!-- TEASER_END -->
    </blockquote>
    <h4 id="mid-term-evaluations-are-nearing">Mid term evaluations are nearing!</h4>
    <p>This week, my focus was on extending the test suite to include examples of loading an <code>NDCube</code> backed by various <code>gwcs.WCS</code> objects and testing the roundtrip serialization of the NDCube. I needed to verify that the ExtraCoords and GlobalCoords objects are correctly serialized and deserialized. Adding the gWCS test suite presented some challenges, but seeing it function correctly was incredibly rewarding. Completing these tasks was essential to ensure everything was in place for the mid-term evaluation 🚀.</p>
    <h3 id="adding-gwcs-test-suite">Adding gWCS Test Suite</h3>
    <p>This was the most challenging part for me this week. To check the roundtrip serialization of <code>gwcs.WCS</code> objects (i.e., ensuring all attributes of the <code>wcs</code> attribute of the NDCube are preserved when read and loaded through an ASDF file), I had to write a test suite for NDCube backed by different <code>gwcs.WCS</code> objects as the wcs attribute for the NDCube objects which would then be loaded into an NDCube and checked for roundtrip serialization.</p>
    <blockquote>
    <p>One of the <code>gwcs.WCS</code> test object which would be loaded in an NDCube and checked for roundtrip serialization.</p>
    </blockquote>
    <pre><code>def gwcs_4d_t_l_lt_ln():
    &quot;&quot;&quot;
    Creates a 4D GWCS object with time, wavelength, and celestial coordinates.
    
    - Time: Axis 0
    - Wavelength: Axis 1
    - Sky: Axes 2 and 3
    
    Returns:
    wcs.WCS: 4D GWCS object.
    &quot;&quot;&quot;
    
    time_model = models.Identity(1)
    time_frame = cf.TemporalFrame(axes_order=(0, ), unit=u.s,
    reference_frame=Time(&quot;2000-01-01T00:00:00&quot;))
    
    wave_frame = cf.SpectralFrame(axes_order=(1, ), unit=u.m, axes_names=('wavelength',))
    wave_model = models.Scale(0.2)
    
    shift = models.Shift(-5) &amp; models.Shift(0)
    scale = models.Scale(5) &amp; models.Scale(20)
    tan = models.Pix2Sky_TAN()
    celestial_rotation = models.RotateNative2Celestial(0, 0, 180)
    cel_model = shift | scale | tan | celestial_rotation
    sky_frame = cf.CelestialFrame(axes_order=(2, 3), name='icrs',
    reference_frame=coord.ICRS(),
    axes_names=(&quot;longitude&quot;, &quot;latitude&quot;))
    
    transform = time_model &amp; wave_model &amp; cel_model
    
    frame = cf.CompositeFrame([time_frame, wave_frame, sky_frame])
    detector_frame = cf.CoordinateFrame(name=&quot;detector&quot;, naxes=4,
    axes_order=(0, 1, 2, 3),
    axes_type=(&quot;pixel&quot;, &quot;pixel&quot;, &quot;pixel&quot;, &quot;pixel&quot;),
    unit=(u.pix, u.pix, u.pix, u.pix))
    
    return (wcs.WCS(forward_transform=transform, output_frame=frame, input_frame=detector_frame))
    </code></pre>
    <h3 id="checking-the-extracoords-and-globalcoords">Checking the ExtraCoords and GlobalCoords</h3>
    <p>I had to make sure the converters written for these objects preserved all the required parameters when saved to an ASDF file and read from an ASDF file. Doing this was straightforward as my mentors helped me during the process of writing the tests and ensuring good coverage.</p>
    <h3 id="handling-unsupported-attributes">Handling Unsupported Attributes</h3>
    <p>It is as important to test the supported API as it is to throw a warning to the user when a particular attribute serialization is unsupported. I added warnings for attributes that are not yet supported (such as a sliced <code>NDCube</code> and <code>wcs</code> attribute of the <code>NDCube</code> as the <code>astropy.wcs.WCS</code> object), which I plan to support in the future.</p>

