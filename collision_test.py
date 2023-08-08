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


class Sprite(pygame.sprite.Sprite):  # Sprite 클래스
  def __init__(self, image_path, x_pos, y_pos):
    super().__init__()
    self.image = pygame.image.load(image_path)
    self.width = self.image.get_rect().size[0]
    self.height = self.image.get_rect().size[1]
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.point_1 = [self.x_pos, self.y_pos]
    self.point_2 = [self.x_pos + self.width, self.y_pos]
    self.point_3 = [self.x_pos, self.y_pos + self.height]
    self.point_4 = [self.x_pos + self.width, self.y_pos + self.height]
    self.to_x = 0
    self.to_y = 0

  def draw(self):  # 그리기 method
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


class Monster(Sprite):  # Monster 클래스. 움직임과 공격 기능 추가

  def __init__(self, image_path, x_pos, y_pos):
    super().__init__(image_path, x_pos, y_pos)
    self.speed = 5
    self.move_count = 0

  def move(self):
    self.to_x += self.speed 

  def update(self):
    self.move()
    self.x_pos += self.to_x
    if self.x_pos > screen_width:  # 화면을 벗어나면 몬스터를 제거
      self.kill()


class Player(Sprite):   # Player 클래스. 점프 기능 추가
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

  def gravity(self):  # 중력 설정
    self.to_y += min(1, (self.fall_count / FPS) * GRAVITY)
    self.fall_count += 1


def handle_move(player, weapon, objects):
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
  if player.y_velocity < -player.jump_height:
    player.jumping = False
    player.y_velocity = player.jump_height

  player.gravity()  # 중력 함수 사용

  player.x_pos += player.to_x
  player.y_pos += player.to_y


def pos_update(weapon, player):  #  위치 초기화 함수
  weapon.x_pos = player.x_pos + 50
  weapon.y_pos = player.y_pos

  player.point_1 = [player.x_pos, player.y_pos]
  player.point_2 = [player.x_pos + player.width, player.y_pos]
  player.point_3 = [player.x_pos, player.y_pos + player.height]
  player.point_4 = [player.x_pos + player.width, player.y_pos + player.height]


def array_draw(array):
  for sprites in array:
    sprites.draw()


def top_side_collision(player, objects):
  for obj in objects:
    if player.point_3[1] == obj.point_1[1]:
      if obj.point_1[0] < player.point_3[0] < obj.point_2[0]  or  obj.point_1[0] < player.point_4[0] < obj.point_2[0]:
        player.y_pos = obj.point_1[1]



player = Player(player_path, 100, 700)    # 클래스 생성
background = Sprite(background_path, 0, 0)
ground = Sprite(ground_path, 0, 800)
weapon = Weapon(weapon_path, player.x_pos + 50, player.y_pos)
monster_array = [
    Monster(monster_path, 1400, 700),
    Monster(monster_path, 1000, 500),
    Monster(monster_path, 900, 300)
]
objects = [ground]


running = True
while running:
  dt = clock.tick(60)
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      running = False


  handle_move(player, weapon, objects)
  top_side_collision(player, objects)
  pos_update(weapon, player)  # 위치 초기화 함수

  background.draw()  # 화면에 그리기
  ground.draw()
  player.draw()
  array_draw(monster_array)

  weapon.weapon_active()  # 무기 활성화

  pygame.display.update()
  # print(player.y_pos, player.point_1)

pygame.quit()

print(player.point_1)
# print(player.point_2)
# print(player.point_3)
# print(player.point_4)
