.. title: GSoC Post 4
.. slug:
.. date: 2021-08-15 14:02:15 
.. tags: gnuastro
.. author: ndanzanello
.. link: https://ndanzanello.wordpress.com/2021/08/15/gsoc-post-4/
.. description:
.. category: gsoc2021


.. raw:: html

    <p>Hi! In the last weeks we have finished the Astrometry linear part programming. <img alt="🙂" class="wp-smiley" src="https://s0.wp.com/wp-content/mu-plugins/wpcom-smileys/twemoji/2/72x72/1f642.png" style="height: 1em;" /></p>
    
    
    <!-- TEASER_END -->
    
    <p>We added an option to solve for more pixel catalogs, which are a part of a field image. This is an important case in real world scenarios. The image below is a good illustration of this: we have a field and a lot of exposures that are used to build the final image.</p>
    
    
    
    <figure class="wp-block-image"><img alt="https://archive.stsci.edu/prepds/xdf/images/xdf_buildup.png" src="https://archive.stsci.edu/prepds/xdf/images/xdf_buildup.png" /><figcaption>Source: <a href="https://archive.stsci.edu/prepds/xdf/" rel="noreferrer noopener" target="_blank">https://archive.stsci.edu/prepds/xdf/</a></figcaption></figure>
    
    
    
    <p>Also, we are moving our code to Gnuastro, so it can be a Gnuastro program. To do this, we have to follow Gnuastro conventions, so everything can be organized. Luckily, it&#8217;s very well documented how to do it, as you can see <a href="https://www.gnu.org/software/gnuastro/manual/html_node/The-TEMPLATE-program.html#The-TEMPLATE-program" rel="noreferrer noopener" target="_blank">here</a> and <a href="https://www.gnu.org/software/gnuastro/manual/html_node/Mandatory-source-code-files.html" rel="noreferrer noopener" target="_blank">also here</a>.</p>

