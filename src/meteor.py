import pygame
import random

class Meteor(pygame.sprite.Sprite):
    def __init__(self, x, y, eid):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/asteroid.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.id = eid


