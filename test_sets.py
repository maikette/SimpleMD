import random
import numpy as np
import constants as con
import classes

box = np.array([30, 30])
dim = 2
nearest = 1

def mag(a):
    return np.linalg.norm(a)

def nearest_image(par1,par2):
    #Returns a vector pointing from par1 to par2's nearest imagine, under periodic boundary conditions. 
    #print(par1.output_string())
    #print(par2.output_string())
    r_min = (par1.pos-par2.pos) / box #Find the simple distance, adjusted to be fraction of box length
    #print(r_min *constants.box)
    r_norm = mag(r_min) 
    for k in con.combin: 
        r_curr = r_min + k
        #print(r_curr)
        #print(mag(r_curr))
        if mag(r_curr) < r_norm:
            r_min = r_curr
    #print(r_min *constants.box)
    return r_min * box

output = "pos1.txt"

type = [0]
num = 50

with open(output,'w') as f:
    f.close()

with open(output,'a') as f:
    for i in range(0,num):
        goodFlag = True
        ty = random.choice(type)
        con.part_list.append(classes.Particle(random.uniform(0,box[0]), random.uniform(0,box[1]),ty))
        ty = random.choice(type)
        while goodFlag:
            par = classes.Particle(random.uniform(0,box[0]), random.uniform(0,box[1]),ty)
            for particle in con.part_list:
                r = nearest_image(par,particle)
                if mag(r) >= mag(nearest):
                    goodFlag = False
        con.part_list.append(par)
        f.write("type " + str(par.type))
        f.write(" | " + str(par.pos[0]) + " " + str(par.pos[1]))
        f.write("\n")