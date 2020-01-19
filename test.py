#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:30:21 2020

@author: daniellandesman
"""

print ("TEST")

import sys
sys.stdout.write("Hello")

import datetime
 
with open('dateInfo.txt','a') as outFile:
    outFile.write('\n' + str(datetime.datetime.now()))