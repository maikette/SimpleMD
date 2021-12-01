#Verlet integration

# Particle Class, to store particle information.
# Stores location, 
class Particle:
    def __init__(self, x, y, type = 0):
        #type (type for interactions)
        self.type = type
        #postion
        self.x = x
        self.y = y
        #velocity
        self.xvel = 0
        self.yvel = 0
        #forces
        self.xfor = 0
        self.yfor = 0


#I may implment a linked-list cell method, if there is time. 
class Cell:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z