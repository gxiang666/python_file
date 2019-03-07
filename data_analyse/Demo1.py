import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

""""
    matplotlib:绘图
    numpy:对函数操作，线性代数，傅里叶变，数组
    pandas:处理数据
    scipy:解决标准域
"""
x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.plot([1, 2, 3], [3, 2, 1])  # x轴，y轴对应的坐标
plt.show()  # 显示图像
