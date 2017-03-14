#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from myo_raw import MyoRaw
# from csv_collector_myo import CSVCollector
import pygame
from pygame.locals import *
import random
import time
import sys
import os

fullscreen_on = False

size = width, height = int(2560/2), int(1600/2)

black = (0,0,0)
white = (255, 255, 255)
background_color = white

def stroop(congruent = False, speed=1.0, duration=20):
    """Stroop Test HARD"""
    colors = {"BLUE" : (0,0,225), "GREEN" : (0,100,0), "YELLOW" : (230,212,41),
              "RED" : (255,0,0), "PURPLE" : (160,32,240), "BLACK" : (0,0,0)}

    def newcolor():
        # any color but black or white
        return (random.choice(list(colors.values())))

    def write(msg="Hello", color = (0,100,0)):
        myfont = pygame.font.SysFont("None", 250)
        mytext = myfont.render(msg, True, color)
        mytext = mytext.convert_alpha()
        return mytext

    x = width / 2.0
    y = height / 2.0
    dx = 0
    dy = 0

    background = pygame.Surface((screen.get_width(), screen.get_height()))
    background.fill(background_color) # white
    background = background.convert()
    screen.blit(background, (0,0)) # clean whole screen
    clock = pygame.time.Clock()
    # FPS = 1.5 * speed  # desired framerate in frames per second.
    wait_time = 1.0 / speed

    start = time.time()

    while time.time() - start < duration:
        screen.blit(background, (0,0)) # clean whole screen
        # milliseconds = clock.tick(FPS)  # milliseconds passed since last frame
        # seconds = milliseconds / 1000.0 # seconds passed since last frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        text = random.choice(["RED", "GREEN", "BLUE", "BLACK", "PURPLE"])
        color = (newcolor())
        if congruent:
            color = colors[text]
        textsurface = write(text, color)
        #screen.blit(background, (0,0)) # clean whole screen

        rect = textsurface.get_rect()
        rect.center = (x, y)

        screen.blit(textsurface, rect)
        pygame.display.flip()

        time.sleep(wait_time)
        check_collection()
    # pygame.quit()
    return True


def draw_text(text, center, color=black, size=22, bold=False, background=None,
              left=False):
    # font = pygame.font.Font(font_path, size, bold=bold)
    font = pygame.font.SysFont("None", size, bold=bold)
    if background:
        surface = font.render(text, True, color, background)
    else:
        surface = font.render(text, True, color)

    rect = surface.get_rect()
    rect.center = tuple(center)
    if left:
        rect.left = center[0]

    screen.blit(surface, rect)
    return rect

def text_slide(text, duration=20):
    screen.fill(background_color)
    draw_text(text, (width/2.0, height/2.0), size=250)
    pygame.display.flip()

    start = time.time()
    
    while time.time() - start < duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        time.sleep(0.01)
        check_collection()

    return True

def focus_slide(duration=20):
    return text_slide('+', duration)

fname = '../data/data_stroop_myo_{}.csv'.format(int(time.time()))
if len(sys.argv) >= 2:
    fname = sys.argv[1]

# collector = CSVCollector(fname=fname)
# collector.tag('start')

def check_collection():
    # if collector.time_since_last_sample() > 1.2:
    #     print('detected disconnect!')
    #     print('attempting reconnect')
    #     # collector.stop()
    #     time.sleep(1.5)
    #     # collector.start()
    #     time.sleep(2)
    pass
    
# print("get ready...")
# time.sleep(2)
# collector.start()
# print("a bit more...")
# time.sleep(2)
# print("go!")

pygame.init()

if fullscreen_on:
    screen = pygame.display.set_mode(size, FULLSCREEN)
else:
    screen = pygame.display.set_mode(size)

pygame.mouse.set_visible(False)

# relax, movement
# low, medium, hard
# speed 0.5, 1.0, 2.0

trial_duration = 10
focus_duration = 5
num_repeats = 2

# trial_duration = 2
# focus_duration = 1
# num_repeats = 1

conditions = [
    # ('relax', None, None), ('move', None, None),
    ('low', 1.1, True), ('medium', 1.1, False), ('hard', 1.8, False)
]

conds = conditions * num_repeats
random.shuffle(conds)

for cond_name, speed, congruent in conds:
    # collector.tag('focus')
    x = focus_slide(focus_duration)
    if not x:
        break
    
    if speed is None:
        # collector.tag(cond_name)
        x = text_slide(cond_name, trial_duration)
    else:
        # collector.tag(cond_name)
        x = stroop(congruent, speed, trial_duration)

    # check_collection()
        
    if not x:
        break
    # print(cond_name)
    # time.sleep(1)
    # time.sleep(trial_duration)
# stroop()
# collector.stop()
pygame.quit()
os._exit(0)









