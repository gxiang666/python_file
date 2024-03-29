import numpy as np
from mayavi import mlab

# 建立数据
t = np.linspace(0, 4 * np.pi, 20)  # 0-4pi之间均匀的20个数
x = np.sin(2 * t)
y = np.cos(t)
z = np.cos(2 * t)
s = 2 + np.sin(t)

# 对数据进行可视化
points = mlab.points3d(x, y, z, s, colormap="Greens", scale_factor=.25)
mlab.show()
