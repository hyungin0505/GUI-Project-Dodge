from core.debugger import d_print
from utils import config
from utils.config import PLAYER_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_HEIGHT, PLAYER_WIDTH
from core import keyboard


def move(w):
    if config.game_started == 1:
        x, y = w.getPosition(w.data.player)

        if w.keys['w'] and not w.keys['s']:
            y = w.getPosition(w.data.player)[1]
            if y >= 0-PLAYER_HEIGHT/2:
                y -= PLAYER_SPEED
            d_print("\033[93m[KeyBoard Input]\033[0m Pressed 'w'.")
            d_print("\033[90m[Player Moved] Player is to ({}, {}).\033[0m".format(x, y))
        if w.keys['s'] and not w.keys['w']:
            y = w.getPosition(w.data.player)[1]
            if y <= SCREEN_HEIGHT-PLAYER_HEIGHT/2:
                y += PLAYER_SPEED
            d_print("\033[93m[KeyBoard Input]\033[0m Pressed 's'.")
            d_print("\033[90m[Player Moved] Player is to ({}, {}).\033[0m".format(x, y))
        if w.keys['a'] and not w.keys['d']:
            x = w.getPosition(w.data.player)[0]
            if x >= 0-PLAYER_WIDTH/2:
                x -= PLAYER_SPEED
            d_print("\033[93m[KeyBoard Input]\033[0m Pressed 'a'.")
            d_print("\033[90m[Player Moved] Player is to ({}, {}).\033[0m".format(x, y))
        if w.keys['d'] and not w.keys['a']:
            x = w.getPosition(w.data.player)[0]
            if x <= SCREEN_WIDTH-PLAYER_WIDTH/2:
                x += PLAYER_SPEED
            d_print("\033[93m[KeyBoard Input]\033[0m Pressed 'd'.")
            d_print("\033[90m[Player Moved] Player is to ({}, {}).\033[0m".format(x, y))

        w.moveObject(w.data.player, new_x=x, new_y=y)
        keyboard.cheat_input(w)