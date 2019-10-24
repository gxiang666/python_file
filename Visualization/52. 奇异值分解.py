import numpy as np
from scipy import linalg

A = np.array([[1, -0.3], [-0.1, 0.9]])
U, s, V = linalg.svd(A)
