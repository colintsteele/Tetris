#the Tetra Bucket is charged with keeping track of the tetras which are currently
import pygame
import numpy
import np
import TetraFactory
import traceback

class Bucket():
    def __init__(self, factory, gameDisplay):
        self.factory = factory
        self.activeTetra = self.factory.newTetra()
        self.gameDisplay = gameDisplay
        self.range = []
        self.occupiedBlocks = [[0 for y in range(22)] for x in range(11)]

    def update(self):
        'draws occupiedblocks'
        for i in range(0,11):
            for j in range(0,22):
                if self.occupiedBlocks[i][j] == 1:
                    pygame.draw.rect(self.gameDisplay, (255,255,255), [i*10, j*10, 10, 10])


    def rotate(self):
        'method to rotate the given tetra in place using numpy'
        self.activeTetra.orientation = np.rot90(np.array(self.activeTetra.orientation), 1)
        self.render(self.activeTetra)

    def checkAdjacent(self, direction, tetra):
        'checks the bucket object\'s matrix to see if adjacent blocks are occupied or out of bounds'
        #print('checking: {} : {}').format(self.getCoords(),tetra.posY/5+len(tetra.orientation))
        #bounds
        if direction.lower() == 'down':
            #lower bound
            if (tetra.posY + len(tetra.orientation)*5 == 105):
                self.cement()
                return True

            #if the lowest tetra block is just above an occupied block
            for i in self.getCoords():
                if self.occupiedBlocks[i[0]][i[1]+1] == 1:
                    self.cement()
                    return True


        if direction.lower() == 'left':
            #left bound
            if tetra.posX == 5:
                return True
            #left tetra
            for i in self.getCoords():
                if self.occupiedBlocks[i[0]-1][i[1]] == 1:
                    return True

        if direction.lower() == 'right':
            #right bound
            if tetra.posX + len(tetra.orientation[0])*5 == 55:
                return True
            for i in self.getCoords():
                if self.occupiedBlocks[i[0]+1][i[1]] == 1:
                    return True

    def cement(self):
        coords = self.getCoords()
        for i in coords:
            self.occupiedBlocks[i[0]][i[1]] = 1

        self.activeTetra = self.factory.newTetra()

    def move(self, direction = 'down'):
        'Move the active tetra a single space in the given direction'
        self.update()

        if self.checkAdjacent(direction, self.activeTetra):
            print('cannot move in that direction!')

        else:
            #moving in that direction is ok, check which direction to move in, and move there
            if direction.lower() == 'down':
                self.activeTetra.update("posY",self.activeTetra.posY+5)
                self.render(self.activeTetra)

            elif direction.lower() == 'left':
                self.activeTetra.update("posX",self.activeTetra.posX-5)
                self.render(self.activeTetra)

            elif direction.lower() == 'right':
                self.activeTetra.update("posX",self.activeTetra.posX+5)
                self.render(self.activeTetra)

            elif direction.lower() == 'up':
                self.activeTetra.update("posY",self.activeTetra.posY-5)
                self.render(self.activeTetra)

            else:
                print('no direction given')


    def render(self, tetra):
        self.gameDisplay.fill((0,0,0))

        for i in self.getCoords():
            pygame.draw.rect(self.gameDisplay, (122, 43, 175), [i[0]*10, i[1]*10, 10, 10] )


    def setActiveTetra(self, tetra):
        self.activeTetra = tetra

    def test(self):
        print(self.activeTetra.toHash())
        print(self.checkAdjacent('left', self.activeTetra))
        print(self.checkAdjacent('right', self.activeTetra))
        print(self.checkAdjacent('down', self.activeTetra))

    def getCoords(self):
        'return a list of tuples which contain the indices the active tetra occupies'
        tetra = self.activeTetra
        space = []
        row = 0

        for i in tetra.orientation:
            col = 0
            for j in i:
                if j == 1:
                    space.append( (int((tetra.posX)/5+col), int((tetra.posY)/5+row)) )
                col +=1
            row+=1

        return space




