This folder contains the source used to generate a static site using Nikola.

Installation and documentation at https://getnikola.com/

Configuration file for the site is ``conf.py``.

To build the site::

    nikola build

To see it::

    nikola serve -b

To check all available commands::

    nikola help

# Updates for new season:

1. Add properties on `gsoc.yml` and on `gsoc_times.yml` for new students. For names we are using their github handles.
1. Create a PR and ask students to PR to that filling it in. As in: [2018](https://github.com/OpenAstronomy/Universe_OA/pull/8)
1. copy the new config file into the `run` branch, for example with:
```bash
git rebase --onto run <x> <z>
```
where `<x>` is the commit before than `<y>` which is the one we want to copy (up to <z> included) to `run`.

Then push it and all should work.
