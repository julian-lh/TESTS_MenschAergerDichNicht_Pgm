#carClass
import pygame
pygame.init()

carImg = pygame.image.load('car.png')

def car(x,y):
	gameDisplay.blit(carImg, (x,y))

