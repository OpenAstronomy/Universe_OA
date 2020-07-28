.. title: Connecting Spark Logs with Jupyter UI
.. slug:
.. date: 2020-07-27 13:41:49 
.. tags: astronomy-commons
.. author: Biswarup Banerjee
.. link: https://medium.com/@biswarupbanerjee/connecting-spark-logs-with-jupyter-ui-3a522a2b89e4?source=rss-24ea8c0c5f0d------2
.. description:
.. category: gsoc2020


.. raw:: html

    <p>I have successfully been able to show the kernel logs in realtime into the Jupyter front end.<br>
    So basically I configured the Jupyter kernel to dump the logs in real-time in a log file.<br>
    Then I created a new function that runs in a separate thread and pulls the content of the log file every 2 seconds.<br>
    <!-- TEASER_END -->
    Then the fetched data is sent to the front end via sockets every two seconds ONLY when the user opens the log.<br>
    So when the user is not in the logs page the socket communication and the reading of the log file do not happen.</p>
    <blockquote>def fetch_logs(comm):</blockquote><blockquote>f = open(“log.file”, “r”)</blockquote><blockquote>logs = f.read()</blockquote><blockquote>comm.send({‘status’ : ‘log_fetched_success’ , ‘log’ : logs})</blockquote><blockquote>if (ipython.ev(‘shouldFetchLog’)):</blockquote><blockquote>threading.Timer(2.0,fetch_logs, [comm]).start()</blockquote><img src="https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=3a522a2b89e4" width="1" height="1">

