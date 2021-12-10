#overal variables
import numpy as np
from itertools import product

dt = int() #time-step, in sec
maxstep = int() #maximum number of simulation steps to take. 
cutoff = int() #cutoff for interactions
box = list() #box dimentions
start_temp = 275.0 #Default starting temp, if not overridden by value in file. 

#Data structures to hold info
part_list = list() #List to hold all the particles in. May not be the best way to do it... but works for now. 
masses = dict() #dict to hold the masses of varying particles types. 
interactions = dict() #to hold the constants for the Lenard-Jones potential
current_step = 0


#things that are just nice to pre-calc:
combin = np.array(list(product([-1,0,1],repeat=2)))
#next_id = 0

#Physical constants
kB = 1.38064852*10**(-23)