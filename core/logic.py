from core.debugger import d_print
from utils import config
from utils.config import COLLIDE_CORRECTION_VALUE


def is_collided(self, enemy, player):
    x1, y1 = enemy
    x2, y2 = player

    length1 = 16-COLLIDE_CORRECTION_VALUE
    length2 = 32-COLLIDE_CORRECTION_VALUE

    if (x1 < x2 + length2 and
            x1 + length1 > x2 and
            y1 < y2 + length2 and
            y1 + length1 > y2):
        if config.game_started == 1:
            d_print("\033[94m[Game Over]\033[0m Player is collided with enemies")
        return True
    return False