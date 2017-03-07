#!/usr/bin/env python2

import pygame
import platform
import time
from pygame.locals import *

fullscreen_on = False

size = 1280,800
width, height = size

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


space_x = 100
space_y = 100

rect_width = width - space_x*2
rect_height = height - space_y*2
rect_xs = space_x
rect_ys = space_y

freq = 10
stimulus = 0
wait_time = 0


if fullscreen_on:
    screen = pygame.display.set_mode(size, FULLSCREEN)
else:
    screen = pygame.display.set_mode(size)

if platform.system() == 'Windows':
   wallclock = time.clock
else:
   wallclock = time.time

pygame.mouse.set_visible(False)


def check_for_escape():
   event = pygame.event.poll()
   if event.type == 0:
       return
   elif event.dict.get('key', -1) == K_ESCAPE:
       pygame.quit()
       exit()

def draw_stimuli():
    screen.fill(black)

    s, x, y = stimulus, rect_xs, rect_ys

    if s == 0:
        col = black
    else:
        col = white

    rect = ((x, y), (rect_width, rect_height))
    screen.fill(col, rect)

    pygame.display.flip()


to_wait = 0

while True:
    t = time.time()
    check_for_escape()

    draw_stimuli()

    
    if wait_time <= 1e-5:
        stimulus = 1 - stimulus
        wait_time = 1.0/freq

    to_wait = 0.005
    time.sleep(to_wait)
    wait_time -= time.time() - t
    

