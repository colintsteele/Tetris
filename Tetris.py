import TetraFactory
import TetraBucket
import pygame


#region pygame initialization and configuration
pygame.init()
gameDisplay = pygame.display.set_mode((120,220))
pygame.display.set_caption('Taylor Swift\'s 1999 Buick LeSabre')

#bg = pygame.image.load('1993-buick-lesabre-7.jpg')
white = (255,255,255)
black = (10,10,10)
#endregion
gameDisplay.fill(black)

#region Tetra factory and Tetra Bucket initialization and configuration
factory = TetraFactory.Factory()
bucket = TetraBucket.Bucket(factory, gameDisplay)
#endregion

#region Main game loop
gameExit = False
while not gameExit:

    #set background to totally sic, undoctored pic of tswift and her lesabre
    #gameDisplay.blit(bg, (0, 0))
    #draw rectangle                     [posx, posy, width, height]

    #left edge
    pygame.draw.rect(gameDisplay, white, [0,0,10,220])
    #right edge
    pygame.draw.rect(gameDisplay, white, [110,0,10,220])
    #bottom edge
    pygame.draw.rect(gameDisplay, white, [0,210,120,10])
    #pygame.draw.rect(gameDisplay, white, [90,20,10,210])
    #pygame.draw.rect(gameDisplay, white, [150,20,10,210])
    pygame.display.update()

    for event in pygame.event.get():

        #pygame.display.update()

        if event.type == pygame.QUIT:
            gameExit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                bucket.move("down")
                pygame.display.update()
            if event.key == pygame.K_UP:
                bucket.move("up")
                pygame.display.update()
            if event.key == pygame.K_LEFT:
                bucket.move("left")
                pygame.display.update()
            if event.key == pygame.K_RIGHT:
                bucket.move("right")
                pygame.display.update()
            if event.key == pygame.K_i:
                bucket.test()



#endregion
pygame.quit()
quit()
