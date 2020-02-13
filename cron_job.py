#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 19:49:10 2020

@author: daniellandesman
"""

from crontab import CronTab

my_cron = CronTab(user=True)
for job in my_cron:
    print(job)
    

monday_job = my_cron.new(command='/Users/daniellandesman/Library/Caches/pypoetry/virtualenvs/manage-minyan-LqV_F-sg-py3.7/bin/python /Users/daniellandesman/minyan_poetry/manage_minyan/on_monday.py >> /Users/daniellandesman/minyan_poetry/manage_minyan/log.txt  2>&1')
thursday_job = my_cron.new(command='/Users/daniellandesman/Library/Caches/pypoetry/virtualenvs/manage-minyan-LqV_F-sg-py3.7/bin/python /Users/daniellandesman/minyan_poetry/manage_minyan/on_thursday.py >> /Users/daniellandesman/minyan_poetry/manage_minyan/log.txt  2>&1')
friday_job = my_cron.new(command='/Users/daniellandesman/Library/Caches/pypoetry/virtualenvs/manage-minyan-LqV_F-sg-py3.7/bin/python /Users/daniellandesman/minyan_poetry/manage_minyan/on_friday.py >> /Users/daniellandesman/minyan_poetry/manage_minyan/log.txt  2>&1')
last_call_job = my_cron.new(command='/Users/daniellandesman/Library/Caches/pypoetry/virtualenvs/manage-minyan-LqV_F-sg-py3.7/bin/python /Users/daniellandesman/minyan_poetry/manage_minyan/last_call.py >> /Users/daniellandesman/minyan_poetry/manage_minyan/log.txt  2>&1')


monday_job.dow.on('MON')
monday_job.hour.on(0)
monday_job.minute.on(0)

thursday_job.dow.on('THU')
thursday_job.hour.on(0)
thursday_job.minute.on(0)

friday_job.dow.on('FRI')
friday_job.hour.on(0)
friday_job.minute.on(0)

last_call_job.dow.on('FRI')
last_call_job.hour.on(14)
last_call_job.minute.on(0)

my_cron.write()
