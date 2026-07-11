.. title: Coming up for Air
.. slug:
.. date: 2026-07-10 14:53:14 
.. tags: Astropy
.. author: Reem Hamraz
.. link: https://dev.to/reemhamraz/coming-up-for-air-587f
.. description:
.. category: gsoc2026


.. raw:: html

    <p>After the absolute gauntlet of the past few weeks, this week finally offered a little bit of breathing room. I'm not going to lie, I needed it. But "lighter" in the open-source world doesn't mean stopping; it just means you finally have the time to sit back and actually think before you code.</p>
    
    <h2>
    <!-- TEASER_END -->
    
    
    Writing .pyi Stub Files
    </h2>
    
    <p>A good chunk of my time went into writing <code>.pyi</code> stub files. It sounds mundane on the surface, like just writing Python type hints, BUT it's actually this bizarre, highly precise exercise in translation. You are basically acting as a diplomat between the ruthless C-engine and Python's static type checkers. It's microscopic work. Every single argument has to align perfectly with how the C-level memory actually allocates it, otherwise the whole illusion shatters. It requires a sort of discipline.</p>
    
    <h2>
    
    
    My Main Target
    </h2>
    
    <p>But my main focus, and what I'm gearing up to dive back into, is the <code>unit_list_proxy.c</code> file.</p>
    
    <p>There is a nasty runtime dependency lurking in there. Right now, the C-code aggressively tries to import a massive Python library the second it gets created, locking everything into this heavy, tangled cycle. For a minute, I was dreading having to do a complete, tear-it-down-to-the-studs refactor just to untangle it.</p>
    
    <p>Thankfully, I pitched an alternative to my mentor, Clément, and he gave me the green light to run with it. We'll see how that goes.</p>
    
    <h2>
    
    
    The fix?
    </h2>
    
    <p>Instead of a massive rewrite, we are going to use <strong>structural sub-typing</strong> which is a more specific form of <strong>duck typing</strong> (I guess don't come at me if I'm wrong) right at the C-level. Rather than forcing the C-engine to check an object's exact, official DNA (which requires importing the whole Python library), we are just going to check its behavior. Does it have the method we need? If it walks like a duck and quacks like a duck, the C-engine will blindly trust that it's a duck and process it.</p>
    
    <p>It is such an elegant workaround. It completely severs the nasty dependency chain without us having to burn the house down to fix the plumbing (I was pretty proud of actually thinking about it).</p>
    
    <h2>
    
    
    Thoughts..
    </h2>
    
    <p>It's a smarter, cleaner way forward. The C-layer is still intimidating, but for the first time in a while, I feel like I'm actually outsmarting the machine instead of just wrestling with it.</p>
    
    <p>Back into the dark I go.</p>

