# Automatic color changer. It seems that creating different threads and then trying to kill them really messess up Python. 
# Another thing, it seems there's a lot of glitches involving the changing of lights. 

# If you find an easier way to have various tasks running at the same time that's fast and efficient there should be no issue. 

# If you want to create good color dictionaries work backwards: Choose the color from the Hue App and then get the properties
# by accessing the bridge and obtaining the color codes. 


from phue import Bridge
import time
import random
import threading
from rgbxy import Converter

# Add functionality to discord.
color_dictionary = { 'red' : 'ff0000',
                    'orange' : 'f04c00',
                    'light_orange' : 'f07c00',
                    'brown' : '522100',
                    'neon_pink' : 'DB3EB1',
                    'neon_purple' : 'B026FF',
                    'neon_blue' : '4D4DFF',
                    'neon_orange' : 'FFAD00',
                    'neon_red' : 'D22730',
                    'neon_green' : '44D62C',
                    'grape' : '8031A7',
                    'dark_grape' : '411159',
                    'cherry_red' : '990011FF',
                    'off_white' : 'FCF6F5FF',
                    'pastel_orange' : 'FFA351FF',
                    'peach' : 'FFBE7BFF',
                    'custard' : 'EED971FF',
                    'baby_purple' : 'E663D9',
                    'notbaby_purple' : '8E33A8',
                    'blue' : '1855D9',
                    'dark_purple' : '2D0C46',
                    'baby_blue' : '37A3FD',
                    'gucci_red' : 'D71B0E',
                    'gucci_green' : '00FF00',
                    'gucci_yellow' : 'F29E1F',
                    'dark_blue' : '030056',
                    'dark_blue1' : '10133a',
                    'neon_blue1' : '010b8b',
                    'fire1' : 'e25822',
                    'opaque_yellow' : 'FAC000',
                    'orange1' : 'FF7500',
                    'dark_orange' : 'B62203',
                    'dark_red' : '801100',
                    'red1' : 'a60000',
                    'red2' : 'e20000',
                    'red3' : 'cb0000',
                    'pastel_red' : 'ff5b5b',
                    'dessert1' : 'ff9c2e',
                    'dessert2' : 'fc8500',
                    'dessert3' : 'cc6b00',
                    'dessert4' : '9b5100',
                    'mil1' : 'E3826F',
                    'mil2' : 'E4A9A4',
                    'mil3' : 'EFBA97',
                    'mil4' : 'F1CCBB',
                    'mil5' :'E7D5C7'}

# Presets
presets = { 'hawaii' : {'time_slept1': 3,
          'time_slept2': 4,
          'trans_time': 25,
          'colors': [color_dictionary['neon_pink'],
                     color_dictionary['baby_purple'],
                     color_dictionary['blue'],
                     color_dictionary['neon_purple']]},  # Short and smooth.
            'neon_wild' : {'time_slept1': 2,
                      'time_slept2': 2,
                      'trans_time': 10,
                      'colors': [color_dictionary['neon_pink'],
                                 color_dictionary['neon_purple'],
                                 color_dictionary['neon_blue'],
                                 color_dictionary['neon_red']]},  # Too much attention.
            'gucci' : {'time_slept1': 15,
                      'time_slept2': 20,
                      'trans_time': 1,
                      'colors': [color_dictionary['gucci_red'],
                                 color_dictionary['gucci_yellow'],
                                 color_dictionary['gucci_green']]} , # Long, but assertive.
            'oceans' : {'time_slept1': 6,
                      'time_slept2': 8,
                      'trans_time': 50,
                      'colors': [color_dictionary['neon_blue'],
                                 color_dictionary['neon_blue1'],
                                 color_dictionary['dark_blue'],
                                 color_dictionary['dark_blue1']]} , # Fast and smooth.
            'fire' : {'time_slept1': 2,
                      'time_slept2': 5,
                      'trans_time': 50,
                      'colors': [color_dictionary['neon_orange'],
                                 color_dictionary['fire1'],
                                 color_dictionary['orange'],
                                 color_dictionary['orange1'],
                                 color_dictionary['dark_orange'],
                                 color_dictionary['dark_red']]} , # Short and smooth.
            'sred' : {'time_slept1': 7,
                      'time_slept2': 10,
                      'trans_time': 35,
                      'colors': [color_dictionary['neon_red'],
                                 color_dictionary['dark_red'],
                                 color_dictionary['red1'],
                                 color_dictionary['red2'],
                                 color_dictionary['red3'],
                                 color_dictionary['pastel_red']]} , # Smoothhh.
            'tokyo_adv' : {'time_slept1': 16,
                      'time_slept2': 13,
                      'trans_time': 1,
                      'colors': [color_dictionary['neon_pink'],
                                 color_dictionary['neon_orange'],
                                 color_dictionary['neon_blue'],
                                 color_dictionary['neon_purple']]},  # Strong but slow.
            'desert' : {'time_slept1': 3,
                      'time_slept2': 2,
                      'trans_time': 25,
                      'colors': [color_dictionary['dessert1'],
                                 color_dictionary['dessert2'],
                                 color_dictionary['dessert4'],
                                 color_dictionary['dessert3']]} , # Strong but slow.
            'purple' : {'time_slept1': 3,
                      'time_slept2': 2,
                      'trans_time': 10,
                      'colors': [color_dictionary['notbaby_purple'],
                                 color_dictionary['neon_purple'],
                                 color_dictionary['grape'],
                                 color_dictionary['dark_grape']]}, # Strong but slow.
            'party' : {'time_slept1': 1,
                      'time_slept2': 1,
                      'trans_time': 1,
                      'colors': [color_dictionary['neon_pink'],
                                 color_dictionary['neon_purple'],
                                 color_dictionary['neon_blue'],
                                 color_dictionary['neon_orange']]}, # Strong but slow.
            'peach1' : {'time_slept1': 7,
                      'time_slept2': 3,
                      'trans_time': 50,
                      'colors': [color_dictionary['mil1'],
                                 color_dictionary['mil2'],
                                 color_dictionary['mil3'],
                                 color_dictionary['mil4'],
                                 color_dictionary['mil5']]} # Aesthetically pleasing.
}


