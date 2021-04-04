class Item:
    def __init__(self, id, name, desc, weight, interact, consumeable):
        self.id = id
        self.name = name
        self.description = desc
        self.weight = weight
        self.interactions = interact
        self.consumeable = consumeable

class Armor(Item):
    def __init__(self, id, name, desc, weight, interact, defence, body_part):
        super().__init__(id, name, desc, weight, interact, False)
        self.defence = defence
        self.body_part = body_part

class Weapon(Item):
    def __init__(self, id, name, desc, weight, interact, damage, two_handed):
        super().__init__(id, name, desc, weight, interact, False)
        self.damage = damage
        self.two_handed = two_handed
