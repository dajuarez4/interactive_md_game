import pygame
n = 100  # Number of balls
initial_velocity = 1 # initial velocity
WIDTH, HEIGHT = 800, 600 # screen (x,y)
radius = 10
k = 50  # force constant value
dt = 1 / 60  # time step
#colors in rgb
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
colors = [RED, BLUE]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
