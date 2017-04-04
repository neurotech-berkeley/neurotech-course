# Lab 4: Neurofeedback

### Introduction
In this lab, we will play around with some neurofeedback training!

### Setup

First, install the libraries:
``` bash
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
- Run neurofeedback: `python neurofeedback.py`

When running `neurofeedback.py`, it will show a bar representing the ratio of beta (12-20Hz) to theta (4-8Hz) rhythms in all 4 electrodes.
The goal is to increase beta while decreasing theta, which has been shown to improve symptoms of ADHD [1].

You can play around with which frequency bands to use in the ratio for the bar by changing the following two variables in `neurofeedback.py`:

``` python
decrease_fs = [4, 8]
increase_fs = [12, 20]
```

References
[1] Arns, M., de Ridder, S., Strehl, U., Breteler, M., & Coenen, A. (2009). Efficacy of neurofeedback treatment in ADHD: the effects on inattention, impulsivity and hyperactivity: a meta-analysis. Clinical EEG and neuroscience, 40(3), 180-189. [(PDF)](http://www.bakerneuropsychology.com/files/Arns_2009_ClinEEGNeurosci_Efficacy_for_ADHD_meta-analysis.pdf)
