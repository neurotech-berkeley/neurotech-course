from pylsl import StreamInfo, StreamOutlet
import numpy as np
import time
info = StreamInfo('Ganglion_EEG', 'Markers', 1, 0.0, 'int32',
                  'marker')
outlet = StreamOutlet(info)
count = 0
while True:
    print(count)
    stamp = time.time()
    outlet.push_sample([count], stamp)
    outlet.push_sample([count], stamp)
    count += 1
    time.sleep(0.1)
    # print('Pushed Sample At: ' + strSample[0])
