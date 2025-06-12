'''
gui 모듈을 사용하기 위한 기본 구조를 미리 적어 둔 파일입니다.

- 여러분은 이 아래에 있는, 함수 initialize()와 update()에 대한
  함수 정의 내용물을 구성함으로써 프로그램을 구성해야 해요

- 중간중간 F5를 눌러 interactive를 켜 둔 다음 진행하면
  IDLE이 함수 호출식 적을 때마다 적당한 툴팁을 읽어 보여줄 거예요
'''

'''
────────────────────────────────────────────────────────────────────────────────────────────────────────
────────────────────────────────────────────────────────────────────────────────────────────────────────
이름: 고형인 (20254482)
프로그램 이름: Dodge Game
────────────────────────────────────────────────────────────────────────────────────────────────────────
사용 방법: 
1. 키보드 입력
    W, A, S, D - 상하좌우 이동
    / - 무적 모드 (치트) 켜고 끄기
    Esc - 게임 나가기 및 프로그램 종료
    Enter - 메인 화면에서 게임 플레이 시작
2. Game Play
    플레이어를 움직여 날아오는 적들을 피하는 게임입니다.
    한번이라도 충돌하면 게임에서 패배하며 시간이 지날수록 더 많은 적들이 생성됩니다. (일정 시간이 지나면 균일하게 생성됩니다.)
    생성된 총 적의 수는 창 제목에 함께 표시됩니다.
    무적 모드를 사용하면 창 제목이 "GOD Mode On.."으로 변경되며 적들과 충돌해도 게임에서 패배하지 않습니다.
────────────────────────────────────────────────────────────────────────────────────────────────────────
────────────────────────────────────────────────────────────────────────────────────────────────────────
'''

import gui_core as gui
from scenes import main_screen
from gui import player_sprite, game_over_sprite
from utils.config import SCREEN_WIDTH, SCREEN_HEIGHT
from core import game, keyboard, title

w = gui.Window(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

def initialize(timestamp):
    '''

    '''
    global enemies
    enemies = []
    main_screen.init(w)
    player_sprite.init(w)
    game_over_sprite.init(w)

    pass


def update(timestamp):
    '''
    여러 줄짜
    설명 메시지
    '''
    global enemies
    keyboard.esc_input(w)
    game.start(w, enemies)
    title.isGod(w)

    pass


w.initialize = initialize
w.update = update

w.start()
