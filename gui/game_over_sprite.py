from utils.config import GAME_OVER_WIDTH, GAME_OVER_HEIGHT, SCREEN_HEIGHT, SCREEN_WIDTH


def init(w):
    w.data.game_over = w.newImage(
        x = (SCREEN_WIDTH-GAME_OVER_WIDTH)/2,
        y = (SCREEN_HEIGHT-GAME_OVER_HEIGHT)/2,
        filename= './assets/images/game_over.png',
        new_width=GAME_OVER_WIDTH,
        new_height=GAME_OVER_HEIGHT,
        isVisible=False,
        isPixelwiseModifiable=False
    )