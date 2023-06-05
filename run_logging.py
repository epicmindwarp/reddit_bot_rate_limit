import logging
logging.basicConfig(filename='epic_reddit_bot_rate_limit.csv', filemode='a')

import praw
import time
import datetime

#######################################
redditor_name = 'enter your reddit username here'

# Enter bot details here
bot1_username       = ''
bot1_password       = ''
bot1_clientid       = ''
bot1_clientsecret   = ''
bot1_useragent      = f'{bot1_username} - {redditor_name} Bot Rate Limit Count v0.1'

# If you don't have multiple bots, you can remove the next three lines
bot2_username       = ''
bot2_password       = ''
bot2_clientid       = ''
bot2_clientsecret   = ''
bot2_useragent      = f'{bot2_username} - {redditor_name} Bot Rate Limit Count v0.1'
#######################################

# If you have multiple bots, add them in here

# User name, user agent, bot account, last count, rest time
bots = {    0: [bot1_username, bot1_password, bot1_clientid, bot1_clientsecret, bot1_useragent]
        
        # If you don't have a second bot, remove the next line
        ,   1:[bot2_username, bot2_password, bot2_clientid, bot2_clientsecret, bot2_useragent]
        
        # If you have multiple bots, add more lines here to the dictionary
        }

#######################################
#######################################
#######################################

# Time to sleep between runs
sleep_seconds = 60
date_format = '%Y/%m/%d %H:%M:%S'

try:

    # Always add line break at the top, even in new files, to make it easier to recognise restarts
    logging.warning('')

    while True:
        
        for u in range(0, len(bots)):
        
            time_now = datetime.datetime.now().strftime(date_format)
        
            # Login each minute, as the rate limit count doesn't seem to refresh otherwise
            print(f'\nLogging in as {bots[u][0]}...')
            r = praw.Reddit(username       = bots[u][0],
                        password        = bots[u][1],
                        client_id       = bots[u][2],
                        client_secret   = bots[u][3],
                        user_agent      = bots[u][4])

            # Get the username first, as it seems to more consistently get the rate limit this way
            username = r.user.me()
            limits = r.auth.limits

            reset_time = limits['reset_timestamp']
            remaining = limits['remaining']
            used = limits['used'] 

            print(f'Bot: \t\t {username}')
            print(f'Now: \t\t {time_now}')
            print(f'Used: \t\t {used}')
            print(f'Remaining: \t {remaining}')
            if reset_time:
                reset_time = datetime.datetime.fromtimestamp(reset_time).strftime(date_format)
                print(f'Reset: \t\t {reset_time}')

            logging.warning(f',{time_now},{bots[u][0]},{reset_time},{used},{remaining}')
            
            print('#'*60)

        print(f'\nSleeping {sleep_seconds} secs...', end='\r')
        for x in range(0, sleep_seconds):
            time.sleep(1)
        print(' '*30)

except Exception as e:

    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f'\n\t### ({current_time}) Error (sleeping {sleep_seconds} sec)- {e}', end='\n')

    for x in range(0, sleep_seconds):
        time.sleep(1)