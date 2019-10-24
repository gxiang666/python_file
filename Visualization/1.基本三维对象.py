# 打开帮助文档
from tvtk.tools import tvtk_doc
tvtk_doc.main()

# 长方体数据源
from tvtk.api import tvtk
s = tvtk.CubeSource(x_length=1.0,y_length=2.0, z_length=3.0)
print(s)
print(s.x_length)
print(s.y_length)
print(s.center)
print(s.output_points_precision)

# 圆锥数据源
s = tvtk.ConeSource(height=3.0, radius=1.0, resolution=36)
# resolution指的是底面圆分辨率，即用36边形近似圆形
print(s)
