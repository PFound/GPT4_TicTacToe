import pygame
from board import Board
from button import Button
from constants import *

# Add the RED color to your constants
RED = (255, 0, 0)

class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = 'X'
        self.game_over = False
        self.winner = None

    def is_draw(self):
        for row in range(3):
            for col in range(3):
                if self.board.grid[row][col] == '':
                    return False
        return not (self.board.check_win("X") or self.board.check_win("O"))

    def handle_click(self, pos):
        if self.game_over:
            return

        x, y = pos
        row = y // 200
        col = x // 200

        if self.board.grid[row][col] == '':
            self.board.grid[row][col] = self.current_player

            if self.board.check_win(self.current_player):
                self.game_over = True
                self.winner = self.current_player
            elif self.is_draw():
                self.game_over = True
                self.winner = None
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def draw_win_message(self, screen):
        if self.game_over:
            font = pygame.font.Font(None, 75)
            if self.winner is not None:
                text = font.render(f"{self.winner} wins!", True, RED)
            else:
                text = font.render("Draw!", True, RED)
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

    def create_restart_button(self):
        font = pygame.font.Font(None, 36)
        return Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 50, 200, 40, "Restart", font, WHITE, RED)

    def run(self):
        pygame.display.set_caption('Tic Tac Toe')
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        running = True
        clock = pygame.time.Clock()

        restart_button = self.create_restart_button()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.game_over and restart_button.is_clicked(event.pos):
                            self.__init__()
                        else:
                            self.handle_click(event.pos)

            screen.fill(WHITE)
            self.board.draw(screen)
            self.draw_win_message(screen)
            if self.game_over:  # Draw the restart button only when the game is over
                restart_button.draw(screen)
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
