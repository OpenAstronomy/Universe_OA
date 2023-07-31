.. title: GSoC Week 5-8
.. slug:
.. date: 2023-07-30 07:35:19 
.. tags: stingray
.. author: pupper emeritus
.. link: https://dev.to/pupperemeritus/gsoc-week-5-8-5198
.. description:
.. category: gsoc2023


.. raw:: html

    <h2>
    
    
    <!-- TEASER_END -->
    Brief
    </h2>
    
    <p>I have worked on creating unit tests for the Lomb Scargle Cross Spectrum class, cross verifying the algorithm by comparing with the papers and fixed typos in docstrings. Apologies for the delay. Had my exams.</p>
    
    <h2>
    
    
    Details
    </h2>
    
    <p>I have noticed a few faults in both the fast and the slow algorithms. I have gone back to the drawing board and tried to address those issues by following the papers as closely as possible. All the changes are visible in the following draft pull request.<br />
    <a href="https://github.com/StingraySoftware/stingray/pull/737">https://github.com/StingraySoftware/stingray/pull/737</a></p>
    
    <p>After the fixing, the fast and the slow algorithm have started giving very similar outputs. I am starting to suspect that the time lags might be broken in the algorithms themselves. It is starting to get a little suspicious when different methods are giving very similar results and they are still not what that is expected. Last time around the fast and slow algorithms have given different results. After cross verifying with the papers, The results from both have fast and slow algorithms converged.</p>
    
    <p>To keep the project sailing along while I wait for confirmation that this is an issue with the implementation or the algorithm , I have decided to work on writing unit tests for the various classes and methods. Furthermore I also worked on fixing the docstrings.</p>
    
    
    <div class="ltag_gist-liquid-tag">
    
    </div>

