# -*- coding: utf-8 -*-

# menu.py made by Mauro M.

# Made as part of the 9ºB app for emc
# Intended to generate a .json menu file for use with the app, requires a converted csv file

# This code is protected and released to the public under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) License 
# wich can be viewed on the Creative Commons website (https://creativecommons.org/licenses/by-nc-nd/4.0/).
# Any faliure to comply with the terms stipulated in the license will be met with swift legal action 
# by the Creator.

import csv

def delete_empty(data: list):
    for i in data:
        if i == "":
            data.remove(i)
        else:
            pass
    return data


with open('ementas.csv', newline='', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar=' ')
    last_row = next(reader)
    for row in reader:
        if len(delete_empty(row)) == 1:
            if row[0] in ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Feriado']:
                pass
            else:
                print(last_row[0] + ': ' + row[0])
                last_row = row
        else:
            print(row[0].replace(' ', '') + ': ' + row[1])