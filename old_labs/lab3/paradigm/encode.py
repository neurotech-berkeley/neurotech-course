import pygame
from pygame.locals import *
from constants import *
import time
from extract_words import get_words
import pandas as pd
from pylsl import StreamInfo, StreamOutlet

pygame.init()
#pygame.mouse.set_visible(False)

from screen import screen
from drawstuff import *

study_time = int(time.time())
print(study_time)

word_fname = '../data/words_latest.csv'.format(study_time)

words = get_words()
words.to_csv(word_fname)

info = StreamInfo('Ganglion_EEG', 'Markers', 1, 0.0, 'int32',
                  'marker')
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
while not check_for_key(K_SPACE):
    pass

focus_slide()
outlet.push_sample([-1], time.time())
time.sleep(0.5)

for i in xrange(words.shape[0]):
    d = dict(words.ix[i])

    if d['is_shown'] != 1:
        continue

    word = d['word']

    simple_slide(word)
    outlet.push_sample([d['id']], time.time())
    time.sleep(2.0)

    if check_for_escape():
        finish_stuff(early=True)
        exit()

    focus_slide()
    outlet.push_sample([-1], time.time())
    time.sleep(0.5)

    if check_for_escape():
        finish_stuff(early=True)
        exit()
