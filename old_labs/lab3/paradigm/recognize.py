#!/usr/bin/env python2

import pygame
from pygame.locals import *
from constants import *
import time
from extract_words import get_words
import pandas as pd
import sys
from pylsl import StreamInfo, StreamOutlet


pygame.init()
#pygame.mouse.set_visible(False)

from screen import screen
from drawstuff import *

words_fname = sys.argv[1].replace('.csv', '_labeled.csv')

words = pd.read_csv(sys.argv[1])
words['recognized'] = 'null'

def wait_for_keys(keys, escape=True):
    pygame.event.clear()
    while True:
        event=pygame.event.wait()
        if(event.type == KEYDOWN):
            if event.key in keys or \
               (escape and event.key == K_ESCAPE):
                return event.key

def check_for_escape():
    while True:
        event = pygame.event.poll()
        if event.type == 0:
            return False
        elif event.dict.get('key', -1) == K_ESCAPE:
            return True

def finish_stuff(early=False):
    return

info = StreamInfo('Ganglion_EEG', 'Markers', 1, 0.0, 'int32', 'marker')
outlet = StreamOutlet(info)


def check_for_key(key=K_ESCAPE):
    while True:
        event = pygame.event.poll()
        if event.type == 0:
            return False
        elif event.dict.get('key', -1) == key:
            return True

def check_for_escape():
    return check_for_key(K_ESCAPE)

def finish_stuff(early=False):
    return

text_slide("""Start recording and
press space to continue""")  
wait_for_keys([K_SPACE])

for i in xrange(words.shape[0]):
    d = dict(words.ix[i])

    word = d['word']

    recognize_slide(word)
    outlet.push_sample([d['id']], time.time())

    key = wait_for_keys([K_1, K_4])
    if key == K_ESCAPE:
        finish_stuff(early=True)
        exit()

    labeled = key == K_4

    words.ix[i, 'recognized'] = labeled
    words.to_csv(words_fname)

    focus_slide()
    outlet.push_sample([-1], time.time())
    time.sleep(0.5)

simple_slide("END OF EXPERIMENT")
exit()
