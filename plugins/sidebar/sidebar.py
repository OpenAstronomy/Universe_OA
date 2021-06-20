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
                author_lists[author] = {'date': datepost, 'dates': [datepost]}
            else:
                if datepost > author_lists[author]['date']:
                    author_lists[author] = {'date':{datepost}}
                author_lists[author]['dates'].append(datepost)
            author_lists[author]['team'] = team
            post_link = post.meta['en']['link']
            if ("medium" in post_link and "@" in post_link) or "dev.to" in post_link:
                usertag = '\@' if 'medium' in post_link else ''
                regex_url = f"(?P<url>https?://[^\s+/\s+/]+\/{usertag}\w+(\.\w+)?)"
            else:
                regex_url = "(?P<url>https?://[^\s/]+(/blog/)?)" # adds an optional blog as some have it as a different repository
            try:
                author_lists[author]['url'] = re.search(regex_url, post_link).group("url")
            except AttributeError:
                # Some medium bloggers subgrouping their posts, skipping those for now
                author_lists[author]['url'] = None
        author_lists = OrderedDict(sorted(author_lists.items(), key=lambda t: str.lower(t[0])))

        def html_bit(authors, site=None, context=None):
            utc = pytz.UTC
            text_mobile = """
            <style>
@media screen and (max-width: 600px) {
.table-done {
    visibility: hidden;
    clear: both;
    padding: 0px 300px;
    width: 50%;
    display: block;
  }
}
            </style>
            """

            final_text = text_mobile + u'<div class="sidebar" style="width:100%; max-width:100%; float:initial; margin:0px;"><ul>'
            now_2w = datetime.datetime.utcnow() - datetime.timedelta(weeks=2)
            now_2w = now_2w.replace(tzinfo=utc)
            this_year = datetime.datetime.utcnow().year
            image = site.config["LOGOS"]
            dates = site.config["DATES"].get(this_year)

            date_ranges = [ (datetime.datetime.combine(x["start"], datetime.datetime.min.time()).replace(tzinfo=utc),
                             (datetime.datetime.combine(x["end"], datetime.datetime.min.time()).replace(tzinfo=utc)))  for x in dates]
            for author in authors.keys():
                if authors[author]['date'].year < this_year:
                    continue
                if author == 'rkiman':
                    continue
                style = ''
                # filling table:
                filltable = ""
                for st, en in date_ranges:
                    if datetime.datetime.utcnow().replace(tzinfo=utc) < st:
                        symbol = "🔲"
                        style = "opacity: 0.5;"
                    else:
                        anydate = any(filter(lambda x: st < x <= en, authors[author]['dates']))
                        if anydate:
                            symbol = "✅"
                        else:
                            if st < datetime.datetime.utcnow().replace(tzinfo=utc) < en:
                                symbol = "🔲"
                            else:
                                symbol = "❌"
                    filltable += f"<span style=\"display:table-cell; width:7%;{style}\" data-toggle=\"tooltip\" title=\"{st:%Y-%m-%d} - {en:%Y-%m-%d}\">{symbol}</span>"

                style = ''
                if authors[author]['date'] < now_2w:
                    style = 'style="color:rgb(255,0,0)"'

                if authors[author]['url']:
                    href = '''<a href="{url}" data-toggle="tooltip" data-placement="top" title="{date}" {style}>
                    {author}
                   </a>'''.format(url=authors[author]['url'],
                                  author=author,
                                  style=style,
                                  date=authors[author]['date'])
                else:
                    href = '''<span data-toggle="tooltip" data-placement="top" title="{date}" {style}>
                    {author}
                    </span>'''.format(url=authors[author]['url'],
                                      author=author,
                                      style=style,
                                      date=authors[author]['date'])
                final_text += '''<li>
                   <img src="{img}" height="16" width="16">
                   {href}
                   <span class="table-done" style="float: right; padding-right:600px;">{intable}</span>
                </li>'''.format(img=image[authors[author]['team']],
                                href=href,
                                intable=filltable,
                )
            final_text += '</ul></div>'
            return final_text

        site.template_hooks['page_header'].append(html_bit, True, author_lists)
        super(Sidebar, self).set_site(site)
