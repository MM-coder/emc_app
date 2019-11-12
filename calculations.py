# calcuations.py made by Mauro M.

# Made as part of the 9ºB app for emc
# Provides a series of helper datetime calculation functions

# This code is protected and released to the public under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) License 
# wich can be viewed on the Creative Commons website (https://creativecommons.org/licenses/by-nc-nd/4.0/).
# Any faliure to comply with the terms stipulated in the license will be met with swift legal action 
# by the Creator.


import datetime, json


current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day
current_min = datetime.datetime.now().minute
current_hour = datetime.datetime.now().hour

dummy_object = datetime.datetime(current_year, current_month, 11, 10, 50)

dummy_min = dummy_object.minute
dummy_hour = dummy_object.hour

def next_weekday(d: datetime.datetime, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

def get_weekday(day: str):
    if day.upper == "monday":
        return 1
    if day.upper == "tuesday":
        return 2
    if day.upper == "wednesday":
        return 3
    if day.upper == "thursday":
        return 4
    if day.upper == "friday":
        return 5
    else:
        return 0

def get_day_timetable(day: str):
    with open('timetable.json', 'r', encoding='utf-8') as f:
        day_timetable = []
        data = json.load(f)
        for x in data['subjects']:
            if x['day'] == day:
                day_timetable.append(x)
            else:
                pass
        return day_timetable

def get_closest_class(day: list):
    formatted_time = float(str(dummy_hour) + '.' + str(dummy_min))
    for x in day:
        if x['start'] >= formatted_time and get_weekday(str(x['day'])) == dummy_object.weekday():
            return x
            break
        else:
            pass

def return_readable_time(time):
    if type(time) == float:
        if time <= 12.00:
            work = str(time).replace('.', ':')
            check =  work + '0' + ' AM'
        else:
            work = str(time).replace('.', ':')
            check =  work + '0' + ' PM'
        return check
    else:
        if time <= 12:
            work = str(time).replace('.', ':') + ' AM'
        else:
            work = str(time).replace('.', ':') + ' PM'
        return work
