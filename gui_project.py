'''
gui 모듈을 사용하기 위한 기본 구조를 미리 적어 둔 파일입니다.

- 여러분은 이 아래에 있는, 함수 initialize()와 update()에 대한
  함수 정의 내용물을 구성함으로써 프로그램을 구성해야 해요

- 중간중간 F5를 눌러 interactive를 켜 둔 다음 진행하면
  IDLE이 함수 호출식 적을 때마다 적당한 툴팁을 읽어 보여줄 거예요
'''

import gui_core as gui

w = gui.Window(width=1200, height=800)


def initialize(timestamp):
    '적절한 설명 메시지'
    # 배경 이미지
    w.data.image_main_background = w.newImage(
        x = 0, 
        y = 0, 
        filename = './images/background_sky.png', 
        new_width=1200, 
        new_height=800, 
        isVisible=True, 
        isPixelwiseModifiable=False
       )

    # 게임 시작 버튼
    w.data.image_main_button_play = w.newImage(
        x = 450, 
        y = 400, 
        filename = './images/main_play_button.png', 
        new_width=300, 
        new_height=100, 
        isVisible=True, 
        isPixelwiseModifiable=False
        )

    pass


def update(timestamp):
    '''
    여러 줄짜리
    설명 메시지
    '''
    if w.keys['Escape']:
        w.stop()
        return
    
    if w.mouse_buttons[1]:
        if (w.mouse_position_x >= 450 and w.mouse_position_x <= 750) and (w.mouse_position_y>=400 and w.mouse_position_y<=500):
            w.hideObject(w.data.image_main_button_play)

    pass


w.initialize = initialize
w.update = update

w.start()
