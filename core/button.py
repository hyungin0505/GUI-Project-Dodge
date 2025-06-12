from core.debugger import d_print
from core import game, keyboard
from utils import config

def play(w):
    if w.mouse_buttons[1]:
        d_print("\033[96mMouse 1 Clicked. ({}, {})\033[0m".format(w.mouse_position_x, w.mouse_position_y))
        if (w.getPosition(w.data.play_button)[0]
            <= w.mouse_position_x
            <= w.getPosition(w.data.play_button)[0] + w.getSize(w.data.play_button)[0]
        ) and (
                w.getPosition(w.data.play_button)[1]
                <= w.mouse_position_y
                <= w.getPosition(w.data.play_button)[1] + w.getSize(w.data.play_button)[1]
        ) and  not config.game_started:
            game.init(w)
    keyboard.enter_input(w)