import pygame
import random
import sys

# Константы
WIDTH, HEIGHT = 640, 480
TILE_SIZE = 40

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Roguelike Adventure")

# Символы
PLAYER_SYMBOL = '@'
MONSTER_SYMBOL = '#'
EMPTY_SYMBOL = '.'

class Game:
    def __init__(self):
        self.player_pos = [1, 1]
        self.monsters = [[random.randint(1, 10), random.randint(1, 10)] for _ in range(5)]
        self.grid = [[' ' for _ in range(WIDTH // TILE_SIZE)] for _ in range(HEIGHT // TILE_SIZE)]
        self.populate_grid()

    def populate_grid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if random.random() < 0.1:
                    self.grid[i][j] = MONSTER_SYMBOL
                if [i, j] == self.player_pos:
                    self.grid[i][j] = PLAYER_SYMBOL

    def draw_grid(self):
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                text = font.render(cell, True, WHITE)
                screen.blit(text, (j * TILE_SIZE, i * TILE_SIZE))

    def move_player(self, direction):
        dx, dy = 0, 0
        if direction == 'UP':
            dy = -1
        elif direction == 'DOWN':
            dy = 1
        elif direction == 'LEFT':
            dx = -1
        elif direction == 'RIGHT':
            dx = 1

        new_x = self.player_pos[0] + dx
        new_y = self.player_pos[1] + dy

        if self.is_valid_move(new_x, new_y):
            self.player_pos = [new_x, new_y]
            self.update_grid()

    def is_valid_move(self, x, y):
        return 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]) and self.grid[x][y] != MONSTER_SYMBOL

    def update_grid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j] = EMPTY_SYMBOL
        self.grid[self.player_pos[0]][self.player_pos[1]] = PLAYER_SYMBOL
        for m in self.monsters:
            self.grid[m[0]][m[1]] = MONSTER_SYMBOL

def main():
    global font
    font = pygame.font.SysFont('Arial', TILE_SIZE)

    game = Game()
    
    while True:
        screen.fill(BLACK)
        game.draw_grid()
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    game.move_player('UP')
                if event.key == pygame.K_d:
                    game.move_player('DOWN')
                if event.key == pygame.K_w:
                    game.move_player('LEFT')
                if event.key == pygame.K_s:
                    game.move_player('RIGHT')

if __name__ == '__main__':
    main()
