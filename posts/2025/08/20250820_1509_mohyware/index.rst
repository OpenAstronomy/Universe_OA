.. title: RADIS Web App Final GSoC Blog
.. slug:
.. date: 2025-08-20 15:09:45 
.. tags: radis
.. author: mohyware
.. link: https://medium.com/@mohyware/radis-web-app-final-gsoc-blog-f1f5580da556?source=rss-9dc0b0efcdaa------2
.. description:
.. category: gsoc2025


.. raw:: html

    <p>In this final update, I’ll be covering the latest improvements.</p>
    <h3><strong>Option to run the backend locally with Docker:</strong></h3><ul><li>Simply follow the steps in the app to get started:</li></ul><figure><img alt="" src="https://cdn-images-1.medium.com/max/634/1*Qmn_cqV9vRFldFA_0ydUAQ.png" /></figure><ul><li>Improve performance if local machine is powerful.</li><li>You can even mount your existing databases (if you’ve used the RADIS package) by running the container with the following command:</li></ul><pre>docker run -d -p 8080:8080 \<br />-v /home/mohy/.radisdb:/root/.radisdb \ <br />-v /home/mohy/radis.json:/root/radis.json \<br />radis-app-backend</pre><h3><strong>Moved to </strong><strong>SpectrumFactory instead of the simpler </strong><strong>calc_spectrum:</strong></h3><ul><li>This enables GPU-based calculations if implemented in the future.</li><li>Also improves ExoMol database performance by avoiding unnecessary broad file downloads.</li></ul><h3><strong>UI improvements:</strong></h3><ul><li>Better layout and space utilization to make the graph display larger and clearer.</li></ul><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*nIhU6Hej2xRGMecUAN7m2A.png" /></figure><h3><strong>There is a new option to c</strong>hoose between using <strong>all isotopes</strong> or <strong>only the first one</strong>.</h3><figure><img alt="" src="https://cdn-images-1.medium.com/max/714/1*TD8Ks6cnUBMSIE1yQKzLqQ.png" /></figure><h3>Testing</h3><p>I’ve added tests for all the new features on both the frontend and backend, and ensured coverage of the core existing functionalities.</p>
    <p>Overall, it has been a fantastic journey working on this project with such a supportive community and mentors.</p>
    <!-- TEASER_END -->
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=f1f5580da556" width="1" />

