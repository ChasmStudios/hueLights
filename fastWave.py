from phue import Bridge
import time
import pprint

b = Bridge('192.168.1.15')
# pprint.pp(b.get_api())

red = [0.6906, 0.3078]
pink = [0.3078, 0.1224]
blue = [0.1532, 0.0486]
green = [0.2571, 0.6345]

lights = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
light_names = ['Under Counter', 'L3', 'L2', 'L1', 'W1', 'W2', 'TV', 'TV 2', 'W3', 'W4', 'Balcony', 'W5', 'WComputer', 'A1', 'A2', 'A3', 'A4', 'Adrian','A5', 'A6', 'Adrian Lighstrip', 'Hallway2', 'Hallway1', 'Floor', 'Gym4', 'Gym3', 'Gym2', 'Gym1']

def fast_wave():
    while True:
        time.sleep(5)
        for x in light_names:
            b.set_light(x, 'xy', pink, transitiontime=1)
            b.set_light(x, 'xy', red, transitiontime=50)

fast_wave()
