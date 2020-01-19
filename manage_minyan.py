#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 19:33:46 2019

@author: daniellandesman
"""
import smtplib
import email.utils
#from email.mime.multipart import MIMEMultipart
import config_test as config
import quickstart_test as quickstart
import email_messages as mm
#from datetime import datetime
import datetime as dt
#import time
import logging
import inspect

#from collections import defaultdict
from yaml_dict_test import store_yaml, load_yaml

cur_time = '{:%Y-%m-%d %H:%M:%S}'.format(dt.datetime.now())
subject = "Shabbat {}"

confirm_flag = False

def set_confirm_flag_to_false():
    global confirm_flag
    confirm_flag = False
    
def set_confirm_flag_to_true():
    global confirm_flag
    confirm_flag = True

def get_msg_id(subj,toaddr):
    key = (toaddr,subj)
    id_dict = load_yaml()
    if key in id_dict.keys():
        msg_id = id_dict[(toaddr,subj)]
    else:
        id_dict[(toaddr,subj)] = email.utils.make_msgid()
        msg_id = id_dict[(toaddr,subj)]
    store_yaml(id_dict)
    return msg_id

    
    
fromaddr = config.EMAIL_ADDRESS
toaddr = config.RECIPIENT
#CC = ['<INSERT CC RECIPIENT>']
#BCC = ['<INSERT BCC RECIPIENT>']
def send_email(subject, msg):
    
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
    except:
        print("server fail")
    try:
        server.ehlo()
        server.starttls()
        try:
            server.login(config.EMAIL_ADDRESS, config.PASSWORD)
            
            subj = '{}'.format(subject.format(quickstart.parsha))
            
            id_subj = "".join(subj.split())
            id_toaddr = "".join(toaddr.split())
            myid = get_msg_id(id_subj,id_toaddr)
            
            message = ("From: %s\r\n" % config.EMAIL_ADDRESS 
                    + "To: %s\r\n" % toaddr 
                    #+ "CC: %s\r\n" % ",".join(CC)
                    + "Subject: %s\r\n" % subj
                    + "Message-ID: %s\r\n" % myid
                    + "\r\n" + msg)
            
            #toaddrs = [toaddr] + CC
            toaddrs = [toaddr]
          
        except:
            logging.error('Error sending email\n Function Trace: {} > {}'
            #print('Error sending email\n Function Trace: {} > {}'
                          .format(inspect.stack()[0].function,
                                  inspect.stack()[1].function))
            
        server.sendmail(config.EMAIL_ADDRESS, toaddrs, message)
        server.quit()

    except:
        print("email failed to send")


def on_monday():
    quickstart.clear_sheet()
    set_confirm_flag_to_false()
    msg = mm.msg_minyan_details.format(quickstart.candles,
                                  quickstart.friday_mincha,
                                  quickstart.saturday_mincha,
                                  quickstart.havdalah)
    msg = msg + mm.msg_signup + mm.msg_signoff
    if mm.msg_welcome != mm.msg_welcome_default:
        msg = mm.msg_welcome + msg
    send_email(subject, msg)

def on_thursday(subject=subject,friday_flag = False):
    friday_tally, saturday_tally = quickstart.get_rsvps()
    msg = mm.msg_minyan_details.format(quickstart.candles,
                                  quickstart.friday_mincha,
                                  quickstart.saturday_mincha,
                                  quickstart.havdalah)
    msg2 = mm.msg_current_tally.format(friday_tally,saturday_tally)
    msg = msg + msg2
    
    if friday_flag == True:
        msg_end = mm.msg_will_confirm
    else:
        msg_end = ""
        
    if friday_tally < 10:
        msg = msg + mm.msg_need_ppl_fri.format((10-friday_tally))
    else:
        msg = msg + mm.msg_fri_minyan_confirmed
    if saturday_tally < 10:
        msg = msg + mm.msg_need_ppl_sat.format((10-saturday_tally)) + msg_end
    else:
        if friday_tally >= 10:
            msg = msg + mm.msg_both_confirmed
            msg2 =""
            set_confirm_flag_to_true()
        else:
            msg = msg + mm.msg_sat_minyan_confirmed + msg_end
    
    msg = msg + mm.msg_signup + mm.msg_signoff
    send_email(subject, msg)


def on_friday(subject=subject):
    global confirm_flag
    if confirm_flag == False: #Don't send email if minyan already confirmed
        on_thursday(friday_flag=True)
    elif confirm_flag == True:
        pass

def last_call(subject=subject):
    global confirm_flag
    if confirm_flag == False:
        friday_tally, saturday_tally = quickstart.get_rsvps()
        msg = mm.msg_minyan_details.format(quickstart.candles,
                              quickstart.friday_mincha,
                              quickstart.saturday_mincha,
                              quickstart.havdalah)
        msg = msg + mm.msg_current_tally.format(friday_tally,saturday_tally)

        if friday_tally < 10 and saturday_tally < 10:
            msg = msg + mm.msg_both_nogo
        elif friday_tally >= 10 and saturday_tally < 10:
            msg = msg + mm.msg_fri_minyan_confirmed + mm.msg_sat_nogo
        elif friday_tally < 10 and saturday_tally >= 10:
            msg = msg + mm.msg_sat_minyan_confirmed + mm.msg_fri_nogo
        else:
            msg = msg + mm.msg_both_confirmed
        msg = msg + mm.msg_signup + mm.msg_signoff
        send_email(subject, msg)
        
    else: #Don't send email if minyan already confirmed
        pass
   
#on_monday()
#on_thursday()
#on_friday()
#last_call()
