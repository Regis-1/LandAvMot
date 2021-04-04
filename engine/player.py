from characters import Character

class Player(Character):
    def __init__(self, name, max_hp, current_hp, items, attributes, curr_location, curr_instance, weight_cap):
        super().__init__(name, max_hp, current_hp, items, attributes)
        self.curr_location = curr_location
        self.curr_instance = curr_instance
        self.weight_cap = weight_cap
