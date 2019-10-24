import numpy as np
from scipy import spatial
from tvtk.api import tvtk
from tvtkfunc import ivtk_scene, event_loop


def convexhull(ch3d):
    poly = tvtk.PolyData()
    poly.points = ch3d.points
    poly.polys = ch3d.simplices
    sphere = tvtk.SphereSource(radius=0.02)
    points3d = tvtk.Glyph3D()
    points3d.set_source_connection(sphere.output_port)
    points3d.set_input_data(poly)
    # 绘制凸多面体的面，设置半透明度
    m1 = tvtk.PolyDataMapper()
    m1.set_input_data(poly)
    a1 = tvtk.Actor(mapper=m1)
    a1.property.opacity = 0.3
    # 绘制凸多面体的边，设置为红色
    m2 = tvtk.PolyDataMapper()
    m2.set_input_data(poly)
    a2 = tvtk.Actor(mapper=m2)
    a2.property.representation = "wireframe"
    a2.property.line_width = 2.0
    a2.property.color = (1.0, 0, 0)
    # 绘制凸多面体的顶点，设置为绿色
    m3 = tvtk.PolyDataMapper(input_connection=points3d.output_port)
    a3 = tvtk.Actor(mapper=m3)
    a3.property.color = (0.0, 1.0, 0.0)
    return [a1, a2, a3]

np.random.seed(42)
points3d = np.random.rand(40, 3)
ch3d = spatial.ConvexHull(points3d)
actors = convexhull(ch3d)  # 定义convexhull的Actor
win = ivtk_scene(actors)  # 场景用VTK绘制出来
win.scene.isometric_view()
event_loop()
