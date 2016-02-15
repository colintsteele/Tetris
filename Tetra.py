class Tetra(object):
    def __init__(self, shape, dimX, dimY):
        self.shape = shape
        self.dimX = dimX
        self.dimY = dimY
        self.pos = [[]]

    def toHash(self):
        return {'shape':self.shape,'dimX':self.dimX,'dimY':self.dimY}


