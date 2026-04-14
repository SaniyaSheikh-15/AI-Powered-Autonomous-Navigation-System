import pygame
from simulation.grid import draw_grid
from src.utils import generate_grid
from src.astar import astar
from src.agent import Agent

ROWS, COLS = 20, 30
WIDTH, HEIGHT = COLS*30, ROWS*30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Autonomous Navigation System")

grid = generate_grid(ROWS, COLS)

start = (ROWS-2, 1)
goal = (1, COLS-2)

grid[start[0]][start[1]] = 0
grid[goal[0]][goal[1]] = 0

agent = Agent(start)
path = astar(grid, start, goal)
agent.set_path(path)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill((10, 10, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    agent.move()
    draw_grid(screen, grid, agent.position, goal)

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
