#coding: utf-8

from google.appengine.api import mail

def sendEmailAlert(sendto, body):
    # if type(sendto) == str or type(sendto) == unicode:
    #     sendto=Accounts.all().filter('v_user = ', sendto).get()

    # sender = 'noreply@%s.appspotmail.com' % app_identity.get_application_id()
    sender = 'linhaoran.china@gmail.com'

    message = mail.EmailMessage()
    message.sender = sender #sender.author.email()
    message.to = sendto
    message.subject = u'V2EX-Daily.appspot.com Notification'
    message.body = u'%s\nUsername: Linhaoran\n\n\nhttp://v2ex-daily.appspot.com' % (body)
    message.send()


mail_address = 'linhaoran@163.com'
mail_body = 'GAE Test Eamil.'

sendEmailAlert(mail_address, mail_body)