#overal variables
dt = int() #time-step, in sec
cutoff = int() #cutoff for interactions
box = list() #box dimentions
start_temp = 275.0 #Default starting temp, if not overridden up value in file. 

#Data structures to hold info
part_list = list() #List to hold all the particles in. May not be the best way to do it... but works for now. 
masses = dict() #dict to hold the masses of varying particles types. 
interactions = dict() #to hold the constants for the Lenard-Jones potential