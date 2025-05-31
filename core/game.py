import random

from core.button import check_play_button_clicked
from core.enemy import make_enemy
from core import player

def game_start(w, enemies):
    check_play_button_clicked(w)

    player.move(w)

    make_enemy(w, enemies)

    for e in enemies:
        e.move(w, enemies)