from utils.config import SCREEN_WIDTH, SCREEN_HEIGHT


def init(w):
    w.data.main_background = w.newImage(
        x = 0,
        y = 0,
        filename = './assets/images/background_sky.png',
        new_width=SCREEN_WIDTH,
        new_height=SCREEN_HEIGHT,
        isVisible=True,
        isPixelwiseModifiable=False
    )