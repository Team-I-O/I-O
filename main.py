import pygame
import os
import map
import object

# import pickle



img_path = os.path.join(os.path.dirname(__file__), 'img')

# 기본 초기화
pygame.init()
pygame.font.init()

# 화면 크기 설정
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = pygame.display.get_window_size()

# 게임 이름 및 아이콘 설정
pygame.display.set_caption("null")
pygame.display.set_icon(pygame.image.load(os.path.join(img_path, 'icon.png')))

# FPS 설정
clock = pygame.time.Clock()


class Ui():
    def __init__(self, path, parent,):
        pass

    def set_ui(self, num):

        return




class Character(object.Object):
    """???"""

    def __init__(self, name):
        super().__init__(name)
        # self.hp = 100
        # self.attack = 100

    def attack(self):
        """"""
        pass

    def defense(self):
        """"""
        pass

    def is_boss(self):
        pass


def update():
    pygame.display.update()


class codes:
    def __init__(self):
        self.floor = object.Object(name='main.png', path="floor")
        self.first = True
        self.next = False
        self.main_choice = 0

    def ui(self, num):
        match num:
            case 0.0:  # 처음 화면 UI
                self.text_ui = object.Object(path="ui")
                self.text1 = object.Object(parent=self.text_ui, color='#FFFFFF',)
                self.text2 = object.Object(parent=self.text_ui, color='#999999')
                self.text3 = object.Object(parent=self.text_ui, color='#999999')
            case 0.1:  # 직업 선택 UI
                self.text_ui = object.Object(path="ui")
                self.job = object.Object(parent=self.text_ui, color='#FFFFFF')

                self.job_list = [[object.Object(parent=self.job,color='#FFFFFF'),
                                  object.Object(parent=self.job, path='ui'),
                                  object.Object(parent=self.job, color='#FFFFFF')]for _ in range(3)]
                                    # 직업 이름, 사진, 설명.(캐릭터 클래스?) + 기본 스탯 필요

                self.name_text = object.Object(parent=self.text_ui, color='#FFFFFF')
                self.name_img = object.Object(parent=self.text_ui, path='ui')

                pass
            case 0.2:  # 저장한 게임 선택 UI
                pass
            case 1.0:  # 인게임 하단 바(null) UI
                pass
            case 1.1:  # 인게임 하단 바(스킬) UI
                pass
            case 1.2:  # 인게임 하단 바(패시브) UI
                pass
            case 1.3:  # 인게임 하단 바(아이템) UI
                pass
            case 2.0:  # 인게임 지도 UI
                pass
            case 3.0:  # 게임 오버 UI
                pass




    def choice_main(self, go, nextup=False):
        if nextup or self.next:
            match self.main_choice:
                case 0:
                    return self.main()
                case 1:
                    return self.saved()
                case 2:
                    global running
                    running = False
        if self.first:
            self.ui(0.0)
            self.first = False

        screen.blit(self.text_ui.draw('main_ui.png', pos=('50%', '50%')),
                    (self.text_ui.pos[0], self.text_ui.pos[1]))
        screen.blit(self.text1.texting('던전 진입하기', pos=('15%', '20%'), color=self.text1.color),
                    (self.text1.pos[0], self.text1.pos[1]))
        screen.blit(self.text2.texting('과거 불러오기', pos=('15%', '45%'), color=self.text2.color),
                    (self.text2.pos[0], self.text2.pos[1]))
        screen.blit(self.text3.texting('돌아가기', pos=('15%', '70%'), color=self.text3.color),
                    (self.text3.pos[0], self.text3.pos[1]))

        go += self.main_choice
        texts = [self.text1, self.text2, self.text3]
        texts[(go-1) % 3].set_color('#999999')
        texts[go % 3].set_color('#FFFFFF')
        texts[(go+1) % 3].set_color('#999999')

        self.main_choice = go

    def main(self, ):
        screen.fill('#333333')

        if self.first == False:
            self.text_ui = object.Object(path="ui")
            self.text1 = object.Object(parent=self.text_ui, color='#FFFFFF')
            self.text2 = object.Object(parent=self.text_ui, color='#999999')
            self.text3 = object.Object(parent=self.text_ui, color='#999999')
            self.first = True

        return True


    def saved(self, ):
        pass


code = codes()



running = True
while running:
    dt = clock.tick(60)
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 게임 종료
            running = False
        elif event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_ESCAPE:
                    running = False
                case pygame.K_UP:
                    codes.choice_main(-1)
                case pygame.K_DOWN:
                    codes.choice_main(1)
                case pygame.K_RETURN:
                    next = True

    # 화면에 배경 그리기
    # code.
    screen.blit(floor.draw(floor.name, 'center'), (floor.pos[0], floor.pos[1]))

    # 화면에 버튼 그리기


    update()

# 게임 종료
pygame.quit()
