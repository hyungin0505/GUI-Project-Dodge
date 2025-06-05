from utils.config import PLAYER_WIDTH, PLAYER_HEIGHT


def init(w):
    w.data.player = w.newImage(
        x = (1200-PLAYER_WIDTH)/2,
        y = (800-PLAYER_HEIGHT)/2,
        filename = './assets/images/player/player1.png',
        new_width=PLAYER_WIDTH,
        new_height=PLAYER_HEIGHT,
        isVisible=False,
        isPixelwiseModifiable=False
    )