from pylsl import StreamInfo, StreamOutlet
import numpy as np
info = StreamInfo('Ganglion_EEG', 'EEG', 4, 200, 'float32',
                  'Ganglion_123456789')
outlet = StreamOutlet(info)
while True:
    strSample = raw_input().split(': ', 1)
    sample = 1e6*np.array(map(float, strSample[1].split(' ')))
    stamp = float(strSample[0])*1e-3
    outlet.push_sample(sample, stamp)
    # print('Pushed Sample At: ' + strSample[0])
