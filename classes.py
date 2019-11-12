# classes.py made by Mauro M.

# Made as part of the 9ºB app for emc
# Provides a series of helper functions to work with the dictionary-like class objects

# This code is protected and released to the public under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) License 
# wich can be viewed on the Creative Commons website (https://creativecommons.org/licenses/by-nc-nd/4.0/).
# Any faliure to comply with the terms stipulated in the license will be met with swift legal action 
# by the Creator.

def create_readable_class(data: dict):
    usename = ""
    if data['name'] == 'hist':
        usename = "História"
    if data['name'] == 'geog':
        usename = 'Geografia'
    if data['name'] == 'mat':
        usename = 'Matématica'
    if len(data['name']) == 2 or len(data['name']) == 3:
        usename = data['name'].upper()
    else:
        return {"name": data['name'], "day": data['day'], "start": data['start'], "finish": data['finish']}
    return {"name": usename, "day": data['day'], "start": data['start'], "finish": data['finish']}

def create_readable_class_list(data: list):
    for i in data:
        pass