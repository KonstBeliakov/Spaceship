from time import perf_counter
from utils import *


class Object:
    def __init__(self):
        self.mass = 1
        self.x = 0
        self.y = 0
        self.speedX = 0
        self.speedY = 0
        self.time = perf_counter()
        self.direction = 0
        self.turning_speed = 0
        self.img = pg.image.load('test.png')
        self.img_rect = self.img.get_rect(center=(100, 100))

    def update(self):
        self.direction += self.turning_speed * (perf_counter() - self.time)
        self.x += self.speedX * (perf_counter() - self.time)
        self.y += self.speedY * (perf_counter() - self.time)
        self.time = perf_counter()

    def draw(self, screen, x, y):
        img_rotated, img_rotated_rect = rotate(self.img, self.direction, (self.x - x, self.y - y))
        screen.blit(img_rotated, img_rotated_rect)