def user_action(player, instance, user_in):
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