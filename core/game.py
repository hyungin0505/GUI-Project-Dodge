from core import player, enemy, button, title
from core.debugger import d_print
from utils import config

def init(w):
    w.hideObject(w.data.play_button)
    w.hideObject(w.data.logo)
    config.game_started = 1
    w.showObject(w.data.player)
    d_print("\033[96mGame Play Started\033[0m")

def start(w, enemies):
    if config.game_started == 0 or config.game_started == 2:
        button.is_clicked(w)
    else:
        player.move(w)
        enemy.generate(w, enemies)
    for e in enemies:
            e.move(w, enemies)
    title.isGod(w)