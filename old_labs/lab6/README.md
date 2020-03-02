# Lab 6: Stress

### Introduction
In this lab, we will record EEG while trying to remember words, as well as later recognizing these same words among others. Hopefully, we'll be able to see the event related potentials corresponding to remembered vs not-remembered words, and possibly recognized vs not recognized words.

### Setup

First, install the libraries:
``` bash
npm install
pip install -r requirements.txt
```

(If you don't have `npm`, you can install by running `brew install node`. You can get `brew` from https://brew.sh/)

### Stimulus Presentation + Recording


- Attach electrodes to participant's head, preferably in visual cortex on the back of the head. 
- Have participant sit in chair in front of monitor
- Connect to the ganglion and stream data: `node ganglion-lsl.js`
- Run lsl-viewer to check connections and stream: `python lsl-viewer.py`
- Record data: `python lsl-record.py`
- Run stress test: `python stroop_test.py medium` (can change "medium" to "hard" or "easy" for more or less stress)


