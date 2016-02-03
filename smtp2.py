# coding: utf-8


def create_email_body(dbname, start_dt, end_dt):
    import FetchRSS2 as FR
    import keywords
    import SMZDMscaner as SZ
    import datetime as dt

    # smzdmitems_query = FR.SmzdmItem.all().ancestor(FR.smzdmitem_key(dbname)).order('-dt')
    smzdmitems_query = FR.SmzdmItem.all().ancestor(FR.smzdmitem_key(dbname)).filter("dt >=", start_dt).filter('dt <', end_dt).order('-dt')
    query = smzdmitems_query.fetch(smzdmitems_query.count())
    keywords_list = keywords.Keywords().keywords_list

    # query2 = smzdmitems_query.filter("title like ", '%xbox%')

    # body_html = u"<p>========================================</p>"
    body_html = u""
    for q in query:
        sz = SZ.SMZDMscaner(q.title)
        if sz.SearchForKeywords(keywords_list):
            if q.keyword:
                body_html += u'''<H3>{0}<a href="{1}">直达链接</a></H3>
                                 <p><b>简介：</b>{2}</p>
                                 <p><b>命中关键字：</b>{3}  <b>发布时间：</b><i>{4}</i></p>
                                 <p></p>'''.format(q.title, q.link, q.desc, q.keyword, q.dt)
            else:
                body_html += u'''<H3>{0}<a href="{1}">直达链接</a></H3>
                                 <p><b>简介：</b>{2}  <b>发布时间：</b><i>{3}</i></p>
                                 <p></p>'''.format(q.title, q.link, q.desc, q.dt)
            body_html += u"<p>----------------------------------------</p>"

    return body_html


def send_email(sender="", pwd="",
               to="", cc="", subject="SMZDM Notification",
               body='', send_ind=False):
    import smtplib
    from email.mime.text import MIMEText

    # try:
    msg = MIMEText(body, 'html', 'utf8')
    msg['FROM'] = sender
    msg['TO'] = ", ".join(to if type(to) is list else [to])
    msg['CC'] = ", ".join(cc if type(cc) is list else [cc])
    msg['SUBJECT'] = subject
    print(msg.as_string())
    server = smtplib.SMTP("smtp.163.com", 25)
    server.login(sender, pwd)
    if send_ind:
        server.sendmail(sender, to, msg.as_string())
    server.close()
    print 'Successfully sent the mail. Over.'
    # except Exception, e:
    #     print(e)
    #     print "Failed to send mail."


if __name__ == "__main__":
    # body_html = u'''
    #         <H1>值得买提醒</H1>
    #         <p></p>
    #        '''
    # send_email(sender="linhaoran_kindle@163.com",
    #            pwd="10131201",
    #            to="linhaoran_smzdm@163.com",
    #            # cc="haoran.lin@icbc.com.cn",
    #            subject="关键字：",
    #            body=body_html)
    # send_email(subject='abc', body=body_html)

    create_email_body("smzdmtest")
