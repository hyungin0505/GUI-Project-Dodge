from core import game
from core.debugger import d_print
from utils import config


def esc_input(w):
    if w.keys['Escape']:
        d_print("\033[93m[KeyBoard Input]\033[0mPressed 'Esc'")
        d_print("\033[96mExit Program\033[0m")
        w.stop()
    return

def enter_input(w):
    if w.keys['Return'] and config.game_started == 0:
        d_print("\033[93m[KeyBoard Input]\033[0mPressed 'Enter'")
        game.init(w)
    return

def cheat_input(w):
    if w.keys['Period'] and config.game_started == 1:
        d_print("\033[93m[KeyBoard Input]\033[0m Pressed '.'")
        config.god_mode = False
        d_print("\033[31m[Mode Changed]\033[0mSet GOD mode Off")
    if w.keys['Comma'] and config.game_started == 1:
        d_print("\033[93m[KeyBoard Input]\033[0m Pressed ','")
        config.god_mode = True
        d_print("\033[31m[Mode Changed]\033[0mSet GOD mode On")