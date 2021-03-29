import pygame
import sys

pygame.init()

class Sprite():
    def __init__(self,
        image: pygame.Surface,
        x: int,
        y: int
        ):

        self.image = image

        self.x = x
        self.y = y
        self.position = (x, y)
