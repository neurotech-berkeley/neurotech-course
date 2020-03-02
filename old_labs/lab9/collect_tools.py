#!/usr/bin/env python

import numpy as np
import pandas as pd
from time import time, strftime, gmtime
from pylsl import StreamInlet, resolve_byprop

def get_channel_names(inlet):
    """Get channel names for an LSL inlet"""
    info = inlet.info()
    description = info.desc()

    freq = info.nominal_srate()
    Nchan = info.channel_count()

    ch = description.child('channels').first_child()
    ch_names = [ch.child_value('label')]
    for i in range(1, Nchan):
        ch = ch.next_sibling()
        ch_names.append(ch.child_value('label'))
        
    if np.all(np.array(ch_names) == ""):
        ch_names = ['C{}'.format(x) for x in range(1,len(ch_names)+1)]
        
    return ch_names


def collect_eeg(inlet, duration=10, tag=None):
    """Collect EEG data from stream.
    Returns a pandas object with the data
    
    Arguments:
    duration -- length of recording in seconds.
    tag -- optionally tag the data
    """
    
    ### ignore any data stored
    data = [0]
    while len(data) != 0:
        data, timestamp = inlet.pull_chunk(max_samples=1024)
    
    res = []
    timestamps = []

    t_init = time()
    print('Start recording at time t={:.3f}'.format(t_init))
    last = t_init
    while (last - t_init) < duration:
        try:
            data, timestamp = inlet.pull_chunk(timeout=1.0,
                                               max_samples=24)
            if timestamp:
                res.append(data)
                timestamps.extend(timestamp)
                last = timestamp[-1]

        except KeyboardInterrupt:
            break
    t_done = time()
    print('Finished recording at time {:.3f} ({:.3f} seconds)'.format(t_done, t_done - t_init))
    
    res = np.concatenate(res, axis=0)
    timestamps = np.array(timestamps)
    
    res = np.c_[timestamps, res]
    ch_names = get_channel_names(inlet)

    columns = ['timestamps'] + ch_names
    if tag is not None:
        columns += ['tag']
        tagc = np.repeat(tag, res.shape[0])[:, np.newaxis]
        res = np.hstack([res, tagc])
    
    data = pd.DataFrame(data=res, columns=columns)

    
    
    return data
