class Tetra(object):
    def __init__(self, orientation, dimX, dimY):
        self.orientation = orientation
        self.dimX = dimX
        self.dimY = dimY

        self.posX = 50
        self.posY = 0

        rows = len(orientation)
        columns =len(orientation[0])

        #draw square on surface

    def update(self, choice, value):
        if choice.lower() == "posx":
            self.posX = value
        if choice.lower() == "posy":
            self.posY = value
        if choice.lower() == "dimx":
            self.dimX = value
        if choice.lower() == "dimy":
            self.dimY = value

    def test(self):
        print(self.orientation)

    def toHash(self):
        print( {'shape':self.orientation,'dimX':self.dimX,'dimY':self.dimY,"posX":self.posX,"posY":self.posY} )


