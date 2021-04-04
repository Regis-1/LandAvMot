# Instance is class that represent 'chunk' of the world.
# This allow me to avoid loading whole game's content only
# for little use by the player. 
class Instance:
    def __init__(self, name):
        self.name = name
        self.locations = []
        self.items = []
        self.characters = []