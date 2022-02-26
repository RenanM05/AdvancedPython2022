import numpy as np

some_array = np.array([1,2,0,0,4,0])

def get_non_zero_values(array):
    get_values = np.array([])
    bool_array = np.array(array, dtype=bool)
    for i in range(len(bool_array)):
        if bool_array[i] == True:
            get_values = np.append(get_values, array[i])
    return get_values

def find_idx(array, non_zero_value):    
    return np.where(array == non_zero_value)

for i in get_non_zero_values(some_array):
    idx = find_idx(array=some_array, non_zero_value=i)
    print(idx)
    