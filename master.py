import classes
import constants
import numpy as np
import math

def mag(a):
    return math.sqrt(np.dot(a,a))

def normalized(a, axis=-1, order=2):
    #barrowed from here https://stackoverflow.com/questions/21030391/how-to-normalize-a-numpy-array-to-a-unit-vector
    l2 = np.atleast_1d(np.linalg.norm(a, order, axis))
    l2[l2==0] = 1
    return a / np.expand_dims(l2, axis)


def init_velocity():
    #Initalize velocity based on starting temp
    return

def initi(postion_inputs, constant_inputs):
    #Takes information in files stored in posInputs and conInputs, and loads into common files. 
    with open(postion_inputs,"r") as f:
        lines = f.readlines()
        for l in lines:
            if "type" in l: #Finds a line that contains particle information
                spl = l.split()
                constants.part_list.append(classes.Particle(int(spl[3]),int(spl[4]),int(spl[1]))) #Create particle object, saves to the particle list
    with open(constant_inputs,"r") as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            if "end ~" in lines[i]:
                break
            elif "maxstep" in lines[i]:
                constants.maxstep = int(lines[1].split()[1])
            elif "dt" in lines[i]:
                constants.dt = float(lines[i].split()[1])
            elif "cutoff" in lines[i]:
                constants.cutoff = float(lines[i].split()[1])
            elif "box" in lines[i]:
                constants.box = [float(k) for k in lines[i].split()[1:]]
            elif "start_temp" in lines [i]:
                constants.start_temp = float(lines[i].split()[1])
            elif "masses" in lines[i]:
                k = i + 1
                while lines[k].split(): #While there is something more than a space in the line:
                    spl = lines[k].split()
                    constants.masses[int(spl[0])] = float(spl[2])
                    k = k + 1
            elif "interactions" in lines[i]:
                k = i + 1
                while lines[k].split(): #While there is something more than a space in the line:
                    spl = lines[k].split()
                    constants.interactions[(int(spl[0]),int(spl[1]))] = float(spl[3])
                    k = k + 1
            
    #init_velocity() #Initalize velocities
    return

def nearest_image(par1,par2):
    #Returns a vector pointing from par1 to par2's nearest imagine, under periodic boundary conditions. 
    r_max = (par1.pos-par2.pos) / constants.box #Find the simple distance, adjusted to be fraction of box length
    r_norm = mag(r_max) 
    for k in constants.combin:
        r_curr = r_max + k
        #print(r_curr)
        #print(mag(r_curr))
        if mag(r_curr) < r_norm:
            r_max = r_curr
    return r_max * constants.box

def forces(par1):
    #Calcuate pair forces based on the Lenard-Lones Potential. Compaires for all 
    
    return

def update_velocity():
    #updates velocities
    return

def update_pos():
    for par in constants.part_list:
        half_vel = par.vel + 0.5 * constants.masses[par.type]**(-1) * forces()
    return

def verlet():
    return
    #simple verlet with periodic boundary consitions. Updates postion and velocity

def outputStep():
    #Outputs info on the current system configuation to the output file.
    return

def check_pos_inputs():
    for par in constants.part_list:
        for i in len(par.pos):
            if par.pos[i] > constants.box[i]:
                print("Error - provided postion is outside bounds")

def output_positions():
    return

def output_thermodynamics():
    return

def run_md(position_inputs, constants_inputs):
    #Runs MD similation. 
    initi(position_inputs, constants_inputs) #Iniiate similation 
    while constants.current_step < constants.maxstep:
        verlet() #Calcuate forces, velocities, and updates postions
        output_positions() #Output postions
        output_thermodynamics() 
    #Outputs

    
    return


initi("pos.txt", "constants.txt")
print(constants.part_list)
print(constants.box)
print("dt: " + str(constants.dt))
print("cutoff: " + str(constants.cutoff))
print("start_temp: " + str(constants.start_temp))
print("masses: " + str(constants.masses))
print("interactions: " + str(constants.interactions))

print(nearest_image(classes.Particle(1,1), classes.Particle(4,4)))

h= 8
