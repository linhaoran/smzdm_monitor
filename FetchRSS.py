# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
# import codecs
import urllib2 as ureq
import json

# import urllib.request as ureq

# rss_url = 'http://feed.smzdm.com'  # 优惠精选
# rss_url = 'http://haitao.smzdm.com/feed'  # 海淘
# rss_url = 'http://post.smzdm.com/feed'  # 原创
# rss_url = 'http://faxian.smzdm.com/feed'  # 发现
# rss_url = 'http://news.smzdm.com/feed'  # 咨询


class FetchRSS(object):
    def __init__(self, url):
        self.url = url
        # self.tree = ET.parse(self.url)
        # self.tree = ET.fromstring(self.url)
        # self.rss = self.tree.getroot()
        self.rss = ET.fromstring(self.url)
        # print(self.tree, self.rss)

    def get_item_list(self):
        item_list = []
        item_title = []
        item_link = []

        for channel in self.rss:
            # print(channel.tag, channel.text)
            for items in channel:
                # print(items.tag)
                if items.tag == 'item':
                    for item in items:
                        # print(item.tag)
                        if item.tag == 'title':
                            # print(item.text)
                            item_title.append(item.text)
                        elif item.tag == 'link':
                            item_link.append(item.text)
        # print(item_title)
        # print(item_link)
        # item_list = dict(zip(item_title, item_list))
        # return item_list
        return [item_title, item_link]


if __name__ == "__main__":
    url = open('rss.txt', mode='r')
    tmp = FetchRSS(url.read())

    # rss_url = 'http://feed.smzdm.com'  # 优惠精选
    # opener = ureq.build_opener()
    # opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    # rss_text = opener.open(rss_url).read()
    # tmp = FetchRSS(rss_text)

    (tmpA, tempb) = tmp.get_item_list()

    print(json.dumps(tmpA, encoding='utf8', ensure_ascii=False))
    print(json.dumps(tempb, encoding='utf8', ensure_ascii=False))
