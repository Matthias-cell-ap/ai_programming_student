"""
Oefening 2: Sliding Puzzle (8-puzzle)
======================================
Implementeer de sliding puzzle en los hem op met BFS/DFS.
"""
import numpy as np
from collections import deque


class SlidingPuzzle:
    GRIDSIZE = 3
    EMPTY = 0
    GOAL = [  # noqa: RUF012
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    def __init__(self, game):
        self.Game = np.array(game)

    def possible_new_configurations(self):
        y, x = self.locate_empty()
        options = []

        if y - 1 >= 0:
            new = self.Game.copy()
            new[y][x], new[y-1][x] = new[y-1][x], new[y][x]
            options.append(new)

        if y + 1 < self.GRIDSIZE:
            new = self.Game.copy()
            new[y][x], new[y+1][x] = new[y+1][x], new[y][x]
            options.append(new)

        if x - 1 >= 0:
            new = self.Game.copy()
            new[y][x], new[y][x-1] = new[y][x-1], new[y][x]
            options.append(new)

        if x + 1 < self.GRIDSIZE:
            new = self.Game.copy()
            new[y][x], new[y][x+1] = new[y][x+1], new[y][x]
            options.append(new)

        return options

    def locate_empty(self):
        for row in range(self.GRIDSIZE):
            for col in range(self.GRIDSIZE):
                if self.Game[row][col] == self.EMPTY:
                    return (row, col)
        raise Exception("Geen leeg vakje!")

    def manhattan_distance(self):
        total = 0
        for row in range(self.GRIDSIZE):
            for col in range(self.GRIDSIZE):
                tile = self.Game[row, col]
                if tile != self.EMPTY:
                    goal_row, goal_col = divmod(tile - 1, self.GRIDSIZE)
                    total += abs(goal_row - row) + abs(goal_col - col)
        return total

    def is_goal(self):
        return np.array_equal(self.Game, self.GOAL)

    def duplicate(self):
        return SlidingPuzzle([[self.Game[r][c] for c in range(self.GRIDSIZE)] for r in range(self.GRIDSIZE)])

    def log(self):
        print("---")
        for row in self.Game:
            print(", ".join(str(int(x)) for x in row))
        print("---")


def solve_puzzle(start_puzzle):
    q = deque([start_puzzle])
    visited = {tuple(start_puzzle.Game.flatten())}

    while q:
        puzzle = q.popleft()

        if puzzle.is_goal():
            return puzzle.Game

        for action in puzzle.possible_new_configurations():
            if tuple(action.flatten()) not in visited:
                visited.add(tuple(action.flatten()))
                q.append(SlidingPuzzle(action))
    
    return False


if __name__ == "__main__":
    game = [
        [1, 2, 3],
        [4, 5, 0],
        [7, 8, 6]
    ]
    puzzle = SlidingPuzzle(game)
    print("Startconfiguratie:")
    puzzle.log()

    oplossing = solve_puzzle(puzzle)
    print("Oplossing:", oplossing)