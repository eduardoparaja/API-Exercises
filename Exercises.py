# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 19:48:09 2018

@author: edup_
"""

import requests

lyrics = requests.get("https://api.lyrics.ovh/v1/Black Sabbath/Paranoid").json()

print(lyrics)

#%%

ISS_location = requests.get("http://api.open-notify.org/iss-now.json").json()

print("These are the coordinates of the ISS: " + str(ISS_location["iss_position"]))

#%%
from itertools import islice

Countries = requests.get("http://api.population.io:80/1.0/countries").json()

def get_all_countries():
    for country in Countries["countries"]:
        print(country)

def get_first_10_countries():    
    iterator = islice(Countries["countries"], 10)

    for country in iterator:
        print(country)

def get_country_population():
    population = requests.get("http://api.population.io:80/1.0/population/Spain/today-and-tomorrow/").json()
    return population["total_population"]                        