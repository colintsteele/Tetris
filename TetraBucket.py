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
        self.occupiedBlocks = [[0 for y in range(21)] for x in range(10)]

    def rotate(self):
        'method to rotate the given tetra in place using numpy'
        self.activeTetra.orientation = np.rot90(np.array(self.activeTetra.orientation), 1)
        self.render(self.activeTetra)



    def checkAdjacent(self, direction, tetra):
        'checks the bucket object\'s matrix to see if adjacent blocks are occupied or out of bounds'
        # if direction.lower() == 'down':
        #     #find lowest tetra block
        #     if tetra.posY == 100:
        #         print('eek')
        #         return True

        if direction.lower() == 'down':
            if tetra.posY + len(tetra.orientation)*5 == 105:
                print(self.getCoords(tetra))
                return True


        if direction.lower() == 'left':
            #find leftmost tetra block
            if tetra.posX == 5:
                print('eek')
                return True

        if direction.lower() == 'right':
            #find rightmost tetra block
            if tetra.posX + len(tetra.orientation[0])*5 == 55:
                return True

    def move(self, direction = 'down'):
        'Move the active tetra a single space in the given direction'

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
                #TODO write exception for no direction being given
        self.activeTetra.toHash()

    def render(self, tetra):
        self.gameDisplay.fill((0,0,0))
        first = True

        row = 0
        for i in tetra.orientation:
            col = 0
            for j in i:
                try:
                    if j == 1:
                        x = tetra.posX + (10 * col)
                        y = tetra.posY + (10 * row)
                        if first:
                            pygame.draw.rect(self.gameDisplay, (255,255,255), [tetra.posX+(x), tetra.posY+(y), 10,10])
                            first = False
                        else:
                            pygame.draw.rect(self.gameDisplay, (200,200,200), [tetra.posX+(x), tetra.posY+(y), 10,10])

                except:
                    #print(i, j)#[ix, iy] j
                    #print(j == 1)#truthy
                    traceback.print_exc()
                col+=1

            row+=1

        #pygame.draw.rect(self.gameDisplay, (255,255,255), deets)
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

    def getCoords(self, tetra):
        space = []
        row = 0
        for i in tetra.orientation:
            col = 0
            for j in i:
                if j == 1:
                    space.append( (tetra.posX+col*5, tetra.posY+row*5) )
                col +=1
            row+=1
        return space




