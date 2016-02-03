# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import datetime as dt
from google.appengine.ext import db
import webapp2
import os
from google.appengine.ext.webapp import template
import smtp2


class SmzdmItem(db.Model):
    title = db.StringProperty()
    link = db.URLProperty()
    dt = db.DateTimeProperty(auto_now_add=True)
    desc = db.StringProperty(multiline=True)
    content = db.TextProperty()
    price = db.FloatProperty(default=0.0)
    cheap = db.BooleanProperty(default=False)
    keyword = db.StringListProperty()


class Keywords(db.Model):
    keyword_list = db.StringListProperty()
    expect_price = db.FloatProperty(default=0.0)


def smzdmitem_key(smzdmitem_name=None):
    print(db.Key.from_path("smzdmitem_category", smzdmitem_name or 'default_itemcategory'))
    return db.Key.from_path("smzdmitem_category", smzdmitem_name or 'default_itemcategory')


class FetchRSS2(object):
    def __init__(self, url):
        self.url = url
        self.rss = ET.fromstring(self.url)
        self.item_count = 0
        self.item_list = []

    def get_item_list(self, dbname):
        for channel in self.rss:
            # print(channel.tag, channel.text)
            for items in channel:
                # print(items.tag)
                if items.tag == 'item':
                    # smzdmitem_name = 'smzdmtest'
                    t = SmzdmItem(parent=smzdmitem_key(dbname))
                    # self.item_list.append(t)
                    # self.item
                    for item in items:
                        # print(item.tag)
                        if item.tag == 'title':
                            # print(item.text)
                            t.title = item.text
                        elif item.tag == 'link':
                            t.link = item.text
                        elif item.tag == 'pubDate':
                            t.dt = dt.datetime.strptime(item.text,
                                                        "%a, %d %b %Y %H:%M:%S")
                        elif item.tag == 'description':
                            t.desc = item.text
                        elif item.tag == "{http://purl.org/rss/1.0/modules/content/}encoded":
                            t.content = item.text
                    t.put()
                    # print(t.title)


def GetDataDTSection(now, period=15):
    start_time = dt.datetime(now.year, now.month, now.day, now.hour, now.minute) - dt.timedelta(minutes=period)
    end_time = dt.datetime(now.year, now.month, now.day, now.hour, now.minute) + dt.timedelta(minutes=0)
    return start_time, end_time


class TestHandler(webapp2.RequestHandler):
    def get(self):
        # smzdmitem_name = self.request.get("smzdmitem_category")
        smzdmitem_name = "smzdmtest"
        smzdm = SmzdmItem(parent=smzdmitem_key(smzdmitem_name))

        url = open('rss.txt')
        # 数据更新开关
        # FetchRSS2(url.read()).get_item_list(smzdmitem_name)

        smzdmitems_query = SmzdmItem.all().ancestor(smzdmitem_key(smzdmitem_name)).order('-dt')
        query = smzdmitems_query.fetch(smzdmitems_query.count())
        template_values = {
            'query': query,
        }
        path = os.path.join(os.path.dirname(__file__), 'templates/test.html')
        self.response.out.write(template.render(path, template_values))


class TestHandler2(webapp2.RequestHandler):
    def get(self):
        # smzdmitem_name = self.request.get("smzdmitem_category")
        smzdmitem_name = "smzdmtest"
        smzdm = SmzdmItem(parent=smzdmitem_key(smzdmitem_name))

        url = open('rss.txt')
        # # 数据更新开关
        # FetchRSS2(url.read()).get_item_list(smzdmitem_name)

        smzdmitems_query = SmzdmItem.all().ancestor(smzdmitem_key(smzdmitem_name)).order('-dt')
        query = smzdmitems_query.fetch(smzdmitems_query.count())
        template_values = {
            'query': query,
        }
        # path = os.path.join(os.path.dirname(__file__), 'templates/test.html')
        start_dt, end_dt = GetDataDTSection(dt.datetime(2016, 1, 20, 20, 15), 120)
        # start_dt, end_dt = GetDataDTSection(dt.datetime.now())
        self.response.out.write("Start_dt is: {0} End_dt is {1}".format(start_dt, end_dt))
        self.response.out.write(smtp2.create_email_body(smzdmitem_name, start_dt, end_dt))


app = webapp2.WSGIApplication([
    ('/test', TestHandler),
    ('/test2', TestHandler2),
], debug=True)

if __name__ == "__main__":
    app.run()
    # url = open('rss.txt')
    #
    # tmp = FetchRSS2(url.read())
    # tmp.get_item_list()
    #
    # q = SmzdmItem.all().ancestor(smzdmitem_key(smzdmitem_name)).order('-dt')
    # # q = db.Query(SmzdmItem)
    # q2 = q.fetch(q.count())
    #
    # for p in q2:
    #     print p.title
    #
    #     # print(SmzdmItem.all().filter('title = ', "abc"))
