from core.debugger import d_print
from utils import *

def game_start(w):
    if w.mouse_buttons[1]:
        d_print("Mouse 1 Clicked. ({}, {})".format(w.mouse_position_x, w.mouse_position_y))
        if (450 <= w.mouse_position_x <= 750) and (400 <= w.mouse_position_y <= 500) and  config.game_started == 0:
            d_print("Game Play Button Clicked.")
            w.hideObject(w.data.image_main_button_play)
            config.game_started = 1