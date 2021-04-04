import items
import locations
import json

from engine.instance import Instance
from engine.player import Player

# Function used for loading specific object from json file
def load_for_instance(name, coll, t):
    path = ""
    if t is locations.Location:
        path = "locations/"
    elif t is items.Item:
        path = "items/"
    else:
        print("Unknown type to load!")

    data = None
    with open(path+name+".json", "r", encoding="utf-8") as rf:
        data = json.load(rf)
    for n in data:
        coll.append(t(*n.values()))

# Function used to load all necessary data instance class
def load_instance(name):
    i = Instance(name)
    load_for_instance(name, i.locations, locations.Location)

    return i

# Loading player data from player.json file
def load_player():
    data = None
    with open("characters/player.json", "r") as rf:
        data = json.load(rf)
    p = Player(*data.values())

    return p
