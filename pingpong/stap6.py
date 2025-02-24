WIDTH = 800
HEIGHT = 450

bal_x = 200
bal_y = 100
bal_straal = 25
bal_vx = 5
bal_vy = 0

middelijn_breedte = 10

pad_breedte = 100
pad_hoogte = 20
pad_y = 400

pad1_x = 150
pad2_x = 550

def teken_rechthoek(x, y, breedte, hoogte, kleur):
    plaats = (x, y)
    afmeting = (breedte, hoogte)
    rechthoek = Rect(plaats, afmeting)
    screen.draw.filled_rect(rechthoek, kleur)

def draw():
    screen.fill("blue")
    screen.draw.filled_circle((bal_x, bal_y), bal_straal, "beige")
    teken_rechthoek(WIDTH/2-middelijn_breedte/2, 0, middelijn_breedte, HEIGHT, "beige")
    teken_rechthoek(pad1_x, pad_y, pad_breedte, pad_hoogte, "beige")
    teken_rechthoek(pad2_x, pad_y, pad_breedte, pad_hoogte, "beige")

def update():
    global bal_x, bal_y
    bal_x = bal_x + bal_vx
    bal_y = bal_y + bal_vy

import pgzrun
pgzrun.go()
