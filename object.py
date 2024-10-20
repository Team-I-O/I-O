import os
import pygame

img_path = os.path.join(os.path.dirname(__file__), 'img')


class Object:
    # 이미지 파일 경로 설정

    # 폰트 설정
    fonts = os.path.join(os.path.dirname(__file__), 'fonts')
    font_B = pygame.font.Font(os.path.join(fonts, "이순신돋움체B.ttf"), 48)
    font_L = pygame.font.Font(os.path.join(fonts, "이순신돋움체L.ttf"), 30)
    font_M = pygame.font.Font(os.path.join(fonts, "이순신돋움체M.ttf"), 30)

    def __init__(self, screen, name='', path="character", parent=None, color="#FFFFFF"):
        """
        __init__(parent, path="character", width=0, height=0)
        object 위치, 크기(너비,높이), 부모 object 지정
        """
        self.name = name
        self.img = None
        self.object_path = os.path.join(img_path, path)
        self.width = None
        self.height = None
        self.pos = (0, 0)
        self.color = color
        self.text = None
        self.screen = screen
        self.parent = parent

    def draw(self, name, pos=(0, 0)):
        """
        draw(name,pos)
        이름에 따른 이미지 반환, 또한 위치 지정
        center 라고 입력시
        (부모 있을시 부모 객체 내에서 좌표 계산 ex. position : absolute)
        """

        self.name = name
        self.img = pygame.image.load(os.path.join(self.object_path, self.name))

        self.set_size(self.img)
        self.set_position(pos)

        return self.img

    def texting(self, name, pos=(0, 0), color=None):
        """
        texting(name, pos=None)
        name 에 따른 텍스트 렌더링 및 위치 지정
        """
        self.name = name
        self.color = color if color else self.color
        self.text = Object.font_B.render(self.name, False, self.color)

        self.set_size(self.text)
        self.set_position(pos)
        return self.text

    def set_position(self, pos):
        """
        :param pos:
        위치 계산 후 지정
        """
        if pos == 'center' and self.parent:
            self.pos = (self.parent.pos[0] + (self.parent.width - self.width) / 2,
                        self.parent.pos[1] + (self.parent.height - self.height) / 2)
        elif pos == 'center':
            self.pos = ((self.screen.width - self.width) / 2, (self.screen.height - self.height) / 2)
        else:
            x, y = pos

            if '%' in x and self.parent:
                x = self.parent.pos[0] + int(pos[0][:-1]) / 100 * self.parent.width
            elif '%' in x:
                x = self.screen.width * int(pos[0][:-1]) / 100
            elif self.parent:
                x = int(pos[0]) + self.parent.pos[0]

            if '%' in y and self.parent:
                y = self.parent.pos[1] + int(pos[1][:-1]) / 100 * self.parent.height
            elif '%' in y:
                y = self.screen.height * int(pos[1][:-1]) / 100
            elif self.parent:
                y = int(pos[1]) + self.parent.pos[1]

            self.pos = (x, y)
    # pos = ('~~%', 100)

    def set_name(self, name):
        self.name = name

    def set_size(self, parent, width=None, height=None, ):
        self.width = width
        self.height = height
        if not self.width:
            self.width = parent.get_width()
        if not self.height:
            self.height = parent.get_height()
        pygame.transform.scale(parent, (self.width, self.height))

    def set_color(self, color):
        self.color = color
