#!/usr/bin/env python
## code by Alexandre Barachant
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
from time import time, sleep
from pylsl import StreamInlet, resolve_byprop
import seaborn as sns
from threading import Thread
from scipy import signal

sns.set(style="whitegrid")

from optparse import OptionParser

parser = OptionParser()

parser.add_option("-w", "--window",
                  dest="window", type='float', default=0.5,
                  help="window lenght to display in seconds.")
parser.add_option("-s", "--scale",
                  dest="scale", type='float', default=100,
                  help="scale in uV")
parser.add_option("-r", "--refresh",
                  dest="refresh", type='float', default=0.2,
                  help="refresh rate in seconds.")
parser.add_option("-f", "--figure",
                  dest="figure", type='string', default="15x6",
                  help="window size.")

filt = True
subsample = 2
buf = 12

(options, args) = parser.parse_args()

window = options.window
scale = options.scale
figsize = np.int16(options.figure.split('x'))
refresh = options.refresh

decrease_fs = [4, 8]
increase_fs = [12, 20]


print("looking for an EEG stream...")
streams = resolve_byprop('type', 'EEG', timeout=2)

if len(streams) == 0:
    raise(RuntimeError("Cant find EEG stream"))
print("Start aquiring data")


class LSLViewer():
    def __init__(self, stream, fig, axes,  window, scale, dejitter=True):
        """Init"""
        self.stream = stream
        self.window = window
        self.scale = scale
        self.dejitter = dejitter
        self.inlet = StreamInlet(stream, max_chunklen=buf)
        self.filt = True
        info = self.inlet.info()
        description = info.desc()

        self.sfreq = info.nominal_srate()
        self.n_samples = int(self.sfreq * self.window)
        self.n_chan = info.channel_count()

        ch = description.child('channels').first_child()
        ch_names = [ch.child_value('label')]

        for i in range(self.n_chan):
            ch = ch.next_sibling()
            ch_names.append(ch.child_value('label'))

        self.ch_names = ch_names

        fig.canvas.mpl_connect('key_press_event', self.OnKeypress)
        fig.canvas.mpl_connect('button_press_event', self.onclick)

        self.fig = fig
        self.axes = axes


        sns.despine(left=True)

        self.data = np.zeros((self.n_samples, self.n_chan))
        self.times = np.arange(-self.window, 0, 1./self.sfreq)
        impedances = np.std(self.data, axis=0)
        lines = []

        self.rects = axes.bar(0, 1)

        # self.text = axes.

        axes.xaxis.grid(False)
        axes.set_xticks([])
        self.value = None

        self.display_every = int(refresh / (12/self.sfreq))

        self.bf1, self.af1 = butter(4, np.array(decrease_fs)/(self.sfreq/2.),
                                  'bandpass')
        self.bf2, self.af2 = butter(4, np.array(increase_fs)/(self.sfreq/2.),
                                  'bandpass')

        self.low = 10000
        self.high = 0

    def compute_value(self):
        data_f1 = filtfilt(self.bf1, self.af1, self.data, axis=0)
        data_f2 = filtfilt(self.bf2, self.af2, self.data, axis=0)

        v1 = np.sqrt(np.sum(np.square(data_f1)))
        v2 = np.sqrt(np.sum(np.square(data_f2)))

        return v2 / v1


    def update_plot(self):
        value = self.compute_value()

        if self.value is None:
            self.value = value

        self.value = 0.8 * self.value + 0.2 * value

        self.low = min(self.low, self.value)
        self.high = max(self.high, self.value)

        rect = self.rects.get_children()[0]
        rect.set_height(self.value)

        self.axes.set_ylim([self.low, self.high])
        self.fig.canvas.draw()
        plt.pause(0.01)


    def update_data_and_plot(self):
        k = 0
        while self.started:
            samples, timestamps = self.inlet.pull_chunk(timeout=1.0,
                                                        max_samples=buf)

            if timestamps:
                self.data = np.vstack([self.data, samples])
                if self.dejitter:
                    timestamps = np.float64(np.arange(len(timestamps)))
                    timestamps /= self.sfreq
                    timestamps += self.times[-1] + 1./self.sfreq
                self.times = np.concatenate([self.times, timestamps])

                self.n_samples = int(self.sfreq * self.window)
                self.data = self.data[-self.n_samples:]
                self.times = self.times[-self.n_samples:]


                k += 1

                if k >= self.display_every:
                    self.update_plot()
                    k = 0
            else:
                sleep(0.1)

    def onclick(self, event):
        print((event.button, event.x, event.y, event.xdata, event.ydata))

    def OnKeypress(self, event):
        if event.key == 'r':
            self.low = 10000
            self.high = 0
        elif event.key == '+':
            self.window += 1
        elif event.key == '-':
            if self.window > 1:
                self.window -= 1
        elif event.key == 'd':
            self.filt = not(self.filt)

    def start(self):
        self.started = True
        self.thread = Thread(target=self.update_data_and_plot)
        self.thread.daemon = True
        self.thread.start()

    def stop(self):
        self.started = False


fig, axes = plt.subplots(1, 1, figsize=figsize, sharex=True)
lslv = LSLViewer(streams[0], fig, axes, window, scale)

help_str = """
            reset scale: r
            increase time scale : -
            decrease time scale : +
           """
print(help_str)
lslv.start()

plt.show()
lslv.stop()
