from utils.config import SCREEN_WIDTH, SCREEN_HEIGHT


def init(w):
    w.data.logo = w.newImage(
        x = (SCREEN_WIDTH-340)/2,
        y = (SCREEN_HEIGHT-250)/2-100,
        filename = './assets/images/logo.png',
        new_width=340,
        new_height=250,
        isVisible=True,
        isPixelwiseModifiable=False
    )