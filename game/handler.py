from argparse import ArgumentParser
from os import system, name as os_name
from random import random
import copy
from time import sleep, time


class Game(object):
    def __init__(self, args):
        self.fps = args.refresh_rate
        self.generation = 1
        self.size = args.size
        self.spawn_rate = args.spawn_rate
        self.clear_terminal = args.clear_terminal
        if args.size > 30:
            # Restricitng user input since I do not know how to handle large values of output.
            print('Size above limits, resetting to default')
            self.size = 15
        self.show_coordinates = args.show_coordinates
        self.board = [
            [1 if random() < .50 else 0 for _ in range(self.size)]
            for _ in range(self.size)
        ]
        self.seen = dict() # This is used to see if a board has appeared before
        self.cycle = False

    def board_alive(self):
        s = sum([sum(y) for y in self.board])
        return s != 0

    def check_against_rules(self, live_neighbors, alive):
        # Rule 4
        if not alive and live_neighbors == 3:
            return self.spawn_check()
        # Rule 2
        if alive and live_neighbors in (2, 3):
            return self.spawn_check()
        # Rule 1 and 3
        return 0

    def generate_next_iteration(self):
        self.generation += 1
        new_generation = copy.deepcopy(self.board)
        for x in range(len(self.board)):
            for y in range(len(self.board[0])):
                live_neighbors = self.get_number_of_live_neighbors(x, y)
                new_generation[x][y] = self.check_against_rules(live_neighbors, self.board[x][y])
        self.board = new_generation
        self.hash_board()
        return self.board_alive()

    def spawn_check(self):
        """
        Chance of new element being spawned
        :return: int: 1 or 0
        """
        return 1 if random() < (self.spawn_rate / 100) else 0

    def get_number_of_live_neighbors(self, x, y):
        '''
        Returns the number of live neighbors for a given cell (8 directions)

        :param x:  x-coordinate of the cell
        :param y:  y-coordinate of the cell
        :return:  the number of live neighbors for the given cell (8 directions)
        '''

        count = 0
        n_diff = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]
        neighbors = [(x + d[0], y + d[1]) for d in n_diff]
        for a, b in neighbors:
            if 0 <= a < len(self.board) and 0 <= b < len(self.board[0]) and self.board[a][b] % 2 == 1:
                count += 1
        return count

    def clear_terminal_controller(self):
        '''
        Clears Terminal.
        Stops trying to clear terminal if exception occures.
        :return: None
        '''
        if self.clear_terminal:
            try:
                system('cls' if os_name == 'nt' else 'clear')
            except Exception as e:
                print('Unable to clear terminal, feature disabled')
                self.clear_terminal = False


    def hash_board(self):
        '''
        dict(hash_value : list of generations)
        '''
        h = repr(self.board)
        if h in self.seen:
            print('This board was previously seen on generation(s): {}'.format(', '.join(self.seen[h])))
            self.cycle = True
            self.seen[h].append(str(self.generation))
        else:
            self.seen[h] = [str(self.generation)]



    def __str__(self):
        # I have not worked with dynamically adjustable terminal interfaces before.
        # I have spent 1 hour trying to figure out how to handle outputs for any windows size, but I'm unable to do it.
        # Ignoring this restriction
        self.clear_terminal_controller()
        lines = [''.join(['*'.ljust(3, ' ') if e else ' ' * 3 for e in row])
                 for row in self.board]
        if self.show_coordinates:
            for y in range(self.size):
                lines[y] = str(y).ljust(3, ' ') + '|' + lines[y]
            x_axis = ' ' * 4
            for x in list(range(self.size)):
                x_axis += str(x).ljust(3, ' ')

            lines.append(x_axis)

        return '\n'.join(['Generation {0}\n'.format(self.generation)] + lines)


def controller(args):
    board = Game(args)
    print(board)
    go_to_next_iteration = True
    while go_to_next_iteration:
        start_time = time()
        go_to_next_iteration = board.generate_next_iteration()
        print(board)
        wait_time = args.refresh_rate - (time() - start_time) if args.refresh_rate - (time() - start_time) > 0 else 0
        try_sleeping(wait_time)
    print('All players are dead after {} iterations. Stopping program now'.format(board.generation))


def try_sleeping(ms):
    try:
        sleep(ms / 1000)
    except Exception:
        print('Unable to implement refresh rate.')


def entry():
    args = __process_args()
    controller(args)


def __process_args():
    parser = ArgumentParser(prog='game-of-life',
                            description="""Conway's Game of Life implemented in Terminal.""")
    parser.add_argument('--refresh-rate', type=int, default=1000,
                        help="""Refresh rate (in ms).""")
    parser.add_argument('--size', type=int, default=20,
                        help="""Size of the board (nXn)""")
    parser.add_argument('--spawn-rate', type=int, default=100,
                        help="""Spawn percentage of new players after Generation 1 (default 100, guaranteed spawn)""")
    parser.add_argument('--show-coordinates', type=bool, default=False,
                        help="""The board should have the X axis coordinates along the bottom and Y coordinates along 
                        the left.""")
    parser.add_argument('--clear-terminal', type=bool, default=False,
                        help="""Clears the terminal.""")
    return parser.parse_args()


if __name__ == "__main__":
    class Temp:
        def __init__(self):
            self.refresh_rate = 1000
            self.size = 6
            self.spawn_rate = 100
            self.show_coordinates = True
            self.clear_terminal = True


    game = controller(Temp())
