import pygame
import random
import src.bullet

class Rocket(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10
        self.health = 4

    def damage(self,opponent):
        if(random.randrange(1)):
            self.health -= 1
            return False
            if self.rocket.health == 0:
                self.state = "exit"

    def move(self, direction):
        if "RIGHT" in direction:
            self.rect.x += self.speed
        if "LEFT" in direction:
            self.rect.x -= self.speed
        if "UP" in direction:
            self.rect.y -= self.speed
        if "DOWN" in direction:
            self.rect.y += self.speed
        #if "SPACE" in direction:
            #self.bullets = pygame.Rect(self.rocket.x + self.rocket.get_width() / 2-2, self.rocket.y -15,5,10)
        if "NE" in direction:
            self.rect.x += self.speed
            self.rect.y -= self.speed
        if "NW" in direction:
            self.rect.x -= self.speed
            self.rect.y -= self.speed
        if "SE" in direction:
            self.rect.x += self.speed
            self.rect.y += self.speed
        if "SW" in direction:
            self.rect.x -= self.speed
            self.rect.y += self.speed

    def release_shoot(self):
        return src.bullet.Bullet(self.rect.x, self.rect.y, "assets/bullet.png")

    def update(self):
        if self.rect.x < 0:
            self.rect.x = 0
        else:
            self.rect.x = 250
            self.rect.y = 468
	 	#pygame.key.set_repeat(1,60)



