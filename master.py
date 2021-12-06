from itertools import product
from numpy.lib.function_base import _parse_input_dimensions

from numpy.lib.type_check import common_type
import classes
import constants as con
import numpy as np
import math
from random import gauss
import matplotlib.pyplot as plt

def mag(a):
    return np.linalg.norm(a)

def normalized(a, axis=-1, order=2):
    #barrowed from here https://stackoverflow.com/questions/21030391/how-to-normalize-a-numpy-array-to-a-unit-vector
    l2 = np.atleast_1d(np.linalg.norm(a, order, axis))
    l2[l2==0] = 1
    return a / np.expand_dims(l2, axis)

def init_velocity():
    #Initalize velocity based on starting temp
    for par in con.part_list:
        par.vel = (con.kB * con.start_temp / con.masses[par.type] ) ** 0.5 * np.array([gauss(0,1),gauss(0,1)])
    return

def starting_force():
    #Calcuate pair forces based on the Lenard-Lones Potential. Compaires for all 
    for i in range(len(con.part_list)):
        curr_par = con.part_list[i]
        curr_par.force.fill(0) #make all forces zero here to start
        #print(constants.part_list[np.arange(len(constants.part_list)) != i])
        for inter_par in con.part_list[np.arange(len(con.part_list)) != i]:
            #inter_par = interact[0]
            r = nearest_image(curr_par,inter_par)
            r_mag = mag(r)
            #print(r_mag)
            if r_mag <= con.cutoff:
                r_hat = normalized(r)
                #print(r_mag)
                if (curr_par.type, inter_par.type) in con.interactions:
                    a = con.interactions[curr_par.type, inter_par.type][0]
                    b = con.interactions[curr_par.type, inter_par.type][1]
                elif (inter_par.type, curr_par.type) in con.interactions:
                    a = con.interactions[inter_par.type, curr_par.type][0]
                    b = con.interactions[inter_par.type, curr_par.type][1]
                else: 
                    print("error - no interaction listed")
                curr_force = (6*b / r_mag**7 - 12*a / r_mag**13) * r_hat
                #print(curr_force)
                con.part_list[i].force_last = con.part_list[i].force_last + curr_force
                #print(constants.part_list[i].force)
                #print ("\n")
            return

def initi(postion_inputs, constant_inputs):
    #Takes information in files stored in posInputs and conInputs, and loads into common files. 
    with open(postion_inputs,"r") as f:
        lines = f.readlines()
        for l in lines:
            if "type" in l: #Finds a line that contains particle information
                spl = l.split()
                con.part_list.append(classes.Particle(float(spl[3]),float(spl[4]),int(spl[1]))) #Create particle object, saves to the particle list
        con.part_list = np.array(con.part_list)
    with open(constant_inputs,"r") as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            if "end ~" in lines[i]:
                break
            elif "maxstep" in lines[i]:
                con.maxstep = int(lines[i].split()[1])
            elif "dt" in lines[i]:
                con.dt = float(lines[i].split()[1])
            elif "cutoff" in lines[i]:
                con.cutoff = float(lines[i].split()[1])
            elif "box" in lines[i]:
                con.box = [float(k) for k in lines[i].split()[1:]]
            elif "start_temp" in lines [i]:
                con.start_temp = float(lines[i].split()[1])
            elif "masses" in lines[i]:
                k = i + 1
                while lines[k].split(): #While there is something more than a space in the line:
                    spl = lines[k].split()
                    con.masses[int(spl[0])] = float(spl[2])
                    k = k + 1
            elif "interactions" in lines[i]:
                k = i + 1
                while lines[k].split(): #While there is something more than a space in the line:
                    spl = lines[k].split()
                    a = 4 * float(spl[3]) * float(spl[4])**12
                    b = 4 * float(spl[3]) * float(spl[4])**6
                    con.interactions[(int(spl[0]),int(spl[1]))] = [a,b]
                    k = k + 1

    #check_pos_inputs()    
    starting_force()
    init_velocity() #Initalize velocities
    return

