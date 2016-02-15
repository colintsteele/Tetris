#the Tetra Bucket is charged with keeping track of the tetras which are currently

class Bucket(object):
    def __init__(self, field):
        self.activeTetra = None
        #TODO list comprehension which initializes an empty 10X22 field (100 px by 220px + bottom row and edges = 120px x 230px)

    def setActiveTetra(self, tetra):
        self.activeTetra = tetra

    def rotateCW(self):
        stub = True
        #TODO create an actual rotate method, maybe with numpy

    def rotateCCW(self):
        stub = True
        #TODO create an actual rotate method, maybe with numpy

    def move(self, direction = 'down'):
        stub = True
        #TODO create an actual down method
        #
