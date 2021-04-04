import curses

def printLocationInfo(win, loc):
    win.clear()
    win.addstr(loc)
    win.addstr(">> ")
    win.refresh()