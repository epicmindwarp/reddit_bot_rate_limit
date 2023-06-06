# reddit bot rate limit checker
Checks the rate limit usage of a bot, every minute, and exports to a CSV

# Requirements
- Python (tested on 3.9, should work on 3.6+)
- praw (7.5+)
- Works on windows and linux (DigitalOcean Droplet)

# How to run
1. Download the file `run_logging.py` - no other file is required.
2. Put your reddit username in the redditor_name field (/u/ not required)
3. **If you have just one bot**
    - Update the bot1_username/password/clientid/clientsecret fields
    - If you only have one bot, delete the bot2 section below it
    - Under bots, delete the single line that starts with `, 1:[bot_username...` as this is not required (a python index starts from 0, so the 1 represents bot2)
4. **If you have multiple bots**
    - Add each set of credentials in the same fashion as bot1_username/bot2_.... etc.
    - No additional changes required
5. It will automatically start logging the data to a csv file in the same folder location
    - It will automatically create the csv file if it doesn't exist
    - It will not overwrite any existing data in the csv, always appending from a new line
    - It will always leave a semi-blank line each time you start a run, so you can easily differentiate when you restart the script
    - Opening the file in Excel as a CSV will automatically split the columns
6. The following data is logged
    - Current time (local to your machine)
    - Bot username
    - Rate limit reset time (as provided by reddit)
    - Rate limit used since last reset time
    - Remaining rate limit until next reset time (converted from unix timestamp to local time)
7. The date format is hardcoded to yyyy/mm/dd - all other heathen date formats should be avoided
8. I hate working with dates, times, and time zones, so sorry if the above is somehow wrong
