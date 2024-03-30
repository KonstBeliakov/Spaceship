import pygame as pg


def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) * 2) ** .5


def acceleration(x1, y1, x2, y2, m):
    d = dist(x1, y1, x2, y2)
    return m / (d ** 2)


def rotate(surface, angle, position):
    img = pg.transform.rotozoom(surface, angle, 1)
    img_rect = img.get_rect(center=position)
    return img, img_rect
