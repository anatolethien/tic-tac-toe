import numpy as np


class QLearning:
    """
    Algorithm
    """

    def __init__(self, ttc, alpha: float, gamma: float):
        self.ttc = ttc
        self.__ALPHA = alpha
        self.__GAMMA = gamma

    def __get_encoded_index(self, grid: str, x: int, y: int) -> int:
        return y * np.sqrt(len(grid)) + x

    def input(self, grid: str, mode: str = 'random') -> tuple[int, int]:
        valid = {1, 2, 3}
        x = 0
        y = 0
        while True:
            match mode:
                case 'random':
                    x = np.random.choice(tuple(valid), 1)
                    y = np.random.choice(tuple(valid), 1)
            if grid[self.__get_encoded_index(grid, x, y)] == self.ttc.EMPTY:
                break
        return x, y
