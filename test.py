# -*- coding: utf-8 -*-
import webapp2
import SMZDMscaner as sz
import FetchRSS as fr
import urllib2 as ureq
import Keywords
import json
import smtp2

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

body_html = u""
subject = []
for i in range(len(item_title)):
    smzdm = sz.SMZDMscaner(item_title[i])
    if smzdm.SearchForKeywords(keywords_list):
        print(json.dumps((item_title[i], item_link[i]), encoding='utf8', ensure_ascii=False))
        print(json.dumps(smzdm.match_keyword, encoding='utf8', ensure_ascii=False))
        subject.append(' '.join([''.join(x) for x in smzdm.match_keyword]))
        print(' '.join([''.join(x) for x in smzdm.match_keyword]))
        body_html += u'''
            <H3>{0}</H3>
            <p><a href="{1}">直达链接</a></p>
            <p><b>简介：</b>{2}aaaaaaaaaaaaaa</p>
            <p><b>详细介绍：</b>{3}bbbbbbbbbbbbb</p>
            <p></p>'''.format(item_title[i], item_link[i], "", "")

# print(json.dumps(body_html, encoding='utf8', ensure_ascii=False))
# print(body_html)
# print(subject)
print(json.dumps(u"【"+u'】,【'.join(subject)+u"】", encoding='utf8', ensure_ascii=False))
# from email.mime.text import MIMEText
# msg = MIMEText(body_html, 'html', 'utf8')
# print(msg.as_string())

smtp2.send_email(subject=' '.join(u"【"+u'】,【'.join(subject)+u"】"),
                 body=body_html, send_ind=False)

rss_file.close()
