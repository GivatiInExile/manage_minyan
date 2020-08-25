#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 20:19:26 2019

@author: daniellandesman
"""
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")

subject = "Shabbat {}"

msg_minyan_details = '''
Minyan details for this week:
Candle lighting {}
Mincha Friday: {}
Mincha Shabbat: {}
Maariv Motzei Shabbat: {}
Shabbat Ends: {}

*NOTE: NEW LOCATION AND WEATHER PENDING
@ 566 Ridgeland Terrace in the backyard of Mr. & Mrs. Jacobovitz, 
(enter backyard through Cross Creek: https://www.google.com/maps/place/566+Ridgeland+Terrace,+Englewood,+NJ+07631/@40.8717365,-73.9756547,3a,75y,117.56h,75.58t/data=!3m6!1e1!3m4!1sN4GV0EUAbw_Pn1CVTw1qng!2e0!7i16384!8i8192!4m5!3m4!1s0x89c2f6d33c72da43:0x34fb2d9660cb39e9!8m2!3d40.8714797!4d-73.9751746)

Yes, this means minyan bottles are back!\n.
'''
msg_signup = os.getenv("GOOGLE_DOC")

msg_signoff = '''
P.S. This email is auto-generated. If you notice something wrong, please feel free to reach out.
'''

msg_current_tally = '''
Current Tally:
    Friday: {} 
    Saturday: {}
'''

#msg_monday = msg_minyan_details + msg_signup + msg_signoff
#
#msg_thursday = msg_minyan_details + msg_current_tally + msg_signoff
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