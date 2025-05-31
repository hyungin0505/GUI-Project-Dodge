from core.debugger import d_print
from utils import config

def check_play_button_clicked(w):
    if w.mouse_buttons[1]:
        d_print("Mouse 1 Clicked. ({}, {})".format(w.mouse_position_x, w.mouse_position_y))
        if (w.getPosition(w.data.image_main_button_play)[0]
            <= w.mouse_position_x
            <= w.getPosition(w.data.image_main_button_play)[0]+w.getSize(w.data.image_main_button_play)[0]
        ) and (w.getPosition(w.data.image_main_button_play)[1]
               <= w.mouse_position_y
               <= w.getPosition(w.data.image_main_button_play)[1]+w.getSize(w.data.image_main_button_play)[1]
        ) and  config.game_started == 0:
            d_print("Game Play Button Clicked.")
            w.hideObject(w.data.image_main_button_play)
            config.game_started = 1
            w.showObject(w.data.image_game_player)