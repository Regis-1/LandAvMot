import items
import locations
import json

from engine.instance import Instance
from engine.player import Player

# Function used for loading specific object from json file
def load_for_instance(name, coll, t, prefix=""):
    path = ""
    if t is locations.Location:
        path = "locations/"
    elif issubclass(t, items.Item):
        path = "items/"
    else:
        print("Unknown type to load!")

    data = None
    with open(path+name+".json", "r", encoding="utf-8") as rf:
        data = json.load(rf)
    if issubclass(t, items.Item):
        for n in data:
            if n["id"][0] == prefix:
                coll.append(t(*n.values()))
    else:
        for n in data:
            coll.append(t(*n.values()))

# Function used to load all necessary data instance class
def load_instance(name):
    i = Instance(name)
    load_for_instance(name, i.locations, locations.Location)
    load_for_instance(name, i.items, items.Armor, "a")
    load_for_instance(name, i.items, items.Weapon, "w")

    return i

# Loading player data from player.json file
def load_player():
    data = None
    with open("characters/player.json", "r") as rf:
        data = json.load(rf)
    p = Player(*data.values())

    return p
