class Item:
    def __init__(self, id, name, desc, weight, interact, value, consumeable):
        self.id = id
        self.name = name
        self.description = desc
        self.weight = weight
        self.interactions = interact
        self.value = value
        self.consumeable = consumeable

    def __str__(self):
        output = "--"+self.name+"--\n"
        output += self.description+"\n\n"
        output += "Waga: " + str(self.weight) + "\tWartość: "+str(self.value)+"\n"
        
        return output

class Armor(Item):
    def __init__(self, id, name, desc, weight, interact, value, defence, body_part):
        super().__init__(id, name, desc, weight, interact, value, False)
        self.defence = defence
        self.body_part = body_part

class Weapon(Item):
    def __init__(self, id, name, desc, weight, interact, value, damage, two_handed):
        super().__init__(id, name, desc, weight, interact, value, False)
        self.damage = damage
        self.two_handed = two_handed
