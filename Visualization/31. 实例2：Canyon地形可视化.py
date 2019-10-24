import zipfile
import numpy as np
from mayavi import mlab

# 读取压缩文件
# N36W113.hgt：北纬36-37度，西经113-114度 地形高程数据。
hgt = zipfile.ZipFile('Data/N36W113.hgt.zip').read('N36W113.hgt')
data = np.fromstring(hgt, '>i2')
# 转换数据类型
data.shape = (3601, 3601)
data = data.astype(np.float32)
# 选取一部分数据
data = data[:1000, 900:1900]
# data == -32768代表空缺值
# 令空缺值等于最小值
data[data == -32768] = data[data > 0].min()

# 渲染地形hgt的数据data
mlab.figure(size=(400, 320), bgcolor=(0.16, 0.28, 0.46))
mlab.surf(data, colormap='gist_earth', warp_scale=0.2,
          vmin=1200, vmax=1610)

# 清空内存
del data
# 创建交互式的可视化窗口
mlab.view(-5.9, 83, 570, [5.3, 20, 238])
mlab.show()
