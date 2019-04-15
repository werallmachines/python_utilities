#!/usr/bin/env python

##########################################################
# This is a Python mailer capable of sending out mail to #
# single users or multiple users. Its purpose is to send #
# out emails with plaintext attachments as the body      #
##########################################################

from email.mime.text import MIMEText
import smtplib

webteam = ['matt.sanderson@encana.com', 'logan.noonan@encana.com', 'adam.stewart@encana.com']
toaddr = webteam
fromaddr = 'matt.sanderson@encana.com'
subject = ''
attachment = ''
mailhost = 'mailhost'

def send_mail():
    with open(attachment, "rb") as fo:
        msg = MIMEText(fo.read())

    msg['Subject'] = subject'
    msg['From'] = fromaddr
    msg['To'] = toaddr

    smtp = smtplib.SMTP(mailhost)
    smtp.sendmail(fromaddr, toaddr, msg.as_string())
    smtp.quit()