.. title: GSoC 2024 @OpenAstronomy: Overview of Merged and Pending PRs
.. slug:
.. date: 2024-08-24 11:17:02 
.. tags: SunPy
.. author: ViciousEagle03
.. link: https://viciouseagle03.github.io/post/gsoc-pr_merged/
.. description:
.. category: gsoc2024


.. raw:: html

    <p><img alt="img" src="https://viciouseagle03.github.io/images/PR-Merged.png" /></p>
    <blockquote>
    <p>This blogpost deals with all the PRs that were merged/opened in NDCube/ SunPy / Astropy for completing the project.</p>
    <!-- TEASER_END -->
    </blockquote>
    <hr />
    <blockquote>
    <p>The PRs were filed in accordance with the tasks recorded in the GitHub <a href="https://github.com/orgs/sunpy/projects/12">task-tab</a>.</p>
    </blockquote>
    <h2 id="ndcube">NDCube</h2>
    <h4 id="pr-708-asdf-supporthttpsgithubcomsunpyndcubepull708">PR #708: <a href="https://github.com/sunpy/ndcube/pull/708">Asdf-Support</a></h4>
    <h4 id="merged">(Merged)</h4>
    <ul>
    <li>PR for supporting the serialization of basic <code>ndcube.NDCube</code> objects with the serialization logic written for the below classes
    NDCube, GlobalCoords, ExtraCoords.</li>
    </ul>
    <h4 id="pr-751-add-support-for-the-serialization-of-the-ndcube-wcs-wrappershttpsgithubcomsunpyndcubepull751">PR #751: <a href="https://github.com/sunpy/ndcube/pull/751">Add support for the serialization of the ndcube WCS wrappers</a></h4>
    <h4 id="yet-to-be-merged">(Yet to be Merged)</h4>
    <ul>
    <li>This PR introduces serialization support for <code>ndcube</code> WCS wrappers, including <code>CompoundLowLevelWCS</code>, <code>ResampledLowLevelWCS</code> and <code>ReorderedLowLevelWCS</code>, allowing them to be saved in ASDF format.</li>
    </ul>
    <h4 id="pr-756-add-serialization-logic-for-the-ndcubesequence-and-ndcollectionhttpsgithubcomsunpyndcubepull756">PR #756: <a href="https://github.com/sunpy/ndcube/pull/756">Add serialization logic for the NDCubeSequence and NDCollection</a></h4>
    <h4 id="yet-to-be-merged-1">(Yet to be Merged)</h4>
    <ul>
    <li>This PR introduces serialization support for <code>NDCubeSequence</code> and <code>NDCollection</code> objects, enabling their conversion to and from ASDF format.</li>
    </ul>
    <h2 id="astropy">Astropy</h2>
    <h4 id="pr-237-remove-astropy-version-checkhttpsgithubcomastropyasdf-astropypull237">PR #237: <a href="https://github.com/astropy/asdf-astropy/pull/237">Remove astropy version check</a></h4>
    <h4 id="merged-1">(Merged)</h4>
    <ul>
    <li>This PR removes the <code>astropy</code> version check, which was previously set to version 5.1, from the codebase. The minimum required version is updated to 5.2, and associated conditional logic in <code>test_transform.py</code> is removed.</li>
    </ul>
    <h4 id="pr-235-support-serialization-of-astropywcswcs-objects-to-asdfhttpsgithubcomastropyasdf-astropypull235">PR #235: <a href="https://github.com/astropy/asdf-astropy/pull/235">Support serialization of astropy.wcs.WCS objects to ASDF</a></h4>
    <h4 id="yet-to-be-merged-2">(Yet to be Merged)</h4>
    <ul>
    <li>This PR introduces support for serializing <code>astropy.wcs.WCS</code> and <code>astropy.wcs.wcsapi.SlicedLowLevelWCS</code> objects to ASDF format. With this enhancement, any <code>ndcube.NDCube</code> objects can be serialized to ASDF while preserving the underlying WCS as <code>astropy.wcs.WCS</code>. Additionally, it ensures that sliced <code>ndcube.NDCube</code> objects maintain proper WCS preservation when serialized and are restored correctly upon deserialization.</li>
    </ul>
    <h4 id="pr-239-add-serialization-logic-for-uncertainty-objectshttpsgithubcomastropyasdf-astropypull239">PR #239: <a href="https://github.com/astropy/asdf-astropy/pull/239">Add serialization logic for uncertainty objects</a></h4>
    <h4 id="yet-to-be-merged-3">(Yet to be Merged)</h4>
    <ul>
    <li>This PR adds serialization logic for <code>astropy.nddata.StdDevUncertainty</code> and <code>astropy.nddata.UnknownUncertainty</code> objects. This update enables the serialization of these uncertainty types, ensuring that the uncertainty attribute of the <code>ndcube.NDCube</code> object is properly preserved and restored.</li>
    </ul>
    <h2 id="sunpy">SunPy</h2>
    <h4 id="pr-7686-asdf-schema-update-minor-changehttpsgithubcomsunpysunpypull7686">PR #7686: <a href="https://github.com/sunpy/sunpy/pull/7686">ASDF schema update: minor change</a></h4>
    <h4 id="merged-2">(Merged)</h4>
    <ul>
    <li>This PR updates the ASDF schema by removing incorrect usage of the unsupported <code>allowAdditionalProperties</code> validator. This minor change ensures that the schema files for generic_map (versions <code>1.0.0</code>, <code>1.1.0</code>, and <code>1.2.0</code>) are correctly formatted.</li>
    </ul>

