import numpy as np 

def elements():
    return np.random.randint(low=0, high=8) 

def matrix(nrow=3, ncol=3):
    return np.array([
    [[elements() for i in range(ncol)] for j in range(nrow)]])
    
print(matrix(nrow=3, ncol=3))
