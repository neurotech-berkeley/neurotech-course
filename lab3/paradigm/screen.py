import pygame
from pygame.locals import *
from constants import *

if fullscreen_on:
    screen = pygame.display.set_mode(size, FULLSCREEN)
else:
    screen = pygame.display.set_mode(size)
