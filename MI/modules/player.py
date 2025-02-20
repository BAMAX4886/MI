class Player:
    def __init__(self, start_pos, screen):
        self.x, self.y = start_pos
        self.health = 100
        self.screen = screen

    def get_new_position(self, direction):
        if direction == curses.KEY_UP:
            return self.y - 1, self.x
        elif direction == curses.KEY_DOWN:
            return self.y + 1, self.x
        elif direction == curses.KEY_LEFT:
            return self.y, self.x - 1
        elif direction == curses.KEY_RIGHT:
            return self.y, self.x + 1

    def move(self, new_y, new_x):
        self.y, self.x = new_y, new_x
