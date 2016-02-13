class Tetra(object):
    # let A and B be the dimensions of the tetra itself.
    # Some tetras need only be 2x2, while other, more accommodating tetras are 4x1

    def __init__(self, shape, dimX, dimY):
        self.shape = shape
        self.dimX = dimX
        self.dimY = dimY

    def toHash(self):
        return {'shape':self.shape,'dimX':self.dimX,'dimY':self.dimY}

