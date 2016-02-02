# coding: utf-8
import smtplib
from email.mime.text import MIMEText


def create_email_body():
    import SMZDMscaner as SZ
    import FetchRSS as FR
    import Keywords
    import json
    import smtp2

    rss_file = open('rss.txt')
    rss_text = rss_file.read()
    tmp = FR.FetchRSS(rss_text)

    keywords_list = Keywords.Keywords().keywords_list

    (item_title, item_link) = tmp.get_item_list()

    body_html = u""
    subject = []
    for i in range(len(item_title)):
        smzdm = SZ.SMZDMscaner(item_title[i])
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

    print(json.dumps(u"【" + u'】,【'.join(subject) + u"】", encoding='utf8', ensure_ascii=False))
    smtp2.send_email(subject=' '.join(u"【" + u'】,【'.join(subject) + u"】"),
                     body=body_html, send_ind=False)

    rss_file.close()
    return body_html


def send_email(sender="linhaoran_kindle@163.com", pwd="10131201",
               to="linhaoran_smzdm@163.com", cc="", subject="SMZDM Notification",
               body='', send_ind=False):
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
    body_html = u'''
            <H1>值得买提醒</H1>
            <p></p>
           '''
    # send_email(sender="linhaoran_kindle@163.com",
    #            pwd="10131201",
    #            to="linhaoran_smzdm@163.com",
    #            # cc="haoran.lin@icbc.com.cn",
    #            subject="关键字：",
    #            body=body_html)
    send_email(subject='abc', body=body_html)
