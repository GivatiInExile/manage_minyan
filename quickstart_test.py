#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 22:10:17 2019

@author: daniellandesman
"""

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
#from googleapiclient import discovery
#from pprint import pprint
import inspect
import logging
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = 'YOUR SPREADSHEET ID'
#EDIT RANGE FOR TALLY VALUES
SAMPLE_RANGE_NAME = 'Form Responses 1!C45:D45'
#EDIT RANGE TO CLEAR INPUTS AT BEGINNING OF EACH WEEK
ERASE_RANGE_NAME = 'Form Responses 1!C2:D43'

#Use erase range below for testing
#ERASE_RANGE_NAME = 'Form Responses 1!C48:D56'


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
                'credentials.json', SCOPES)
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
    url = f"https://www.ahavathtorah.org/calendar?view=day&cal_date={date}&date_start=specific+date&date_start_date={date}"
    # Get raw html text
    try:
        f = requests.get(url)
    except:
        logging.error('Error getting url\n Function Trace: {} > {}'
                      .format(inspect.stack()[0].function,
                              inspect.stack()[1].function))
    
    raw_text =f.text
    
    # Convert raw HTML to clean sting
    h = html2text.HTML2Text()
    h.ignore_links = True
    clean_text = h.handle(raw_text)
    #text = text
    start_idx = clean_text.find(text)
    zman = clean_text[start_idx-offset_1:start_idx+offset_2].replace("\n","")
    return zman
    
today = datetime.date.today()
friday = today + datetime.timedelta( (4-today.weekday()) % 7 )
saturday = friday + datetime.timedelta(1)
mincha_txt = "p |    |  |\n\nMincha"
candle_text = "p |    |  |\n\nCandle Lighting"
havdalah_text = "p |    |  |\n\nHavdalah"
parsha_text = "Parshat"


candles = get_zman(friday, candle_text,5,0)
friday_mincha = get_zman(friday, mincha_txt,5,0)
saturday_mincha = get_zman(saturday, mincha_txt,5,0)
havdalah = get_zman(saturday, havdalah_text,5,0)
parsha = get_zman(saturday, parsha_text,0,20)
#print(parsha)