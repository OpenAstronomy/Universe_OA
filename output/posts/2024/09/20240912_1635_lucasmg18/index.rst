.. title: Concluding GSoC24
.. slug:
.. date: 2024-09-12 16:35:00 
.. tags: irsa-fornax
.. author: Lucas Martin Garcia
.. link: https://lucasmartingarciagsoc24openastronomy.blogspot.com/2024/09/concluding-gsoc24.html
.. description:
.. category: gsoc2024


.. raw:: html

    <p>As the sun sets on the Google Summer of Code 2024, it's time to reflect on our exploration of Active Galactic Nuclei (AGN) light curve interpolation using advanced neural networks. Over the course of this project, we ventured into the complexities of AGN data, developing and refining models to better predict and understand the erratic behaviors of these celestial objects.</p>
    <p><strong>Overview of the Project</strong><br />Our journey began with the goal of enhancing the accuracy of AGN light curve predictions. We employed custom Bidirectional Recurrent Neural Networks (BRNNs), coupled with an interpretative neural network layer, aiming to leverage both past and future context in our predictions.</p>
    <p><strong>Final Results</strong><br />In our last phase, we meticulously tested our BRNN model against traditional linear interpolation and K-Nearest Neighbors (KNN) methods:</p>
    <!-- TEASER_END -->
    <ul><li><strong>Linear Interpolation:</strong> Test Loss = 1.2790908372984307e-07</li><li><strong>KNN Interpolation:</strong> Test Loss = 1.211259949511657e-07</li><li><strong>BRNN Model:</strong> Test Loss = 7.520762018434385e-08</li></ul><p>While the BRNN model showcased a promising improvement in test loss compared to the other methods, the enhancements, although significant, did not fully justify the computational expense and complexity involved in deploying and refining such advanced models.</p>
    <p>Here we can see the test results of the BRNN Model for an specific AGN:</p>
    <p><br /></p>
    <div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgiqHhDIC4IDZ5XzGQN5j5gRJ_21w6dRoYyUAhGpIr5FdB3HzX10jsQUwz3gC_IurXeAEkyKobScGJH4dxhXJTjtXw23KcMSnwFugKya29S9oOacig6UfBBJlDdt4lkNRgTWxL5xlUHpE2aIF656HTpzWWG6YvR4_2pC7vjNPE8h3Plrry1MpAyw5Sz-95g/s1400/Results.png" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="643" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgiqHhDIC4IDZ5XzGQN5j5gRJ_21w6dRoYyUAhGpIr5FdB3HzX10jsQUwz3gC_IurXeAEkyKobScGJH4dxhXJTjtXw23KcMSnwFugKya29S9oOacig6UfBBJlDdt4lkNRgTWxL5xlUHpE2aIF656HTpzWWG6YvR4_2pC7vjNPE8h3Plrry1MpAyw5Sz-95g/w900-h643/Results.png" width="900" /></a></div><br /><p><br /></p>
    <p><strong>Reflections and Future Directions</strong><br />The findings suggest that while the advanced BRNN model holds potential, further refinement and optimization are necessary to fully harness its capabilities in a cost-effective manner. Future explorations could focus on integrating additional data types and exploring even more complex neural network architectures.<br /></p>
    <p><strong>Conclusion</strong><br />This project has been a profound learning experience, not only in terms of technical development but also in understanding the intricate complexity of celestial phenomena. As GSoC24 concludes, we hope the insights gained will fuel further research and innovation in the field of astrophysics.</p>
    <p><strong>Acknowledgments</strong><br />A heartfelt thank you to my mentors, Jessica Krick and Shoubaneh Hemmati, peers, and the vibrant GSoC community for their support, guidance, and invaluable insights throughout this amazing journey.</p>
    <p><b>Google Summer of Code 2024</b></p>
    <p>This project was developed during Google Summer of Code 2024 by contributor Lucas Martin Garcia and mentors Jessica Krick and Shoubaneh Hemmati.</p>
    <p><a href="https://summerofcode.withgoogle.com/programs/2024/projects/CR12H6Wf">Official GSOC 2024 Project</a></p>
    <div><p><b>GitHub Official Repository</b></p>
    <p>This project is published in the following GitHub repository.</p>
    </div><div><a href="https://github.com/OpenAstronomy/rnn-lightcurve-gapfill">Official GitHub Repository</a><br /></div><div><span style="color: #0000ee;"><br /></span></div><div><span style="color: #0000ee;"><br /></span></div><div><span style="color: #0000ee;"><br /></span></div><div><span style="color: #0000ee;"><br /></span></div><div><span style="color: #0000ee;"><br /></span></div><div><span style="color: #0000ee;"><br /></span></div>

