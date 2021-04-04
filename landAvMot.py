import curses

import items
import locations
import engine

WIN_COLS = 80
WIN_ROWS = 40

def main(stdscr):
    win = curses.newwin(WIN_ROWS, WIN_COLS, 0, 0)
    curses.echo()
    player = engine.load_player()
    instance = engine.load_instance("Prolog")
    while True:
        engine.printLocationInfo(win, str(instance.locations[player.curr_location]))
        usr_input = win.getstr()
        engine.user_action(player, instance, usr_input.decode(encoding="utf-8"))

curses.wrapper(main)