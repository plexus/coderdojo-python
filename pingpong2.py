WIDTH = 800
HEIGHT = 450

PADDLE_HEIGHT = 20
PADDLE_WIDTH = 80
PADDLE_LEVEL = 150
PADDLE_Y = HEIGHT - PADDLE_LEVEL - PADDLE_HEIGHT
PADDLE_SPEED = 5

LINE_WIDTH = 5

Red = (181, 4, 4)
White = (255, 255, 255)

paddle1_x = WIDTH/4 - PADDLE_WIDTH/2
paddle2_x = WIDTH*3/4 - PADDLE_WIDTH/2

def draw_paddle(x):
    screen.draw.filled_rect(Rect((x, y), (breedte, hoogte)), RED)

def draw_line():
    screen.draw.filled_rect(Rect((x, y), (breedte, hoogte)), RED)

def update():
    global paddle1_x, paddle2_x
    if keyboard[keys.LEFT]:
        paddle2_x = paddle2_x - PADDLE_SPEED

def draw():
    screen.fill((0,0,0))



paddle2_x = 535
paddle2_x = 530
