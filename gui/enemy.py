import random
from utils import *

class Enemy:
    def __init__(self, w, x=0, y=0, speed=0, direction_x=0, direction_y=0):
        self.speed = speed
        self.direction_x = direction_x
        self.direction_y = direction_y

        edge = random.choice(['top', 'bottom', 'left', 'right'])
        if edge == 'top':
            self.x = random.randint(0, SCREEN_WIDTH)
            self.y = 0
        elif edge == 'bottom':
            self.x = random.randint(0, SCREEN_WIDTH)
            self.y = SCREEN_HEIGHT
        elif edge == 'left':
            self.x = 0
            self.y = random.randint(0, SCREEN_HEIGHT)
        else:
            self.x = SCREEN_WIDTH
            self.y = random.randint(0, SCREEN_HEIGHT)

        self.image = w.newImage(
            x=self.x,
            y=self.y,
            filename='./assets/images/enemy.png',
            new_width=32,
            new_height=32,
            isVisible=True,
            isPixelwiseModifiable=False,
        )