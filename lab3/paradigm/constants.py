#!/usr/bin/env python2

import platform
import time

fullscreen_on = False

size = 1280, 800
SCREEN_WIDTH, SCREEN_HEIGHT = size

white = 255,255,255
black = 0,0,0
red = 255,0,0
green = 0,255,0
blue = 0,0,255
chartreuse = 127,255,0
light_green = 131,255,100
nice_red = 207,45,64
sky_blue = 100,244,255
nice_blue = 0,194,255
dark_gray = 20,20,20

anna_blue = 79,129,189
anna_green = 0,128,0
anna_gray = 146,146,146
anna_grayblue = 45,74,108

background_color = black

if platform.system() == 'Windows':
   wallclock = time.clock
else:
   wallclock = time.time


