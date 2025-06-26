# Dodge Game
중앙대학교 2025학년도 1학기 오픈소스SW와파이썬프로그래밍 03분반 기말 프로젝트 제출물입니다.   

## 프로젝트 개요
[강사님](https://www.youtube.com/@m.l)께서 수업 시간에 소개한 gui 모듈(`gui_core.py`)을 활용하여 간단한 gui 프로그램 만들기 

`gui_core.py`에 대한 저작권은 [이주호](https://www.youtube.com/@m.l) 강사님께 있습니다.

### 구성 조건
<details>
<summary>모듈 관련</summary> 

  - 수업 표준 환경에 포함되어 있는 [time](https://docs.python.org/3/library/time.html), [random](https://docs.python.org/3/library/random.html) 모듈 등 import하여 사용 가능
  - 수업 시간에 소개한 gui 모듈 사용 가능
  - [pygame](https://github.com/pygame/pygame) 등 별도의 라이브러리를 다운로드 및 import할 수는 없음
  - `gui_blank.py`에 마련된 기본적인 구조를 사용
</details>
<details>
<summary>프로그램 설명</summary>

  - `.py` 파일 상단에 다음과 같은 내용을 적어 두어야 함
    - 자신의 이름
    - 프로그램 이름
    - 사용 방법
</details>
<details>
<summary>데이터 구성</summary>

  - 최소 다섯 가지 입력 활용
  - 최소 세 개의 그래픽 물체를 다루어야 함
</details>
<details>
<summary>코드 구성</summary>

  - 제작자 본인은 클리어할 수 있어야 함
    - 끝이 없을 경우 최소 10초는 패배하지 않고 버틸 수 있어야 함
  - 강사가 정상적으로 플레이할 때 가끔은 패배할 수 있어야 함
    - 아무것도 안 해도 무조건 클리어하거나 10초 버틸 수 있도록 만들면 안 됨
    - 거의 항상 패배할 정도로 어렵게 만들어도 됨 
  - 최소 세 가지 실행 흐름 구성
    - 정상적으로 플레이하여 클리어(또는 10초 버티기)하는 실행 흐름
    - 플레이하다 패배하는 실행 흐름
    - 간단한 조작으로 손쉽게 클리어 가능한 실행 흐름 (치트 가능)
</details>

## 프로젝트 설명 
<table>
  <tr>
    <td align="center"><a href="https://youtu.be/4zaos1_TjkU" target="_blank">Ingame</a></td>
    <td align="center"><a href="https://youtu.be/7kXo61SOJkc" target="_blank">Ingame (God Mode)</a></td>
  </tr>
  <tr>
    <td><img src="./etc/ingame_play.gif"/></td>
    <td><img src="./etc/ingame_play(god).gif"/></td>
  </tr>
</table>

해상도로 인해 gif 프레임이 떨어질 수 있습니다.

조작키를 사용해 플레이어를 움직여 날아오는 적들을 피하는 게임입니다.  
한 번이라도 충돌하면 게임에서 패배하며, 시간이 지날수록 생성되는 적들이 많아집니다.  

각 파일 및 코드에 대한 설명은 해당 파일 내에 주석으로 작성하였습니다.  

### 실행
Python 3.13 버전 환경에서 제작되었습니다.
```bash
git clone https://github.com/hyungin0505/GUI-Project-Dodge.git
```
클론하거나 ZIP 파일을 다운로드하여 압축을 풀어주세요.  
```bash
python3 gui_project.py
```
`gui_project.py`를 실행하여 게임을 시작할 수 있습니다.  

**CPU 성능에 따라 프레임 업데이트 속도에 차이가 있어 난이도가 상이할 수 있습니다**  
(`.utils/config`에서 게임 난이도를 임의로 설정할 수 있습니다.)

### 조작
- `W`, `A`, `S`, `D`
  - 상, 하, 좌, 우 방향 조작
  - 두 키 동시에 눌러 대각선 이동 가능
  - 상하 또는 좌우 동시에 누를 경우 상쇄되어 정지
- `Esc`
  - 언제든 게임 종료 (프로그램 종료)
- `Enter`
  - 메인 화면에서 게임 시작 버튼 클릭과 동일한 기능
- `/`
  - 인게임 중 치트 활성화 (무적 모드)

### 리소스
- `./assets/lgoo.png` 로고 이미지 [AI](https://www.design.com/) 생성
- 이외 이미지들 [Piskel](https://www.piskelapp.com/)에서 제작
  - `./piskel` 디렉토리에 Player, Enemy, Background 프로젝트 파일

### 설정
`./utls/config.py`에서 게임에서 사용될 상수와 전역 변수 등을 관리할 수 있습니다.   
- 전체 화면 크기, 물체 가로 세로 길이 등 그래픽 관련 설정
- Player 및 Enemy 속도, 난이도, Enemy 이동 방향, 보정치 등 인게임 로직 관련 설정  
- `DEBUGGING` 활성화를 통해 디버깅에 필요한 정보 출력하는 함수 `d_print()` 함수 활용