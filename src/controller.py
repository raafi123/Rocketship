import pygame
import random
import src.rocket
import src.bullet
import src.meteor
import src.evil
import time

class Controller:
	def __init__(self):
		pygame.init() # ref - https://stackoverflow.com/questions/28517979/pygame-font-error/54082238
		self.score = 0
		pygame.font.init()
		pygame.display.set_caption("Space Force: Final Frontier")
		self.font = pygame.font.SysFont(None,30)
		self.display = pygame.display.set_mode((500, 500))
		self.background = pygame.image.load("assets/background.png").convert_alpha()
		self.rocket = src.rocket.Rocket(250, 400, "assets/spaceship.png")
		self.bullets = pygame.sprite.Group()
		self.enemies = pygame.sprite.Group()




	

		#Enemies
		num_enemies = 10
		evil_id = 1		
		for i in range(num_enemies):
			x = random.randrange(0, 468)
			y = random.randrange(0, 350)
			evil_id += 1
			self.enemies.add(src.evil.Evil(x, y, evil_id))

		#Meteors
		self.meteors = pygame.sprite.Group()
		num_meteors = 10
		meteor_id = 1		
		for i in range(num_meteors):
			x = random.randrange(0, 468)
			y = random.randrange(30, 400)
			meteor_id += 1
			self.meteors.add(src.meteor.Meteor(x, y, meteor_id))

		#Main Menu
		largeText = pygame.font.Font('freesansbold.ttf',50)
		self.textSurface = largeText.render("Space Force", True, (30,144,255))
		self.textRect = self.textSurface.get_rect()
		smallText = pygame.font.Font('freesansbold.ttf',20)
		self.textSurface2 = smallText.render("PLAY GAME!", True, (0,0,0))
		self.textRect2 = self.textSurface2.get_rect()
		self.textSurface3 = smallText.render("QUIT", True, (0,0,0))
		self.textRect3 = self.textSurface3.get_rect()		
		self.STATE = "intro"
		

		#End Menu
		largeText4 = pygame.font.Font('freesansbold.ttf',50)
		self.textSurface4 = largeText4.render("Thanks For Playing", True, (30,144,255))
		self.textRect4 = self.textSurface4.get_rect()
		smallText5 = pygame.font.Font('freesansbold.ttf',20)
		self.textSurface5 = smallText5.render("RESTART?", True, (0,0,0))
		self.textRect5 = self.textSurface5.get_rect()
		self.textSurface6 = smallText5.render("QUIT", True, (0,0,0))
		self.textRect6 = self.textSurface6.get_rect()		
		self.STATE2 = "end"
		


	def mainloop(self):
		while True:
			if self.STATE == "game":
				self.gameloop()
			elif self.STATE == "exit":
				self.exitloop()	
			elif self.STATE == "intro":
				self.introloop()
			elif self.STATE2 == "end":
				self.ending()

	def reset(self):
		self.score = 0
		self.time = 0

		self.rocket = src.rocket.Rocket(250, 400, "assets/spaceship.png")
		self.bullets = pygame.sprite.Group()
		self.enemies = pygame.sprite.Group()
		num_enemies = 10
		evil_id = 1		
		for i in range(num_enemies):
			x = random.randrange(0, 468)
			y = random.randrange(0, 350)
			evil_id += 1
			self.enemies.add(src.evil.Evil(x, y, evil_id))
		self.meteors = pygame.sprite.Group()
		num_meteors = 10
		meteor_id = 1		
		for i in range(num_meteors):
			x = random.randrange(0, 468)
			y = random.randrange(30, 400)
			meteor_id += 1
			self.meteors.add(src.meteor.Meteor(x, y, meteor_id))


	def introloop(self): #ref - https://pythonprogramming.net/pygame-start-menu-tutorial/
		pygame.display.update()
		while self.STATE == "intro":
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.STATE = "exit"
			self.display.fill((0,0,0))
			self.display.blit(self.background,(0,0))
			self.textRect.center = ((500/2),(100))
			self.display.blit(self.textSurface, self.textRect)			
			pygame.draw.rect(self.display, (0,200,0), (75,300,150,50))
			pygame.draw.rect(self.display, (200,0,0), (275,300,150,50))
			mouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			if 75+150 > mouse[0] > 75 and 300+50 > mouse[1] > 300:
				pygame.draw.rect(self.display, (0,255,0), (75,300,150,50))
				if click[0] == 1:
					#self.time = time.clock()
					self.STATE = "game"	
			if 275+150 > mouse[0] > 275 and 300+50 > mouse[1] > 300:
				pygame.draw.rect(self.display, (255,0,0), (275,300,150,50))
				if click[0] == 1:
					self.STATE = "exit"
			self.textRect2.center = ((75+(150/2)),(300+(50/2)))
			self.display.blit(self.textSurface2, self.textRect2)
			self.textRect3.center = ((275+(150/2)),(300+(50/2)))
			self.display.blit(self.textSurface3, self.textRect3)			
			pygame.display.update()

	def ending(self):
		pygame.display.update()
		while self.STATE == "end":
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.STATE = "exit"
			self.display.fill((0,0,0))
			self.display.blit(self.background,(0,0))
			self.textRect4.center = ((500/2),(100))
			self.display.blit(self.textSurface4, self.textRect4)			
			pygame.draw.rect(self.display, (0,200,0), (75,300,150,50))
			pygame.draw.rect(self.display, (200,0,0), (275,300,150,50))
			mouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			if 75+150 > mouse[0] > 75 and 300+50 > mouse[1] > 300:
				pygame.draw.rect(self.display, (0,255,0), (75,300,150,50))
				if click[0] == 1:
					self.STATE = "game"	
			if 275+150 > mouse[0] > 275 and 300+50 > mouse[1] > 300:
				pygame.draw.rect(self.display, (255,0,0), (275,300,150,50))
				if click[0] == 1:
					self.STATE = "exit"
			self.textRect5.center = ((75+(150/2)),(300+(50/2)))
			self.display.blit(self.textSurface5, self.textRect5)
			self.textRect6.center = ((275+(150/2)),(300+(50/2)))
			self.display.blit(self.textSurface6, self.textRect6)			
			pygame.display.update()


	def gameloop(self):
		pygame.display.update()
		pygame.key.set_repeat(1,60)
		#self.time = time.clock()
		while self.STATE == "game":
			self.time = time.clock()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.STATE = "exit"
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						a = self.rocket.release_shoot()
						self.bullets.add(a)
					if event.key == pygame.K_RIGHT:
						self.rocket.move("RIGHT")
					if event.key == pygame.K_LEFT:
						self.rocket.move("LEFT")
					if event.key == pygame.K_UP:
						self.rocket.move("UP")
					if event.key == pygame.K_DOWN:
						self.rocket.move("DOWN")
					if event.key == pygame.K_w:
						self.rocket.move("NE")
					if event.key == pygame.K_a:
						self.rocket.move("NW")
					if event.key == pygame.K_s:
						self.rocket.move("SE")
					if event.key == pygame.K_d:
						self.rocket.move("SW")
			#rocket borders
			if self.rocket.rect.x <= 0:
				self.rocket.rect.x = 0
			if self.rocket.rect.x >= 468:
				self.rocket.rect.x = 468
			if self.rocket.rect.y <= 0:
				self.rocket.rect.y = 0
			if self.rocket.rect.y >= 468:
				self.rocket.rect.y = 468
			#check for collisions

			#Bullet/Enemy collisions
			lst = self.bullets.sprites()
			colliding_enemies = []			
			for bulli in lst:
				lst2 = len(colliding_enemies)
				colliding_enemies.extend(pygame.sprite.spritecollide(bulli, self.enemies, False))
				lst3 = len(colliding_enemies)
				while (lst3 - lst2) > 1:
					colliding_enemies.pop()
					lst3 = len(colliding_enemies)
			for collisions in colliding_enemies:
				collisions.kill()
				bulli.kill()
				self.score += 100
				if self.score == 1000:
					self.reset()
					self.STATE = "end"
					self.ending()
					


			#Rocket/Enemy collision
			for enemy in self.enemies:
				if enemy.rect.colliderect(pygame.Rect(self.rocket.rect.x, self.rocket.rect.y, self.rocket.image.get_width(), self.rocket.image.get_height())):
					self.rocket.health -= 1
					self.rocket.update()
				if self.rocket.health == 0:
					self.reset()
					self.STATE = "intro"
					self.introloop()
					
					#self.rocket.health += 100
					#self.STATE = "intro"
					#self.introloop()

			#Meteor obstacle collision
			lst2 = self.bullets.sprites()
			colliding_meteors = []			
			for bulli in lst:
				lst4 = len(colliding_meteors)
				colliding_meteors.extend(pygame.sprite.spritecollide(bulli, self.meteors, False))
				lst5 = len(colliding_meteors)
				while (lst5 - lst4) > 1:
					colliding_meteors.pop()
					lst4 = len(colliding_meteors)
			for collisions in colliding_meteors:
				bulli.kill()

			#If rocket touches meteor, rocket resets
			for meteor in self.meteors:
				if meteor.rect.colliderect(pygame.Rect(self.rocket.rect.x, self.rocket.rect.y, self.rocket.image.get_width(), self.rocket.image.get_height())):
					self.rocket.update()

			self.display.fill((0,0,0))
			self.display.blit(self.background,(0,0))
			self.enemies.update()
			self.meteors.update()

			for i in self.bullets:
				if i.rect.y < 0:
					i.kill()
			self.bullets.update()
		#all drawing stuff below
			self.enemies.draw(self.display)
			self.bullets.draw(self.display)
			self.meteors.draw(self.display)

		#displays score and health%
			self.display.blit(self.font.render("Score: {}".format(self.score), -1,(255,255,255)),(200,10))
			self.display.blit(self.font.render("Lives: {}".format(self.rocket.health), -1,(255,255,255)),(10,10))

			self.display.blit(self.font.render("Time: {}".format(self.time), -1,(255,255,255)),(400,10))


			#self.display.blit(self.font.render("Time: {}".format(inital_time/100000), -1,(255,255,255)),(300,10))



			self.display.blit(self.rocket.image, (self.rocket.rect.x, self.rocket.rect.y))
			pygame.display.flip()

	def exitloop(self):
		pygame.quit()
		exit()

