import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3
        self.direction = 90
        #self.bullet = none
        self.bullet = []

    def update(self):
        #game.screen.blit(self.image, self.rect)
        #self.rect.y += self.speed * self.direction
        #if self.rect.y < 15 or self.rect.y > 600:
         #       self.kill()
        #if self.rect.y > 0:
         #   self.direction = 'u'
        #elif self.rect.y < 0:
         #   self.kill()

       # if self.direction == 'u':
        self.rect.y -= self.speed
