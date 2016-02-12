class Tetra(object):
    # let A and B be the dimensions of the tetra itself.
    # Some tetras need only be 2x2, while other, more accommodating tetras are 4x1

    def __init__(self, shape, dimX, dimY):
        self.shape = shape
        self.dimX = dimX
        self.dimY = dimY

    #
    def showDim(self):
        # The rules for rotating a tetra will change given its dimensions.
        #TODO change .format(a=self.__X... to a=self.shape dims
        print('I am a Tetra and my size is {a} x {b}'.format(a=self.__X, b=self.__Y))

    def toHash(self):
        tetraHash = {'shape':self.shape,'dimX':self.dimX,'dimY':self.dimY}
        print(tetraHash)


