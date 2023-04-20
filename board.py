import pygame
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        #variables
        #change
        #testing fork

        pass
    def draw(self):
        # I think this may need more detail
        for row in self.grid:
            for cell in row:
                cell.draw()
    def select(self, row, col):
        pass

    def click(self, x, y):
        if x < 0 or y < 0 or x > self.width * 50 or y > self.height * 50:
            return None
        row = y // 50
        col = x // 50
        return (row, col)
    def clear(self):
        pass
    def sketch(self, value):
        if self.selected:
            self.grid[self.selected[0]][self.selected[1]].sketch = value
    def place_number(self, value):
        if self.selected:
            cell = self.grid[self.selected[0]][self.selected[1]]
            if not cell.original:
                cell.value = value
                cell.sketch = None
    def reset_to_original(self):
        pass
    def is_full(self):
        pass
    def update_board(self):
        for row in self.grid:
            for cell in row:
                cell.update_value()
    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col].value == 0:
                    return (row, col)
        return None
    def check_board(self):
        pass
