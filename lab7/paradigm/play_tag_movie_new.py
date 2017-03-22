# from kivy.app import App
# from kivy.uix.video import Video
import sys
import time
from pylsl import StreamInfo, StreamOutlet
import subprocess

try:
   input = raw_input
except NameError:
   pass

info = StreamInfo('Ganglion_EEG', 'Markers', 1, 0.0, 'int32',
                  'marker')
outlet = StreamOutlet(info)

if len(sys.argv) != 2:
    print("usage: %s file" % sys.argv[0])
    sys.exit(1)

outlet.push_sample([-1], time.time())
_ = input('\nStart recording and press Enter to start')

outlet.push_sample([1], time.time())
subprocess.run(['mpv',sys.argv[1]])
outlet.push_sample([2], time.time())
