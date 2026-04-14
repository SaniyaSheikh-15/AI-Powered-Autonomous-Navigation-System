import pygame

CELL_SIZE = 30

def draw_grid(screen, grid, agent_pos, goal):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            rect = pygame.Rect(j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE)

            if grid[i][j] == 1:
                color = (80, 80, 80)
            else:
                color = (20, 30, 50)

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (40, 60, 90), rect, 1)

    pygame.draw.rect(screen, (0, 255, 0),
                     (agent_pos[1]*CELL_SIZE, agent_pos[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen, (255, 165, 0),
                     (goal[1]*CELL_SIZE, goal[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
