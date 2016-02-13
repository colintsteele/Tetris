import Tetra

class TetraFactory:

    __Cube = [[1,1],[1,1]]
    __L = [[1,0],[1,0],[1,0],[1,1]]
    __backwardsL = [[0,1],[0,1],[0,1],[1,1]]
    __Z = [[0,1],[1,1],[1,0]]
    __backwardsZ = [[1,0],[1,1],[0,1]]
    __T = [[0,1,0],[1,1,1]]
    __Jesus = [[1],[1],[1],[1]]

    def new(self, shape):
        if shape.lower() == 'cube':
            return Tetra.Tetra(self.__Cube, 2, 2)

        if shape.lower =='L':
            return Tetra.Tetra(self.__L, 2, 3)

        if shape.lower =='backwardsL':
            return Tetra.Tetra(self.__backwardsL, 2, 3)

        if shape.lower =='Z':
            return Tetra.Tetra(self.__Z, 2, 3)

        if shape.lower =='backwardsZ':
            return Tetra.Tetra(self.__backwardsZ, 2, 3)

        if shape.lower =='T':
            return Tetra.Tetra(self.__T, 3, 2)

        if shape.lower =='jesus':
            return Tetra.Tetra(self.__Jesus, 1, 4)



