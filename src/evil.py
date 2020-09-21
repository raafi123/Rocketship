import pygame
import random

class Evil(pygame.sprite.Sprite):
    def __init__(self, x, y, eid):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/evil.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3
        self.id = eid


    def update(self):
        self.rect.x += (random.randrange(-2,3))
        self.rect.y += (random.randrange(-2,3))
        #self.rect.x += self.speed
        #self.rect.y += random.randrange(-1,2)
        if self.rect.x <= 0:
            self.rect.x = 468
        if self.rect.x >= 468:
            self.rect.x = 0
        if self.rect.y <= 0:
           self.rect.y += 468
        if self.rect.y >= 468:
           self.rect.y = 0

