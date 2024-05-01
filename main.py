
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
fig, ax = plt.subplots()
x = []
y = []

# Set up plot
line, = ax.plot(x, y)
ax.set_xlabel('Time')
ax.set_ylabel('Value')

# Update plot function
def update_plot():
    x.append(datetime.now())
    y.append(random.random())
    line.set_xdata(x)
    line.set_ydata(y)
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw()
    fig.canvas.flush_events()

# Continuously update plot
while True:
    update_plot()
    #time.sleep(0.1)