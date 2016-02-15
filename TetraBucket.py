#the Tetra Bucket is charged with keeping track of the tetras which are currently

class Bucket(object):
    def __init__(self):
        self.activeTetra = None
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
        if not self.checkAdjacent(direction, self.activeTetra):
            print('cannot move in that direction!')
            #TODO write exception for not being able to move, catch and do nothing... or something like that
        else:
            #moving in that direction is ok, check which direction to move in, and move there
            if direction.lower() == 'down':
                #stub

                self.activeTetra.pos[0] += 10


            elif direction.lower() == 'left':
                stub = True

            elif direction.lower() == 'right':
                stub = True
            elif direction.lower() == 'top':
                stub = True
            else:
                print('no direction given')
                #TODO write exception for no direction being given

    def cement(self, tetra):
        stub = True
        #TODO write method for cement, where the active tetra cannot move down, and the timer for movement has expired


    def setActiveTetra(self, tetra):
        self.activeTetra = tetra





