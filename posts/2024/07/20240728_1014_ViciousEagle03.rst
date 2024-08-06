.. title: GSoC [Week 06-07] Progress
.. slug:
.. date: 2024-07-28 10:14:09 
.. tags: SunPy
.. author: ViciousEagle03
.. link: https://viciouseagle03.github.io/post/week-06-progress/
.. description:
.. category: gsoc2024


.. raw:: html

    <p><img alt="img" src="https://viciouseagle03.github.io/images/mid_term.png" /></p>
    <blockquote>
    <p>This blog post covers all the work done in the sixth week of Google Summer of Code.</p>
    <!-- TEASER_END -->
    </blockquote>
    <p>After having developed the serialization logic for NDCube with wcs as <code>gWCS</code>, the next step was to extend this support to handle the serialization of NDCube where the wcs attribute is <code>astropy.wcs.WCS</code>. This week my primary focus has been on enabling the serialization of <code>astropy.wcs.WCS</code> objects to ASDF. This task involves adding the necessary serialization logic to the asdf-astropy repository.</p>
    <h3 id="discussions-on-wcs-serialization">Discussions on WCS Serialization</h3>
    <p>We had a discussion about the process of serializing WCS objects and covered the following points:</p>
    <h4 id="complex-wcs-types">Complex WCS Types:</h4>
    <p>WCS types like tabular and distortion ones are tricky because they involve data tables. Handling these types requires a more sophisticated approach.</p>
    <h4 id="approach-discussion">Approach Discussion:</h4>
    <p>We discussed serializing a HDUList object or using <code>WCS.to_hdu</code> for the complex WCS types but that seems pretty complex for a first attempt. We agreed on initially not supporting these complex WCS types and just using <code>WCS.to_header()</code> for now for supporting the serialization of the basic WCS objects.</p>
    <h3 id="whats-new">What&rsquo;s new</h3>
    <p>So after my PR gets merged asdf-astropy would support the serialization of the <code>astropy.wcs.WCS</code> objects to ASDF.
    Ideally we would want to detect tabular and distortion WCS types and throw an error if they come up. This way, we’re clear about what’s supported and we agreed on revisiting this part and in the future and to extend this to support the serialization of the complex WCS objects.</p>
    <blockquote>
    <p>Serialized simple <code>astropy.wcs.WCS</code> object to ASDF</p>
    </blockquote>
    <pre><code>#ASDF 1.0.0
    #ASDF_STANDARD 1.5.0
    %YAML 1.1
    %TAG ! tag:stsci.edu:asdf/
    --- !core/asdf-1.1.0
    asdf_library: !core/software-1.0.0 {author: The ASDF Developers, homepage: 'http://github.com/asdf-format/asdf',
    name: asdf, version: 3.0.1}
    history:
    extensions:
    - !core/extension_metadata-1.0.0
    extension_class: asdf.extension._manifest.ManifestExtension
    extension_uri: asdf://asdf-format.org/core/extensions/core-1.5.0
    software: !core/software-1.0.0 {name: asdf, version: 3.0.1}
    - !core/extension_metadata-1.0.0
    extension_class: asdf.extension._manifest.ManifestExtension
    extension_uri: asdf://astropy.org/astropy/extensions/astropy-1.0.0
    software: !core/software-1.0.0 {name: asdf-astropy, version: 0.6.1.dev10+gdab5b4d.d20240723}
    fits: !&lt;tag:astropy.org:astropy/fits/fitswcs-1.0.0&gt;
    header: {CDELT1: 0.4, CDELT2: 2.0e-11, CDELT3: 0.0055555555555556, CDELT4: 0.0013888888888889,
    CRPIX1: 0.0, CRPIX2: 0.0, CRPIX3: 0.0, CRPIX4: 5.0, CRVAL1: 0.0, CRVAL2: 0.0,
    CRVAL3: 0.0, CRVAL4: 0.0, CTYPE1: TIME, CTYPE2: WAVE, CTYPE3: HPLT-TAN, CTYPE4: HPLN-TAN,
    CUNIT1: min, CUNIT2: m, CUNIT3: deg, CUNIT4: deg, DATEREF: '2020-01-01T00:00:00',
    LATPOLE: 0.0, LONPOLE: 180.0, MJDREF: 58849.0, WCSAXES: 4}
    ...
    </code></pre>

