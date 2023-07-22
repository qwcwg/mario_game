import pygame
import os

pygame.init()

screen_width = 1600
screen_hight = 900
screen = pygame.display.set_mode((screen_width, screen_hight))
clock = pygame.time.Clock()

  # 파일 Path 설정
currunt_path = os.path.dirname(__file__) 
image_path = os.path.join(currunt_path, "image")

  #이미지 불러오기
background = pygame.image.load(os.path.join(image_path, "background.png"))  
ground = pygame.image.load(os.path.join(image_path, "ground.png"))  
player = pygame.image.load(os.path.join(image_path, "player.png"))

  # player 설정
player_size = player.get_rect().size
player_width = player_size[0]
player_hight = player_size[1]
player_x_pos = 100 
player_y_pos = 800 - player_hight
player_speed = 10
player_to_x = 0
player_to_y = 0
jumping = False  # 점프 설정
jump_hight = 15
y_velocity = jump_hight



running = True
while running:
  dt = clock.tick(60)
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN:  # 키를 눌렀을 때
      if event.key == pygame.K_RIGHT:   
        player_to_x += player_speed
      if event.key == pygame.K_LEFT:
        player_to_x -= player_speed
      if event.key == pygame.K_SPACE:
        jumping = True
    if event.type == pygame.KEYUP:  # 키를 뗐을 때
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
        player_to_x = 0
 

  if jumping == True:   # 점프 설정
    player_y_pos -= y_velocity
    y_velocity -= 1
    if y_velocity < -jump_hight:
      jumping = False
      y_velocity = jump_hight


  player_x_pos += player_to_x   # 위치 변화 설정
  player_y_pos += player_to_y

  screen.blit(background, (0, 0))  # 화면에 그리기
  screen.blit(ground, (0, 800))
  screen.blit(player, (player_x_pos, player_y_pos))


  pygame.display.update()






