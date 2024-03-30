import pygame as pg
from time import perf_counter
import math

pg.font.init()
font_size = 15
font = pg.font.Font('pixy.ttf', font_size)


def rotate(surface, angle, position):
    img = pg.transform.rotozoom(surface, angle, 1)
    img_rect = img.get_rect(center=position)
    return img, img_rect


class Spaceship():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speedX = 0
        self.speedY = 0
        self.acceleration = .1
        self.color = (100, 255, 100)
        self.time = perf_counter()
        self.pressed_buttons = set()
        self.direction = 0
        self.turning_speed = 0
        self.turning_acceleration = .01
        self.img = pg.image.load('test.png')
        self.img_rect = self.img.get_rect(center=(100, 100))

    def move(self, event):
        if event.type == pg.KEYDOWN:
            self.pressed_buttons.add(event.key)
        elif event.type == pg.KEYUP:
            self.pressed_buttons.remove(event.key)

    def update(self):
        for key in self.pressed_buttons:
            match key:
                case pg.K_w:
                    self.speedY -= self.acceleration * math.cos(math.radians(self.direction))
                    self.speedX -= self.acceleration * math.sin(math.radians(self.direction))
                case pg.K_s:
                    self.speedY += self.acceleration * math.cos(math.radians(self.direction))
                    self.speedX += self.acceleration * math.sin(math.radians(self.direction))
                case pg.K_d:
                    self.turning_speed += self.turning_acceleration
                case pg.K_a:
                    self.turning_speed -= self.turning_acceleration
        self.direction += self.turning_speed * (perf_counter() - self.time)
        self.x += self.speedX * (perf_counter() - self.time)
        self.y += self.speedY * (perf_counter() - self.time)
        self.time = perf_counter()

    def draw(self, screen, x, y):
        img_rotated, img_rotated_rect = rotate(self.img, self.direction, (self.x - x, self.y - y))
        screen.blit(img_rotated, img_rotated_rect)
        self.draw_info(screen)

    def draw_info(self, screen):
        img1 = font.render(f'position: {round(self.x, 3)} {round(self.y, 3)}\n', True, self.color)
        img2 = font.render(f'speed: {round((self.speedX ** 2 + self.speedY ** 2) ** .5, 3)}', True, self.color)
        img3 = font.render(f'direction: {round(self.direction, 3)}', True, self.color)
        screen.blit(img1, (10, 10))
        screen.blit(img2, (10, 10 + font_size))
        screen.blit(img3, (10, 10 + 2 * font_size))
