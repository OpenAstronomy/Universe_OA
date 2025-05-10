import os
import time
import datetime as dt
from html.parser import HTMLParser
import pickle
import pprint

import yaml
import feedparser

pp = pprint.PrettyPrinter(indent=4)

TEMPLATE = '''.. title: {title}
.. slug:
.. date: {date:%Y-%m-%d %H:%M:%S %Z}
.. tags: {tags}
.. author: {author}
.. link: {link}
.. description:
.. category: {category}


{post}

'''


class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def remove_indent(text):
    """Removes leading and trailing spaces from each line in the text."""
    lines = text.splitlines()
    lines = [x.strip() for x in lines]
    return "\n".join(lines)


def html2rst_allign_post(text):
    if not text:
        raise ValueError("Empty post!")

    lines = text.splitlines()
    # Some feed provide the whole post into a single line. This won't work on the RST file
    # so we split it by introducing `\n` at the end of <br> and </p> tags.
    if len(lines) < 2:
        lines = '\n'.join(lines).replace("br>", "newline>\n").replace("/p>", "/pline>\n").splitlines()
        lines = [x.replace("newline>", "br>").replace("/pline>","/p>") for x in lines]
    # Insert teaser marker
    lines.insert(3, "<!-- TEASER_END -->")
    lines = ["    " + x.strip() for x in lines]
    lines = [".. raw:: html", ""] + lines

    return "\n".join(lines)


def grab_student(last_date, rss_url, project, student, season):
    """Fetches blog posts of students and processes them into rst files."""
    feed = feedparser.parse(rss_url)
    dates = [last_date]

    for item in feed['items']:
        item_date = dt.datetime.fromtimestamp(time.mktime(item['published_parsed']))
        # item_date.tm_zone; tm_gmtoff
        # wordpress; time.struct_time

        # Filter posts after the last grabbed date
        if item_date > last_date:
            # Handle Medium posts specifically related to GSoC
            if "https://medium" in rss_url and not any('gsoc' in x.get('term').lower() for x in item.get('tags', [{'term': ''}])):
                continue

            print("#################### New post!")
            pp.pprint(item)
            dates.append(item_date)

            # Create directories for storing posts
            directory = os.path.join('posts', '{:%Y}'.format(item_date), '{:%m}'.format(item_date))
            if not os.path.exists(directory):
                os.makedirs(directory)

            filename = '{date:%Y%m%d_%H%M}_{student}.rst'.format(date=item_date, student=student)
            fullcontent = ""

            # Fetch content, either HTML or plain text
            try:
                html = "html" in item['content'][0]['type']
                content = item['content'][0]['value']
            except KeyError:
                html = "html" in item['summary_detail']['type']
                content = item['summary']

            try:
                # Convert the content to rst with correct handling of HTML
                fullcontent = html2rst_allign_post(content) if html else strip_tags(content)
            except ValueError as e:
                # post contains no text
                dates.pop() # removing the last added date for the empty post
                print("#################### Empty post!")
                continue

            with open(os.path.join(directory, filename), 'w', encoding="utf-8") as post:
                # some posts have an empty title, taking the first 30 characters.
                title_post = item['title'] if item['title'] != '' else strip_tags(item['summary'])[:30] + '...'
                author = item.get('author_detail', {'name': student})  # Fallback to student's name if author is missing
                summary = remove_indent(strip_tags(item['summary'][:300]))
                post.write(TEMPLATE.format(title=title_post,
                                           date=item_date,
                                           tags=project,
                                           author=author['name'],
                                           link=item['link'],
                                           category=season,
                                           post=fullcontent,
                                           summary=summary,
                                           ))
    return(max(dates))


# Load student times from YAML file
with open('gsoc_times.yml', 'r') as file_times:
    levels = yaml.load_all(file_times, Loader=yaml.BaseLoader)
    for level in levels:
        students_times = level

# Load student RSS feed details from YAML file
with open('gsoc.yml', 'r') as stream:
    list_seasons = yaml.load(stream, Loader=yaml.BaseLoader)
    for season, list_students in list_seasons.items():
        yearseason = int(season[4:])
        if yearseason < dt.datetime.utcnow().year:
            continue
        for student, propers in list_students.items():
            print(f"{student} : {propers['rss_feed']}")
            print(f"{student} : {propers['project']}")

            # Update the last post date
            students_times[student] = dt.datetime.strptime(students_times[student], '%Y-%m-%d %H:%M:%S')

            # Grab new posts
            students_times[student] = grab_student(students_times[student],
                                                   propers['rss_feed'],
                                                   propers['project'],
                                                   student,
                                                   season)

# Save the updated student times back to YAML
with open('gsoc_times.yml', 'w') as file_times:
    file_times.write(yaml.dump(students_times, default_flow_style=False))
