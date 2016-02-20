import time
import datetime as dt
from html.parser import HTMLParser
import pickle

import yaml
import feedparser

TEMPLATE = '''.. title: {title}
.. slug:
.. date: {date:%Y-%m-%d %H:%M:%S %Z}
.. tags: {tags}
.. author: {author}
.. link: {link}
.. description:
.. category: {category}

{summary} `...READ MORE... <{link}>`__

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


def grab_student(last_date, rss_url, project, student):
    feed = feedparser.parse(rss_url)
    dates = [last_date]
    for item in feed['items']:
        item_date = dt.datetime.fromtimestamp(time.mktime(item['published_parsed']))
        # item_date.tm_zone; tm_gmtoff
        # wordpress; time.struct_time
        if item_date > last_date:
            dates.append(item_date)
            filename = '{date:%Y%m%d_%H%M}_{student}.rst'.format(date=item_date, student=student)# TODO: make it so it goes to the directory
            with open(filename,'w') as post:
                post.write(TEMPLATE.format(title=item['title'],
                                           date=item_date,
                                           tags=project,
                                           author=item['author_detail']['name'],
                                           link=item['link'],
                                           category='gsoc2016',
                                           summary=strip_tags(item['summary'])[:300]))
    return(max(dates))


with open('gsoc_times.yml', 'r') as file_times:
    levels = yaml.load_all(file_times)
    for level in levels:
        students_times  = level

with open('gsoc.yml', 'r') as stream:
    list_students = yaml.load_all(stream)
    for students in list_students:
        for student,propers in students.items():
            print(student,':',propers['rss_feed'])
            print(student,':',propers['project'])
            students_times[student] = grab_student(students_times[student], propers['rss_feed'], propers['project'], student)


with open('gsoc_times.yml', 'w') as file_times:
    file_times.write(yaml.dump(students_times, default_flow_style=False))
# write page of students with css time_ranges
