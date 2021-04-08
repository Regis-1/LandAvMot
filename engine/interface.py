import curses
import items
from locations import Location

def add_prompt(win):
    win.addstr(">> ")

def print_location_info(win, i, id):
    win.clear()
    win.addstr(i.locations[id].str_full_desc())
    win.addstr("\n")
    win.addstr(i.locations[id].str_directions())
    add_prompt(win)
    win.refresh()

def print_item_list(win, items, title=""):
    win.clear()
    if title:
        win.addstr("--"+title+"--\n")
    for i, item in enumerate(items):
        win.addstr(str(i+1)+". "+item.name+"\tWaga:"+str(item.weight)+
                   "\tWartość:"+str(item.value)+" monet\n")
    win.addstr("\n")
    add_prompt(win)
    win.refresh()

def print_description(win, obj):
    win.clear()
    win.addstr("--"+obj.name+"--\n")
    win.addstr(obj.description+"\n\n")
    if issubclass(type(obj), items.Item):
        win.addstr("Waga:"+str(obj.weight)+"\tWartość:"+str(obj.value)+" monet\n")
    add_prompt(win)
    win.refresh()