def nearest_image(par1,par2):
    #Returns a vector pointing from par1 to par2's nearest imagine, under periodic boundary conditions. 
    #print(par1.output_string())
    #print(par2.output_string())
    r_min = (par1.pos-par2.pos) / con.box #Find the simple distance, adjusted to be fraction of box length
    #print(r_min *constants.box)
    r_norm = mag(r_min) 
    for k in con.combin:
        r_curr = r_min + k
        #print(r_curr)
        #print(mag(r_curr))
        if mag(r_curr) < r_norm:
            r_min = r_curr
    #print(r_min *constants.box)
    return r_min * con.box

def forces():
    #Calcuate pair forces based on the Lenard-Lones Potential. Compaires for all 
    for i in range(len(con.part_list)):
        curr_par = con.part_list[i]
        curr_par.force.fill(0) #make all forces zero here to start
        #print(constants.part_list[np.arange(len(constants.part_list)) != i])
        for inter_par in con.part_list[np.arange(len(con.part_list)) != i]:
            #inter_par = interact[0]
            r = nearest_image(curr_par,inter_par)
            r_mag = mag(r)
            #print(r_mag)
            if r_mag <= con.cutoff:
                r_hat = normalized(r)
                #print(r_mag)
                if (curr_par.type, inter_par.type) in con.interactions:
                    a = con.interactions[curr_par.type, inter_par.type][0]
                    b = con.interactions[curr_par.type, inter_par.type][1]
                elif (inter_par.type, curr_par.type) in con.interactions:
                    a = con.interactions[inter_par.type, curr_par.type][0]
                    b = con.interactions[inter_par.type, curr_par.type][1]
                else: 
                    print("error - no interaction listed")
                curr_force = (6*b / r_mag**7 - 12*a / r_mag**13) * r_hat
                #print(curr_force)
                con.part_list[i].force = con.part_list[i].force + curr_force
                #print(constants.part_list[i].force)
                #print ("\n")
    return


def update_velocity():
    #updates velocities, then shift forces. 
    for par in con.part_list:
        par.vel = par.vel + con.dt * (par.force + par.force_last) * (2 * con.masses[par.type])**(-1) 
        par.force_last = np.array(par.force)
    return

def update_pos():
    for par in con.part_list:
        par.pos = par.pos + par.vel * con.dt + con.dt**2 * par.force_last * (2 * con.masses[par.type])**(-1)
        par.pos = par.pos % con.box
    return

def verlet():
    #Runs simple Velocity Verlet on particles, moving them fowards by the time step (dt). 
    # Updates particles in the 
    update_pos()
    forces()
    update_velocity()
    return

def outputStep():
    #Outputs info on the current system configuation to the output file.
    return

def check_pos_inputs():
    for par in con.part_list:
        for i in len(par.pos):
            if par.pos[i] > con.box[i]:
                print("Error - provided postion is outside bounds")

def output_positions():
    return

def output_thermodynamics():
    return

def plot_velocity():
    x_vel = list()
    y_vel = list()
    magni = list()
    for par in con.part_list:
        x_vel.append[par.vel[0]]
        y_vel.append[par.vel[1]]
        magni.append[mag(par.vel)]

    plt.hist(x_vel, bins= 20 )
    print(y_vel)
    return

def run_md(position_inputs, constants_inputs):
    #Runs MD similation. 
    initi(position_inputs, constants_inputs) #Iniiate similation 
    while con.current_step < con.maxstep:
        verlet() #Calcuate forces, velocities, and updates postions
        con.current_step += 1
        print(con.current_step)
        print_vel()
        output_thermodynamics() 
    #Outputs

    
    return

def print_forces():
    for i in con.part_list:
        print(str(i.force))
    return

def print_postions():
    for i in con.part_list:
        print(str(i.pos))
    return

def print_vel():
    for i in con.part_list:
        print(str(i.vel))
    return

#initi("pos.txt", "constants.txt")
#print(con.part_list)
#print(con.box)
#print("dt: " + str(con.dt))
#print("cutoff: " + str(con.cutoff))
#print("start_temp: " + str(con.start_temp))
#print("masses: " + str(con.masses))
#print("interactions: " + str(con.interactions))

#print("\n\n")
#forces()

run_md("pos.txt", "constants.txt")
print_forces()
plot_velocity()