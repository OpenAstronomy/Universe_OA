.. title: Moving to the Frontend
.. slug:
.. date: 2025-06-20 05:05:37 
.. tags: radis
.. author: mohyware
.. link: https://medium.com/@mohyware/moving-to-the-frontend-5ae8056490f5?source=rss-9dc0b0efcdaa------2
.. description:
.. category: gsoc2025


.. raw:: html

    <p>As part of the ongoing development, we’ve now begun focusing on the frontend side of the project, improving the user experience and preparing for more database integrations.</p>
    <h3>Initial Cleanup</h3><p>To ensure a clean development workflow, I started by:</p>
    <ul><li>Fixing linting and type-checking issues to maintain code quality.</li><li>Repairing frontend tests to make sure new changes are verifiable.</li><li>This was important to establish a solid pipeline, so any new code added to the frontend can be tested and reviewed confidently.</li></ul><h3>Full Dark Mode Support</h3><p>A major enhancement was implementing <strong>dark mode</strong> across the entire frontend, not just the MUI (Material UI) components, but also the <strong>plotting graph area</strong>.</p>
    <!-- TEASER_END -->
    <p>This took some effort as it required:</p>
    <ul><li>Migrating from <strong>Joy UI components</strong> (buttons, inputs, etc.) to <strong>Material UI components</strong> to ensure compatibility with CssVarsProvider.</li><li><strong>Refactoring existing styles</strong> to align with the new Material UI design system.</li></ul><p>The result is a visually cohesive and fully functional dark mode experience!</p>
    <h3>Database Integrations on the Frontend</h3><p>I’ve also added frontend support for <strong>ExoMol</strong> and <strong>NIST</strong> databases:</p>
    <ul><li><strong>ExoMol</strong> is now functional. However, it still requires optimization. Specifically, setting the broadf variable to False can help reduce unnecessary broadening downloads overhead.</li><li><strong>NIST</strong> and <strong>HITEMP</strong> are not yet fully working, as they require login through the HITRAN website. To address this, I’ve added a script that automatically sets the email and password in the RADIS configuration, enabling these databases to work when the application is run.</li></ul><img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=5ae8056490f5" width="1" />

