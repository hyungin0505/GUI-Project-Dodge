from core import player, enemy, button
from utils.config import game_started


def start(w, enemies):
    if not game_started:
        button.play(w)

    player.move(w)
    enemy.generate(w, enemies)
    for e in enemies:
        e.move(w, enemies)