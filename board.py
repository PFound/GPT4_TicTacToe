import pygame
from constants import *

class Board:
    def __init__(self):
        self.grid = [['' for _ in range(3)] for _ in range(3)]

    def draw_lines(self, screen):
        for i in range(1, 3):
            pygame.draw.line(screen, BLACK, (i * SCREEN_WIDTH // 3, 0), (i * SCREEN_WIDTH // 3, SCREEN_HEIGHT), 5)
            pygame.draw.line(screen, BLACK, (0, i * SCREEN_HEIGHT // 3), (SCREEN_WIDTH, i * SCREEN_HEIGHT // 3), 5)

    def draw_symbols(self, screen):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell != '':
                    symbol_x = x * SCREEN_WIDTH // 3 + SCREEN_WIDTH // 6
                    symbol_y = y * SCREEN_HEIGHT // 3 + SCREEN_HEIGHT // 6
                    if cell == 'X':
                        pygame.draw.line(screen, BLACK, (symbol_x - 60, symbol_y - 60), (symbol_x + 60, symbol_y + 60), 10)
                        pygame.draw.line(screen, BLACK, (symbol_x - 60, symbol_y + 60), (symbol_x + 60, symbol_y - 60), 10)
                    else:
                        pygame.draw.circle(screen, BLACK, (symbol_x, symbol_y), 60, 10)

    def draw(self, screen):
        self.draw_lines(screen)
        self.draw_symbols(screen)

    def check_win(self, player):
        for row in self.grid:
            if all(cell == player for cell in row):
                return True

        for col in range(3):
            if all(self.grid[row][col] == player for row in range(3)):
                return True

        if all(self.grid[i][i] == player for i in range(3)):
            return True

        if all(self.grid[i][2 - i] == player for i in range(3)):
            return True

        return False
