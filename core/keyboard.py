from core import game
from core.debugger import d_print
from utils import config


def esc_input(w):
    if w.keys['Escape']:
        w.stop()
    return

def enter_input(w):
    if w.keys['Return'] and config.game_started == 0:
        game.init(w)
    return

def cheat_input(w):
    if w.keys['Slash'] and config.game_started == 1:
        d_print("[KeyBoard Input] Pressed '/'")
        if config.god_mode:
            config.god_mode = False
            d_print("GOD mode off")
        else:
            config.god_mode = True
            d_print("GOD mode on")