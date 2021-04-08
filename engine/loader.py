import items
import locations
import json

from engine.instance import Instance
from engine.player import Player

# Function used to load all necessary data instance class
def load_instance(name):
    inst = Instance(name)
    paths = ["items/", "locations/"]

    data = None
    for i, path in enumerate(paths):
        with open(path+name+".json", "r", encoding="utf-8") as rf:
            data = json.load(rf)
        if i == 0:
            for n in data:
                if n["id"][0] == "a":
                    inst.armor.append(items.Armor(*n.values()))
                elif n["id"][0] == "w":
                    inst.weapons.append(items.Weapon(*n.values()))
        elif i == 1:
            for n in data:
                tmp_items = []
                for loc_item in n["items"]:
                    tmp_items.append(inst.get_item(loc_item))
                n["items"] = tmp_items
                inst.locations.append(locations.Location(*n.values()))
    
    return inst

# Loading player data from player.json file
def load_player(instance):
    tmp_items = []
    data = None
    with open("characters/player.json", "r") as rf:
        data = json.load(rf)
    for loc_item in data["items"]:
        tmp_items.append(instance.get_item(loc_item))
    data["items"] = tmp_items
    p = Player(*data.values())

    return p
