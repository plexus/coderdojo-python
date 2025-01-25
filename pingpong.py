# pgzrun pingpong.py
import pygame
import math

WIDTH = 800
HEIGHT = 450

YELLOW = pygame.Color("#e0da63")
BLUE = pygame.Color("#306097")
RED = pygame.Color("#D24D3A")
ORANGE = pygame.Color("#DC9F42")
GREEN = pygame.Color("#3BB44C")

LINE_WIDTH = 6
PADDLE_HEIGHT = 20
PADDLE_WIDTH = 120
PADDLE_LEVEL = 30
PADDLE_SPEED = 3.0
BALL_SIZE = 10
GRAVITY = 0.07
BOUNCE_ANGLE_FACTOR = 4
PADDLE_DEAD_POINT = PADDLE_WIDTH/2 - PADDLE_WIDTH/5
BALL_START_X = WIDTH/4 - PADDLE_DEAD_POINT
BALL_START_Y = HEIGHT/4

paddle_y = HEIGHT - PADDLE_LEVEL - PADDLE_HEIGHT
paddle1_x = WIDTH/4
paddle2_x = 3*WIDTH/4

ball_x = BALL_START_X
ball_y = BALL_START_Y
ball_vx = 0
ball_vy = 0

def draw_background():
    screen.fill(YELLOW)

def draw_middle_line(width, height):
    x = (width - LINE_WIDTH) / 2
    for i in range(LINE_WIDTH):
      screen.draw.line((x+i, 0), (x+i, height), BLUE)

def draw_paddle(height, x):
    rect = Rect((x - (PADDLE_WIDTH/2), paddle_y),
                (PADDLE_WIDTH, PADDLE_HEIGHT))
    screen.draw.filled_rect(rect, RED)

def draw_ball(x, y):
    screen.draw.filled_circle((x, y), BALL_SIZE, GREEN)

def update_ball():
    global ball_x, ball_y, ball_vy
    ball_x = ball_x + ball_vx
    ball_y = ball_y + ball_vy
    ball_vy += GRAVITY

def update_paddles():
    global paddle1_x, paddle2_x
    width, height = pygame.display.get_surface().get_size()

    if keyboard[keys.LEFT]:
        paddle2_x -= PADDLE_SPEED
    if keyboard[keys.RIGHT]:
        paddle2_x += PADDLE_SPEED
    if keyboard[keys.X]:
        paddle1_x -= PADDLE_SPEED
    if keyboard[keys.C]:
        paddle1_x += PADDLE_SPEED

    paddle1_x = max(PADDLE_WIDTH/2, paddle1_x)
    paddle1_x = min((width-LINE_WIDTH-PADDLE_WIDTH)/2, paddle1_x)
    paddle2_x = max((width+LINE_WIDTH+PADDLE_WIDTH)/2, paddle2_x)
    paddle2_x = min(width - PADDLE_WIDTH/2, paddle2_x)

def ball_paddle_collision_check(bx, by, px, py):
    paddle_left = px - PADDLE_WIDTH/2
    paddle_right = px + PADDLE_WIDTH/2
    tx = bx
    if bx < paddle_left:
      tx = paddle_left
    if bx > paddle_right:
      tx = paddle_right
    dist = math.sqrt((bx-tx)**2 + (by-py)**2)
    return dist < BALL_SIZE

def bounce_ball():
    global ball_vx, ball_vy
    if ball_paddle_collision_check(ball_x, ball_y, paddle1_x, paddle_y):
        ball_vy = - ball_vy
        ball_vx = (ball_x - paddle1_x + PADDLE_DEAD_POINT) * BOUNCE_ANGLE_FACTOR/100
    if ball_paddle_collision_check(ball_x, ball_y, paddle2_x, paddle_y):
        ball_vy = - ball_vy
        ball_vx = (ball_x - paddle2_x - PADDLE_DEAD_POINT) * BOUNCE_ANGLE_FACTOR/100

def check_out_of_bounds():
    global ball_x, ball_y, ball_vx, ball_vy
    if ball_x < 0 or ball_x > WIDTH or ball_y < 0 or ball_y > HEIGHT:
        ball_x = BALL_START_X
        ball_y = BALL_START_Y
        ball_vx = 0
        ball_vy = 0

############################################

def update():
    update_ball()
    update_paddles()
    bounce_ball()
    check_out_of_bounds()

def draw():
    width, height = pygame.display.get_surface().get_size()
    draw_background()
    draw_middle_line(width, height)
    draw_paddle(height, paddle1_x)
    draw_paddle(height, paddle2_x)
    draw_ball(ball_x, ball_y)
