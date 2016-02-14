class Tetra(object):
    def __init__(self, shape, dimX, dimY):
        self.shape = shape
        self.dimX = dimX
        self.dimY = dimY

    def toHash(self):
        return {'shape':self.shape,'dimX':self.dimX,'dimY':self.dimY}

    def rotate(self):
        print('create a rotate method')
        #TODO create an actual rotate method, maybe with numpy