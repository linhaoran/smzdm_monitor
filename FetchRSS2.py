# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import datetime as dt
from google.appengine.ext import db


class SmzdmItem(db.Model):
    # info = {
    #     title: '',
    #     link: '',
    #     dt: '',
    #     desc: '',
    #     content: '',
    #     price: '',
    #     cheap_ind: ''
    # }
    title = db.StringProperty()
    link = db.URLProperty()
    dt = db.DateTimeProperty()
    desc = db.StringProperty()
    content = db.StringProperty()
    price = db.FloatProperty(default=0.0)
    cheap = db.BooleanProperty(default=False)


class Keywords(db.Model):
    # title = db.ListProperty()
    price = db.FloatProperty(default=0.0)


class SmzdmRssItem(object):
    def __init__(self):
        self.title = ''
        self.link = ''
        self.dt = ''
        self.desc = ''
        self.content = ''

    def __set__(self, instance, value):
        if instance == 'pubDate':
            self.dt == dt.datetime.strptime(value, "%a, %d %b %Y %H:%M:%S")
        elif instance == "title":
            self.title = value
        elif instance == "link":
            self.link = value
        elif instance == "description":
            self.desc = value
        elif instance == "{http://purl.org/rss/1.0/modules/content/}encoded":
            self.content = value

    def __get__(self, instance, owner):
        if instance == 'dt':
            # dt.datetime.strptime(item.text, "%a, %d %b %Y %H:%M:%S").strftime(
            # '%Y-%m-%d %H:%M:%S'))
            return self.dt.strf('%Y %m %d')
        else:
            # return  self.title
            pass

    def show_item_info(self):
        pass
        return


class FetchRSS2(object):
    def __init__(self, url):
        self.url = url
        self.rss = ET.fromstring(self.url)
        self.item_count = 0
        self.item_list = []

    def get_item_list(self):
        for channel in self.rss:
            # print(channel.tag, channel.text)
            for items in channel:
                # print(items.tag)
                if items.tag == 'item':
                    self.item_count += 1
                    t = SmzdmRssItem()
                    self.item_list.append(t)
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


def GetDataDTSection(now):
    start_time = dt.datetime(now.year, now.month, now.day, now.hour, now.minute) - dt.timedelta(minutes=10)
    end_time = dt.datetime(now.year, now.month, now.day, now.hour, now.minute) + dt.timedelta(minutes=0)
    return start_time, end_time


if __name__ == "__main__":
    url = open('rss.txt')

    # sitem= SmzdmRssItem()
    # sitem.title = 'abc'
    # sitem.dt = dt.datetime(2015,12,12,1,1,1)
    # print(sitem.title)
    # print(sitem.dt)


    tmp = FetchRSS2(url.read())
    tmp.get_item_list()

    for i in range(tmp.item_count):
        t = tmp.item_list[i]
        # print(t.title)
        # print(t.link, str(t.dt))
        # print(t.desc)
        # print("")

    a = SmzdmItem()
    a.title = 'abc'
    a.dt = dt.datetime(2015, 1, 1, 12, 21, 0)
    b = SmzdmItem()
    b.title = 'def'
    b.dt = dt.datetime(2016, 1, 1, 12, 21, 0)
    # print(SmzdmItem.all().filter('title = ', "abc").count(1))

    # tmp = FetchRSS2(url.read())
    # tmp.get_item_list()
    #
    # print(json.dumps(tmp.item_title, encoding='utf8', ensure_ascii=False))
    # print(json.dumps(tmp.item_link, encoding='utf8', ensure_ascii=False))
    # print(json.dumps(str(tmp.item_dt1), encoding='utf8', ensure_ascii=False))
    # print(json.dumps(str(tmp.item_dt2), encoding='utf8', ensure_ascii=False))
    # print(json.dumps(tmp.item_desc, encoding='utf8', ensure_ascii=False))
    # print(json.dumps(tmp.item_content, encoding='utf8', ensure_ascii=False))
    #
    # now_dt = dt.datetime.now()
    # start_dt, end_dt = GetDataDTSection(now_dt)
    # print('Now is {0}, Start_dt is {1}, End_dt is {2}'.format(now_dt, start_dt, end_dt))
