class Enemy:
    def __init__(self, health=50):
        self.health = health

class Combat:
    def __init__(self, player):
        self.player = player
        self.enemies = []

    def attack_enemy(self, enemy):
        damage = 10
        enemy.health -= damage
        if enemy.health <= 0:
            self.enemies.remove(enemy)
            print("Enemy defeated!")

    def spawn_enemy(self):
        self.enemies.append(Enemy())
