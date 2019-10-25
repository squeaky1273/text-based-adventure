class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

class Weapon(Item):
    def __init__(self, name, description, value, damage):

class Rock(Weapon):
    def __init__(self):
        super.__init__()

class Bottle(Weapon):
    def __init__(self):
        super.__init__()
