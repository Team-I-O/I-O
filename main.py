import pygame,pickle,object,floor,skill
import os

# 기본 초기화
pygame.init()

# 화면 크기 설정
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

# 게임 이름 설정
pygame.display.set_caption("null")

# 폰트 설정
pygame.font = pygame.font.Font("fonts\a.ttf ", 30)

# FPS 설정
clock = pygame.time.Clock()

# 메인 화면 배경 만들기
background = pygame.image.load(os.path.join("images", "background.png"))

# 캐릭터 만들기
character = pygame.image.load(os.path.join("images", "character.png"))
character_size =  character.get_rect().size



running = True
while running:
    dt = clock.tick(60)


    # 화면에 배경 그리기
    screen.blit(background,(0,0))

# 게임 종료
pygame.quit()



# ##############################################
# # 기본 초기화 (반드시 해야 하는 것들)
# pygame.init() # 초기화
#
# # 화면 크기 설정
# screen_width = 480 # 가로 크기
# screen_height = 640 # 세로 크기
# screen = pygame.display.set_mode((screen_width, screen_height))
#
#
# # 화면 타이틀 설정
# pygame.display.set_caption("Nado Game") # 게임 이름
#
# # FPS
# clock = pygame.time.Clock()
# ##############################################
#
# # 1. 사용자 게임 초기화( 배경화면, 게임 이미지, 좌표, 폰트 등)
#
#
# running  = True
#
# while running:
#     dt = clock.tick(30)
#
#     # 2. 이벤트 처리(키보드, 마우스 등)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # 3. 게임 캐릭터 위치 정의
#
#     # 4. 충돌 처리
#
#     # 5. 화면에 그림 그리기
#     screen.fill((0, 0, 255))
#
#     screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
#
#     screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기
#
#     pygame.display.update()
#
# pygame.quit()
