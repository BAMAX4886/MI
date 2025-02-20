class SurvivalSystem:
    def __init__(self, player):
        self.player = player
        self.hunger = 100
        self.thirst = 100

    def update(self):
        self.hunger -= 1
        self.thirst -= 1
        if self.hunger <= 0 or self.thirst <= 0:
            self.player.health -= 10
