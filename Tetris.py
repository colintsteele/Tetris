import TetraFactory
import pygame

myFactory = TetraFactory.TetraFactory()

#create a random tetra
foo = myFactory.newTetra()
foo.toHash()

pygame.init()
gameDisplay = pygame.display.set_mode((600,800))
pygame.display.set_caption('Taylor Swift\'s 1999 Buick LeSabre')


gameExit = False

while not gameExit:
    for event in pygame.event.get():
        print(event)

pygame.display.update()

pygame.quit()


quit()
