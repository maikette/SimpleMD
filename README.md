# thermoFinal

Simple Molecular Dynamics Simulation
Goal : single point particles, moving around in a 3D box, doing stuff, being free (but contained in box)
revised = 2D, at least at first. 

First Plan: 
Use Verlet Algorthum to Integrate, as simple as possable. 
No periodic boundary conditions. Maybe if there is time. 

First Goals: 
(1) Set up initalization. Get mass and positon from files, leave room to possablly add velocity, maybe molicule-type.  But START SIMPLE, please. please don't go crazy. 
Define random velocities based on a normal distribution. 
(2) Write the simple loop. first, calcuate forces. Then update postion, then velocity. 

Sources: 
http://www.fhi-berlin.mpg.de/~luca/Course_TU/03_Classical_MolecularDynamics.pdf

https://github.com/idgmatrix/pygame-physics 
(steal integration from here haha)