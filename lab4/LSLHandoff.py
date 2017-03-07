## code by Alexandre Barachant
## adapted by Pierre Karashchuk for compatibility with Python3

from pylsl import StreamInfo, StreamOutlet
import numpy as np
try:
   input = raw_input
except NameError:
   pass

info = StreamInfo('Ganglion_EEG', 'EEG', 4, 200, 'float32',
                  'Ganglion_123456789')
outlet = StreamOutlet(info)
while True:
    strSample = input().split(': ', 1)
    sample = 1e6*np.array(list(map(float, strSample[1].split(' '))))
    stamp = float(strSample[0])*1e-3
    outlet.push_sample(sample, stamp)
    # print('Pushed Sample At: ' + strSample[0])
