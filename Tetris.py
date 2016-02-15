import TetraFactory
import pygame


myFactory = TetraFactory.TetraFactory()

#create a random tetra
foo = myFactory.newTetra()
foo.toHash()

pygame.init()
gameDisplay = pygame.display.set_mode((600,800))
pygame.display.set_caption('Taylor Swift\'s 1999 Buick LeSabre')
bg = pygame.image.load('1993-buick-lesabre-7.jpg')

white = (255,255,255)
black = (10,10,10)

gameExit = False

#gameDisplay.fill(black)

while not gameExit:
    for event in pygame.event.get():
        gameDisplay.blit(bg, (0, 0))
        pygame.display.update()

        if event.type == pygame.QUIT:
            gameExit = True


pygame.quit()

quit()
