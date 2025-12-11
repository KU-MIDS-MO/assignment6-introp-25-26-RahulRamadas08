import numpy as np

def estimate_pi(num_samples):
    
    points = np.random.rand(num_samples, 2)
    
    num_points_in_circle = 0.0
    
    for i in range(num_samples):
        if np.linalg.norm(points[i], ord=2) < 1:
            num_points_in_circle += 1
    
    return num_points_in_circle / num_samples * 4

print(estimate_pi(100000))
