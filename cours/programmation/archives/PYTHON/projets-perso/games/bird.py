import pygame

class Bird:
    def __init__(self, x, y):
        self.image = pygame.image.load("bird.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = 0
        self.gravity = 0.5
        self.jump_speed = -8

    def update(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity

    def jump(self):
        self.velocity = self.jump_speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
