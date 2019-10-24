import numpy as np
from scipy import linalg
import timeit

m, n = 50, 50
A = np.random.rand(m, n)
B = np.random.rand(m, n)


def my_func1():
    X1 = linalg.solve(A, B)
    return X1


def my_func2():
    X2 = np.dot(linalg.inv(A), B)
    return X2


X1 = my_func1()
X2 = my_func2()
print(np.allclose(X1, X2))
t1 = timeit.Timer(stmt=my_func1).timeit(number=10000)
t2 = timeit.Timer(stmt=my_func2).timeit(number=10000)
print(t1, t2)
