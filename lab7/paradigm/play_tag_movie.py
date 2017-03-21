from kivy.app import App
from kivy.uix.video import Video
import sys
import time
from pylsl import StreamInfo, StreamOutlet
try:
   input = raw_input
except NameError:
   pass

info = StreamInfo('Ganglion_EEG', 'Markers', 1, 0.0, 'int32',
                  'marker')
outlet = StreamOutlet(info)

outlet.push_sample([-1], time.time())
_ = input('\nStart recording and press Enter to start')

if len(sys.argv) != 2:
    print("usage: %s file" % sys.argv[0])
    sys.exit(1)

class VideoApp(App):
    def build(self):
        self.v = Video(source=sys.argv[1], state='play')
        self.v.bind(state=self.update_state)
        return self.v

    def update_state(self, *args):
        if self.v.state == 'stop':
            outlet.push_sample([2], time.time())
            exit()

outlet.push_sample([1], time.time())            
VideoApp().run()
