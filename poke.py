from pygame import Color

WIDTH = 800
HEIGHT = 450

ball_x = 200
ball_y = 100

MIDDELIJN_BREEDTE = 6

def draw():
    screen.fill(Color("blue"))
    screen.draw.filled_circle((ball_x, ball_y), 20, Color("seagreen1"))

    middelijn = Rect((WIDTH/2 - MIDDELIJN_BREEDTE/2, 0), (MIDDELIJN_BREEDTE, HEIGHT))
    screen.draw.filled_rect(middelijn, Color("seagreen1"))

def ball_paddle_collision(paddle_x):
    global ball_x, ball_y
    if ball_x < paddle_x:
       test_x = paddle_x
    elif ball_x > paddle_x + PADDLE_BREEDTE:
       test_x = paddle_x + PADDLE_BREEDTE
    else:
       test_x = ball_x
    afstand = math.sqrt((ball_x-test_x)**2 + (ball_y - paddle_y)**2)
    return afstand < BALL_GROOTTE

ball_vx = 1
ball_vy = 0

def update():
    global ball_x, ball_y
    ball_x = ball_x + ball_vx
    ball_y = ball_y + ball_vy
    if ball_paddle_collision(paddle1_x, PADDLE_Y):
       ball_vx = -ball_vx
       ball_vy = 5
    if ball_paddle_collision(paddle2_x, PADDLE_Y):
       ball_vx = -ball_vx
       ball_vy = -5


import pgzrun
pgzrun.go()
