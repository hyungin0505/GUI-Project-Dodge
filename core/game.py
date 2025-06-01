from core import player, enemy, button
from core.debugger import d_print
from utils import config

def init(w):
    w.hideObject(w.data.play_button)
    w.hideObject(w.data.logo)
    config.game_started = True
    w.showObject(w.data.player)
    d_print("Game Play Started")

def start(w, enemies):
    if not config.game_started:
        button.play(w)

    player.move(w)
    enemy.generate(w, enemies)
    for e in enemies:
        e.move(w, enemies)