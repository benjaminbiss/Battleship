# Battleship
The game Battleship in python


# Rough UML
main.py
    gamespace.py
        player.py
            gameboard.py
            ship.py
                aircraft_carrier.py 'A'
                battleship.py   'B'
                submarine.py    'S'
                destroyer.py    'D'

- import getPass - used to mask inputs
- print a version of the board that does not show ship locations
- maybe, use a table display tool

# 2d list

        grid[y][x] - print each row to show table

      x -  1    2    3...
    y
    -
    a    [a1,  a2,  a3]
    b    [b1,  b2,  b3]
    c    [c1,  c2,  c3]

    Table legend:

    w : water
    a : aircraft carrier
    b : battleship
    s : submarine
    d : destroyer

    ''x : ship hit
    m : water hit/ miss