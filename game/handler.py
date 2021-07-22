from argparse import ArgumentParser
from os import system
from random import random
import copy
from sys import version_info
from time import sleep, time


class Species(object):
    def __init__(self, args):
        self.fps = args.refresh_rate
        self.generation = 1
        #
        # self.board = [
        #     [0, 0, 0, 0, 0, 0],
        #     [0, 0, 1, 1, 1, 0],
        #     [0, 0, 0, 0, 0, 0]
        # ]
        self.board = [
            [1 if random() < .50 else 0 for _ in range(15)]
            for _ in range(15)
        ]

    def generate_next_iteration(self):
        self.generation += 1
        new_generation = copy.deepcopy(self.board)
        for x in range(len(self.board)):
            for y in range(len(self.board[0])):
                live_neighbors = self.get_number_of_live_neighbors(x, y)
                # Rule 4

                if self.board[x][y] == 0 and live_neighbors == 3:
                    new_generation[x][y] = 1
                elif self.board[x][y] == 1 and live_neighbors in (2, 3):  # Rule 2
                    new_generation[x][y] = 1
                else:  # Rule 1 and 3
                    new_generation[x][y] = 0
        self.board = new_generation

    def get_number_of_live_neighbors(self, x, y):
        count = 0
        n_diff = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]
        neighbors = [(x + d[0], y + d[1]) for d in n_diff]
        for a, b in neighbors:
            if 0 <= a < len(self.board) and 0 <= b < len(self.board[0]) and self.board[a][b] % 2 == 1:
                count += 1
        return count

    def __str__(self):
        lines = [' '.join(['*' if e else ' ' for e in row])
                 for row in self.board]
        return '\n'.join(['Generation {0}\n'.format(self.generation)] + lines)


def controller(args):
    board = Species(args)
    try_sleeping(args.refresh_rate)
    print(board)
    while True:
        start_time = time()
        board.generate_next_iteration()
        print(board)
        wait_time = args.refresh_rate - (time() - start_time) if args.refresh_rate - (time() - start_time) > 0 else 0
        try_sleeping(wait_time)


def try_sleeping(ms):
    try:
        sleep(ms / 1000)
    except Exception as e:
        print('Unable to implement refresh rate feature')


def entry():
    args = __process_args()
    controller(args)


def __process_args():
    parser = ArgumentParser(prog='game-of-life',
                            description="""Conway's Game of Life implemented in Terminal.""")
    parser.add_argument('--refresh-rate', type=int, default=1000,
                        help="""Refresh rate (in ms).""")
    return parser.parse_args()


if __name__ == "__main__":
    class Temp:
        def __init__(self, refresh_rate=None):
            self.refresh_rate = 1000
            if refresh_rate:
                self.refresh_rate = refresh_rate


    controller(Temp())
