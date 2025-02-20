class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for i, item in enumerate(self.items):
            if item.name == item_name:
                del self.items[i]
                return True
        return False

    def use_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                print(f'You used {item.name}: {item.description}')
                return True
        return False
