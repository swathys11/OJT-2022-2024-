import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
HEIGHT = 10  # Initial height of the ball
GRAVITY = 9.8  # Acceleration due to gravity
BOUNCE_FACTOR = 0.8  # Factor of velocity retained after each bounce

# Function to calculate position at each time step
def update_position(frame):
    global height, velocity
    velocity += GRAVITY * dt
    height -= velocity * dt
    
    # Check if the ball has hit the ground
    if height <= 0:
        height = 0
        velocity = -velocity * BOUNCE_FACTOR

    # Update ball position
    ball.set_data([0], [height])
    return ball,

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(0, HEIGHT)

# Initialize the ball
ball, = ax.plot([0], [HEIGHT], 'o', markersize=20)

# Set up the animation
dt = 0.05  # Time step for the animation
velocity = 0  # Initial velocity of the ball
height = HEIGHT  # Initial height of the ball
ani = animation.FuncAnimation(fig, update_position, frames=np.arange(0, 100), interval=dt*1000, blit=True)

plt.title('Elastic Ball Animation')
plt.xlabel('X')
plt.ylabel('Y')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
