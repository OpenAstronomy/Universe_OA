.. title: Blog 0: The First Two Weeks
.. slug:
.. date: 2024-05-25 14:59:31 
.. tags: SunPy
.. author: Deus1704
.. link: https://deus1704.vercel.app/posts/blog_0/
.. description:
.. category: gsoc2024


.. raw:: html

    <h4 id="a-summary-of-activities-completed-in-the-two-weeks-leading-up-to-the-start-of-the-coding-period">A summary of activities completed in the two weeks leading up to the start of the coding period.</h4>
    <h2 id="table-of-contents">Table of Contents</h2>
    <ul>
    <!-- TEASER_END -->
    <li><a href="https://deus1704.vercel.app/posts/blog_0/#draft_pr">Wrapping up the draft pull request</a></li>
    <li><a href="https://deus1704.vercel.app/posts/blog_0/#issue1">Incorporating suggestions for STARA &amp; its examples</a></li>
    <li><a href="https://deus1704.vercel.app/posts/blog_0/#fix_doc_fails">Fixing the doc failures</a></li>
    <li><a href="https://deus1704.vercel.app/posts/blog_0/#first_meet">First Meet with Mentors</a></li>
    </ul>
    <p>After completing my end-semester exams, I was overwhelmed by the outstanding tasks that I had let accumulate over time.
    In order to address those, I tried resolving dependencies and package issues of the previous environments of
    sunpy &amp; sunkit-image but, ultimately gave up and initialised a new environment. After discussions with mentors, the project priorities were clarified, allowing me to efficiently plan &amp; complete my tasks during the community bonding period. What follows is the detailed account of all the tasks completed during these two weeks.</p>
    <h2 id="incorporating-suggestions-for-sunspot-tracking-and-recognition-algorithm-stara">Incorporating suggestions for Sunspot Tracking and Recognition Algorithm (STARA)</h2>
    <p>Incorporated suggestions and made several changes to the STARA example. Attempted to create a mock HMI continuum data with an artificial &ldquo;sunspot&rdquo; at a chosen location with a certain radius. But it did not meet the exact requirements of the STARA, hence no regions could be identified. The written mock hmi map are demonstrated below,</p>
    <table>
    <thead>
    <tr>
    <th style="text-align: center;"><img alt="Mock HMI Map without Sunspot" src="https://deus1704.vercel.app/images/mock_wo.png" /></th>
    <th style="text-align: center;"><img alt="Mock HMI Map with Sunspot" src="https://deus1704.vercel.app/images/mock_withspot.png" /></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: center;">Mock HMI Map without Sunspot</td>
    <td style="text-align: center;">Mock HMI Map with Sunspot</td>
    </tr>
    </tbody>
    </table>
    <p>Discussed alternative approaches with mentor Nabil regarding the mock HMI map. According to his suggestion I tried the HMI continuum test data present in <code>sunpy/data/test</code> directory, but it had some issues with the WCS hence STARA couldn&rsquo;t properly find the sunspot regions.</p>
    <h2 id="wrapping-up-the-draft-pull-request">Wrapping up the draft pull request</h2>
    <p>I began working on the transformation of a vector field some time ago but encountered challenges in validating the approach. Using Astropy for the transformation confirmed the accuracy of the function I wrote. The next step is to seek feedback from mentors and the SunPy community. But I still feel a need to test this more rigorously which can validate that this would work with different frames too. I studied about different frames provided by the SPICE toolkit and tried to match the sunpy frames and the SPICE frames and have confirmed that the function works with the static frames.</p>
    <h2 id="fixing-the-doc-failures">Fixing the doc failures</h2>
    <p>Two out of my three open pull requests encountered documentation failures due to incorrect referencing of functions or modules, or example galleries. After studying the conventions of Sphinx and SunPy, I resolved these issues. Additionally, I discovered how to set up GitHub CI actions on my forks.</p>
    <h2 id="first-meet-with-mentors">First Meet with Mentors</h2>
    <p>In our initial meeting, my mentor Will provided a brief overview of the purpose of sunkit-image, emphasizing its primary function: coalignment. He explained the fundamental concepts of coalignment, user expectations, and desired functionalities of the new API. We also reviewed the current coalignment API&rsquo;s shortcomings. We agreed that an improved API was necessary and discussed my proposed structure for this enhancement. We also drafted a plan for the entire rethinking and redesigning the new API over the span of 4 weeks.</p>

