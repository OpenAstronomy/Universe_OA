.. title: GSoC Post 2
.. slug:
.. date: 2021-07-05 14:17:22 
.. tags: gnuastro
.. author: ndanzanello
.. link: https://ndanzanello.wordpress.com/2021/07/05/gsoc-post-2/
.. description:
.. category: gsoc2021


.. raw:: html

    <p>Hi! In the previous post I mentioned that the matching part between the quads was done. Following that, the past 2 weeks were devoted to:</p>
    
    
    <!-- TEASER_END -->
    
    <ul><li>first get the theta (rotation) and scale values related to each quad. To do this, we use a linear transformation between the pixel coordinates and the projection plane coordinates (that come from the celestial ones);</li><li>use some statistics in the thetas and scales above to get the parameters of the wcs (world coordinate system). Also, we have to decide where the reference point is. To do this, we use the A vertex that is closer to the median of all A vertices from the matched quads;</li><li>after the parameters of the wcs are ready, we write them into a fits file.</li></ul>
    
    
    
    <p>Basically, this would make this part over. But we noticed a problem that needed a debug: we were finding few matches. In examples with fainter stars, we wouldn&#8217;t even get one match. So, to solve this, we had to change the way we were making the quads, because we were not considering all the possible quads combinations of the stars we selected. After that, we could go, for example, from ten of thousands of quads to millions of quads! This also improves a lot the statistics that we need to do.</p>
    
    
    
    <p>So now we have to start dealing with some distortions too! <img alt="🙂" class="wp-smiley" src="https://s0.wp.com/wp-content/mu-plugins/wpcom-smileys/twemoji/2/72x72/1f642.png" style="height: 1em;" /></p>
    
    
    
    <p></p>

