import numpy as np

a = np.arange(9, -1, -1)     # a = array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
b = a[np.arange(len(a))!=0]  # b = array([9, 8, 7, 5, 4, 3, 2, 1, 0])

print(b)