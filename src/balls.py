import numpy as np
import random
from src.configs import radius,WIDTH,HEIGHT,initial_velocity,colors,n,screen
balls = []
for i in range(n):
    pos = np.array([
        random.uniform(radius, WIDTH - radius),
        random.uniform(radius, HEIGHT - radius)
    ], dtype=float)
    vel = np.array([
        random.uniform(-initial_velocity, initial_velocity),
        random.uniform(-initial_velocity, initial_velocity)
    ], dtype=float)

    color = colors[0] if i < n // 2 else colors[1]

    balls.append({
        "pos": pos,
        "vel": vel,
        "color": color,
        "holding": False
    })
