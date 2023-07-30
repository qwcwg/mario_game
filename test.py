import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):

        # self.width = self.image.get_rect().size[0]
        # self.hight = self.image.get_rect().size[1]
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = pygame.Rect(x_pos, y_pos, 50, 50)

player = Player(40, 60)

print(player.rect.top)
print(player.rect.bottom)