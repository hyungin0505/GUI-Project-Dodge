import random
from utils import *
from core.debugger import d_print

class Enemy:
    def __init__(self, w, x=0, y=0, speed=0, direction_x=0, direction_y=0):
        self.speed = speed
        self.direction_x = direction_x
        self.direction_y = direction_y

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
    def move(self):
        self.x += self.direction_x