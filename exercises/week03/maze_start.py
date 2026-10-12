"""
Oefening 3: Maze met DFS
=========================
Implementeer DFS om een weg door het maze te vinden.
"""
import numpy as np


class Maze:
    def __init__(self, size, start, end, walls):
        self.size = size
        self.start = start
        self.end = end
        self.maze = np.zeros(size, dtype=str)
        self.maze[:, :] = '.'
        self.maze[start] = 'S'
        self.maze[end] = 'E'
        for wall in walls:
            self.maze[wall] = '#'

    def valid_moves(self, current):
        options = []
        neighbors = [(current[0] +1, current[1]), (current[0], current[1]+1), (current[0]-1, current[1]), (current[0], current[1]-1)]
        allowed = ['.', 'E']
        
        for neighbor in neighbors:
            if neighbor[0] > -1 and neighbor[0] < self.size[0] and neighbor[1] > -1 and neighbor[1] < self.size[1] and self.maze[neighbor[0]][neighbor[1]] in allowed:
                options.append(neighbor)

        return options

    def extract_path(self, stack):
        return (stack, len(stack)-1)

    def print_maze(self):
        for row in self.maze:
            print(' '.join(row))


def find_path(maze: Maze):
    stack = [[maze.start]]
    visited = set()
 
    while len(stack) > 0:
        path = stack.pop()
        cords = path[-1]
 
        if (cords[0], cords[1]) == maze.end:
            return maze.extract_path(path)
        
        visited.add(cords)

        for neighbor in maze.valid_moves(cords):
            if neighbor not in visited:
                stack.append(path + [neighbor])
 
    return [], 0
 


if __name__ == "__main__":
    maze_size = (10, 10)
    start_point = (0, 0)
    end_point = (9, 9)
    walls = [(2, 1), (2, 2), (2, 3), (4, 6), (6, 6), (7, 6), (8, 6),
             (4, 7), (4, 8), (2, 2), (5, 2), (6, 2), (4, 2), (3, 2),
             (8, 0), (9, 6), (1, 8), (2, 8), (6, 9), (7, 9),
             (3, 6), (3, 7), (4, 1), (5, 1)]

    my_maze = Maze(maze_size, start_point, end_point, walls)
    pad, stappen = find_path(my_maze)

    my_maze.print_maze()
    print("Pad:", pad)
    print("Stappen:", stappen)