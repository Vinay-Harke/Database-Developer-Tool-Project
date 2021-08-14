# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 16:02:56 2020

@author: hp
"""

import capt_demo as cpd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def login_email(recipients_mail):   
    email='Enter Your Email Id '
    password='Enter Your Password'
    send_to_email=recipients_mail
    subject="Confirmed Registration Of DB-Project"
    message="Welcome\nYour registration has been done sucessfully now you can sign in directly.\n"
    
    msg=MIMEMultipart()
    msg['From']=email
    msg['To']=send_to_email
    msg['subject']=subject
    
    msg.attach(MIMEText(message,'plain'))
    
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email,password)
    text=msg.as_string()
    server.sendmail(email,send_to_email,text)
    server.quit()
def reset_email(recipients_mail):
    email='Enter Your Email '
    password='Password'
    send_to_email=recipients_mail
    reset_password_text=cpd.create_random_captcha_text(4)
    subject='Reset Password'
    message='Use below temporary code for login into your database project ! \n'+reset_password_text
    
    msg=MIMEMultipart()
    msg['From']=email
    msg['To']=send_to_email
    msg['subject']=subject
    
    msg.attach(MIMEText(message,'plain'))
    
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email,password)
    text=msg.as_string()
    server.sendmail(email,send_to_email,text)
    server.quit()
    return reset_password_text