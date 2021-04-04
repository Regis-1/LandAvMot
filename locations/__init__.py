# Class used to store data about place where player is or where he/she can be.
class Location:
    cardinal_directions = ["east", "north", "west", "south", "up", "down"]

    def __init__(self, id, name, desc, items, interest, interact, directions):
        self.id = id
        self.name = name
        self.description = desc
        self.items = items
        self.interesting = interest
        self.interactive = interact
        self.directions = directions

    def str_full_desc(self):
        return f"--{self.name}--\n{self.description}\n"

    def str_directions(self):
        output = "Wyjścia: "
        for i, d in enumerate(self.directions):
            if d is not None:
                output += self.cardinal_directions[i]+" "
            
        output += "\n"
        return output
