from __future__ import unicode_literals
from nikola.plugin_categories import ConfigPlugin

from collections import OrderedDict
import datetime
import pytz
import re

# Have to inherit Task to be a task plugin
class Sidebar(ConfigPlugin):
    """Copy theme assets into output."""

    name = "sidebar"
    dates = {}
    def set_site(self, site):
        site.scan_posts()
        # NAVIGATION_LINKS is a TranslatableSetting, values is an actual dict
        author_lists = dict()
        for post in site.posts:
            author = post.author()
            datepost = post.date
            team = post.tags[0]
            text = post.text()
            if author not in author_lists.keys():
                author_lists[author] = {'date': datepost}
            else:
                if datepost > author_lists[author]['date']:
                    author_lists[author] = {'date':{datepost}}
            author_lists[author]['team'] = team
            author_lists[author]['url'] = re.search("(?P<url>https?://[^\s/]+)", text).group("url")
        author_lists = OrderedDict(sorted(author_lists.items(), key=lambda t: str.lower(t[0])))

        def html_bit(authors, site=None, context=None):
            utc = pytz.UTC
            final_text = u'<div class="sidebar">'
            now_2w = datetime.datetime.utcnow() - datetime.timedelta(weeks=2)
            now_2w = now_2w.replace(tzinfo=utc)
            image = {'Astropy':'http://www.astropy.org/favicon.ico',
                     'SunPy': 'https://cdn.rawgit.com/sunpy/sunpy-logo/master/generated/sunpy_icon.svg'}
            for author in authors.keys():
                style = ''
                print(authors[author])
                print(now_2w)
                if authors[author]['date'] < now_2w:
                    style = 'style="color:rgb(255,0,0)"'
                final_text += u'''<li>
                   <img src="{img}" height="16" width="16">
                   <a href="{url}" data-toggle="tooltip" data-placement="top" title="{date}" {style}>
                    {author}
                   </a>
                </li>'''.format(img=image[authors[author]['team']], url=authors[author]['url'],
                                date=authors[author]['date'],
                                author=author, style=style)
            final_text += u'</div>'
            return final_text

        site.template_hooks['page_header'].append(html_bit, True, author_lists)
        super(Sidebar, self).set_site(site)
