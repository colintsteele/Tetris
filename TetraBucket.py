#the Tetra Bucket is charged with keeping track of the tetras which are currently
import pygame
import TetraFactory

class Bucket():
    def __init__(self, factory, gameDisplay):
        self.factory = factory
        self.activeTetra = self.factory.newTetra()
        self.gameDisplay = gameDisplay
        self.range = []
        self.occupiedBlocks = [[0 for y in range(21)] for x in range(10)]
        #TODO list comprehension which initializes an empty 10X22 field (100 px by 220px + bottom row and edges = 120px x 230px)

    def rotateCW(self):
        stub = True
        #TODO create an actual rotate method, maybe with numpy

    def rotateCCW(self):
        stub = True
        #TODO create an actual rotate method, maybe with numpy

    def checkAdjacent(self, direction, tetra):
        'checks the bucket object\'s matrix to see if adjacent blocks are occupied or out of bounds'
        if direction.lower() == 'down':
            #we check to see if the tetra's posY is past badY
            if tetra.posY == 200:
                return True

        if direction.lower() == 'left':
            if tetra.posX == 10:
                return True

        if direction.lower() == 'right':
            if tetra.posX == 100:
                return True

    def move(self, direction = 'down'):
        'Move the active tetra a single space in the given direction'

        if self.checkAdjacent(direction, self.activeTetra):
            print('cannot move in that direction!')
            #TODO write exception for not being able to move, catch and do nothing... or something like that
        else:
            #moving in that direction is ok, check which direction to move in, and move there
            if direction.lower() == 'down':
                self.activeTetra.update("posY",self.activeTetra.posY+10)
                self.render(self.activeTetra)

            elif direction.lower() == 'left':
                self.activeTetra.update("posX",self.activeTetra.posX-10)
                self.render(self.activeTetra)

            elif direction.lower() == 'right':
                self.activeTetra.update("posX",self.activeTetra.posX+10)
                self.render(self.activeTetra)

            elif direction.lower() == 'up':
                self.activeTetra.update("posY",self.activeTetra.posY-10)
                self.render(self.activeTetra)

            else:
                print('no direction given')
                #TODO write exception for no direction being given

    def render(self, tetra):
        self.gameDisplay.fill((0,0,0))
        deets = [tetra.posX,tetra.posY,10,10]

        rows = len(self.activeTetra.orientation)
        columns =len(self.activeTetra.orientation[0])

        #for 1s in tetra:
        for i in rows:
            for j in columns:
                #pygame.draw.rect(self.gameDisplay, (255,255,255),
                if self.activeTetra.orientationp[i][j] == 1:
                    pygame.draw.rect(self.gameDisplay), (255,255,255), [tetra.posX+(i*10), tetra.posY+(j*10), 10,10]

        pygame.draw.rect(self.gameDisplay, (255,255,255), deets)
        pygame.display.update()

    def cement(self, tetra):
        stub = True
        #TODO write method for cement, where the active tetra cannot move down, and the timer for movement has expired


    def setActiveTetra(self, tetra):
        self.activeTetra = tetra

    def test(self):
        print(self.activeTetra.toHash())
        print(self.checkAdjacent('left', self.activeTetra))
        print(self.checkAdjacent('right', self.activeTetra))
        print(self.checkAdjacent('down', self.activeTetra))
        localX = self.activeTetra.posX
        localY = self.activeTetra.posX
        #print( 'x location:', int(localX-self.offset[0]) )
        #print( 'y location:', int(localY-self.offset[1]) )


        #print(self.occupiedBlocks[int(localX-self.offset[0]/10)][int(localY-self.offset[1]/10)])





