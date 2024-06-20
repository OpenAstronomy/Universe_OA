.. title: Finally ported from functional approach to class based approach
.. slug:
.. date: 2024-06-19 13:11:00 
.. tags: stingray
.. author: Kartik Mandar
.. link: https://gsoc2024.kartikmandar.com/2024/06/finally-ported-from-functional-approach.html
.. description:
.. category: gsoc2024


.. raw:: html

    <p>&nbsp;I earlier had developed the basic structure of app in terms of functions in separate files and somehow had managed to serve the dashboard through only one panel serve ( panel serve app.py --autoreload). It was a clever use of view to turn on and off when use clicks the button and importing the UI from different functions(that is different .py files). But this was an unmaintainable and unscalable approach. So now I have shifted to a class based approach and have made important classes to do the stuff.&nbsp;</p>
    <!-- TEASER_END -->

