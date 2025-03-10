import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import psutil
import time

# Initialize data lists
x = []  # Time (seconds)
y = []  # CPU usage (percentage)

# Set up the figure and axis
fig, ax = plt.subplots()
line, = ax.plot([], [], marker='o', linestyle='-', color='blue')

# Set axis limits
ax.set_xlim(0, 100)  # X-axis from 0 to 100 seconds
ax.set_ylim(0, 100)  # Y-axis from 0 to 100% CPU usage

# Add labels, title, and grid
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('CPU Usage (%)')
ax.set_title('Real-Time CPU Usage Monitor')
ax.grid(True)

# Animation function
def animate(frame):
    # Get current CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)  # Get CPU usage over 1 second
    current_time = time.localtime().tm_sec  # Get current second

    # Append new data
    x.append(current_time)
    y.append(cpu_usage)

    # Keep only the last 20 data points
    if len(x) > 20:
        x.pop(0)
        y.pop(0)

    # Update the line data
    line.set_data(x, y)

    # Adjust x-axis limits dynamically
    ax.set_xlim(min(x), max(x) + 1)

    return line,

# Create the animation
ani = FuncAnimation(fig, animate, frames=None, interval=1000, blit=True)

# Display the animation
plt.show()
