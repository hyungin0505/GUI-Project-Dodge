import random
from utils import *
from core.debugger import d_print
from utils.config import difficulty, player_speed
from core.math import *

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

        if config.enemy_target_player:
            dx = w.getPosition(w.data.image_game_player)[0] - w.getPosition(self.image)[0]
            dy = w.getPosition(w.data.image_game_player)[1] - w.getPosition(self.image)[1]
        else:
            dx = w.getPosition(w.data.image_game_player)[0] - w.getPosition(self.image)[0] + random.randint(-100, 100)
            dy = w.getPosition(w.data.image_game_player)[1] - w.getPosition(self.image)[1] + random.randint(-100, 100)

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