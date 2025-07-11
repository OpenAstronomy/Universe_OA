.. title: Fitting Feature Now Available in the RADIS App
.. slug:
.. date: 2025-07-10 15:48:47 
.. tags: radis
.. author: mohyware
.. link: https://medium.com/@mohyware/fitting-feature-now-available-in-the-radis-app-a5ff4a0b0a7a?source=rss-9dc0b0efcdaa------2
.. description:
.. category: gsoc2025


.. raw:: html

    <p>The main goal of fitting is to find the <strong>best values</strong> for unknown parameters (like temperature Tgas, mole fraction, etc.) that make your theoretical (simulated) spectrum <strong>match</strong> the experimental data as closely as possible.</p>
    <p>This feature was not previously available in the app, but it is now (once the PR gets merged).</p>
    <p>To use it: <strong>Activate Fit Spectrum Mode</strong> from the header to open the fitting form.</p>
    <!-- TEASER_END -->
    <p><a href="https://radis.readthedocs.io/en/latest/auto_examples/3_Fitting/plot1_fit_Tgas.html#sphx-glr-auto-examples-3-fitting-plot1-fit-tgas-py">You can try this example from the RADIS docs</a></p>
    <h3>Step 1: Prepare a .spec file and upload it to the app</h3><p>Create a file containing your experimental spectrum in one of the supported formats: .spec, .txt, or .csv. You can do this using RADIS by saving a Spectrum object.</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/712/1*GGJlLCU_vVOfIeY03xiVOw.png" /></figure><h3>Step 2: Fill out the form</h3><p>Fitting requires filling in four form sections:</p>
    <ul><li>experimental_conditionsGround-truth data about your experimental environment.</li><li>fit_parametersParameters you want to fit (e.g. Tgas, mole fraction).</li><li>bounding_rangesAllowed ranges for the parameters listed in fit_parameters.</li><li>fit_propertiesAdditional settings for the fitting pipeline.</li></ul><p>In the app, all the main input fields fall under experimental_conditions. Some fields have checkboxes next to them, activating these checkboxes marks the field as a <strong>fit parameter</strong>, and an bounding_range input will appear for it (like Tgas in the image below).</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/740/1*EpB7grvfBH9duAReynU6Gg.png" /></figure><p>You can also adjust some fit_properties, like max loops and normalization. However, the fitting method and its parameters (e.g., tol) are currently hardcoded. The method used is least_squares.</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/697/1*wiLIZeOXPiNzCKQDZfvicg.png" /></figure><h3>Step 3: Click and see the results!</h3><p>The app will compute the best fit, load the experimental spectrum, and show the fitting history and results through logs, as shown below.</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/755/1*jGlF03yxKqOZBh13Hnz_QQ.png" /></figure><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*f1XvZP8EAB_vkdIvWHPtnQ.png" /><figcaption>the fitting history for tgas</figcaption></figure><img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=a5ff4a0b0a7a" width="1" />

