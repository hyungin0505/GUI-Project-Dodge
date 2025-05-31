from core.debugger import d_print
from utils import config
from utils.config import player_speed, SCREEN_WIDTH, SCREEN_HEIGHT


def move(w):
    if config.game_started == 1:
        x, y = w.getPosition(w.data.image_game_player)

        if w.keys['w'] and not w.keys['s']:
            y = w.getPosition(w.data.image_game_player)[1]
            if y >= 0-16:
                y -= player_speed
            d_print("[KeyBoard Input] Pressed 'w'.")
        if w.keys['s'] and not w.keys['w']:
            y = w.getPosition(w.data.image_game_player)[1]
            if y <= SCREEN_HEIGHT-16:
                y += player_speed
            d_print("[KeyBoard Input] Pressed 's'.")
        if w.keys['a'] and not w.keys['d']:
            x = w.getPosition(w.data.image_game_player)[0]
            if x >= 0-16:
                x -= player_speed
            d_print("[KeyBoard Input] Pressed 'a'.")
        if w.keys['d'] and not w.keys['a']:
            x = w.getPosition(w.data.image_game_player)[0]
            if x <= SCREEN_WIDTH-16:
                x += player_speed
            d_print("[KeyBoard Input] Pressed 'd'.")

        w.moveObject(w.data.image_game_player, new_x=x, new_y=y)
        d_print("[Player Moved] Player is to ({}, {}).".format(x, y))