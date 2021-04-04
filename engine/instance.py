# Instance is class that represent 'chunk' of the world.
# This allow me to avoid loading whole game's content only
# for little use by the player. 
class Instance:
    def __init__(self, name):
        self.name = name
        self.locations = []
        self.items = []
        self.characters = []

    def str_loc_items(self, id):
        output = "Przedmioty w pobliżu:\n"
        for item1 in self.locations[id].items:
            for item2 in self.items:
                if item1 == item2.id:
                    output += "\t"+item2.name+"\n"

        return output