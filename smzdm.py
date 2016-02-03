# -*- coding: utf-8 -*-
import webapp2
import SMZDMscaner as SZ
import FetchRSS2 as FR
import urllib2 as ureq
import keywords
import os
from google.appengine.ext.webapp import template
import smtp2
import datetime as dt


class KeywordsHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.write("keyword.html")

        keywords_list = keywords.Keywords().keywords_list
        template_values = {
            'keywords': keywords_list,
            # 'url': url,
            # 'url_linktext': url_linktext,
        }

        path = os.path.join(os.path.dirname(__file__), 'templates/KeywordsShow.html')
        print(path)
        # self.response.out.write(template.render('templates/index.html', template_values))
        self.response.out.write(template.render(path, template_values))

    def post(self):
        pass


class NotifyHandler(webapp2.RequestHandler):
    def get(self):
        smzdmitem_name = "smzdmtest"
        start_dt, end_dt = FR.GetDataDTSection(dt.datetime.now(), period=120)

        # rss_url = 'http://feed.smzdm.com'  # 优惠精选
        # rss_url = 'http://faxian.smzdm.com/feed'  # 发现
        rss_url_list = [
            'http://feed.smzdm.com',
            'http://faxian.smzdm.com/feed'
        ]
        for rss_url in rss_url_list:
            opener = ureq.build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_10_2) \
                                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36')]
            rss_file = opener.open(rss_url)
            rss_text = rss_file.read()

            # rss_file = open('rss.txt')
            # rss_text = rss_file.read()
            # # 数据更新开关
            FR.FetchRSS2(rss_text).get_item_list(smzdmitem_name, start_dt, end_dt)

            smzdmitems_query = FR.SmzdmItem.all().ancestor(FR.smzdmitem_key(smzdmitem_name)).order('-dt')
            # query = smzdmitems_query.fetch(smzdmitems_query.count())

            # start_dt, end_dt = FR.GetDataDTSection(dt.datetime(2016, 1, 20, 20, 15), 120)
            # self.response.out.write("Start_dt is: {0} End_dt is {1}".format(start_dt, end_dt))
            # self.response.out.write(smtp2.create_email_body(smzdmitem_name, start_dt, end_dt))

            self.response.out.write("Start_dt is: {0} End_dt is {1}".format(start_dt, end_dt))
            self.response.out.write(smtp2.create_email_body(smzdmitem_name, start_dt, end_dt))

            body_html = smtp2.create_email_body(smzdmitem_name, start_dt, end_dt)
            smtp2.send_email(subject="SMZDM Notification: " + rss_url, body=body_html, send_ind=True)

            rss_file.close()


class MainHandler(webapp2.RequestHandler):
    def get(self):
        # rss_url = 'http://feed.smzdm.com'  # 优惠精选
        # opener = ureq.build_opener()
        # opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_10_2) \
        # AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36')]
        # rss_file = opener.open(rss_url)
        # rss_text = rss_file.read()

        rss_file = open('rss.txt')
        rss_text = rss_file.read()
        tmp = FR.FetchRSS(rss_text)

        keywords_list = keywords.Keywords().keywords_list

        (item_title, item_link) = tmp.get_item_list()

        for i in range(len(item_title)):
            smzdm = SZ.SMZDMscaner(item_title[i])
            if smzdm.SearchForKeywords(keywords_list):
                # print(json.dumps((item_title[i], item_link[i]), encoding='utf8', ensure_ascii=False))
                self.response.write("<p>")
                self.response.write(item_title[i])
                self.response.write(item_link[i])
                self.response.write("</p>")

        rss_file.close()


route = [
    ('/keywords', KeywordsHandler),
    ('/notify', NotifyHandler),
    ('/smzdm', MainHandler),
]

app = webapp2.WSGIApplication(routes=route, debug=True)
