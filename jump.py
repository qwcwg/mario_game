import os
import pygame

pygame.init()

screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
FPS = 60
GRAVITY = 1

# 파일 Path 설정
currunt_path = os.path.dirname(__file__)
image_folder_path = os.path.join(currunt_path, "image")

# image Path 설정
background_path = os.path.join(image_folder_path, "background.png")
ground_path = os.path.join(image_folder_path, "ground.png")
player_path = os.path.join(image_folder_path, "player.png")
weapon_path = os.path.join(image_folder_path, "weapon.png")
monster_path = os.path.join(image_folder_path, "monster.png")
block_1_path = os.path.join(image_folder_path, "block_1.png")
block_2_path = os.path.join(image_folder_path, "block_2.png")
block_3_path = os.path.join(image_folder_path, "block_3.png")

class Sprite(pygame.sprite.Sprite):  # Sprite 클래스

  def __init__(self, image_path, x_pos, y_pos):
    super().__init__()
    self.image = pygame.image.load(image_path)
    self.width = self.image.get_rect().size[0]
    self.height = self.image.get_rect().size[1]
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.point_1 = [self.x_pos, self.y_pos]  #
    self.point_2 = [self.x_pos + self.width, self.y_pos]
    self.point_3 = [self.x_pos, self.y_pos + self.height]
    self.point_4 = [self.x_pos + self.width, self.y_pos + self.height]
    self.left_x = self.x_pos
    self.right_x = self.x_pos + 50
    self.top_y = self.y_pos
    self.bottom_y = self.y_pos + 50
    self.to_x = 0
    self.to_y = 0
    self.gravity = 1

  def draw(self):  # 그리기 method
    screen.blit(self.image, (self.x_pos, self.y_pos))

class Player(Sprite):  # Player 클래스. 점프 기능 추가
  def __init__(self, image_path, x_pos, y_pos):
    super().__init__(image_path, x_pos, y_pos)

    self.jumping = False
    self.jump_height = 15
    self.y_velocity = self.jump_height
    self.speed = 7

    self.fall_count = 1

  def move_right(self):  # 이동 method
    self.to_x += self.speed

  def move_left(self):
    self.to_x -= self.speed

  def move_jump(self):
    self.jumping = True

  def move(self):
    self.x_pos += self.to_x
    self.y_pos += self.to_y

def jump_and_gravity(player):  # 중력 설정
  player.gravity = 1
  player.to_y += player.gravity # 아래로 떨어짐
  player.gravity += 1 
  keys = pygame.key.get_pressed()
  if player.bottom_y >= 800:
    player.to_y = 0
  if player.to_y == 0 :
    if keys[pygame.K_SPACE]:
      player.to_y = -18

def top_collision(player, block):  # 블럭을 플레이어가 밟을 때 충돌
  if block.top_y <= player.bottom_y and player.to_y > 0 :  # 플레이어가 블록의 사이(상하)에 있을 때
    if  block.left_x < player.left_x < block.right_x  or  block.left_x < player.right_x < block.right_x: # 플레이어가 블록의 사이(좌우)에 있을 때
      player.to_y = 0
      player.y_pos = block.top_y + player.height
  
    


    

def handle_move(player):
  keys = pygame.key.get_pressed()
  player.to_x = 0
  if keys[pygame.K_RIGHT]:  # 키를 눌렀을 때
    player.move_right()
  if keys[pygame.K_LEFT]:
    player.move_left()

  jump_and_gravity(player)  # 중력&점프 함수 사용


  player.x_pos += player.to_x
  player.y_pos += player.to_y

 
def pos_update(player):  #  위치 초기화 함수

  player.point_1 = [player.x_pos, player.y_pos]
  player.point_2 = [player.x_pos + player.width, player.y_pos]
  player.point_3 = [player.x_pos, player.y_pos + player.height]
  player.point_4 = [player.x_pos + player.width, player.y_pos + player.height]

  player.left_x = player.x_pos
  player.right_x = player.x_pos + player.width
  player.top_y = player.y_pos
  player.bottom_y = player.y_pos + player.height

  
player = Player(player_path, 100, 750)  # 클래스 생성
background = Sprite(background_path, 0, 0)
ground = Sprite(ground_path, 0, 800)
block_1 = Sprite(block_1_path, 200, 650)


running = True
while running:
  dt = clock.tick(60)
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      running = False


  top_collision(player, block_1)
  handle_move(player)
  pos_update(player)  # 위치 업데이트 함수

  background.draw()  # 화면에 그리기
  ground.draw()
  player.draw()
  block_1.draw()

  pygame.display.update()

pygame.quit()