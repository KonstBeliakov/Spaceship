import pygame as pg
from spaceship import Spaceship
from object import Object

pg.init()
window_size = (800, 800)
pg.display.set_caption("Window")
screen = pg.display.set_mode(window_size)
background_color = (0, 0, 0)


objects = [Object()]

objects[0].set_position(0, 0)

objects.append(Spaceship())
ship = objects[1]
ship.set_position(-200, -200)

screen_center = (-400, -400)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        ship.move(event)

    screen.fill(background_color)

    for obj in objects:
        obj.update(objects)
        obj.draw(screen, *screen_center)

    pg.display.flip()