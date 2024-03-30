import math
from utils import *
from object import Object

pg.font.init()
font_size = 15
font = pg.font.Font('pixy.ttf', font_size)


class Spaceship(Object):
    def __init__(self):
        super().__init__()
        self.acceleration = .1
        self.color = (100, 255, 100)
        self.pressed_buttons = set()
        self.turning_acceleration = .01

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
        super().update()

    def draw(self, screen, x, y):
        super().draw(screen, x, y)
        self.draw_info(screen)

    def draw_info(self, screen):
        img1 = font.render(f'position: {round(self.x, 3)} {round(self.y, 3)}\n', True, self.color)
        img2 = font.render(f'speed: {round((self.speedX ** 2 + self.speedY ** 2) ** .5, 3)}', True, self.color)
        img3 = font.render(f'direction: {round(self.direction, 3)}', True, self.color)
        screen.blit(img1, (10, 10))
        screen.blit(img2, (10, 10 + font_size))
        screen.blit(img3, (10, 10 + 2 * font_size))
