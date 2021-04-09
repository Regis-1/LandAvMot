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

def inspect_item(win, player, location, item_name):
    #checks if item is in player's inventory
    try:
        item_id = next((i for i, x in enumerate(player.items) if item_name.lower() in x.name.lower()))    
        interface.print_description(win, player.items[item_id])
    except:
        #checks if item is in location's items
        try:
            item_id = next((i for i, x in enumerate(location.items) if item_name.lower() in x.name.lower()))
            interface.print_description(win, location.items[item_id])
        except:
            pass
    win.getch()

def user_action(win, player, instance, user_in):
    directions = ["east", "north", "west", "south", "up", "down"]
    
    #QUIT
    if user_in == "wyjdz":
        #save game and quit
        print("The End")
        quit()
    #MOVE
    elif user_in in directions:
        #make move to another location if possible
        next_loc = 0
        for i, d in enumerate(directions):
            if user_in == d:
                next_loc = i
        next_loc = instance.locations[player.curr_location].directions[next_loc]
        if next_loc is not None:
            player.curr_location = next_loc
    #TAKE ITEM
    elif re.search(r"^wez ([a-zA-Z0-9ąężźółńść]{4,}\s?\b)+$", user_in):
        take_item(instance.locations[player.curr_location], player, (user_in.split("wez "))[1])
    #EQUIPMENT
    elif user_in == "ekwipunek":
        show_equipment(win, player)
    #LOOK AT ITEM
    elif re.search(r"^obejrzyj ([a-zA-Z0-9ąężźółńść]{4,}\s?\b)+$", user_in): 
        inspect_item(win, player, instance.locations[player.curr_location], (user_in.split("obejrzyj "))[1])