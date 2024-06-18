.. title: Blog 1: Rethinking Coalignment from Ground-up
.. slug:
.. date: 2024-06-15 14:59:31 
.. tags: SunPy
.. author: Deus1704
.. link: https://deus1704.vercel.app/posts/blog_1/
.. description:
.. category: gsoc2024


.. raw:: html

    <h2 id="the-very-essence-of-coalignment">The Very Essence of Coalignment</h2>
    <p>At its core, coalignment is all about making sure our solar images match up as best they can. It uses a few different techniques, like template matching and solar rotation correction, to get this done. This is really important when we&rsquo;re trying to accurately track and study what&rsquo;s happening on a part of sun over time.
    We re-thought the entire process of what our new API be providing to the users as well as its structure.</p>
    <!-- TEASER_END -->
    <p><img alt="Naive Refactor" src="https://deus1704.vercel.app/images/proposed_struct.png" /></p>
    <p>This was one of the idea that was very naive version, but focused entierly for the user&rsquo;s comfort in applying the coalignment methods.</p>
    <h2 id="the-basic-structure-we-finally-agreed-upon">The Basic Structure we finally agreed Upon</h2>
    <p><img alt="Internal Sturcture" src="https://deus1704.vercel.app/images/internal.png" /></p>
    <p>We agreed to have this as the very basic structure which we would be working/developing upwards. The following example demonstrates the way it would work.</p>
    <div class="highlight"><pre tabindex="0"><code class="language-python"><span style="display: flex;"><span>aia_map1 <span style="color: #f92672;">=</span> sunpy<span style="color: #f92672;">.</span>map<span style="color: #f92672;">.</span>Map(sunpy<span style="color: #f92672;">.</span>data<span style="color: #f92672;">.</span>sample<span style="color: #f92672;">.</span>AIA_193_CUTOUT01_IMAGE)
    </span></span><span style="display: flex;"><span>aia_map2 <span style="color: #f92672;">=</span> sunpy<span style="color: #f92672;">.</span>map<span style="color: #f92672;">.</span>Map(sunpy<span style="color: #f92672;">.</span>data<span style="color: #f92672;">.</span>sample<span style="color: #f92672;">.</span>AIA_193_CUTOUT03_IMAGE)
    </span></span><span style="display: flex;"><span><span style="color: #75715e;">### Creating a template from aia_map1</span>
    </span></span><span style="display: flex;"><span>bottom_left <span style="color: #f92672;">=</span> SkyCoord(<span style="color: #ae81ff;">600</span> <span style="color: #f92672;">*</span> u<span style="color: #f92672;">.</span>arcsec, <span style="color: #f92672;">-</span><span style="color: #ae81ff;">500</span> <span style="color: #f92672;">*</span> u<span style="color: #f92672;">.</span>arcsec, frame<span style="color: #f92672;">=</span>aia_map1<span style="color: #f92672;">.</span>coordinate_frame)
    </span></span><span style="display: flex;"><span>top_right <span style="color: #f92672;">=</span> SkyCoord(<span style="color: #ae81ff;">800</span> <span style="color: #f92672;">*</span> u<span style="color: #f92672;">.</span>arcsec, <span style="color: #f92672;">-</span><span style="color: #ae81ff;">200</span> <span style="color: #f92672;">*</span> u<span style="color: #f92672;">.</span>arcsec, frame<span style="color: #f92672;">=</span>aia_map1<span style="color: #f92672;">.</span>coordinate_frame)
    </span></span><span style="display: flex;"><span>submap <span style="color: #f92672;">=</span> aia_map1<span style="color: #f92672;">.</span>submap(bottom_left, top_right<span style="color: #f92672;">=</span>top_right)
    </span></span><span style="display: flex;"><span>
    </span></span><span style="display: flex;"><span>coaligned_map <span style="color: #f92672;">=</span> coalignment_interface(<span style="color: #e6db74;">"match_template"</span>,aia_map2, submap)
    </span></span></code></pre></div><p><img alt="combined image" src="https://deus1704.vercel.app/images/combined.png" /></p>
    <p>I am currently implementing the decorator structure for the sunkit-image, but that would be covered in another blog.</p>

