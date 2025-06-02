from core import player, enemy, button
from core.debugger import d_print
from utils import config

def init(w):
    w.hideObject(w.data.play_button)
    w.hideObject(w.data.logo)
    config.game_started = 1
    w.showObject(w.data.player)
    d_print("Game Play Started")

def start(w, enemies):
    if config.game_started == 0 or config.game_started == 2:
        button.play(w)

    player.move(w)
    enemy.generate(w, enemies)
    for e in enemies:
        e.move(w, enemies)