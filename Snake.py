import pygame
from pygame.locals import *
import time
import random
# Set up PyGame
pygame.init()

#Initialise Colours
BLACK = (0,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
#Set Fonts

fontBasic = pygame.font.SysFont(None,48)
fontSmall = pygame.font.SysFont(None,36)

#set up window

windowSurface = pygame.display.set_mode((500,500),0,32)
pygame.display.set_caption('Snake V0.0')

#Draw Wall
windowSurface.fill((255,255,255))
pygame.draw.line(windowSurface,BLACK,(10,10), (490,10))
pygame.draw.line(windowSurface,BLACK,(10,10), (10,490))
pygame.draw.line(windowSurface,BLACK,(490,10), (490,490))
pygame.draw.line(windowSurface,BLACK,(10,490), (490,490))
snake = pygame.draw.rect(windowSurface,GREEN,(30,50,10,10))
direction = 0
MOVESPEED = 10
posx = 30
posy = 50

randx = random.randrange(15,485) #gap of 15 either side
randy = random.randrange(15,485)
print (randx)
print (randy)
pygame.draw.line(windowSurface,RED,(randx - 10 , randy), (randx + 10, randy))
pygame.draw.line(windowSurface,RED,(randx,randy - 10), (randx, randy + 10))	
pygame.display.update()
newFood = False
while True:
	Running = True
	if (newFood == True):
		randx = random.randrange(15,485)
		randy = random.randrange(15,485)
		newFood = False
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		keys = pygame.key.get_pressed()
		
		if (keys[pygame.K_UP] != 0):
			direction = 1
		elif (keys[pygame.K_LEFT] != 0):
			direction = 4
		elif (keys[pygame.K_RIGHT] != 0):
			direction = 2
		elif (keys[pygame.K_DOWN] != 0):
			direction = 3
		
	if direction == 1:
		posy-=MOVESPEED
	elif direction == 2:
		posx+=MOVESPEED
	elif direction == 3:
		posy+=MOVESPEED
	elif direction == 4:
		posx-=MOVESPEED
	
			
	windowSurface.fill(WHITE)
	
	pygame.draw.line(windowSurface,BLACK,(10,10), (490,10))
	pygame.draw.line(windowSurface,BLACK,(10,10), (10,490))
	pygame.draw.line(windowSurface,BLACK,(490,10), (490,490))
	pygame.draw.line(windowSurface,BLACK,(10,490), (490,490))
	
	pygame.draw.line(windowSurface,RED,(randx - 5, randy), (randx + 5, randy))
	pygame.draw.line(windowSurface,RED,(randx,randy - 5), (randx, randy + 5))	
	snake = pygame.draw.rect(windowSurface,GREEN,(posx,posy,10,10))
	#print(snake.top)
	
	#Food Collision
	print (snake.centery)	
	if ((snake.centery >= randy - 8 and snake.centery <= randy + 8) and (snake.centerx >=randx - 8 and snake.centerx <=randx + 8)):
		
		print("YESYESYES")
		newFood = True
		
	if (snake.top < 10 or snake.left < 10 or snake.bottom > 490 or snake.right > 490):
		print("Game Over!\n")
		Running = False	
		label = fontBasic.render("Game Over!",1,(10,10,10))
		label2 = fontSmall.render("Press Enter to Continue or Esc to quit",1,(10,10,10))
		labpos = label.get_rect()
		lab2pos = label2.get_rect()
		labpos.centerx = windowSurface.get_rect().centerx
		lab2pos.centerx = labpos.centerx
		labpos.centery = windowSurface.get_rect().centery
		lab2pos.centery = labpos.centery + 50
		windowSurface.blit(label,labpos)
		windowSurface.blit(label2,lab2pos)
		pygame.display.update()
		while Running == False:
			print("Here")	
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.quit()
				key = pygame.key.get_pressed()
				if (key[pygame.K_RETURN]!=0):
					Running = True
					windowSurface.fill(WHITE)
					posx = 20
					posy = 30
					direction = 0
				elif (key[pygame.K_ESCAPE] != 0):
					pygame.quit()
			
			
	pygame.display.update()
	pygame.time.delay(50)



#def collisionDetect(snake):
#	if (snake.top < 0 or snake.left < 0 or snake.down > 500 or snake.right > 500):
#		pass
	# Collision with wall.
	# END GAME
	
