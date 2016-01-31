# -*- coding: utf-8 -*-
import webapp2
import SMZDMscaner as sz
import FetchRSS as fr
import urllib2 as ureq
import json


class MainHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.headers['Content-Type'] = 'text/plain'
        # self.response.write('Hello, World! from Lin Haoran')

        keywords_list = [
            ['大王', '纸尿裤'],
            ['babybjorn', 'one'],
            ['Aptamil', 'pre'],
            ['nutrilon'],
            ['贝亲', '宽口径'],
            ['微信'],
            ['移动'],
            ['ERGObaby', '360'],
            ['mountain', 'buggy', 'nano'],
            [''],
            [''],
            [''],
            [''],
            [''],
            [''],
        ]

        # url = open('rss.txt')
        # tmp = fr.FetchRSS(url.read())

        rss_url = 'http://feed.smzdm.com'  # 优惠精选
        opener = ureq.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        #         req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_10_2) \
        #AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36')
        rss_text = opener.open(rss_url).read()
        tmp = fr.FetchRSS(rss_text)

        (item_title, item_link) = tmp.get_item_list()

        for i in range(len(item_title)):
            smzdm = sz.SMZDMscaner(item_title[i])
            if smzdm.SearchForKeywords(keywords_list):
                # print(json.dumps((item_title[i], item_link[i]), encoding='utf8', ensure_ascii=False))
                self.response.write("<p>")
                self.response.write(item_title[i])
                self.response.write(item_link[i])
                self.response.write("</p>")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
