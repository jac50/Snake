#import pygame
#from pygame.locals import *

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

#set up window

windowSurface = pygame.display.set_mode((500,500),0,32)
pygame.display.set_caption('Snake V0.0')

#Draw Wall
pygame.draw.line(windowSurface,BLACK,(10,10), (490,10))
pygame.draw.line(windowSurface,BLACK,(10,10), (10,490))
pygame.draw.line(windowSurface,BLACK,(490,10), (490,490))
pygame.draw.line(windowSurface,BLACK,(10,490), (490,490))

snake = pygame.draw.rect(windowSurface,GREEN,(30,500,10,10))
direction = 0
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		
		keys = pygame.key.get_pressed()
		if (keys[pygame.K_UP] != 0):
			snake.top -= MOVESPEED
		else if (keys[pygame.K_LEFT] != 0):
			snake.left -= MOVESPEED
		else if (keys[pygame.K_RIGHT] != 0):
			snake.right -=MOVESPEED
		else if (keys[pygame.k.DOWN] != 0):
			snake.down -=MOVESPEED
		
		collisonDetect(snake)
		
		pygame.display.update()
	time.sleep(0.02)



def collisionDetect(snake):
	if snake.top < 0 || snake.left < 0 || snake.down > 500 || snake.right > 500:
	# Collision with wall.
	# END GAME
	
