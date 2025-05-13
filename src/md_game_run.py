import pygame
import sys
import random
import numpy as np

from src.configs import *
from src.balls import balls



def init_simulation(WIDTH, HEIGHT):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Atoms collision and MD")
    clock = pygame.time.Clock()
    return screen, clock

def handle_collision(ball1, ball2):
    diff = ball2["pos"] - ball1["pos"]
    dist = np.linalg.norm(diff)
    min_dist = 2 * radius

    if dist < min_dist and dist != 0:
        overlap = min_dist - dist
        direction = diff / dist
        ball1["pos"] -= direction * overlap / 2
        ball2["pos"] += direction * overlap / 2

        relative_velocity = ball1["vel"] - ball2["vel"]
        vel_along_normal = np.dot(relative_velocity, direction)

        if vel_along_normal > 0:
            return

        impulse = -2 * vel_along_normal / 2
        impulse_vector = impulse * direction
        ball1["vel"] += impulse_vector
        ball2["vel"] -= impulse_vector

def run():
    screen, clock = init_simulation(WIDTH, HEIGHT)

    while True:
        screen.fill(WHITE)

        for ball in balls:
            pygame.draw.circle(screen, ball["color"], ball["pos"].astype(int), radius)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for ball in balls:
                    dx = mouse_x - ball["pos"][0]
                    dy = mouse_y - ball["pos"][1]
                    if dx**2 + dy**2 <= radius**2:
                        ball["holding"] = True

            if event.type == pygame.MOUSEBUTTONUP:
                for ball in balls:
                    ball["holding"] = False

        mouse_pos = np.array(pygame.mouse.get_pos(), dtype=float)
        for ball in balls:
            if ball["holding"]:
                to_mouse = mouse_pos - ball["pos"]
                distance = np.linalg.norm(to_mouse)
                if distance < 100 and distance != 0:
                    direction = to_mouse / distance
                    ball["vel"] += direction * 0.5
            else:
                ball["pos"] += ball["vel"]
                if ball["pos"][0] - radius < 0 or ball["pos"][0] + radius > WIDTH:
                    ball["vel"][0] *= -1
                if ball["pos"][1] - radius < 0 or ball["pos"][1] + radius > HEIGHT:
                    ball["vel"][1] *= -1
                ball["pos"][0] = np.clip(ball["pos"][0], radius, WIDTH - radius)
                ball["pos"][1] = np.clip(ball["pos"][1], radius, HEIGHT - radius)

        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                handle_collision(balls[i], balls[j])

        pygame.display.flip()
        clock.tick(60)
