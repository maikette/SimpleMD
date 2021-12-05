#Verlet integration
import numpy as np
import constants

# Particle Class, to store particle information.
# Stores location, 
class Particle:
    def __init__(self, x, y, type = 0):
        #type (type for interactions)
        self.type = type
        #postion, [pos_x, pos_y]
        self.pos = np.array([x,y])
        #velocity, [vel_x, vel_y]
        self.vel = np.array([0,0])
        #forces, [force_x, force_y]
        self.force = np.array([0,0])
        self.ID = constants.next_id
        constants.next_id = constants.next_id + 1

    #def string_p():
    #    output = "ID: " + str(Self.ID)
    #    return output


#I may implment a linked-list cell method, if there is time. 
class Cell:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z