import pygame
import random

class Pipe:
    def __init__(self, x):
        self.image_top = pygame.image.load("pipe_top.png")
        self.image_bottom = pygame.image.load("pipe_bottom.png")
        self.rect_top = self.image_top.get_rect()
        self.rect_bottom = self.image
