import pygame
import os

pygame.init()

screen_width = 1600
screen_hight = 900
screen = pygame.display.set_mode((screen_width, screen_hight))
clock = pygame.time.Clock()

  # 파일 Path 설정
currunt_path = os.path.dirname(__file__) 
image_folder_path = os.path.join(currunt_path, "image")

  # image Path 설정
background_path = os.path.join(image_folder_path, "background.png")
ground_path = os.path.join(image_folder_path, "ground.png")
player_path = os.path.join(image_folder_path, "player.png")



class Sprite(pygame.sprite.Sprite):  # Sprite 클래스 생성
  def __init__(self, image, x_pos, y_pos):
    super().__init__()
    self.image = pygame.image.load(image)
    self.width = self.image.get_rect().size[0]
    self.hight = self.image.get_rect().size[1]
    self.x_pos = x_pos
    self.y_pos = y_pos - self.width  # 왼쪽 아래의 꼭짓점을 기준으로 설정
    self.to_x = 0
    self.to_y = 0

class Player(Sprite):   # Player 클래스 생성. Sprite 상속
  def __init__(self, image_path, x_pos, y_pos):
    super().__init__(image_path, x_pos, y_pos)
    self.jumping = False
    self.jump_hight = 15
    self.y_velocity = self.jump_hight
    self.speed = 10

player = Player(player_path, 100, 800)   # 클래스 생성
background = Sprite(background_path, 0, 0)
ground = Sprite(ground_path, 0, 800)


running = True
while running:
  dt = clock.tick(60)
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN:  # 키를 눌렀을 때
      if event.key == pygame.K_RIGHT:
        player.to_x += player.speed
      if event.key == pygame.K_LEFT:
        player.to_x -= player.speed
      if event.key == pygame.K_SPACE:
        player.jumping = True
    if event.type == pygame.KEYUP:  # 키를 뗐을 때
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        player.to_x = 0


  if player.jumping == True:   # 점프 설정
    player.y_pos -= player.y_velocity
    player.y_velocity -= 1
    if player.y_velocity < -player.jump_hight:
      player.jumping = False
      player.y_velocity = player.jump_hight


  player.x_pos += player.to_x   # 위치 변화 설정
  player.y_pos += player.to_y

  screen.blit(background.image, (0, 0))  # 화면에 그리기
  screen.blit(ground.image, (0, 800))
  screen.blit(player.image, (player.x_pos, player.y_pos))


  pygame.display.update()





