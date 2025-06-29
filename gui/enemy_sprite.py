import random
from utils import config
from core.debugger import d_print
from utils.config import SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_WIDTH, ENEMY_HEIGHT, PLAYER_TARGET_RANGE, ENEMY_TARGET_PLAYER, ENEMY_SPEED
from math import sqrt
from core import logic

class Enemy:
    def __init__(self, w, x=0, y=0, speed=config.ENEMY_SPEED):
        self.x = x
        self.y = y
        self.speed = speed

        edge = random.choice(['top', 'bottom', 'left', 'right'])
        if edge == 'top':
            self.x = random.randint(0-16, SCREEN_WIDTH)
            self.y = 0-16
        elif edge == 'bottom':
            self.x = random.randint(0-16, SCREEN_WIDTH)
            self.y = SCREEN_HEIGHT
        elif edge == 'left':
            self.x = 0-16
            self.y = random.randint(0-16, SCREEN_HEIGHT)
        elif edge == 'right':
            self.x = SCREEN_WIDTH
            self.y = random.randint(0-16, SCREEN_HEIGHT)
        d_print("\033[92m[Enemy Spawned]\033[0m Enemy is on {}. ({}, {})".format(edge, self.x, self.y))

        self.image = w.newImage(
            x=self.x,
            y=self.y,
            filename='./assets/images/enemies/enemy1.png',
            new_width=ENEMY_WIDTH,
            new_height=ENEMY_HEIGHT,
            isVisible=True,
            isPixelwiseModifiable=False,
        )

        target_offset = 0 if ENEMY_TARGET_PLAYER else random.randint(-PLAYER_TARGET_RANGE, PLAYER_TARGET_RANGE)
        dx = w.getPosition(w.data.player)[0] - w.getPosition(self.image)[0] + target_offset
        dy = w.getPosition(w.data.player)[1] - w.getPosition(self.image)[1] + target_offset

        distance = sqrt(dx * dx + dy * dy)
        self.speed_x = (dx/distance)*ENEMY_SPEED
        self.speed_y = (dy/distance)*ENEMY_SPEED

    def move(self, w, enemies):
        new_x = w.getPosition(self.image)[0] + self.speed_x
        new_y = w.getPosition(self.image)[1] + self.speed_y

        w.moveObject(self.image,new_x=new_x,new_y=new_y)

        if -ENEMY_WIDTH > w.getPosition(self.image)[0] or w.getPosition(self.image)[0] > SCREEN_WIDTH + ENEMY_WIDTH or -ENEMY_HEIGHT > w.getPosition(self.image)[1] or w.getPosition(self.image)[1] > SCREEN_HEIGHT + ENEMY_HEIGHT:
            enemies.remove(self)
            w.deleteObject(self.image)
            d_print("\033[92m[Enemy Event]\033[0m Enemy Deleted")

        if logic.is_collided(self, w.getPosition(self.image), w.getPosition(w.data.player)) and config.god_mode != True:
            w.showObject(w.data.game_over)
            w.hideObject(w.data.player)
            w.raiseObject(w.data.game_over)
            w.setTitle("Game Over... Enemies: {}".format(config.enemy_count))
            config.game_started = 2
