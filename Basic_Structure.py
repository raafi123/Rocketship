import pygame
import turtle

class Rocket(pygame.sprite.Sprite(),turtle.Turtle()):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        turtle.Turtle.__init__(self)
        self.image=pygame.image.load("Spaceship.jpg")
        self.rect=self.image.get_rect()
        self.player=turtle.Turtle()
        self.state="alive"

    def update(self):
        pass
        # Kill the enemy if the weapon hits

    def shoot(self):
        # Shoot weapons
        



class GUI:
    def __init__(self):
        self.user=Rocket()
        self.enemy=Rocket()
        self.screen=pygame.display.set_mode((width,height))
        self.status="Run"

        def mainloop(self):
            while self.status=="Run":
                for event in pygame.event.get():
                    if event==pygame.QUIT:
                        self.status="Exit"
                    
        
