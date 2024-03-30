import pygame as pg
from time import perf_counter

pg.font.init()
font_size = 15
font = pg.font.Font('pixy.ttf', font_size)


class Spaceship():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speedX = 0
        self.speedY = 0
        self.acceleration = .1
        self.color = (100, 255, 100)
        self.time = perf_counter()
        self.pressed_button = None

    def move(self, event):
        if event.type == pg.KEYDOWN:
            self.pressed_button = event.key
        elif event.type == pg.KEYUP:
            self.pressed_button = None

    def update(self):
        match self.pressed_button:
            case pg.K_w:
                self.speedY -= self.acceleration
            case pg.K_s:
                self.speedY += self.acceleration

        self.x += self.speedX * (perf_counter() - self.time)
        self.y += self.speedY * (perf_counter() - self.time)
        self.time = perf_counter()

    def draw(self, screen, x, y):
        pg.draw.rect(screen, self.color, (self.x - x, self.y - y, 10, 10))
        self.draw_info(screen)

    def draw_info(self, screen):
        img1 = font.render(f'position: {round(self.x, 3)} {round(self.y, 3)}\n', True, self.color)
        img2 = font.render(f'speed: {round((self.speedX ** 2 + self.speedY ** 2) ** .5, 3)}', True, self.color)
        screen.blit(img1, (10, 10))
        screen.blit(img2, (10, 10 + font_size))
