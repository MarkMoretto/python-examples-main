

"""
Ref: https://stackoverflow.com/questions/55677010/how-to-allign-data-based-on-time?noredirect=1#comment98039885_55677010

"""

import datetime
import pandas as pd

n = 10
t_base = datetime.datetime.today()
date_list = [t_base - datetime.timedelta(days=x) for x in range(0, n)]

from scipy import signal

import matplotlib.pyplot as plot

import numpy as np

 

# Sampling rate 1000 hz / second
t = np.linspace(0, 1, 1000, endpoint=True)

# Plot the square wave signal
plot.plot(t, signal.square(2 * np.pi * 5 * t))

# Give a title for the square wave plot
plot.title('Sqaure wave - 5 Hz sampled at 1000 Hz /second')


# Give x axis label for the square wave plot
plot.xlabel('Time')


# Give y axis label for the square wave plot
plot.ylabel('Amplitude')


plot.grid(True, which='both')


# Provide x axis and line color
plot.axhline(y=0, color='k')


# Set the max and min values for y axis
plot.ylim(-2, 2)


# Display the square wave drawn
plot.show()