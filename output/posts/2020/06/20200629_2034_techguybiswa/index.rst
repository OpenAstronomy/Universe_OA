.. title: Launching Version 1 of Start Spark
.. slug:
.. date: 2020-06-29 20:34:53 
.. tags: astronomy-commons
.. author: Biswarup Banerjee
.. link: https://medium.com/@biswarupbanerjee/launching-version-1-of-start-spark-b16c4e9516fb?source=rss-24ea8c0c5f0d------2
.. description:
.. category: gsoc2020


.. raw:: html

    <figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*GKZekrHbmzNBggdsyVxSSA.jpeg" /><figcaption>Even my workstation is excited for the product demo!</figcaption></figure><p>So after 4 weeks of planning and coding and debugging, the day came when I had to launch version 1.0 of the product!</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*JGcxp4eCl8d7t0omgPAFIQ.png" /><figcaption>My extension “Start Spark” deployed at the prod servers</figcaption></figure><p>The extension I built is now deployed in the DiRAC Jupyter Hub and is currently getting used by the astronomy community at DiRAC!</p>
    <p>What you can do with my extension:</p>
    <!-- TEASER_END -->
    <ol><li>Create a PySpark cluster on the click of a single button. Creating a PySpark cluster would have otherwise taken writing multiple lines of cumbersome codes.</li><li>Get the link where you can access the PySpark web UI and see all the executors, jobs, and the environment.</li><li>The “spark” variable is automatically injected into the kernel and hence users can use it as they like.</li></ol><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*qUI3KU07owQgFF6x35_V4Q.png" /><figcaption>Get access to the PySpark Web UI</figcaption></figure><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*shTWfgSYlHyTD-KkB7w2mw.png" /><figcaption>“spark” variable is injected in the kernel</figcaption></figure><h3>How does it work?</h3><figure><img alt="" src="https://cdn-images-1.medium.com/max/976/1*sV-BVWeI7hPzr1ZyYFGmKA.png" /><figcaption>Workflow</figcaption></figure><p>Step 1: The extension gets loaded.<br>
    Step 2: While it loads it automatically calls an API/serverextension handler /all-config and that API gives all the list of the available configs.<br>
    Step 3: We can see that list of all available configs in the dropdown.<br>
    Step 4: We can select any config that we want and click on “Start Spark” Button<br>
    Step 5 : When we click Start Spark Button, the front end detects which config we have selected and then tells the serverextension about the selected config via REST API.<br>
    Step 6: The serverextension fetches all the config details of the config that is selected in the frontend from the config dir located at home dir.<br>
    Step 7: Then once it has the required config fetched from the config dir it converts it into a Jinja Template and sends the jinja template to the front end via API<br>
    Step 8: Once the front end receives the Jinja template of the required config it sends the Jinja Template to the Kernel Extension via Sockets<br>
    Step 9: The kernel extension executes the jinja template to start the spark cluster that it receives from the Jupyter front end.</p>
    <blockquote>Select Config -&gt; Click the Start Spark Button -&gt; Config Data fetched in backend -&gt; Config data converted to Jinja Template in Backend -&gt; Jinja Template Sent from backend to front end -&gt; Jinja sent from front end to Kernel → Jinja template gets executed in Kernel to start the cluster!</blockquote><p><strong>Video Reference Link</strong>: <a href="https://slack-redir.net/link?url=https%3A%2F%2Fwww.loom.com%2Fshare%2Fdc18b670e08a47c6a96db3176f3be9ef">https://www.loom.com/share/dc18b670e08a47c6a96db3176f3be9ef</a> (PS: Watch it in 1.5x speed)</p>
    <p>I am super excited to see how the astronomy community feels about it and gives their feedback.</p>
    <img src="https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=b16c4e9516fb" width="1" height="1">

