from scipy.integrate import odeint
import numpy as np
from mayavi import mlab


def lorenz(w, t, a, b, c):
    # 给出位置矢量w，和三个参数a, b, c计算出
    # dx/dt, dy/dt, dz/dt的值
    x, y, z = w.tolist()
    # 直接与lorenz的计算公式对应
    return np.array([a * (y - x), x * (b - z) - y, x * y - c * z])


t = np.arange(0, 30, 0.01)  # 创建时间点
# 调用ode对lorenz进行求解, 用两个不同的初始值
track1 = odeint(lorenz, (0.0, 1.00, 0.0), t, args=(10.0, 28.0, 3.0))
track2 = odeint(lorenz, (0.0, 1.01, 0.0), t, args=(10.0, 28.0, 3.0))
# 绘制图形
mlab.plot3d(track1[:, 0], track1[:, 1], track1[:, 2], color=(1, 0, 0), tube_radius=0.1)
mlab.plot3d(track2[:, 0], track2[:, 1], track2[:, 2], color=(0, 0, 1), tube_radius=0.1)
mlab.show()
