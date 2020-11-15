#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 20:19:26 2019

@author: daniellandesman
"""
import os
from config import *

subject = "Shabbat {}"

msg_minyan_details = '''
Minyan details for this week:
Candle lighting {}
Mincha Friday: {}
Mincha Shabbat: {}
Maariv Motzei Shabbat: {}
Shabbat Ends: {}

*NOTE: MINYAN IS WEATHER PENDING
''' + MINYAN_ADDR + "\n\n"

msg_signup = DOC + "\n"

msg_signoff = '''
\n P.S. This email is auto-generated. If you notice something wrong, please feel free to reach out.
'''

msg_current_tally = '''
Current Tally:
    Friday: {} 
    Saturday: {}
'''

msg_welcome_default = '''
All, please welcome to Cross Creek
'''

msg_welcome = '''
All, please welcome to Cross Creek
'''

msg_current_tally = '''
Current Tally:
    Friday: {} 
    Saturday: {}
'''

msg_need_ppl_fri = '''
Only need {} more for Friday night.
'''

msg_need_ppl_sat = '''
Only need {} more for Saturday evening. 
'''
msg_post_script = '''
P.S. This email is auto-generated. If you notice something wrong, please feel
free to reach out.
'''
msg_post_script_monday = '''
-ShulPresidente
'''
msg_post_script_thursday = '''
ShulPresidente
'''
msg_post_script_friday = '''
- ShulPresidente
'''
msg_post_script_lastcall = '''
-Shul Presidente
'''

msg_fri_minyan_confirmed = '''
All,

We are on for Friday night.
Please try an arrive on time if you signed up.
'''

msg_sat_minyan_confirmed = '''
We are on for Saturday evening
'''
msg_both_confirmed = '''
We are on for both!
'''

msg_fri_nogo = '''
Friday night is a no go. We'll try again next week.
'''

msg_sat_nogo = '''
Saturday evening is a no go.
'''
msg_both_nogo = '''
Minyan is a no go this week. We'll try again next week.
'''

msg_will_confirm = '''
Cutoff to confirm minyan is Friday at 4PM.
'''