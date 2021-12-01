import classes
import constants
import numpy
import pandas


def init_velocity(start_temp):
    #Initalize velocity based on 
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

def update_velocity():
    #updates velocities
    return

def verlet():
    return
    #simple verlet with periodic boundary consitions. Updates postion and velocity

def outputStep():
    #Outputs info on the current system configuation to the output file.
    return

def run_md(position_inputs, constants_inputs):
    #Runs MD similation. 
    initi(position_inputs, constants_inputs) #Iniiate similation 

    return

initi("pos.txt", "constants.txt")