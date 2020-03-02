# Lab 3: Event Related Potentials

### Introduction
In this lab, we will record EEG while trying to remember words, as well as later recognizing these same words among others. Hopefully, we'll be able to see the event related potentials corresponding to remembered vs not-remembered words, and possibly recognized vs not recognized words.

### Setup

First, install the libraries:
```
npm install
pip install -r requirements.txt
```

(If you don't have `npm`, you can install by running `brew install node`. You can get `brew` from https://brew.sh/)

### Stimulus Presentation + Recording


- Attach Ganglion to participant's head.
- Record positions of EEG according to 10-20 system.
- Have participant sit in chair in front of monitor
- Connect to the ganglion and stream data: `node ganglion-lsl.js`
- Run lsl-viewer to check connections and stream: `python lsl-viewer.py`
- Start presentation list of words: `cd paradigm; python encode.py`
- Start recording data (in separate terminal): `python lsl-record.py` 
- Press space to start presentation
- Finally, start recall Procedure: `cd paradigm; python recognize.py ../data/words_latest.csv`