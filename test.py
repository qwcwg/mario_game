# class Sprite(pygame.sprite.Sprite):  # Sprite 클래스
#   def __init__(self, image_path, x_pos, y_pos):
#     super().__init__()
#     self.image = pygame.image.load(image_path)
#     self.width = self.image.get_rect().size[0]
#     self.height = self.image.get_rect().size[1]
#     self.x_pos = x_pos
#     self.y_pos = y_pos
#     self.point_1 = [self.x_pos, self.y_pos]  #
#     self.point_2 = [self.x_pos + self.width, self.y_pos]
#     self.point_3 = [self.x_pos, self.y_pos + self.height]
#     self.point_4 = [self.x_pos + self.width, self.y_pos + self.height]
#     # self.left_x
#     # self.right_x
#     # self.top_y 
#     # self.bottom_y
#     self.to_x = 0
#     self.to_y = 0


# SPRITE = Sprite(image_path, x_pos, y_pos)

# SPRITE = {
#   SPRITE.image : pygame.image.load(image_path)
# }


test1 = {
    "num1": 1,
    "num2": 2,
    "num3": 3,
}

test2 = {
    "num4": 4
    "num5": 5
}
 
arr = [test1, test2]
