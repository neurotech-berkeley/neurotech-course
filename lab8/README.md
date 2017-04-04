# Lab 8: Detecting and controlling hand movements

### Introduction
In this lab, we will try recording EMG signals from various muscles, and then try to stimulate these muscles with a TENS device.

### Recording EMG

We will restrict ourselves to the OpenBCI GUI to visualize EMG signals, as they are clearly visible without much processing.

To setup the Ganglion to record EMG, you can then follow the [Ganglion getting started guide](http://docs.openbci.com/Tutorials/02-Ganglion_Getting%20Started_Guide#ganglion-getting-started-guide-connect-for-emg) .

- Try connecting it to your arm at first, following the tutorial
- Try other areas! Can you detect biceps? Fingers? Leg? Feet? 

### Stimulation with TENS

For this lab, we'll be using the [TENS 3000](https://www.tenspros.com/tens-3000-analogue-tens-unit-dt3002.html) .

This comes with a rather instructive [manual](https://www.tenspros.com/assets/images/manuals/TENS-3000-dt3002-Manual.pdf), which I suggest skim through.

Here are some key points for us:
- This TENS is mainly intended for relieving pain, but it's powerful enough to cause muscle contraction
- Generally you want the mode set to N ("Normal"). B ("Burst") and M ("modulation") are special modes that fix or vary the pulse rate. (See [page](https://www.tenspros.com/tens-3000-analogue-tens-unit-dt3002.html) for details.)
- There are 3 main settings to control:
    - Pulse amplitude, controlled by dial on the top (0-40V, dial shows 0-8). This is the main control of stimulus intensity.
    - Pulse width, from 30 to 260 μs. This also affects stimulus intensity, but not as much as pulse amplitude
    - Pulse rate, 2-150 Hz. This affects how often you get stimulated. 

Warnings:
- DO NOT put electrodes on the front of the neck, around the heart, or on the head (back of neck is okay)
- DO NOT put one electrode on front, and one on back of body, as this could pass current through the body
- DO NOT use this if you have a cardiac pacemaker

Using the device:
- When using the device, make sure to have it off (pulse amplitude at 0) before connecting. 
- There are 2 electrodes, that you place across the muscle you want to stimulate (make sure to follow warnings above when choosing muscle!)
- You can use the settings below to test pain relief and muscle contraction

- Settings recommended by manual for pain relief:
    - Pulse rate: 70-120 Hz
    - Pulse width: 70-120 μs
- Settings for muscle contraction (found by trial and error):
    - Pulse rate: 20-50 Hz
    - Pulse width: 260 μs

    
