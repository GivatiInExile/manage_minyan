#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 19:49:10 2020

@author: daniellandesman
"""

from crontab import CronTab

#my_cron = CronTab(user='daniellandesman')
my_cron = CronTab(user = 'daniellandesman')
for job in my_cron:
    print(job)
    
#job = my_cron.new(command='/Applications/anaconda3/bin/python /Users/daniellandesman/Documents/Python_scripts/personal/manage_minyan/on_monday.py')
job = my_cron.new(command = 'python test.py')
#job.dow.on('SUN')
#job.hour.also.on(20)
#job.minute.also.on(19)
job.minute.every(1)
my_cron.write()