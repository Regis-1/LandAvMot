import copy

# Instance is class that represent 'chunk' of the world.
# This allow me to avoid loading whole game's content only
# for little use by the player. 
class Instance:
    def __init__(self, name):
        self.name = name
        self.locations = []
        self.armor = []
        self.weapons = []
        self.misc = []
        self.characters = []

    def get_item(self, item_id):
        if item_id[0] == "a":
            return copy.deepcopy(self.armor[int(item_id[1:])])
        elif item_id[0] == "w":
            return copy.deepcopy(self.weapons[int(item_id[1:])])
