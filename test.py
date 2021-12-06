import numpy as np

a = np.array([0,1,2])     # a = array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
b = np.array([-1,3,1])

box = np.array([2,3,4])

h = (a + b) % box

print(h)