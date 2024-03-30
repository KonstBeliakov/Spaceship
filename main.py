import pygame as pg
from spaceship import Spaceship

pg.init()
window_size = (800, 800)
pg.display.set_caption("Window")
screen = pg.display.set_mode(window_size)
background_color = (0, 0, 0)


ship1 = Spaceship()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        ship1.move(event)
    ship1.update()

    screen.fill(background_color)

    ship1.draw(screen, -400, -400)

    pg.display.flip()