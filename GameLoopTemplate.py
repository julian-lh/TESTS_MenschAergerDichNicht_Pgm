import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

crashed = False

while not crashed:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
		
#Hi Guys	 ---- Gayyyyy	
		
	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()








# Notizen
# Tupel: 800,600 oder (800,600)

#print(event)