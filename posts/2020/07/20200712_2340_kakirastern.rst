.. title: GSoC 2020: glue-solar project 2.1
.. slug:
.. date: 2020-07-12 23:40:22 
.. tags: SunPy
.. author: Kris Stern
.. link: https://medium.com/@krisastern/gsoc-2020-glue-solar-project-2-1-620347ad3f8d?source=rss-33703681b362------2
.. description:
.. category: gsoc2020


.. raw:: html

    <p>The second coding period is now officially halfway through. Since the end of the first coding period, I have been working on both the <a href="https://github.com/glue-viz/glue/pull/2156">1D Profile viewer</a> and <a href="https://github.com/glue-viz/glue/pull/2161">WCS autolinking</a>. Since much has been discussed about the 1D Profile viewer of glue and now that it is finally working, let me take the opportunity to talk about the wcs-autolinking PR.</p>
    <p><strong>Problem statement</strong>: Originally the wcs-autolinking only worked for some cases, for example for the spatial axes but not for the temporal and wavelength axes in the scenario where the dimensions of the two wcs objects of the data cubes being matched up do not match. This is highly undesirable and needs generalizing while conforming to <a href="https://github.com/astropy/astropy-APEs/blob/master/APE14.rst">APE 14</a>, where the issue of a shared Python interface for World Coordinate Systems is discussed.</p>
    <p><strong>The solution</strong>: So we rewrote the code. Most of the celestial code has been retained, with some new additions to add linking for the other dimensions. The code rewritten is as follows:</p>
    <!-- TEASER_END -->
    <pre># Case for when the axes don&#39;t exactly match up<br>
    if not forwards or not backwards:</pre><pre>    # A generalized APE 14-compatible way<br>
    # Handle also the extra-spatial axes such as those of the time and wavelength dimensions</pre><pre>    if not wcs1.has_celestial or not wcs2.has_celestial:<br>
    raise IncompatibleWCS(&quot;Can&#39;t create WCS link between {0} and {1}&quot;.format(data1.label, data2.label))</pre><pre>    try:<br>
    wcs1_celestial = wcs1.celestial<br>
    wcs2_celestial = wcs2.celestial<br>
    wcs1_celestial_axis_physical_types = wcs1.celestial.world_axis_physical_types<br>
    wcs2_celestial_axis_physical_types = wcs2.celestial.world_axis_physical_types<br>
    print(&#39;wcs1.celestial.world_axis_physical_types&#39;, wcs1_celestial_axis_physical_types)<br>
    print(&#39;wcs2.celestial.world_axis_physical_types&#39;, wcs2_celestial_axis_physical_types)<br>
    except Exception:<br>
    raise IncompatibleWCS(&quot;Can&#39;t create WCS link between {0} and {1}&quot;.format(data1.label, data2.label))</pre><pre>    cids1 = data1.pixel_component_ids<br>
    cids1_celestial = [cids1[wcs1.wcs.naxis - wcs1.wcs.lng - 1],<br>
    cids1[wcs1.wcs.naxis - wcs1.wcs.lat - 1]]<br>
    slicing_axes_celestial1 = [cids1_celestial[0].axis, cids1_celestial[1].axis]<br>
    slicing_axes_celestial1 = sorted(slicing_axes_celestial1, key=str, reverse=False)<br>
    print(&#39;slicing_axes_celestial1&#39;, slicing_axes_celestial1)</pre><pre>    if wcs1_celestial.wcs.lng &gt; wcs1_celestial.wcs.lat:<br>
    cids1_celestial = cids1_celestial[::-1]</pre><pre>    cids2 = data2.pixel_component_ids<br>
    cids2_celestial = [cids2[wcs2.wcs.naxis - wcs2.wcs.lng - 1],<br>
    cids2[wcs2.wcs.naxis - wcs2.wcs.lat - 1]]<br>
    slicing_axes_celestial2 = [cids2_celestial[0].axis, cids2_celestial[1].axis]<br>
    slicing_axes_celestial2 = sorted(slicing_axes_celestial2, key=str, reverse=False)<br>
    print(&#39;slicing_axes_celestial2&#39;, slicing_axes_celestial2)</pre><pre>    if wcs2_celestial.wcs.lng &gt; wcs2_celestial.wcs.lat:<br>
    cids2_celestial = cids2_celestial[::-1]</pre><pre>    # Collect all apparently matching axes in two lists for the two wcs objects being linked up<br>
    wcs1_sliced_physical_types = wcs1_celestial_axis_physical_types<br>
    slicing_axes1 = slicing_axes_celestial1<br>
    wcs2_sliced_physical_types = wcs2_celestial_axis_physical_types<br>
    slicing_axes2 = slicing_axes_celestial2<br>
    for i, physical_type1 in enumerate(wcs1.world_axis_physical_types):<br>
    for j, physical_type2 in enumerate(wcs2.world_axis_physical_types):<br>
    if physical_type1 == physical_type2:<br>
    if physical_type1 not in wcs1_sliced_physical_types:<br>
    slicing_axes1.append(wcs1.world_n_dim - i - 1)<br>
    wcs1_sliced_physical_types.append(physical_type1)<br>
    if physical_type2 not in wcs2_sliced_physical_types:<br>
    slicing_axes2.append(wcs2.world_n_dim - j - 1)<br>
    wcs2_sliced_physical_types.append(physical_type2)</pre><pre>    slicing_axes1 = sorted(slicing_axes1, key=str, reverse=True)<br>
    slicing_axes2 = sorted(slicing_axes2, key=str, reverse=True)</pre><pre>    print(&#39;slicing_axes1&#39;, slicing_axes1)<br>
    print(&#39;slicing_axes2&#39;, slicing_axes2)</pre><pre>    print(&#39;wcs1_sliced_physical_types&#39;, wcs1_sliced_physical_types)<br>
    print(&#39;wcs2_sliced_physical_types&#39;, wcs2_sliced_physical_types)</pre><pre>    # Generate slices for the wcs slicing<br>
    slices1 = (slice(None),) * wcs1.world_n_dim<br>
    slices2 = (slice(None),) * wcs2.world_n_dim</pre><pre>    slices1 = sorted(list(slices1))<br>
    slices2 = sorted(list(slices2))</pre><pre>    for i in range(wcs1.world_n_dim):<br>
    if i in slicing_axes1:<br>
    pass<br>
    else:<br>
    slices1[i] = 0</pre><pre>    for i in range(wcs2.world_n_dim):<br>
    if i in slicing_axes2:<br>
    pass<br>
    else:<br>
    slices2[i] = 0</pre><pre>    wcs1_sliced = wcs1[tuple(slices1)]<br>
    wcs2_sliced = wcs2[tuple(slices2)]</pre><pre>    cids1 = data1.pixel_component_ids<br>
    cids1_sliced = [cids1[x] for x in slicing_axes1]<br>
    cids1_sliced = sorted(cids1_sliced, key=str, reverse=True)</pre><pre>    cids2 = data2.pixel_component_ids<br>
    cids2_sliced = [cids2[x] for x in slicing_axes2]<br>
    cids2_sliced = sorted(cids2_sliced, key=str, reverse=True)</pre><pre>    pixel_cids1, pixel_cids2, forwards, backwards = get_cids_and_functions(<br>
    wcs1_sliced, wcs2_sliced, cids1_sliced, cids2_sliced)</pre><pre>    self._physical_types_1 = wcs1_sliced_physical_types<br>
    self._physical_types_2 = wcs2_sliced_physical_types</pre><pre>    if pixel_cids1 is None:<br>
    raise IncompatibleWCS(&quot;Can&#39;t create WCS link between {0} and {1}&quot;.format(data1.label, data2.label))</pre><p>After checking with the tests written previously the code was modified before it is confirmed with pytest that all CI tests are now passing.</p>
    <p>Now we can link up wcs axes of the same physical types of two data cubes having different dimensions with no problems, illustrated as follows:</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*Ffgo6t1M0ah9UcCyeLVdfg.png" /></figure><img src="https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=620347ad3f8d" width="1" height="1">

