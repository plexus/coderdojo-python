from math import sqrt
import random

WIDTH = 800
HEIGHT = 450

bal_x = 200
bal_y = 100
bal_straal = 25
bal_vx = 0
bal_vy = 0
bal_g = 0.1

middelijn_breedte = 10

pad_breedte = 100
pad_hoogte = 20
pad_y = 400

pad1_x = 150
pad2_x = 550
pad_v = 5

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

def afstand(x1, x2, y1, y2):
    return sqrt((x1-y1)**2 + (x2-y2)**2)

def botst_bal(pad_x_links):
    pad_x_rechts = pad_x_links + pad_breedte
    pad_x_test = min(max(bal_x, pad_x_links), pad_x_rechts)
    return bal_straal > afstand(bal_x, bal_y, pad_x_test, pad_y)

def update():
    global bal_x, bal_y, bal_vx, bal_vy, pad1_x, pad2_x
    bal_x = bal_x + bal_vx
    bal_y = bal_y + bal_vy

    bal_vy = bal_vy + bal_g

    if keyboard[keys.X]:
        pad1_x = pad1_x - pad_v
    if keyboard[keys.C]:
        pad1_x = pad1_x + pad_v
    if keyboard[keys.LEFT]:
        pad2_x = pad2_x - pad_v
    if keyboard[keys.RIGHT]:
        pad2_x = pad2_x + pad_v

    if botst_bal(pad1_x):
        bal_vx = random.uniform(1, 3)
        bal_vy = -bal_vy
    if botst_bal(pad2_x):
        bal_vx = -random.uniform(1, 3)
        bal_vy = -bal_vy

import pgzrun
pgzrun.go()
