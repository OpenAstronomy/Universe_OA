This folder contains the source used to generate a static site using Nikola.

Installation and documentation at https://getnikola.com/

Configuration file for the site is ``conf.py``.

To build the site::

    nikola build

To see it::

    nikola serve -b

To check all available commands::

    nikola help

# Structure of this repository

There are three branches: `master`, `run` and `gh-pages`.

- `master` includes only commits made by people and not automatically.
- `run` runs on Travis and updates the posts and everything
- `gh-pages` is the built version of the page, also done automatically.

We could keep `master` and `run` in the same branch but this makes it easier to
search the commits that we care about.

# Updates for a new season:

1. Update `gsoc_times.yml` from `run` into `master`
   ```
   git restore --source run gsoc_times.yml
   ```
   This brings the latest updates to `gsoc_times.yml`.

1. Add properties on `gsoc.yml` and on `gsoc_times.yml` for new students. For names we are using their github handles.
   ```yaml
   gsocYYYY:
     gh_student_a:
       rss_feed: "
       rss_fed: "rss-url" # TODO (add blog with gsoc tag)
       project: 'suborg' # TODO (add project as named on ..)
   ```
   Then, once completed that file you can run this snippet to fill `gsoc_times.yml`
   ```bash
   year=$(date +"%Y")
   lastyear=$(( ${year} - 1))
   sed -n "/^gsoc${year}/,/gsoc${lastyear}"/p" gsoc.yml | grep "^  [[:alpha:]].*:$" | sed 's/^[ ]*//' | sed "s/$/ ${year}-05-01 00:00:00/g" >> gsoc_times.yml
   LC_COLLATE=C sort -o  gsoc_times.yml gsoc_times.yml # So it sorts as python does, first upper case, then lower
   ```

1. Create a PR and ask students to PR to that filling it in. As in: [2018](https://github.com/OpenAstronomy/Universe_OA/pull/8)

1. copy the new config file into the `run` branch, for example with:
   ```bash
   git rebase --onto run <x> <z>
   ```
   where `<x>` is the commit before than `<y>` which is the one we want to copy
   (up to <z> included) to `run`.
   Then push it and all should work.
