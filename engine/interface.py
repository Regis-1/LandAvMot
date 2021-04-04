import curses

def printLocationInfo(win, i, id):
    win.clear()
    win.addstr(i.locations[id].str_full_desc())
    if len(i.locations[id].items) > 0:
        win.addstr(i.str_loc_items(id))
    win.addstr("\n")
    win.addstr(i.locations[id].str_directions())
    win.addstr(">> ")
    win.refresh()