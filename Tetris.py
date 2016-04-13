import TetraFactory
import TetraBucket
import pygame

#pygame initialization and configuration
pygame.init()
gameDisplay = pygame.display.set_mode((120,220))
pygame.display.set_caption('Tetrus')

#bg = pygame.image.load('1993-buick-lesabre-7.jpg')
white = (255,255,255)
black = (10,10,10)

gameDisplay.fill(black)

#Tetra factory and Tetra Bucket initialization and configuration
factory = TetraFactory.Factory()
bucket = TetraBucket.Bucket(factory, gameDisplay)

gameExit = False

pygame.time.set_timer(pygame.USEREVENT+1, 300)

while not gameExit:

    pygame.draw.rect(gameDisplay, white, [0,0,10,220])
    pygame.draw.rect(gameDisplay, white, [110,0,10,220])
    pygame.draw.rect(gameDisplay, white, [0,210,110,10])
    #left edge

    bucket.update()
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.USEREVENT+1:
            bucket.move('down')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                bucket.move("down")
            if event.key == pygame.K_UP:
                bucket.move("up")
            if event.key == pygame.K_LEFT:
                bucket.move("left")
            if event.key == pygame.K_RIGHT:
                bucket.move("right")
            if event.key == pygame.K_f:
                bucket.rotate()
            if event.key == pygame.K_i:
                print(bucket.getCoords())
            if event.key == pygame.K_c:
                bucket.update()
                bucket.cement()

        if event.type == pygame.QUIT:
            gameExit = True

pygame.quit()
quit()
