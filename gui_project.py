'''
gui 모듈을 사용하기 위한 기본 구조를 미리 적어 둔 파일입니다.

- 여러분은 이 아래에 있는, 함수 initialize()와 update()에 대한
  함수 정의 내용물을 구성함으로써 프로그램을 구성해야 해요

- 중간중간 F5를 눌러 interactive를 켜 둔 다음 진행하면
  IDLE이 함수 호출식 적을 때마다 적당한 툴팁을 읽어 보여줄 거예요
'''

import gui_core as gui
from scenes.main_screen import main_page_init
from gui.player import game_player_init
from utils import *
from core.exit import esc_key_input
from core.game import game_start

w = gui.Window(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

def initialize(timestamp):
    global enemies

    main_page_init(w)
    game_player_init(w)
    enemies = []

    pass


def update(timestamp):
    global enemies
    '''
    여러 줄짜리
    설명 메시지
    '''
    esc_key_input(w)
    game_start(w, enemies)

    pass


w.initialize = initialize
w.update = update

w.start()
