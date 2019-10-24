import csv
import math
import numpy as np
from mayavi import mlab
from mayavi.sources.builtin_surface import BuiltinSurface

'''读取数据'''
# 建立城市-城索引的字典、城市经纬度的列表
cities = dict()
coords = list()
data = csv.reader(open('Data/cities.csv'))
for line in data:
    name, longitude, latitude = line
    cities[name] = len(coords)
    coords.append((float(longitude), float(latitude)))

'''坐标转换'''
# 将经纬度的位置转换为三维坐标
coords = np.array(coords)
latitude, long = coords.T * np.pi / 180
x = np.cos(long) * np.cos(latitude)
y = np.cos(long) * np.sin(latitude)
z = np.sin(long)

'''建立窗口'''
mlab.figure(bgcolor=(0.48, 0.48, 0.48), size=(800, 800))

'''绘制地图'''
# 绘制半透明球体表示地球
sphere = mlab.points3d(0, 0, 0, scale_factor=2,
                       color=(0.67, 0.77, 0.93),
                       resolution=1024,
                       opacity=0.7,
                       name='Earth')
# 调整镜面反射参数
sphere.actor.property.specular = 0.45
sphere.actor.property.specular_power = 5
# 设置背面剔除，以更好的显示透明效果
sphere.actor.property.backface_culling = True

'''绘制城市'''
# 绘制城市位置
points = mlab.points3d(x, y, z, scale_mode='none', scale_factor=0.03, color=(0, 0, 1))
# 绘制城市名称
for city, index in cities.items():
    label = mlab.text(x[index], y[index], city,
                      z=z[index], color=(1, 1, 1),
                      width=0.016 * len(city), name=city)
    # label = mlab.text3d(x[index], y[index], z[index], city,
    #                     color=(0, 0, 0), scale=0.06, name=city)

'''绘制大洲边界'''
continents_src = BuiltinSurface(source='earth', name='Continents')
# 设置LOD为2
# LOD: Levels-of-details
continents_src.data_source.on_ratio = 2
continents = mlab.pipeline.surface(continents_src, color=(0, 0, 0))

'''绘制赤道'''
# 构造组成赤道线的数组
theta = np.linspace(0, 2 * np.pi, 100)  # 平分360为100份
x = np.cos(theta)
y = np.sin(theta)
z = np.zeros_like(theta)
# 绘制
mlab.plot3d(x, y, z, color=(1, 1, 1), opacity=0.2, tube_radius=None)

'''绘制两条纬线'''
alpha = math.sqrt(3)/2
mlab.plot3d(x * alpha, y * alpha, z + 0.5, color=(1, 1, 1), opacity=0.2, tube_radius=None)
mlab.plot3d(x * alpha, y * alpha, z - 0.5, color=(1, 1, 1), opacity=0.2, tube_radius=None)

'''显示可交互窗口'''
# 设置相机及焦点位置
mlab.view(100, 60, 4, [-0.05, 0, 0])
# 显示窗口
mlab.show()
