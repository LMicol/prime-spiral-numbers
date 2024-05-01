
import matplotlib.pyplot as plt
from datetime import datetime
import random
import numpy as np
import time
import math
import signal

# Signal handler to exit gracefully
def signal_handler(signal, frame):
    plt.close()
    print("Exiting...")
    exit(0)

# Set signal handlers
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


# Initialize plot
plt.ion()
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
r = []
theta = []

# Set up plot
line, = ax.plot(theta, r)
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.set_rlabel_position(-22.5)
ax.grid(True)
ax.set_title("A line plot on a polar axis", va='bottom')

# Update plot function
def update_plot():
    r.append(random.random() * 2)  # Random radial value between 0 and 2
    theta.append(random.random() * 2 * np.pi)  # Random angle between 0 and 2*pi
    line.set_xdata(theta)
    line.set_ydata(r)
    fig.canvas.draw()
    fig.canvas.flush_events()

# Continuously update plot
while True:
    update_plot()
    #time.sleep(0.1)