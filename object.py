from time import perf_counter
from utils import *
from utils import *


class Object:
    def __init__(self):
        self.mass = 10**11
        self.x = 0
        self.y = 0
        self.speedX = 0
        self.speedY = 0
        self.time = perf_counter()
        self.direction = 0
        self.turning_speed = 0
        self.img = pg.image.load('test.png')
        self.img_rect = self.img.get_rect(center=(100, 100))

    def update(self, objects):
        for obj in objects:
            if obj != self:
                d = dist(self.x, self.y, obj.x, obj.y)
                if d > 10:
                    a = acceleration(self.x, self.y, obj.x, obj.y, obj.mass)
                    self.speedX += ((obj.x - self.x) / d) * a
                    self.speedY += ((obj.y - self.y) / d) * a
                    print(d, a, self.speedX, self.speedY)
        self.direction += self.turning_speed * (perf_counter() - self.time)
        self.x += self.speedX * (perf_counter() - self.time)
        self.y += self.speedY * (perf_counter() - self.time)
        self.time = perf_counter()
        self.direction %= 360

    def draw(self, screen, x, y):
        img_rotated, img_rotated_rect = rotate(self.img, self.direction, (self.x - x, self.y - y))
        screen.blit(img_rotated, img_rotated_rect)

    def set_position(self, x, y):
        self.x = x
        self.y = y
