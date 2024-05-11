
# Universe OA

This is the blog aggregator of the Open Astronomy community. For now it's only been used
for SoC programmes (GSoC/SoCiS).

## Structure of this repository

There are three branches: `main`, `run` and `gh-pages`.

- `main` includes only commits made by people and not automatically.
- `run` runs on GH actions and updates the posts and everything
- `gh-pages` is the built version of the page, also done automatically.

We could keep `main` and `run` in the same branch but this makes it easier to
search the commits that we care about.


## Blog engine

This blog aggregator is generated as a static site using [Nikola](https://getnikola.com/).

The configuration file for the site is ``conf.py``. Refer to [Nikola's documentation](https://getnikola.com/documentation.html) for details on how to use it.

### The blog aggregator

The blog aggregator is controlled by two files: `gsoc.yml` and `gsoc_times.yml` and executed by `grab.py` script.

- `gsoc.yml` keeps a list of all the gsoc editions, the gsoc participants, their rss feed and the organisation they are working for.
- `gsoc_times.yml` keeps a key-value record of the date from the last contribution for each participant.
- `grab.py` reads from the files above and updates them after a new blog entry has been found. 
   The entry is downloaded and added as an entry in the aggregator.

### The Contributors tracker

A little widget is shown in the top of the website to track the blog posts of each participant.
With our SoC rules, we require one post every fortnight.

The widget is created using a Nikola plugin.
Its source is under `plugins/sidebar/sidebar.py`.
It uses the logos and dates set in `organisations.yml` and `dates_posts.yml` load through the `conf.py`.

The plugin looks whether there are posts in the ranges between the dates provided, and places a symbol for each of the GSoC participants.


# Updates for a new SoC season:

1. Update `gsoc_times.yml` from `run` into `main`
   ```
   git restore --source run gsoc_times.yml
   ```
   This brings the latest updates to `gsoc_times.yml`.

1. Add properties on `gsoc.yml` and on `gsoc_times.yml` for new students. For names we are using their github handles.
   ```yaml
   gsocYYYY:
     gh_student_a:
       rss_feed: "rss-url" # TODO (add blog with gsoc tag)
       project: 'suborg' # TODO (add project as named on ..)
   ```
   Then, once completed that file you can run this snippet to fill `gsoc_times.yml`
   ```bash
   year=$(date +"%Y")
   lastyear=$(( ${year} - 1))
   sed -n "/^gsoc${year}/,/gsoc${lastyear}/p" gsoc.yml | grep "^  [[:alpha:]].*:$" | sed 's/^[ ]*//' | sed "s/$/ ${year}-05-01 00:00:00/g" >> gsoc_times.yml
   LC_COLLATE=C sort -o  gsoc_times.yml gsoc_times.yml # So it sorts as python does, first upper case, then lower
   ```

1. Create a PR and ask students to PR to that filling it in. As in: [2018](https://github.com/OpenAstronomy/Universe_OA/pull/8)

1. squash merge that pull request into `main`.

1. Locally, update `dates_post.yaml` with the new date ranges for this season and commit it to `main`

1. copy the new config files into the `run` branch, for example with:
   ```bash
   git rebase --onto run <x> <z>
   ```
   where `<x>` is the commit before than `<y>` which is the one we want to copy
   (up to <z> included) to `run`.
   Then push it `run` and all should work. And then push to `main`

# Debug it locally

- remove all the output:
  ```bash
  rm -rf .doit.db.* && rm -rf cache && nikola clean && nikola forget && rm -rf __pycache__ && rm -rf output
  ```
- run the grab if needed (modifying the gsoc_times) and build.
- To debug the plugin, add `doit.tools.set_trace()` instead of breakpoint to get pdb working.


