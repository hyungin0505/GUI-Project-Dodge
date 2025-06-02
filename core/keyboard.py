from core import game
from utils import config

def esc_input(w):
    if w.keys['Escape']:
        w.stop()
    return

def enter_input(w):
    if w.keys['Return'] and config.game_started == 0:
        game.init(w)
    return