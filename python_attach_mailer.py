#!/usr/bin/env python

##########################################################
# This is a Python mailer capable of sending out mail to #
# single users or multiple users. Its purpose is to send #
# out emails with plaintext attachments as the body      #
##########################################################

from email.mime.text import MIMEText
import smtplib

mailing_list = ['']
toaddr = mailing_list
fromaddr = ''
subject = ''
attachment = ''
mailhost = 'mailhost'

def send_mail():
    with open(attachment, "rb") as fo:
        msg = MIMEText(fo.read())

    msg['Subject'] = subject
    msg['From'] = fromaddr
    msg['To'] = toaddr

    smtp = smtplib.SMTP(mailhost)
    smtp.sendmail(fromaddr, toaddr, msg.as_string())
    smtp.quit()
