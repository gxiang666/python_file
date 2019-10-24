import numpy as np
from scipy import integrate


def lorenz(w, t, a, b, c):
    # 给出位置矢量w,和三个参数a,b,c计算出
    # dx/dt, dy/dt, dz/dt 的值
    x, y, z = w.tolist()
    # 直接与lorenz的计算公式对应
    return np.array([a * (y - x), x * (b - z) - y, x * y - c * z])


t = np.arange(0, 30, 0.01)  # 创建时间点
# 调用ode对lorenz进行求解
track = integrate.odeint(lorenz, (0.0, 1.00, 0.0), t, args=(10.0, 28.0, 3.0))
print(track)
