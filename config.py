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
doc = os.getenv("GOOGLE_DOC")

#for debugging and ensuring test recipient not set
print(RECIPIENT)

