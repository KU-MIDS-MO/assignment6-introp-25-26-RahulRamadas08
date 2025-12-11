import numpy as np

def get_random_subset_of_naturals_up_to_20():
    
    is_in_subset = np.random.randint(2, size=20)
    
    subset = []
    
    for i in range(20):
        if is_in_subset[i] == 1:
            subset.append(i+1)
            
    return np.array(subset)

print(get_random_subset_of_naturals_up_to_20())


