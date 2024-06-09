.. title: Community Bonding and Week 01 Progress
.. slug:
.. date: 2024-06-07 20:45:27 
.. tags: SunPy
.. author: ViciousEagle03
.. link: https://viciouseagle03.github.io/post/community-bonding-and-week-01/
.. description:
.. category: gsoc2024


.. raw:: html

    <p>This post documents the planning of the project, my learnings during the community bonding period, and the tasks I completed in my first week.</p>
    <h2 id="community-bonding-period">Community Bonding Period</h2>
    <p>After the euphoria of being accepted into GSoC faded, it was time for setting up my workspace and diving back into the codebase after a month. Planning out the project was key, and meeting with my mentors was a big part of that. I was excited for this chat because the mentors had been super helpful and easy to reach during the proposal stage.</p>
    <!-- TEASER_END -->
    <h2 id="setting-the-stage-mentor-meet-up-and-project-planning">Setting the Stage: Mentor Meet-Up and Project Planning</h2>
    <p>During the meet-up, we discussed about the best approach to kick-start the development process. It was mostly the mentors discussing about the possible roadmap and as they outlined the project roadmap, I listened carefully, taking notes on important discussions. One of the key decision was to set up clear communication channels and workflows to make sure we all stay on the same page and to ensure I do not vary off of the project or get stuck in a deadend.</p>
    <p>Additionally, we agreed to use GitHub projects for project management, making it easier to keep track of tasks and monitor progress. You can check out the GitHub project here: <a href="https://github.com/orgs/sunpy/projects/12/views/1"><strong>Github Project</strong></a></p>
    <p>Apart from discussing the project proceedings, I was also tasked with setting up a blog website to document my GSoC journey and share updates with the community. I decided to use Hugo to create the blog website and deployed it through GitHub pages. Additionally, I was asked to share the RSS feed of my blog to ensure that project updates are easily accessible to everyone.</p>
    <p><img alt="" src="https://viciouseagle03.github.io/images/tasks.png" /></p>
    <hr />
    <h1 id="week-01-first-coding-week">Week [01]: First Coding Week</h1>
    <h2 id="a-brief-overview-about-my-project">A brief overview about my project</h2>
    <p>My projects aims to enable the storage and retrieval of NDCube objects using the ASDF file format. Currently, ndcube lacks native support for saving NDCube objects to files and loading them back, limiting its usability. To address this, the project will implement convertors and schema definitions for NDCube objects and related classes ensuring robust serialization and deserialiazation. The first phase of my project requires the complete imlementation of serialization of an <strong>ndcube.NDCube</strong> object when <code>.data</code> is a numpy array and <code>.wcs</code> is a <strong>gwcs.WCS object</strong>.</p>
    <h2 id="the-prototype">The Prototype</h2>
    <p>In our meeting, we discussed the initial steps, which centered around laying the groundwork for serialization support for the NDCube object, particularly focusing on establishing basic functionality. This included implementing the convertor class, registering the convertors as ASDF extensions, and ensuring they were readily available via entry points. Getting a good grasp of the whole serialization process took some dedicated reading through the ASDF docs 🧐.</p>
    <ul>
    <li>
    <p>Convertor Class: I implemented the convertor class, including the <code>to_yaml_tree</code> and <code>from_yaml_tree</code> methods. The former converts NDCube object attributes into a single node object suitable for serialization. Now, here&rsquo;s the super cool part the <code>.wcs</code> attribute of the NDCube object, being a complex object, is accommodated within the node, as the node is permitted to contain nested complex objects.
    <em>Viola!</em> , so I was able to leverage the existing convertor for GWCS objects which made the process somewhat less complicated. The latter method is exactly the opposite, it accepts a single node object from parsed YAML and returns the corresponding NDCube object.</p>
    </li>
    <li>
    <p>Schema and Manifests: The Schema was designed to validate the presence, and the datatype of the validator properties for the NDCube object. The manifest was implemented for acheiving the resource mapping of the schema.</p>
    </li>
    <li>
    <p>ASDF Integration: In entry_point.py, I&rsquo;ve implemented get_resource_mapping to retrieve mappings for schema and manifest files, required for ASDF file validation and identifying NDCube objects and the get_extension is implemented to retrieve extensions , here the extension through which the ndcube convertor was registered</p>
    </li>
    </ul>
    <h2 id="code-demonstration">Code Demonstration</h2>
    <h3 id="ndcube-initialised-with-gwcswcs-object-as-its-wcs-attribute">NDCube initialised with gwcs.WCS object as its &lsquo;.wcs&rsquo; attribute</h3>
    <blockquote>
    </blockquote>
    <pre><code>import numpy as np
    import asdf
    from astropy.time import Time
    from ndcube import NDCube
    from ndcube.extra_coords import QuantityTableCoordinate, TimeTableCoordinate
    import astropy.units as u
    
    
    energy = np.arange(10) * u.keV
    time = Time('2020-01-01 00:00:00') + np.arange(10) * u.s
    energy_coord = QuantityTableCoordinate(energy, names='energy', physical_types='em.energy')
    time_coord = TimeTableCoordinate(time, names='time', physical_types='time')
    
    # Initialize the GWCS object
    wcs = (time_coord &amp; energy_coord).wcs
    data = np.random.rand(len(time), len(energy))
    
    # Initialize the NDCube
    ndcube = NDCube(data, wcs=wcs)
    
    with asdf.AsdfFile() as af:
    af.tree['ndcube'] = ndcube
    af.write_to('ndcube.asdf')
    </code></pre>
    <h3 id="serialized-asdf-file">Serialized ASDF File</h3>
    <pre tabindex="0"><code>#ASDF 1.0.0
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
    extension_uri: asdf://sunpy.org/extensions/ndcube-0.1.0
    software: !core/software-1.0.0 {name: ndcube, version: 2.3.dev224+g04409b5.d20240605}
    - !core/extension_metadata-1.0.0
    extension_class: asdf_astropy._manifest.CompoundManifestExtension
    extension_uri: asdf://astropy.org/core/extensions/core-1.5.0
    software: !core/software-1.0.0 {name: asdf-astropy, version: 0.5.0}
    - !core/extension_metadata-1.0.0
    extension_class: asdf.extension._manifest.ManifestExtension
    extension_uri: asdf://asdf-format.org/transform/extensions/transform-1.5.0
    software: !core/software-1.0.0 {name: asdf-astropy, version: 0.5.0}
    - !core/extension_metadata-1.0.0
    extension_class: asdf.extension._manifest.ManifestExtension
    extension_uri: asdf://asdf-format.org/astronomy/gwcs/extensions/gwcs-1.2.0
    software: !core/software-1.0.0 {name: gwcs, version: 0.20.0}
    ndcube: &amp;id001 !&lt;tag:sunpy.org:ndcube/ndcube/NDCube-0.1.0&gt;
    data: !core/ndarray-1.0.0
    source: 0
    datatype: float64
    byteorder: little
    shape: [10, 10]
    extra_coords: !&lt;tag:sunpy.org:ndcube/extra_coords/extra_coords/ExtraCoords-0.1.0&gt;
    dropped_tables: []
    ndcube: *id001
    wcs: !&lt;tag:stsci.edu:gwcs/wcs-1.2.0&gt;
    name: ''
    pixel_shape: null
    steps:
    - !&lt;tag:stsci.edu:gwcs/step-1.1.0&gt;
    frame: !&lt;tag:stsci.edu:gwcs/frame-1.0.0&gt;
    axes_names: ['', '']
    axes_order: [0, 1]
    axes_type: [PIXEL, PIXEL]
    axis_physical_types: ['custom:PIXEL', 'custom:PIXEL']
    name: PixelFrame
    naxes: 2
    unit: [!unit/unit-1.0.0 pixel, !unit/unit-1.0.0 pixel]
    transform: !transform/concatenate-1.2.0
    forward:
    - !transform/tabular-1.2.0
    bounds_error: false
    fill_value: .nan
    inputs: [x]
    lookup_table: !unit/quantity-1.1.0
    unit: !unit/unit-1.0.0 s
    value: !core/ndarray-1.0.0
    source: 1
    datatype: float64
    byteorder: little
    shape: [10]
    method: linear
    outputs: [y]
    points:
    - !unit/quantity-1.1.0
    unit: !unit/unit-1.0.0 pixel
    value: !core/ndarray-1.0.0
    source: 2
    datatype: float64
    byteorder: little
    shape: [10]
    - !transform/tabular-1.2.0
    bounds_error: false
    fill_value: .nan
    inputs: [x]
    lookup_table: !unit/quantity-1.1.0
    unit: !unit/unit-1.0.0 keV
    value: !core/ndarray-1.0.0
    source: 3
    datatype: float64
    byteorder: little
    shape: [10]
    method: linear
    outputs: [y]
    points:
    - !unit/quantity-1.1.0
    unit: !unit/unit-1.0.0 pixel
    value: !core/ndarray-1.0.0
    source: 4
    datatype: float64
    byteorder: little
    shape: [10]
    inputs: [x0, x1]
    outputs: [y0, y1]
    - !&lt;tag:stsci.edu:gwcs/step-1.1.0&gt;
    frame: !&lt;tag:stsci.edu:gwcs/composite_frame-1.0.0&gt;
    frames:
    - !&lt;tag:stsci.edu:gwcs/temporal_frame-1.0.0&gt;
    axes_names: [time]
    axes_order: [0]
    axis_physical_types: [time]
    name: TemporalFrame
    reference_frame: !time/time-1.1.0 2020-01-01 00:00:00.000
    unit: [!unit/unit-1.0.0 s]
    - !&lt;tag:stsci.edu:gwcs/frame-1.0.0&gt;
    axes_names: [energy]
    axes_order: [1]
    axes_type: [CUSTOM]
    axis_physical_types: [em.energy]
    name: CoordinateFrame
    naxes: 1
    unit: [!unit/unit-1.0.0 keV]
    name: CompositeFrame
    transform: null
    ...
    �BLK0 [TY*ߝ��R�4p}Q����?��#���?ȩȏ��?���#��?��ҩ��?*B��y�?ʱ�tv��?������?�fEp�X�?k1^}��?=���A�?�]����?
    �֜���?���H�?��)9�?{juoPW�?p�:����?0�T9��?w�A��?pWݫ	%�?�K#)cB�?�uv����?V‹����?���^�.�?��2���?���eQ�?^߁}���?�$6mwp�?�&amp;�"��?N�;�[�?4�؅J3�?
    ����?=&gt;��ܨ?��#%�?J6F=s��?E��}.�?°���
    �?����Qa�?;��0�?vM���?q��ǖ'�?�&lt;5��?G]�X�?��.���?��ɐ?�?j��G�L�?&lt;��&amp;��?��q];I?�̱���?X�Dt�v�?Pҧ���?0�=�E��?����?O&gt;&gt;tGj?D.���#�?p�N����?,$�V)��?j��xƦ�?�v�h�?�"�
    �p�?7S�0�?���ۢ`�?8YI�yְ?"E��o��?J�G�8�?�W�����?����ـ�?t���o�?sg���?h�Ȝ���?�)�=g�?e/B/�?�2�;�?�~�xT��?s�S���?t�|1.��?�n��ʳ?��/�؛�?jd����?�oB���?Lz09��?�����?��ga��?`������?���kW��?���P7�?�|�F@�?Oq���?d���$�?&gt;�e�~�?�t�(�?�Ԓ���?&lt;�P����?���a�?�Q΢���?����?Ѳ�#[[�?� �^�X�?jC�����?�mJA��?�BLK0PPP?�N��{I�?N"F98��?`������? @�	@h�����@ @������@x�����@"@�BLK0PPP�����Z
    �η~�ZH�?@@@@@@ @"@�BLK0PPP�����Z
    �η~�ZH�?@@@@@@ @"@�BLK0PPP�����Z
    �η~�ZH�?@@@@@@ @"@#ASDF BLOCK INDEX
    %YAML 1.1
    ---
    - 4304
    - 5158
    - 5292
    - 5426
    - 5560
    ...
    </code></pre><h2 id="gsoc-week-one-reflections">GSoC Week One: Reflections</h2>
    <p>My first week with GSoC has been a thrilling ride, full of learning and growth. The support from the community has been incredible. Looking forward to what lies ahead!🚀</p>
    <blockquote>
    <p>Perseverance is not a long race; it is many short races one after the other.</p>
    </blockquote>

