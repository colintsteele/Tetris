class Tetra(object):
    # let A and B be the dimensions of the tetra itself.
    # Some tetras need only be 2x2, while other, more accommodating tetras are 4x1
    __X = 10
    __Y = 20

    def __init__(self, a, b, x=__X, y=__Y):
        # let x and y be the given "board" dimensions.  The standard board dimensions are:
        self.shape = [[0 for i in range(a)] for j in range(b)]
        # TODO rip out hardcoded position, pass game board to __init__ and have position refernce that board
        self.pos = [[0 for f in range(x)] for g in range(y)]
        self.color = ''

    #
    def showDim(self):
        # The rules for rotating a tetra will change given its dimensions.
        #TODO change .format(a=self.__X... to a=self.shape dims
        print('I am a Tetra and my size is {a} x {b}'.format(a=self.__X, b=self.__Y))
