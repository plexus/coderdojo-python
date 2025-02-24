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

punten1 = 0
punten2 = 0

game_over = False

def teken_rechthoek(x, y, breedte, hoogte, kleur):
    plaats = (x, y)
    afmeting = (breedte, hoogte)
    rechthoek = Rect(plaats, afmeting)
    screen.draw.filled_rect(rechthoek, kleur)

def draw():
    if game_over:
        screen.fill("beige")
        screen.draw.text("GAME OVER", centerx=WIDTH/2, centery=HEIGHT/2, color="blue", fontsize=150)
        if punten1 > punten2:
            screen.draw.text("Player 1 WINS", centerx=WIDTH/2, centery=HEIGHT/2+100, color="blue", fontsize=100)
        else:
            screen.draw.text("Player 2 WINS", centerx=WIDTH/2, centery=HEIGHT/2+100, color="blue", fontsize=100)
    else:
        screen.fill("blue")
        screen.draw.filled_circle((bal_x, bal_y), bal_straal, "beige")
        teken_rechthoek(WIDTH/2-middelijn_breedte/2, 0, middelijn_breedte, HEIGHT, "beige")
        teken_rechthoek(pad1_x, pad_y, pad_breedte, pad_hoogte, "beige")
        teken_rechthoek(pad2_x, pad_y, pad_breedte, pad_hoogte, "beige")
        screen.draw.text(str(punten1), (20, 20), fontsize=100, color="beige")
        screen.draw.text(str(punten2), topright=(WIDTH-20, 20), fontsize=100, color="beige")

def afstand(x1, x2, y1, y2):
    return sqrt((x1-y1)**2 + (x2-y2)**2)

def botst_bal(pad_x_links):
    pad_x_rechts = pad_x_links + pad_breedte
    pad_x_test = min(max(bal_x, pad_x_links), pad_x_rechts)
    return bal_straal > afstand(bal_x, bal_y, pad_x_test, pad_y)

def reset_bal():
    global bal_x, bal_y, bal_vx, bal_vy
    bal_x = 200
    bal_y = 100
    bal_vx = 0
    bal_vy = 0

def update_game():
    global bal_x, bal_y, bal_vx, bal_vy, pad1_x, pad2_x, punten1, punten2, game_over

    if botst_bal(pad1_x):
        bal_vx = (bal_x-pad1_x)/50 + random.uniform(0.5, 1)
        bal_vy = -bal_vy
    if botst_bal(pad2_x):
        bal_vx = -(pad2_x+pad_breedte-bal_x)/50 - random.uniform(0.5, 1)
        bal_vy = -bal_vy

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

    pad1_x = min(pad1_x, WIDTH/2 - middelijn_breedte/2 - pad_breedte)
    pad2_x = max(pad2_x, WIDTH/2 + middelijn_breedte/2)

    if bal_y + bal_straal > HEIGHT:
        reset_bal()
        if bal_x < 0:
            punten1 += 1
        elif bal_x < WIDTH/2:
            punten2 += 1
        elif bal_x < WIDTH:
            punten1 += 1
        else:
            punten2 += 1
    if (punten1 > 3) or (punten2 > 3):
        game_over = True

def update():
    global game_over
    if game_over:
        if keyboard[keys.RETURN] or keyboard[keys.SPACE]:
            punten1=0
            punten2=0
            reset_bal()
            game_over = False
    else:
        update_game()

reset_bal()
import pgzrun
pgzrun.go()
