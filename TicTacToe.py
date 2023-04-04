class TicTacToe:
    """
    TicTacToe is a two-player game played on a three-by-three grid. The two
    players take turns marking either `X` or `O` on the grid. The first player
    that places three marks in a row wins.
    """
    def __init__(self):
        self.__NOUGHT = 'O'
        self.__CROSS = 'X'
        self.__grid = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        self.__round = 0
        self.__player = self.__NOUGHT

    def __str__(self) -> str:
        return '\n-+-+-\n'.join(['|'.join(row) for row in self.__grid])

    def __encode_grid(self) -> str:
        return ''.join([''.join(row) for row in self.__grid])

    def __has_winner(self) -> bool:
        return any([
            self.__grid[0][0] == self.__grid[0][1] == self.__grid[0][2] != ' ',
            self.__grid[1][0] == self.__grid[1][1] == self.__grid[1][2] != ' ',
            self.__grid[2][0] == self.__grid[2][1] == self.__grid[2][2] != ' ',
            self.__grid[0][0] == self.__grid[1][0] == self.__grid[2][0] != ' ',
            self.__grid[0][1] == self.__grid[1][1] == self.__grid[2][1] != ' ',
            self.__grid[0][2] == self.__grid[1][2] == self.__grid[2][2] != ' ',
            self.__grid[0][0] == self.__grid[1][1] == self.__grid[2][2] != ' ',
            self.__grid[0][2] == self.__grid[1][1] == self.__grid[2][0] != ' '
        ])

    def __which_player(self):
        self.__player = self.__NOUGHT if self.__round % 2 == 1 else self.__CROSS

    def __round_info(self) -> str:
        return f'Round {self.__round} - Player {self.__player}'
    
    def __user_input(self) -> tuple[int, int]:
        valid = {1, 2, 3}
        x = 0
        y = 0
        while not x in valid and not y in valid:
            x = int(input('x: '))
            y = int(input('y: '))
        return x, y

    def __move(self, x: int, y: int):
        if self.__grid[x - 1][y - 1] == ' ':
            self.__grid[x - 1][y - 1] = self.__player

    def play(self):
        """
        Starts the game.
        """
        while self.__round <= 9 and not self.__has_winner():
            self.__round += 1
            self.__which_player()
            print(self.__round_info())
            x, y = self.__user_input()
            self.__move(x, y)
            print(self)
        print(f'Player {self.__player} wins!')
