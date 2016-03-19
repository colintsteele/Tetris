class Tetra(object):
    def __init__(self, orientation, dimX, dimY):
        #shape and orientation are the same thing
        self.orientation = orientation
        self.dimX = dimX
        self.dimY = dimY

        self.posX = 50
        self.posY = 0


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


