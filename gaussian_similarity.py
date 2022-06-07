import numpy as np 
from scipy.spatial.distance import euclidean

def gaussian_similarity_kernel(country_a,country_b,sigma):
    numerator = euclidean(country_a,country_b)**2
    denominator = 2*(sigma**2)
    return np.exp(-(numerator/denominator))

