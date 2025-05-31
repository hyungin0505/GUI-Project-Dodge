'''
gui 모듈을 사용하기 위한 기본 구조를 미리 적어 둔 파일입니다.

- 여러분은 이 아래에 있는, 함수 initialize()와 update()에 대한
  함수 정의 내용물을 구성함으로써 프로그램을 구성해야 해요

- 중간중간 F5를 눌러 interactive를 켜 둔 다음 진행하면
  IDLE이 함수 호출식 적을 때마다 적당한 툴팁을 읽어 보여줄 거예요
'''

import gui_core as gui

w = gui.Window()


def initialize(timestamp):
    '적절한 설명 메시지'
    pass


def update(timestamp):
    '''
    여러 줄짜리
    설명 메시지
    '''
    pass


w.initialize = initialize
w.update = update

w.start()
