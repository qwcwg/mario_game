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



class Player(Sprite):   # Player 클래스. 점프 기능 추가
  def __init__(self, image_path, x_pos, y_pos):
    super().__init__(image_path, x_pos, y_pos)
    
    self.jumping = False
    self.jump_hight = 15
    self.y_velocity = self.jump_hight
    self.speed = 10

  def move_right(self):
    self.to_x += self.speed
  def move_left(self):
    self.to_x -= self.speed
  def move_jump(self):
    self.jumping = True

  def move(self):
    self.x_pos += self.to_x
    self.y_pos += self.to_y



  def handle_move(self):
    keys = pygame.key.get_pressed()

    self.to_x = 0
    if keys[pygame.K_RIGHT]:
      self.move_right()
    if keys[pygame.K_LEFT]:
      self.move_left()
    if keys[pygame.K_SPACE]:
      self.move_jump()

    if self.jumping == True:   # 점프 설정
      self.y_pos -= self.y_velocity
      self.y_velocity -= 1
    if self.y_velocity < -self.jump_hight:
      self.jumping = False
      self.y_velocity = self.jump_hight

  def loop(self):
    self.move()
  






player = Player(player_path, 100, 800)   # 클래스 생성
background = Sprite(background_path, 0, 0)
ground = Sprite(ground_path, 0, 800)


running = True
while running:
  dt = clock.tick(60)
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      running = False


  player.handle_move()

  player.loop()

  background.draw()  # 화면에 그리기
  ground.draw()
  player.draw()

  pygame.display.update()

print(player.image.get_rect())



