#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 19:33:46 2019

@author: daniellandesman
"""
import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
import config
import quickstart
import email_messages as mm
# from datetime import datetime
import datetime as dt
# import time
import logging
import inspect
from yaml_dict import store_yaml, load_yaml

cur_time = '{:%Y-%m-%d %H:%M:%S}'.format(dt.datetime.now())
subject = "Shabbat {}"

confirm_flag = False


def set_confirm_flag_to_false():
    global confirm_flag
    confirm_flag = False


def set_confirm_flag_to_true():
    global confirm_flag
    confirm_flag = True


def get_msg_id(subj, toaddr):
    key = (toaddr, subj)
    id_dict = load_yaml()
    if key in id_dict.keys():
        msg_id = id_dict[(toaddr, subj)]
    else:
        id_dict[(toaddr, subj)] = email.utils.make_msgid()
        msg_id = id_dict[(toaddr, subj)]
    store_yaml(id_dict)
    return msg_id


fromaddr = config.EMAIL_ADDRESS
toaddr = config.RECIPIENT


# CC = ['<INSERT CC RECIPIENT>']
# BCC = ['<INSERT BCC RECIPIENT>']
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
            myid = get_msg_id(id_subj, id_toaddr)
            message = ("From: %s\r\n" % config.EMAIL_ADDRESS
                       + "To: %s\r\n" % toaddr
                       # + "CC: %s\r\n" % ",".join(CC)
                       + "Subject: %s\r\n" % subj
                       + "Message-ID: %s\r\n" % myid
                       + "\r\n" + msg)

            # toaddrs = [toaddr] + CC
            toaddrs = [toaddr]

        except:
            logging.error('Error sending email\n Function Trace: {} > {}'
                          # print('Error sending email\n Function Trace: {} > {}'
                          .format(inspect.stack()[0].function,
                                  inspect.stack()[1].function))

        server.sendmail(config.EMAIL_ADDRESS, toaddrs, message)
        server.quit()

    except:
        print("email failed to send")

FRIDAY_STATUS_RANGE_NAME = 'Form Responses 1!D2'
SATURDAY_STATUS_RANGE_NAME = 'Form Responses 1!D3:E3'

def on_monday():
    quickstart.clear_sheet()
    quickstart.update_minyan_status(FRIDAY_STATUS_RANGE_NAME,values = [['TBD']])
    quickstart.update_minyan_status(SATURDAY_STATUS_RANGE_NAME,values = [['TBD']])
    set_confirm_flag_to_false()
    msg = mm.msg_minyan_details.format(quickstart.candles,
                                       quickstart.candles ,
                                       #quickstart.friday_mincha,
                                       # quickstart.saturday_mincha,
                                       "N/A",
                                       quickstart.saturday_maariv,
                                       quickstart.havdalah)
    msg = msg + mm.msg_signup + mm.msg_signoff + mm.msg_post_script_monday
    if mm.msg_welcome != mm.msg_welcome_default:
        msg = mm.msg_welcome + msg
    send_email(subject, msg)


def on_thursday(subject=subject, friday_flag=False):
    friday_tally, saturday_tally = quickstart.get_rsvps()
    msg_info = mm.msg_minyan_details.format(quickstart.candles,
                                       #quickstart.friday_mincha,
                                       quickstart.candles,
                                       # quickstart.saturday_mincha,
                                       "N/A",
                                       quickstart.saturday_maariv,
                                       quickstart.havdalah)
    msg_tally = mm.msg_current_tally.format(friday_tally, saturday_tally)
    #msg = msg2 + msg
    msg_status=""
    if friday_flag == True:
        msg_plan = mm.msg_will_confirm
        msg_signoff=mm.msg_signoff + mm.msg_post_script_friday
    else:
        msg_plan = ""
        msg_signoff = msg_signoff + mm.msg_post_script_thursday
    if friday_tally < 10:
        msg_status = mm.msg_need_ppl_fri.format((10 - friday_tally))
        quickstart.update_minyan_status(FRIDAY_STATUS_RANGE_NAME, values=[['TBD']])
    else:
        msg_status = mm.msg_fri_minyan_confirmed
        quickstart.update_minyan_status(FRIDAY_STATUS_RANGE_NAME, values=[['MINYAN IS ON']])
    if saturday_tally < 10:
        msg_status = msg_status + mm.msg_need_ppl_sat.format((10 - saturday_tally)) #+ msg_end
        quickstart.update_minyan_status(SATURDAY_STATUS_RANGE_NAME, values=[['TBD']])
    else:
        if friday_tally >= 10:
            msg_status = mm.msg_both_confirmed
            msg2 = ""
            set_confirm_flag_to_true()
            quickstart.update_minyan_status(FRIDAY_STATUS_RANGE_NAME, values=[['MINYAN IS ON']])
            quickstart.update_minyan_status(SATURDAY_STATUS_RANGE_NAME, values=[['MINYAN IS ON']])

        else:
            msg_status = mm.msg_sat_minyan_confirmed
            quickstart.update_minyan_status(SATURDAY_STATUS_RANGE_NAME, values=[['MINYAN IS ON']])
    #msg = msg + mm.msg_signup + mm.msg_signoff
    msg = msg_status + msg_tally + msg_plan + msg_info + mm.msg_signup + mm.msg_signoff
    send_email(subject, msg)


def on_friday(subject=subject):
    global confirm_flag
    if confirm_flag == False:  # Don't send email if minyan already confirmed
        on_thursday(friday_flag=True)
    elif confirm_flag == True:
        pass


def last_call(subject=subject):
    global confirm_flag
    if confirm_flag == False:
        friday_tally, saturday_tally = quickstart.get_rsvps()
        msg = mm.msg_minyan_details.format(quickstart.candles,
                                           #quickstart.friday_mincha,
                                           quickstart.candles,
                                           "N/A",
                                           #quickstart.saturday_mincha,
                                           quickstart.saturday_maariv,
                                           quickstart.havdalah)
        msg = mm.msg_current_tally.format(friday_tally, saturday_tally) + msg

        if friday_tally < 10 and saturday_tally < 10:
            msg = mm.msg_both_nogo + msg
            quickstart.update_minyan_status(FRIDAY_STATUS_RANGE_NAME, values=[['MINYAN IS CANCELED']])
            quickstart.update_minyan_status(SATURDAY_STATUS_RANGE_NAME, values=[['MINYAN IS CANCELED']])
        elif friday_tally >= 10 and saturday_tally < 10:
            msg = mm.msg_fri_minyan_confirmed + mm.msg_sat_nogo + msg
            quickstart.update_minyan_status(FRIDAY_STATUS_RANGE_NAME, values=[['MINYAN IS ON']])
            quickstart.update_minyan_status(SATURDAY_STATUS_RANGE_NAME, values=[['MINYAN IS CANCELED']])
        elif friday_tally < 10 and saturday_tally >= 10:
            msg = mm.msg_sat_minyan_confirmed + mm.msg_fri_nogo + msg
            quickstart.update_minyan_status(FRIDAY_STATUS_RANGE_NAME, values=[['MINYAN IS CANCELED']])
            quickstart.update_minyan_status(SATURDAY_STATUS_RANGE_NAME, values=[['MINYAN IS ON']])
        else:
            msg = mm.msg_both_confirmed + msg
            quickstart.update_minyan_status(FRIDAY_STATUS_RANGE_NAME, values=[['MINYAN IS ON']])
            quickstart.update_minyan_status(SATURDAY_STATUS_RANGE_NAME, values=[['MINYAN IS ON']])
        msg = msg + mm.msg_signup + mm.msg_signoff +mm.msg_post_script_lastcall
        send_email(subject, msg)

    else:  # Don't send email if minyan already confirmed
        pass


#on_monday()
#on_thursday()
# on_friday()
# last_call()
