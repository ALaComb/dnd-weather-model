import math
from random import randint
import json


with open('./weather-config.json','r') as infile:
    config = json.load(infile)

def plaintext_days(day):
    year = config["general"]["year"]
    week = config["general"]["year"]

    years = day//year
    weeks = (day%year)//week
    days = (day%year)%week

    plaintext = ''
    if years:
        plaintext += f'{years} years'
    if years and (weeks or days):
        plaintext += ', '
    if weeks:
        plaintext += f'{weeks} weeks'
    if weeks and days:
        plaintext += ', '
    if days:
        plaintext += f'{days} days'
    plaintext += f' ({day} days)'
    return plaintext


def gen_fire_weather(day):
    data = {}

    period = config["fire"]["period"]

    data["scale"] = 0 # COS math
    data["range"] = config["fire"]["max_effect"] - config["fire"]["min_effect"]
    data["coterm"] = {}
    data["coterm"]["since"] = day%period
    data["coterm"]["until"] = period - data["coterm"]["since"]




    return 