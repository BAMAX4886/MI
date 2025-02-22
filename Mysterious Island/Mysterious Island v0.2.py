import pygame
import random
import sys

# Константы
WIDTH, HEIGHT = 1280, 480
TILE_SIZE = 20
PLAYER_HEALTH = 100
MONSTER_HEALTH = 30

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Roguelike Adventure")

# Символы
PLAYER_SYMBOL = '@'
MONSTER_SYMBOL = 'X'
EMPTY_SYMBOL = '.'
ITEM_SYMBOL = '?'

class Player:
    def __init__(self):
        self.position = [1, 1]
        self.health = PLAYER_HEALTH
        self.inventory = []

class Monster:
    def __init__(self, position):
        self.position = position
        self.health = MONSTER_HEALTH

class Game:
    def __init__(self):
        self.player = Player()
        self.monsters = [Monster([random.randint(1, 47), random.randint(1, 35)]) for _ in range(3)]
        self.grid = [[' ' for _ in range(WIDTH // TILE_SIZE)] for _ in range(HEIGHT // TILE_SIZE)]
        self.populate_grid()

    def populate_grid(self):
        for monster in self.monsters:
            x, y = monster.position
            self.grid[x][y] = MONSTER_SYMBOL
        self.grid[self.player.position[0]][self.player.position[1]] = PLAYER_SYMBOL

    def draw_grid(self):
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                text = font.render(cell, True, WHITE)
                screen.blit(text, (j * TILE_SIZE, i * TILE_SIZE))
        health_text = font.render(f"HP: {self.player.health}", True, WHITE)
        screen.blit(health_text, (10, 10))

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

        new_x = self.player.position[0] + dy
        new_y = self.player.position[1] + dx

        if self.is_valid_move(new_x, new_y):
            self.player.position = [new_x, new_y]
            self.update_grid()
            self.check_battle()

    def is_valid_move(self, x, y):
        return 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0])

    def check_battle(self):
        for monster in self.monsters:
            if self.player.position == monster.position:
                self.battle(monster)

    def battle(self, monster):
        while self.player.health > 0 and monster.health > 0:
            monster.health -= 10  # Player attacks
            if monster.health > 0:
                self.player.health -= 5  # Monster attacks

        if self.player.health > 0:
            monster.position = [-1, -1]  # Удаляем монстра
            self.update_grid()
            self.player.inventory.append(ITEM_SYMBOL)

    def update_grid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j] = EMPTY_SYMBOL
        self.grid[self.player.position[0]][self.player.position[1]] = PLAYER_SYMBOL
        for monster in self.monsters:
            if monster.health > 0:
                self.grid[monster.position[0]][monster.position[1]] = MONSTER_SYMBOL
            else:
                monster.position = [-1, -1]  # Удаляем мертвых монстров

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
                if event.key == pygame.K_w:
                    game.move_player('UP')
                if event.key == pygame.K_s:
                    game.move_player('DOWN')
                if event.key == pygame.K_a:
                    game.move_player('LEFT')
                if event.key == pygame.K_d:
                    game.move_player('RIGHT')

if __name__ == '__main__':
    main()
