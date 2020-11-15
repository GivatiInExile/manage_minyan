#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 19:34:52 2019

@author: daniellandesman
"""

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
#load_dotenv(dotenv_path=".env")

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("GMAIL_PASSWORD")
RECIPIENT = os.getenv("RECIPIENT") #Email or group
DOC = os.getenv("GOOGLE_DOC")
SECRET_FILE = os.getenv("SECRET_FILE")
MINYAN_ADDR = os.getenv("MINYAN_ADDR")
SPREADSHEET_ID = os.getenv("SAMPLE_SPREADSHEET_ID")
YAML_ADDR = os.getenv("YAML_ADDR")

#for debugging and ensuring test recipient not set
print(RECIPIENT)

