import pygame
import os


pygame.init()

screen_width = 1600
screen_hight = 900
screen = pygame.display.set_mode((screen_width, screen_hight))
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


class Sprite(pygame.sprite.Sprite):  # Sprite 클래스
  def __init__(self, image_path, x_pos, y_pos):
    super().__init__()
    self.image = pygame.image.load(image_path)
    self.width = self.image.get_rect().size[0]
    self.hight = self.image.get_rect().size[1]
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.to_x = 0
    self.to_y = 0

  def draw(self): # 그리기 method
    screen.blit(self.image, (self.x_pos, self.y_pos))


class Weapon(Sprite):
  def __init__(self, image_path, x_pos, y_pos):
    super().__init__(image_path, x_pos, y_pos)
    self.active = False
    self.time_count = 0

  def weapon_active(self):  # 무기 활성화 함수
    if self.active == True:
      self.draw()  
      self.time_count += 1
      if self.time_count == 10:
        self.time_count = 0
        self.active = False
      

class Player(Sprite):   # Player 클래스. 점프 기능 추가
  def __init__(self, image_path, x_pos, y_pos):
    super().__init__(image_path, x_pos, y_pos)

    self.jumping = False
    self.jump_hight = 15
    self.y_velocity = self.jump_hight
    self.speed = 10

    self.fall_count = 1

  def move_right(self):   # 이동 method
    self.to_x += self.speed
  def move_left(self):
    self.to_x -= self.speed
  def move_jump(self):
    self.jumping = True

  def move(self):
    self.x_pos += self.to_x
    self.y_pos += self.to_y

  def gravity(self):  # 중력 설정
    self.to_y += min(1, (self.fall_count / FPS) * GRAVITY)
    self.fall_count += 1
    


def handle_move(player, weapon):
  keys = pygame.key.get_pressed()

  player.to_x = 0
  if keys[pygame.K_RIGHT]:  # 키를 눌렀을 때
    player.move_right()
  if keys[pygame.K_LEFT]:
    player.move_left()
  if keys[pygame.K_SPACE]:
    player.move_jump()
  if keys[pygame.K_r]:
    weapon.active = True
  
  if player.jumping == True:   # 점프 설정
    player.y_pos -= player.y_velocity
    player.y_velocity -= 1
  if player.y_velocity < -player.jump_hight:
    player.jumping = False
    player.y_velocity = player.jump_hight
  
  # self.gravity()    # 중력 함수 사용

  player.x_pos += player.to_x
  player.y_pos += player.to_y

def weapon_pos(weapon, player):  # weapon 위치 초기화 함수
  weapon.x_pos = player.x_pos + 50
  weapon.y_pos = player.y_pos



player = Player(player_path, 100, 700)    # 클래스 생성
background = Sprite(background_path, 0, 0)
ground = Sprite(ground_path, 0, 800)
weapon = Weapon(weapon_path, player.x_pos + 50, player.y_pos)


running = True
while running:
  dt = clock.tick(60)
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      running = False


  handle_move(player, weapon)
  weapon_pos(weapon, player)  # weapon 위치 초기화 함수

  background.draw()  # 화면에 그리기
  ground.draw()
  player.draw()

  weapon.weapon_active()  # 무기 활성화 


  pygame.display.update()





