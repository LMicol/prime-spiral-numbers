# @Author : Lucas Micol

import matplotlib.pyplot as plt
import numpy as np
import signal
import time

# Parameters
scatter_color = "#55c3b2"
background_color = "#0a0a0a"
marker = '.'

# Signal handler to exit gracefully
def signal_handler(signal, frame):
    plt.close()
    print("Exiting...")
    exit(0)

# Set signal handlers
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def is_prime(n):
    # this should work for up to several billions
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def update_plot():
    global n, ax, fig
    if is_prime(n):
        # Add new prime to the plot
        new_point = np.array([[n, n]])
        old_points = points.get_offsets()
        if len(old_points) > 0:
            new_points = np.concatenate([old_points, new_point])
        else:
            new_points = new_point
        points.set_offsets(new_points)

        # Adjust radial range to zoom out
        # Increase maximum radial value
        ax.set_rmax(max(new_points[:, 1]) + 1)
        fig.canvas.draw()
        fig.canvas.flush_events()
    n += 1

if __name__ == "__main__":
    # Initialize plot
    plt.ion()
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    points = ax.scatter([], [], color=scatter_color, marker=marker)

    # Cosmetic parameters
    ax.grid(False)
    ax.set_rmax(0)
    ax.set_rticks([])    
    ax.set_xticklabels([])
    ax.set_facecolor(background_color)
    fig.set_facecolor(background_color)
    ax.spines['polar'].set_visible(False)

    # Continuously update plot
    n = 0
    t = 0.01
    while True:
        update_plot()
        time.sleep(t)
        t = t/len(str(n)) # makes the sleep faster as the n goes to +inf