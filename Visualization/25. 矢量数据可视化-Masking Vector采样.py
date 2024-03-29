import numpy as np
from mayavi import mlab

x, y, z = np.mgrid[0:1:20j, 0:1:20j, 0:1:20j]
u = np.sin(np.pi * x) * np.cos(np.pi * z)
v = -2 * np.sin(np.pi * y) * np.cos(2 * np.pi * z)
w = np.cos(np.pi * x) * np.sin(np.pi * z) + np.cos(np.pi * y) * np.sin(2 * np.pi * z)

src = mlab.pipeline.vector_field(u, v, w)
mlab.pipeline.vectors(src,
                      mask_points=10,  # 每10个点取一个点
                      scale_factor=2.0  # 放缩比例
                      )
mlab.show()
