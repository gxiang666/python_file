import numpy as np

"""
读取csv文件
np.loadtxt(frame, dtype=np.float, delimiter=None， unpack=False)
• frame : 文件、字符串或产生器，可以是.gz或.bz2的压缩文件
• dtype : 数据类型，可选
• delimiter : 分割字符串，默认是任何空格
• unpack : 如果True，读入属性将分别写入不同变量
"""

b = np.loadtxt("a.csv", delimiter=",")
print(b)
