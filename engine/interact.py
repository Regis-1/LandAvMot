import re
from engine import interface

def take_item(location, player, item_name):
     #find first occurence with given by user string
     item_id = next(i for i, x in enumerate(location.items) if item_name.lower() in x.name.lower())
     player.items.append(location.items[item_id])
     del location.items[item_id]

def show_equipment(win, player):
    interface.print_item_list(win, player.items, "Ekwipunek")
    win.getch()

def inspect_item(win, player, item_name):
    try:
        item_id = next((i for i, x in enumerate(player.items) if item_name.lower() in x.name.lower()), False)
        interface.print_description(win, player.items[item_id])
        win.getch()
    except:
        pass

def user_action(win, player, instance, user_in):
    directions = ["east", "north", "west", "south", "up", "down"]
    
    if user_in == "wyjdz":
        #save game and quit
        print("The End")
        quit()
    elif user_in in directions:
        #make move to another location if possible
        next_loc = 0
        for i, d in enumerate(directions):
            if user_in == d:
                next_loc = i
        next_loc = instance.locations[player.curr_location].directions[next_loc]
        if next_loc is not None:
            player.curr_location = next_loc
    elif re.search(r"^wez ([a-zA-Z0-9ąężźółńść]{4,}\s?\b)+$", user_in):
        take_item(instance.locations[player.curr_location], player, (user_in.split("wez "))[1])
    elif user_in == "ekwipunek":
        show_equipment(win, player)
    elif re.search(r"^obejrzyj ([a-zA-Z0-9ąężźółńść]{4,}\s?\b)+$", user_in): 
        inspect_item(win, player, (user_in.split("obejrzyj "))[1])