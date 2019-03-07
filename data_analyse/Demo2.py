import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 饼图
labels = "Frogs", "Hogs", "Dogs", "Logs"  # 标签
sizes = [15, 30, 45, 10]  # 每块区域的比例
explode = (0, 0.1, 0, 0)  # 突出的区域
# autopct:显示百分比的方式  shadow:饼图是二维的还是有阴影的  startangle:起始角度
plt.pie(sizes, explode, labels, autopct="%1.1f%%", shadow=False, startangle=90)
plt.axis("equal")  # x轴，y轴一样，是一个正圆2
plt.show()  # 显示图像