insert_preset_here = presets['tokyo_adv']
print(f'The following preset will be used {insert_preset_here}')


def convert(x_list):
    conversion = []
    for x in x_list:
        converter = Converter()
        xy = converter.hex_to_xy(x)
        conversion.append(tuple(xy))
    return conversion

def append_dict(xdict):
    normal_colors = xdict['colors']
    xdict['conv_colors'] = convert(normal_colors)
    return xdict

b = Bridge('192.168.1.15')

def run1(main_dict):
    print(f'Running the colors {main_dict["colors"]}')
    time_slept = main_dict['time_slept1']
    time_slept2 = main_dict['time_slept2']
    trans_time = main_dict['trans_time']
    lighting_default = main_dict['conv_colors']

    def light3():
        while True:
            b.set_light(3, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept)

    def light4():
        while True:
            b.set_light(4, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept2)

    def light10():
        while True:
            b.set_light(10, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept)

    def light12():
        while True:
            b.set_light(12, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept2)

    def light14():
        while True:
            b.set_light(14, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept)

    def light11():
        while True:
            b.set_light(11, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept2)

    def light6():
        while True:
            b.set_light(6, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept)

    def light5():
        while True:
            b.set_light(5, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept2)

    def light13():
        while True:
            b.set_light(13, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept)

    def light1():
        while True:
            b.set_light(1, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept2)

    def light2():
        while True:
            b.set_light(2, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept)

    def light7():
        while True:
            b.set_light(7, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept2)

    def light8():
        while True:
            b.set_light(8, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept)

    def light9():
        while True:
            b.set_light(9, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept2)

    def light16():
        while True:
            b.set_light(16, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept)

    def light19():
        while True:
            b.set_light(19, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept2)

    def light17():
        while True:
            b.set_light(17, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept)

    def light18():
        while True:
            b.set_light(18, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept2)

    def light20():
        while True:
            b.set_light(20, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept)

    def light21():
        while True:
            b.set_light(21, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept2)

    def light22():
        while True:
            b.set_light(22, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept)

    def light23():
        while True:
            b.set_light(23, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept2)

    def light24():
        while True:
            b.set_light(24, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept)

    def light25():
        while True:
            b.set_light(25, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept2)

    def light26():
        while True:
            b.set_light(26, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept)

    def light29():
        while True:
            b.set_light(29, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept2)

    def light28():
        while True:
            b.set_light(28, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept)

    def light27():
        while True:
            b.set_light(27, 'xy', random.sample(lighting_default, k=1)[0], transitiontime=trans_time)
            time.sleep(time_slept2)


    p1 = threading.Thread(target=light1)
    p2 = threading.Thread(target=light2)
    p3 = threading.Thread(target=light3)
    p4 = threading.Thread(target=light4)
    p5 = threading.Thread(target=light5)
    p6 = threading.Thread(target=light6)
    p7 = threading.Thread(target=light7)
    p8 = threading.Thread(target=light8)
    p9 = threading.Thread(target=light9)
    p10 = threading.Thread(target=light10)
    p11 = threading.Thread(target=light11)
    p12 = threading.Thread(target=light12)
    p13 = threading.Thread(target=light13)
    p14 = threading.Thread(target=light14)

    p16 = threading.Thread(target=light16)
    p17 = threading.Thread(target=light17)
    p18 = threading.Thread(target=light18)
    p19 = threading.Thread(target=light19)
    p20 = threading.Thread(target=light20)
    p21 = threading.Thread(target=light21)
    p22 = threading.Thread(target=light22)
    p23 = threading.Thread(target=light23)
    p24 = threading.Thread(target=light24)
    p25 = threading.Thread(target=light25)
    p26 = threading.Thread(target=light26)
    p27 = threading.Thread(target=light27)
    p28 = threading.Thread(target=light28)
    p29 = threading.Thread(target=light29)


    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
    p11.start()
    p12.start()
    p13.start()
    p14.start()

    p16.start()
    p17.start()
    p18.start()
    p19.start()
    p20.start()
    p21.start()
    p22.start()
    p23.start()
    p24.start()
    p25.start()
    p26.start()
    p27.start()
    p28.start()
    p29.start()

run1(append_dict(insert_preset_here))