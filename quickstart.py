#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 22:10:17 2019

@author: daniellandesman
"""

from __future__ import print_function
import pickle
import os.path
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient import discovery
import inspect
import logging

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = os.getenv("SAMPLE_SPREADSHEET_ID")
#EDIT RANGE FOR TALLY VALUES
SAMPLE_RANGE_NAME = 'Form Responses 1!C56:D56'
#EDIT RANGE TO CLEAR INPUTS AT BEGINNING OF EACH WEEK
ERASE_RANGE_NAME = 'Form Responses 1!C4:D54'

FRIDAY_STATUS_RANGE_NAME = 'Form Responses 1!D2'
SATURDAY_STATUS_RANGE_NAME = 'Form Responses 1!D3'
#Use erase range below for testing
#ERASE_RANGE_NAME = 'Form Responses 1!C570:D80'


#def main():
def get_sheet():

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '/Users/daniellandesman/minyan_poetry/manage_minyan/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds, cache_discovery=False)
    return service
def clear_sheet():
    service = get_sheet()
    clear_values_request_body = {
    # TODO: Add desired entries to the request body.
    }
    # Call the Sheets API
    sheet = service.spreadsheets()
    
    sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                range=ERASE_RANGE_NAME,body=clear_values_request_body).execute( )

def protect_sheet():
    service = get_sheet()
    sheet = service.spreadsheets()

    nrange = "TALLY_RANGE"

    res1 = service.spreadsheets().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, fields="namedRanges").execute()
    namedRangeId = ""
    for e in res1['namedRanges']:
        if e['name'] == nrange:
            namedRangeId = e['namedRangeId']
            break
    body = {
        "requests": [
            {
                "addProtectedRange": {
                    "protectedRange": {
                        "namedRangeId": namedRangeId,
                        "description": "Protecting Tallys",
                        "warningOnly": False,
                        "editors": {"users": ["shulpresidente@gmail.com","jonathan88.cohen@gmail.com"]},  # Added
                    }
                }
            }
        ]
    }
    res2 = service.spreadsheets().batchUpdate(spreadsheetId=SAMPLE_SPREADSHEET_ID, body=body).execute()
    print(res2)

def unprotect_sheet():
    service = get_sheet()
    sheet = service.spreadsheets()

    nrange = "TALLY_RANGE"

    res1 = service.spreadsheets().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, fields="namedRanges").execute()
    namedRangeId = ""
    for e in res1['namedRanges']:
        if e['name'] == nrange:
            namedRangeId = e['namedRangeId']
            break
    body = {
        "requests": [
            {
                "deleteProtectedRange": {
                    "protectedRangeId": namedRangeId
                }
            }
        ]
    }
    res2 = service.spreadsheets().batchUpdate(spreadsheetId=SAMPLE_SPREADSHEET_ID, body=body).execute()
    print(res2)

def update_minyan_status(range,values):
    service = get_sheet()
    sheet = service.spreadsheets()
    value_range_body = {
        'values': values
    }
    request = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=range,
                                                     valueInputOption='RAW', body=value_range_body).execute()


def get_rsvps():
    service = get_sheet()
    sheet = service.spreadsheets()
    #value_render_option = 'FORMATTED_VALUE'
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME,majorDimension='COLUMNS').execute()

    values = result.get('values', [])

    if not values:
        logging.error('Error sending email\n Function Trace: {} > {}'
                      .format(inspect.stack()[0].function,
                              inspect.stack()[1].function))
    else:

        friday_tally = int(values[0][0])
        saturday_tally = int(values[1][0])

    return friday_tally, saturday_tally



import requests
import html2text
import datetime



def get_zman (date,text,offset_1,offset_2):
    #url = f"https://www.ahavathtorah.org/calendar?view=day&cal_date={date}&date_start=specific+date&date_start_x=0&date_start_date={date}"
    url = f"https://www.ahavathtorah.org/calendar?view=day&cal_date={date}&date_start=specific+date&date_start_date={date}"
    # Get raw html text
    try:
        f = requests.get(url)
        print(f)
    except:
        logging.error('Error getting url\n Function Trace: {} > {}'
                      .format(inspect.stack()[0].function,
                              inspect.stack()[1].function))
    
    raw_text =f.text
    print(raw_text)
    # Convert raw HTML to clean sting
    h = html2text.HTML2Text()
    h.ignore_links = True
    clean_text = h.handle(raw_text)
    print(clean_text)#text = text
    start_idx = clean_text.find(text)
    print(start_idx)
    zman = clean_text[start_idx-offset_1:start_idx+offset_2].replace("\n","")
    return zman
    
today = datetime.date.today()
friday = today + datetime.timedelta( (4-today.weekday()) % 7 )
saturday = friday + datetime.timedelta(1)
mincha_txt = "p |    |  |\n\nMincha"
candle_text = "p |    |  |\n\nCandle Lighting"
havdalah_text = "p |    |  |\n\nHavdalah"
parsha_text = "Parshat"

import time
from datetime import timedelta
candles = get_zman(friday, candle_text,5,0)
friday_mincha = get_zman(friday, mincha_txt,5,0)
saturday_mincha = get_zman(saturday, mincha_txt,5,0)
havdalah = get_zman(saturday, havdalah_text,5,0)
#saturday_maariv = (datetime.datetime.strptime(havdalah,'%H:%M')- datetime.timedelta(minutes=9)).strftime('%H:%M')
parsha = get_zman(saturday, parsha_text,0,20)
#print(parsha)
#update_minyan_status(FRIDAY_STATUS_RANGE_NAME,values = [['OK']])
#protect_sheet()
print(candles)
print(friday_mincha)
print(saturday_mincha)
print(havdalah)
