import TetraFactory
import TetraBucket
import pygame


#region pygame initialization and configuration
pygame.init()
gameDisplay = pygame.display.set_mode((600,800))
pygame.display.set_caption('Taylor Swift\'s 1999 Buick LeSabre')
bg = pygame.image.load('1993-buick-lesabre-7.jpg')
white = (255,255,255)
black = (10,10,10)
#endregion

#region Tetra factory and Tetra Bucket initialization and configuration
factory = TetraFactory.Factory()
bucket = TetraBucket.Bucket(factory, gameDisplay)
#endregion

#region Main game loop
gameExit = False
while not gameExit:

    #set background to totally sic, undoctored pic of tswift and her lesabre
    gameDisplay.blit(bg, (0, 0))
    #draw rectangle
    pygame.draw.rect(gameDisplay, white, [20, 500, 10, 10])

    for event in pygame.event.get():

        pygame.display.update()

        if event.type == pygame.QUIT:
            gameExit = True

        if event.type == pygame.KEYDOWN:
            bucket.move("down")


#endregion

pygame.quit()
quit()
