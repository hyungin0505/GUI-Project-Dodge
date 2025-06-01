def init(w):
    w.data.main_background = w.newImage(
        x = 0,
        y = 0,
        filename = './assets/images/background_sky.png',
        new_width=1200,
        new_height=800,
        isVisible=True,
        isPixelwiseModifiable=False
    )