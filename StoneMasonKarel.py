from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
Karel will repair pre-existing columns,
placing a beeper in every corner of the pre-existing columns.
"""

def main():
    while front_is_clear():
        repair_column()
        move_to_next()
    repair_column()

# pre: Karel is at the southern wall, facing east, at the bottom of a broken column.
# post: Karel is at the southern wall, facing east, at the bottom of a fixed column.

def repair_column():
    turn_left()
    while front_is_clear():
        repair_stone()
    if no_beepers_present():
        put_beeper()
    turn_around()
    move_to_wall()
    turn_left()

def repair_stone():
    if no_beepers_present():
        put_beeper()
    else:
        move()

# pre: Karel is at the southern wall, facing east.
# post: Karel is at the southern wall, facing east, 4 spaces further east.

def move_to_next():
    if front_is_clear():
        for i in range(4):
            move()

def turn_around():
    turn_left()
    turn_left()

def move_to_wall():
    while front_is_clear():
        move()

if __name__ == "__main__":
    run_karel_program()
