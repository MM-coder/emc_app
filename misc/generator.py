# generator.py made by Mauro M.

# Made as part of the 9ºB app for emc
# Intended to generate a .json timetable file for use with the app

# This code is protected and released to the public under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) License 
# wich can be viewed on the Creative Commons website (https://creativecommons.org/licenses/by-nc-nd/4.0/).
# Any faliure to comply with the terms stipulated in the license will be met with swift legal action 
# by the Creator.

import json

with open('timetable.json', 'w+') as f:
    # Uses a template for standardized lessons @ emc
    one = {"name": "", "day": "", "start": 9, "finish": 10.30}
    two = {"name": "break", "day": "", "start": 10.30, "finish": 10.50}
    three = {"name": "", "day": "", "start": 10.50, "finish": 11.50}
    four = {"name": "", "day": "", "start": 11.50, "finish": 12.50}
    five = {"name": "lunch", "day": "", "start": 11.50, "finish": 12.50}
    six = {"name": "", "day": "", "start": 14, "finish": 15}
    seven = {"name": "", "day": "", "start": 15.5, "finish": 16.30}
    subjects = []
    do = True
    while do == True:
        for x in range(5):
            week = str(input("Week name? "))
            one_name = str(input("Name for 1 hour "))
            print("Break")
            three_name = str(input("Name for 3 hour "))
            four_name = str(input("Name for 4 hour "))
            print("Lunch")
            six_name = str(input("Name for 6 hour "))
            seven_name = str(input("Name for 7 hour "))
            one = {"name": one_name, "day": week, "start": 9, "finish": 10.30}
            two = {"name": "break", "day": week, "start": 10.30, "finish": 10.50}
            three = {"name": three_name, "day": week, "start": 10.50, "finish": 11.50}
            four = {"name": four_name, "day": week, "start": 11.50, "finish": 12.50}
            five = {"name": "lunch", "day": week, "start": 11.50, "finish": 12.50}
            six = {"name": six_name, "day": week, "start": 14, "finish": 15}
            seven = {"name": seven_name, "day": week, "start": 15.5, "finish": 16.30}
            subjects.append(one)
            subjects.append(two)
            subjects.append(three)
            subjects.append(four)
            subjects.append(five)
            subjects.append(six)
            subjects.append(seven)
        do = False # Break when done (A bit of a querk I have)
    # print(len(subjects))
    # print(subjects)
    json.dump(subjects, f, indent=1)