from QLearning import QLearning


class TicTacToe:
    """
    TicTacToe is a two-player game played on a three-by-three grid. The two
    players take turns marking either `×` or `○` on the grid. The first player
    that places three marks in a row wins.

    Methods
    -------
    play
    """

    def __init__(self):
        self.EMPTY = '.'
        self.CIRCLE = '○'
        self.CROSS = '×'
        self.__grid = [
            [self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.EMPTY]
        ]
        self.__round = 0
        self.__player = self.CIRCLE

    def __str__(self) -> str:
        return '\n-+-+-\n'.join(['|'.join(row) for row in self.__grid])

    def __encode_grid(self) -> str:
        return ''.join([''.join(row) for row in self.__grid])

    def __has_winner(self) -> bool:
        return any([
            self.__grid[0][0] == self.__grid[0][1] == self.__grid[0][2] != self.EMPTY,
            self.__grid[1][0] == self.__grid[1][1] == self.__grid[1][2] != self.EMPTY,
            self.__grid[2][0] == self.__grid[2][1] == self.__grid[2][2] != self.EMPTY,
            self.__grid[0][0] == self.__grid[1][0] == self.__grid[2][0] != self.EMPTY,
            self.__grid[0][1] == self.__grid[1][1] == self.__grid[2][1] != self.EMPTY,
            self.__grid[0][2] == self.__grid[1][2] == self.__grid[2][2] != self.EMPTY,
            self.__grid[0][0] == self.__grid[1][1] == self.__grid[2][2] != self.EMPTY,
            self.__grid[0][2] == self.__grid[1][1] == self.__grid[2][0] != self.EMPTY
        ])

    def __which_player(self):
        self.__player = self.CIRCLE if self.__round % 2 == 1 else self.CROSS

    def __round_info(self) -> str:
        return f'Round {self.__round} - Player {self.__player}'

    def __input(self) -> tuple[int, int]:
        valid = {1, 2, 3}
        x = 0
        y = 0
        while True:
            x = int(input('x: '))
            y = int(input('y: '))
            if (x in valid and
                y in valid and
                    self.__grid[y - 1][x - 1] == self.EMPTY):
                break
            else:
                print('ERROR:', 'invalid input')
        return x, y

    def __move(self, x: int, y: int):
        if self.__grid[y - 1][x - 1] == self.EMPTY:
            self.__grid[y - 1][x - 1] = self.__player

    def play(self):
        """
        Starts the game against yourself.
        """
        while self.__round < 9 and not self.__has_winner():
            self.__round += 1
            self.__which_player()
            print(self.__round_info())
            x, y = self.__input()
            self.__move(x, y)
            print(self)
        if self.__has_winner():
            print(f'Player {self.__player} wins!')
        else:
            print('Draw!')

    def play_cpu(self):
        """
        Starts the game against the CPU.
        """
        cpu = QLearning(self, alpha=0.1, gamma=2.0)
        while self.__round < 9 and not self.__has_winner():
            self.__round += 1
            self.__which_player()
            print(self.__round_info())
            if self.__player == self.CIRCLE:
                x, y = self.__input()
            else:
                x, y = cpu.input(self.__encode_grid())
            self.__move(x, y)
            print(self)
        if self.__has_winner():
            print(f'Player {self.__player} wins!')
        else:
            print('Draw!')
    
    def train_cpu(self, n: int):
        """
        Trains the CPU against itself.

        Parameters
        ----------
        n : int
            The number of iterations
        """
        cpu1 = QLearning(self, alpha=0.1, gamma=2.0)
        cpu2 = QLearning(self, alpha=0.1, gamma=2.0)
        for _ in range(n):
            while self.__round < 9 and not self.__has_winner():
                self.__round += 1
                self.__which_player()
                if self.__player == self.CIRCLE:
                    x, y = cpu1.input(self.__encode_grid())
                else:
                    x, y = cpu2.input(self.__encode_grid())
                self.__move(x, y)
            if self.__has_winner():
                pass
            else:
                pass
