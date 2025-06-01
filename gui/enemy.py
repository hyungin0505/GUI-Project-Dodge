import random
from utils import *
from core.debugger import d_print
from utils.config import difficulty, player_speed

def abs(x):
    return x if x >= 0 else -x

def sqrt(x, tolerance=1e-15, max_iterations=100):
    if x < 0:
        raise ValueError("math domain error")

    if x == 0:
        return 0.0

    guess = x / 2.0
    for _ in range(max_iterations):
        new_guess = 0.5 * (guess + x / guess)
        if abs(new_guess - guess) < tolerance:
            return new_guess
        guess = new_guess

    return guess

class Enemy:
    def __init__(self, w, x=0, y=0, speed=player_speed):
        self.x = x
        self.y = y
        self.speed = speed

        edge = random.choice(['top', 'bottom', 'left', 'right'])
        if edge == 'top':
            self.x = random.randint(0-8, SCREEN_WIDTH-8)
            self.y = 0-8
            d_print("[Enemy Spawned] Enemy is on top. ({}, {})".format(self.x, self.y))
        elif edge == 'bottom':
            self.x = random.randint(0-8, SCREEN_WIDTH-8)
            self.y = SCREEN_HEIGHT-8
            d_print("[Enemy Spawned] Enemy is on bottom. ({}, {})".format(self.x, self.y))
        elif edge == 'left':
            self.x = 0-8
            self.y = random.randint(0-8, SCREEN_HEIGHT-8)
            d_print("[Enemy Spawned] Enemy is on left. ({}, {})".format(self.x, self.y))
        elif edge == 'right':
            self.x = SCREEN_WIDTH-8
            self.y = random.randint(0-8, SCREEN_HEIGHT-8)
            d_print("[Enemy Spawned] Enemy is on right. ({}, {})".format(self.x, self.y))

        self.image = w.newImage(
            x=self.x,
            y=self.y,
            filename='./assets/images/enemy.png',
            new_width=16,
            new_height=16,
            isVisible=True,
            isPixelwiseModifiable=False,
        )
        dx = w.getPosition(w.data.image_game_player)[0] - w.getPosition(self.image)[0]
        dy = w.getPosition(w.data.image_game_player)[1] - w.getPosition(self.image)[1]
        distance = sqrt(dx * dx + dy * dy)
        self.speed_x = (dx/distance)*player_speed
        self.speed_y = (dy/distance)*player_speed


    def move(self, w, enemies):
        new_x = w.getPosition(self.image)[0] + self.speed_x
        new_y = w.getPosition(self.image)[1] + self.speed_y

        w.moveObject(self.image,new_x=new_x,new_y=new_y)

        if -32 > w.getPosition(self.image)[0] or w.getPosition(self.image)[0] > SCREEN_WIDTH + 32 or -32 > w.getPosition(self.image)[1] or w.getPosition(self.image)[1] > SCREEN_HEIGHT + 32:
            enemies.remove(self)
            w.deleteObject(self.image)
            d_print("[Enemy Event] Enemy Deleted")

        d_print("[Enemy Moved] Enemy Moved to ({}, {})".format(self.x, self.y))