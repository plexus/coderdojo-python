WIDTH = 800
HEIGHT = 450

bal_x = 200
bal_y = 100
bal_straal = 25

def draw():
    screen.fill("blue")
    screen.draw.filled_circle((bal_x, bal_y), bal_straal, "beige")

import pgzrun
pgzrun.go()
