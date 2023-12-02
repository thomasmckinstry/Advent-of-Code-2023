# get_input.py

# Advent of Code

# This file grabs the input file of the day and places it in a marked folder with a template file

from urllib import request
import requests
import pytz
from datetime import datetime
import time
import os
from io import TextIOWrapper
import shutil

"""
Returns current day and time.
"""
def get_date():
    curr_time = datetime.now(pytz.timezone('EST'))
    year = curr_time.year
    month = curr_time.month
    day = curr_time.day

    if (month == 12 and day <= 25):
        return str(year), str(day)
    
    print("It's not time yet.")

"""
Sets up directories for current day, and any previous days that aren't already set.
"""
def set_directories(year, day, cookie):
    #print("DEBUG set_directories(", year, day,")")
    files = os.listdir()
    for i in range(1, int(day) + 1):
        str_i = str(i)
        if (not files.count("Day " + str_i)):
            os.mkdir("Day " + str_i)
            shutil.copy("python-draft.py", "./Day " + str_i + "/day" + str_i + " - solution.py")
            get_input(year, str_i, cookie)

"""
Makes a get request to Advent of Code with my cookie to get my input file
"""
def get_input(year, day, cookie):
    file = requests.get("https://adventofcode.com/" + year + "/day/" + day + "/input", cookies=cookie)
    with open ("./Day " + day + "/day" + day + " - input.txt", "x") as write_file:
        write_file.write(file.text)

"""
Gets my cookie from my environment variables
"""
def get_cookie():
    session = str(os.environ.get("AOC_SESSION"))
    cookies = {'session' : session}
    return cookies


year_day = get_date()
cookies = get_cookie()
#print("DEBUG cookie ->", type(cookies))
set_directories(year_day[0], year_day[1], cookies)