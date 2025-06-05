from utils.config import SCREEN_WIDTH, SCREEN_HEIGHT, LOGO_WIDTH, LOGO_HEIGHT


def init(w):
    w.data.logo = w.newImage(
        x = (SCREEN_WIDTH-LOGO_WIDTH)/2,
        y = (SCREEN_HEIGHT-LOGO_HEIGHT)/2-100,
        filename = './assets/images/logo.png',
        new_width=LOGO_WIDTH,
        new_height=LOGO_HEIGHT,
        isVisible=True,
        isPixelwiseModifiable=False
    )