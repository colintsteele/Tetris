#the Tetra Bucket is charged with keeping track of the tetras which are currently
import pygame
import TetraFactory

class Bucket(object):
    def __init__(self, factory, gameDisplay):
        self.factory = factory
        self.activeTetra = self.factory.newTetra()
        self.gameDisplay = gameDisplay
        #TODO list comprehension which initializes an empty 10X22 field (100 px by 220px + bottom row and edges = 120px x 230px)

    def rotateCW(self):
        stub = True
        #TODO create an actual rotate method, maybe with numpy

    def rotateCCW(self):
        stub = True
        #TODO create an actual rotate method, maybe with numpy

    def checkAdjacent(self, direction, tetra):
        stub = True


    def move(self, direction = 'down'):
        #see if it is ok to move in the given direction
        #if not self.checkAdjacent(direction, self.activeTetra):
        if False:
            print('cannot move in that direction!')
            #TODO write exception for not being able to move, catch and do nothing... or something like that
        else:
            #moving in that direction is ok, check which direction to move in, and move there
            if direction.lower() == 'down':
                print("hey")
                self.activeTetra.update("posY",self.activeTetra.posY+10)
                self.render(self.activeTetra)
                print(self.activeTetra.toHash())

            elif direction.lower() == 'left':
                stub = True

            elif direction.lower() == 'right':
                stub = True
            elif direction.lower() == 'top':
                stub = True
            else:
                print('no direction given')
                #TODO write exception for no direction being given

    def render(self, tetra):
        self.gameDisplay.fill((0,0,0))
        deets = [tetra.posX,tetra.posY,10,10]
        pygame.draw.rect(self.gameDisplay, (255,255,255), deets)
        pygame.display.update()

    def cement(self, tetra):
        stub = True
        #TODO write method for cement, where the active tetra cannot move down, and the timer for movement has expired


    def setActiveTetra(self, tetra):
        self.activeTetra = tetra





