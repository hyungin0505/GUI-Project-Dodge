game_started = False

def main_page_init(w):
    # 배경 이미지
    w.data.image_main_background = w.newImage(
        x = 0,
        y = 0,
        filename = './assets/images/background_sky.png',
        new_width=1200,
        new_height=800,
        isVisible=True,
        isPixelwiseModifiable=False
    )

    # 게임 시작 버튼
    w.data.image_main_button_play = w.newImage(
        x = 450,
        y = 400,
        filename = './assets/images/main_play_button.png',
        new_width=300,
        new_height=100,
        isVisible=True,
        isPixelwiseModifiable=False
    )

    return w.data.image_main_background, w.data.image_main_button_play