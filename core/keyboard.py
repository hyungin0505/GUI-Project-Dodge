from core import game
from utils import config

def esc_input(w):
    if w.keys['Escape']:
        w.stop()
    return

def enter_input(w):
    if w.keys['Return'] and config.game_started == 0:
        game.init(w)
    # if w.keys['Return'] and config.game_started == 2:
    #     from utils.config import SCREEN_WIDTH, SCREEN_HEIGHT
    #     from gui_project import initialize, update
    #     import gui_core as gui
    #
    #     w1 = gui.Window(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    #     w1.initialize = initialize
    #     w1.update = update
    #     w1.start()
    return