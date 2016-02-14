import Tetra
import random

class TetraFactory:

    __shapeList = {
        'cube' : [[1,1],[1,1]],
        'L' : [[1,0],[1,0],[1,0],[1,1]],
        'backwardsL' : [[0,1],[0,1],[0,1],[1,1]],
        'Z' : [[0,1],[1,1],[1,0]],
        'backwardsZ' : [[1,0],[1,1],[0,1]],
        'T' : [[0,1,0],[1,1,1]],
        'Jesus' : [[1],[1],[1],[1]]
    }

    def newTetra(self, shape='random'):
        if shape.lower() == 'random':
            #pick a random shape by name.
            shape = random.choice(list(self.__shapeList.keys()))

        if shape.lower() == 'cube':
            return Tetra.Tetra(self.__shapeList['cube'], 2, 2)

        if shape.lower =='L':
            return Tetra.Tetra(self.__shapeList['L'], 2, 3)

        if shape.lower =='backwardsL':
            return Tetra.Tetra(self.__shapeList['backwardsL'], 2, 3)

        if shape.lower =='Z':
            return Tetra.Tetra(self.__shapeList['Z'], 2, 3)

        if shape.lower =='backwardsZ':
            return Tetra.Tetra(self.__shapeList['backwardsZ'], 2, 3)

        if shape.lower =='T':
            return Tetra.Tetra(self.__shapeList['T'], 3, 2)

        if shape.lower =='jesus':
            return Tetra.Tetra(self.__shapeList['Jesus'], 1, 4)



