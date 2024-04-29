#Muhammad Zedi Mumtaz
#122140223
#Praktikum PBO RB Tugas 5 Membuat Game Sederhana

import pygame
import sys

# Inheritance: TicTacToeGame turunan dari pygame.Surface
class TicTacToeGame(pygame.Surface):
    def __init__(self, width, height):
        super().__init__((width, height))
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.font = pygame.font.Font(None, 100)
        self.running = True
        self.winner = None

    # Encapsulation: Method untuk menggambar board dan isi kotak
    def draw_board(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.line(self.screen, (0, 0, 0), (200, 0), (200, 600), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (400, 0), (400, 600), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, 200), (600, 200), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, 400), (600, 400), 5)

        for y in range(3):
            for x in range(3):
                text_surface = self.font.render(self.board[y][x], True, (0, 0, 0))
                self.screen.blit(text_surface, (x * 200 + 50, y * 200 + 50))

    # Abstraction: Method untuk menangani klik mouse
    def handle_click(self, x, y):
        if self.board[y // 200][x // 200] == '' and not self.winner:
            self.board[y // 200][x // 200] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    # Encapsulation: Method untuk mengecek pemenang
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False

    # Polymorphism: Method untuk menampilkan pesan pemenang
    def display_winner_message(self):
        if self.winner:
            text = f"{self.winner} wins!"
        else:
            text = "It's a draw!"
        text_surface = self.font.render(text, True, (0, 0, 0))
        self.screen.blit(text_surface, (150, 250))

    # Encapsulation: Method untuk menangani event
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.handle_click(*pygame.mouse.get_pos())

    # Abstraction: Method untuk menjalankan permainan
    def run(self):
        while self.running:
            self.handle_events()
            self.draw_board()
            if self.winner:
                self.display_winner_message()
            pygame.display.flip()
            self.clock.tick(30)


if __name__ == "__main__":
    pygame.init()
    game = TicTacToeGame(600, 600)
    game.run()
    pygame.quit()
    sys.exit()
