# -*- coding: utf-8 -*-
import webapp2
import SMZDMscaner as sz
import FetchRSS as fr
import urllib2 as ureq
import Keywords
import os
from google.appengine.ext.webapp import template


class KeywordsHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.write("keyword.html")

        keywords_list = Keywords.Keywords().keywords_list
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
        tmp = fr.FetchRSS(rss_text)

        keywords_list = Keywords.Keywords().keywords_list

        (item_title, item_link) = tmp.get_item_list()

        for i in range(len(item_title)):
            smzdm = sz.SMZDMscaner(item_title[i])
            if smzdm.SearchForKeywords(keywords_list):
                # print(json.dumps((item_title[i], item_link[i]), encoding='utf8', ensure_ascii=False))
                self.response.write("<p>")
                self.response.write(item_title[i])
                self.response.write(item_link[i])
                self.response.write("</p>")

        rss_file.close()


route = [
    ('/smzdm', MainHandler),
    ('/keywords', KeywordsHandler),
]

app = webapp2.WSGIApplication(routes=route, debug=True)
