import pygame





class Start:
    def __init__(self):
        pygame.init()
        pygame.font.init()


        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        screen_width, screen_height = pygame.display.get_window_size()
        screen_object = Object(screen=screen)  #screen이라는 Object 객체 지정
        screen_object.set_size(screen_width, screen_height)


        pygame.display.set_caption("null")
        pygame.display.set_icon(pygame.image.load(os.path.join(img_path, 'icon.png')))

        clock = pygame.time.Clock()


    def update(self):
        pass
# class Game:
#     def __init__(self):
#
#     # 화면, FPS, 상태 설정
#     def main_loop(self):
#
#     # 메인 게임 루프: 이벤트 처리, 상태 업데이트, 화면 갱신
#     def start_game(self):
#
#     # 새 게임 초기화
#     def load_game(self):
# # 저장된 게임 불러오기