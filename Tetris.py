import TetraFactory
import pygame


myFactory = TetraFactory.TetraFactory()

#create a random tetra
foo = myFactory.newTetra()
activeTetra = foo

pygame.init()
gameDisplay = pygame.display.set_mode((600,800))
pygame.display.set_caption('Taylor Swift\'s 1999 Buick LeSabre')
bg = pygame.image.load('1993-buick-lesabre-7.jpg')

white = (255,255,255)
black = (10,10,10)

gameExit = False

#Main game loop
while not gameExit:

    #set background to totally sic, undoctored pic of tswift and her lesabre
    gameDisplay.blit(bg, (0, 0))
    #draw rectangle
    pygame.draw.rect(gameDisplay, white, [20, 500, 10, 10])

    for event in pygame.event.get():

        pygame.display.update()

        if event.type == pygame.QUIT:
            gameExit = True


pygame.quit()

quit()
