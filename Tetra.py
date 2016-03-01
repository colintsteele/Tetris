class Tetra(object):
    def __init__(self, shape, dimX, dimY):
        self.shape = shape
        self.dimX = dimX
        self.dimY = dimY
        self.posX = 5
        self.posY = 5

    def update(self, choice, value):
        if choice.lower() == "posx":
            self.posX = value
        if choice.lower() == "posy":
            self.posY = value
        if choice.lower() == "dimx":
            self.dimX = value
        if choice.lower() == "dimy":
            self.dimY = value


    def toHash(self):
        return {'shape':self.shape,'dimX':self.dimX,'dimY':self.dimY,"posX":self.posX,"posY":self.posY}


