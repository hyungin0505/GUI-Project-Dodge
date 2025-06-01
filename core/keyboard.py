from core import game


def esc_input(w):
    if w.keys['Escape']:
        w.stop()
    return

def enter_input(w):
    if w.keys['Return']:
        game.init(w)
    return