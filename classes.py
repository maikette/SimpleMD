#Verlet integration
import numpy as np
import constants as con

# Particle Class, to store particle information.
# Stores location, 
class Particle:
    def __init__(self, x, y, type = 0):
        #type (type for interactions)
        self.type = type
        #postion, [pos_x, pos_y]
        self.pos = np.array([float(x),float(y)])
        #velocity, [vel_x, vel_y]
        self.vel = np.array([0.0,0.0])
        #forces, [force_x, force_y]
        self.force = np.array([0.0,0.0])
        #previous force
        self.force_last = np.array([0.0,0.0])
        #self.ID = con.next_id
        #con.next_id = con.next_id + 1
        #Potential Energy:
        self.potential = 0.0

    def output_string(self):
        output = "Type: " + str(self.type)
        output += " | Pos: "
        for i in self.pos:
            output += str(i) + " "
        #    print(str(i))
        #    print(" ")
        output += "| Vel: "
        for i in self.vel:
            output += str(i) + " "
        return output


#I may implment a linked-list cell method, if there is time. 
class Cell:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z