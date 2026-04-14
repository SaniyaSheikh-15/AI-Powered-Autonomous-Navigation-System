import random

def generate_grid(rows, cols, obstacle_prob=0.2):
    grid = []
    for _ in range(rows):
        row = [1 if random.random() < obstacle_prob else 0 for _ in range(cols)]
        grid.append(row)
    return grid
