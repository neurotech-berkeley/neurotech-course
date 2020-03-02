from kivy.app import App
from kivy.uix.video import Video
import sys
import time

if len(sys.argv) != 2:
    print("usage: %s file" % sys.argv[0])
    sys.exit(1)

class VideoApp(App):
    def build(self):
        self.v = Video(source=sys.argv[1], state='play')
        self.v.bind(state=self.replay)
        return self.v

    def replay(self, *args):
        if self.v.state == 'stop':
            self.v.state = 'stop'
            time.sleep(1)
            exit()

VideoApp().run()
