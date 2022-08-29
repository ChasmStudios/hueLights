# This seems to be a mess, one must work from here. 

from phue import Bridge
import math
import time
import random
import threading
from rgbxy import Converter
import pprint


b = Bridge('192.168.1.15')
print(b.get_api())


# pprint.pp(b.get_light_objects('id'))

b.set_light(7, 'bri', 255, transitiontime=1)
b.set_light(8, 'bri', 255, transitiontime=1)
b.set_light(9, 'bri', 255, transitiontime=1)

high = 255
low = 1



def fadeWave(var1, var2, var3):
    high = 255
    low = 1

    while True:
        var1 = high
        var2 = low
        var3 = low

        if var1 == high:
            var2 = low
            var3 = low
        elif var2 == high:
            var1 = low
            var3 = low
        elif var3 == high:
            var2 = low
            var3 = low


def fade():  # Works for single lights.
    # Current math doesn't allow for factors of three.
    stepUp = 6
    stepDown = -6  # Has to be negative so we can go back numbers.

    global brightness1
    global brightness2
    global brightness3
    brightness1 = 0
    brightness2 = 255
    brightness3 = 0

    while True:
        b.set_light(7, 'bri', 255, transitiontime=1)
        b.set_light(8, 'bri', 0, transitiontime=1)
        b.set_light(9, 'bri', 0, transitiontime=1)

        b.set_light(7, 'bri', 0, transitiontime=1)
        b.set_light(8, 'bri', 255, transitiontime=1)
        b.set_light(9, 'bri', 0, transitiontime=1)

        b.set_light(7, 'bri', 0, transitiontime=1)
        b.set_light(8, 'bri', 0, transitiontime=1)
        b.set_light(9, 'bri', 255, transitiontime=1)


# fade()