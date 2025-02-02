"""
Переделать программу с погодой так что бы она 
запрашивала город а в ответ выдавала подробную информацию 
о погоде в этом городе в красивом формате.
"""

import pyowm
from pprint import pprint

owm = pyowm.OWM('f7ab670dd123e8e33a8296b1d5ebf253')
mgr = owm.weather_manager()

city = input('Введите название города: ')
obs = mgr.weather_at_place(city)
w = obs.to_dict()["weather"]

pprint(w, width=40, indent=2)