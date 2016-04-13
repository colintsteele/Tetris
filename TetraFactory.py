#The Tetra factory is in charge of creating new tetras.

import Tetra
import random

class Factory():
    #__shapeList
    # each tetra needs an origin point with which to sort of pin to the background

    __shapeList = {
        'cube': [[1,1],[1,1]],
        'L': [[1,0],[1,0],[1,1]],
        'backwardsL': [[0,1],[0,1],[1,1]],
        'Z': [[0,1],[1,1],[1,0]],
        'backwardsZ': [[1,0],[1,1],[0,1]],
        'T': [[0,1,0],[1,1,1]],
        'Jesus': [[1],[1],[1],[1]]
    }

    def newTetra(self, s = 'random'):
        #generate a random shape by default
        if s.lower() == 'random':
            shape = random.choice(list(self.__shapeList.keys()))

        else:
            shape = s
    
        #generate the given shape
        if shape.lower() == 'cube':
            return Tetra.Tetra(self.__shapeList['cube'], 2, 2)
        elif shape.lower() == 'l':
            return Tetra.Tetra(self.__shapeList['L'], 2, 3)
        elif shape.lower() == 'backwardsl':
            return Tetra.Tetra(self.__shapeList['backwardsL'], 2, 3)
        elif shape.lower() == 'z':
            return Tetra.Tetra(self.__shapeList['Z'], 2, 3)
        elif shape.lower() == 'backwardsz':
            return Tetra.Tetra(self.__shapeList['backwardsZ'], 2, 3)
        elif shape.lower() == 't':
            return Tetra.Tetra(self.__shapeList['T'], 3, 2)
        elif shape.lower() == 'jesus':
            return Tetra.Tetra(self.__shapeList['Jesus'], 1, 4)
        else:
            print('no shape generated')


