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


    def run(self):
