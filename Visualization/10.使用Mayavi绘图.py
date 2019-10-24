# import numpy as np
# from mayavi import mlab
# x = np.array([[-1, 1, 1, -1, -1], [-1, 1, 1, -1, -1]], dtype=np.int32)
# y = np.array([[-1, -1, -1, -1, -1], [1, 1, 1, 1, 1]], dtype=np.int32)
# z = np.array([[1, 1, -1, -1, 1], [1, 1, -1, -1, 1]], dtype=np.int32)
# s = np.array(mlab.mesh(x, y, z))
# mlab.show()

from mayavi import mlab
x = [[-1, 1, 1, -1, -1], [-1, 1, 1, -1, -1]]
y = [[-1, -1, -1, -1, -1], [1, 1, 1, 1, 1]]
z = [[1, 1, -1, -1, 1], [1, 1, -1, -1, 1]]
s = mlab.mesh(x, y, z)
mlab.show()
