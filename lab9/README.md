# Lab 9: Measuring brain response to different smells

### Introduction
In this lab, we will record the different brain responses to various smells. 

### Setup

First, install the libraries (there are new python dependencies this time!):
``` bash
npm install
pip install -r requirements.txt
```

(If you don't have `npm`, you can install by running `brew install node`. You can get `brew` from https://brew.sh/)

### Stimulus Presentation + Recording

- Attach electrodes to participant's head, 2 on the frontal cortex (on forehead) and 2 on temporal lobe (right above the ears).
- Connect to the ganglion and stream data: `node ganglion-lsl.js`
- Run lsl-viewer to check connections and stream: `python lsl-viewer.py`
- Record data by opening the `record_data.ipynb` notebook

### Analysis

- Open `analyze_data.ipynb` notebook
- Replace the filenames at the beginning with your filenames
- Run it and see the effects!
