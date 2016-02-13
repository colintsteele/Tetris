import Tetra
import TetraFactory
myFactory = TetraFactory.TetraFactory()

#create a cube tetra
foo = myFactory.new('cube')
foo.toHash()
print(type(foo))