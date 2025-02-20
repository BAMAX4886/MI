import windows_curses as curses
from modules.map_generator import MapGenerator
from modules.player import Player
from modules.inventory import Inventory
from modules.survival_system import SurvivalSystem
from modules.combat import Combat


class Game:
    def __init__(self):
        self.screen = curses.initscr()
        curses.noecho()  # Отключаем эхо символов
        curses.cbreak()  # Включаем немедленное считывание клавиш
        curses.curs_set(0)  # Скрываем курсор

        self.height, self.width = self.screen.getmaxyx()
        self.map_gen = MapGenerator(self.height, self.width)
        self.player = Player(self.map_gen.start_pos, self.screen)
        self.inventory = Inventory()
        self.survival_sys = SurvivalSystem(self.player)
        self.combat = Combat(self.player)

    def run(self):
        while True:
            self.draw_map()
            self.draw_player()
            self.draw_hud()
            key = self.screen.getch()
            if key == ord('q'):
                break
            elif key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
                self.move_player(key)

    def draw_map(self):
        for y in range(self.height):
            for x in range(self.width):
                tile = self.map_gen.tiles[y][x]
                self.screen.addch(y, x, tile.char)

    def draw_player(self):
        self.screen.addch(self.player.y, self.player.x, '@')

    def move_player(self, direction):
        new_y, new_x = self.player.get_new_position(direction)
        if self.map_gen.is_walkable(new_y, new_x):
            self.player.move(new_y, new_x)

    def draw_hud(self):
        self.screen.addstr(0, 0, f'Health: {self.player.health}')
        self.screen.addstr(1, 0, f'Hunger: {self.survival_sys.hunger}')
        self.screen.addstr(2, 0, f'Thirst: {self.survival_sys.thirst}')

if __name__ == "__main__":
    try:
        game = Game()
        game.run()
    finally:
        curses.endwin()