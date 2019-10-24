from traits.api import HasTraits, Str, Int
from traitsui.api import View, Item, Group

g1 = [Item('model_name', label="模型名称"),
      Item('category', label="模型类型")]
g2 = [Item('model_number', label="模型数量"),
      Item('vertices', label="顶点数量")]


class ModelManager(HasTraits):
    model_name = Str
    category = Str
    model_file = Str
    model_number = Int
    vertices = Int
    traits_view = View(
            Group(*g1, label='模型信息', show_border=True),
            Group(*g2, label='统计数据', show_border=True),
            title="内部试图")

global_view = View(
    Group(*g1, label='模型信息', show_border=True),
    Group(*g2, label='统计数据', show_border=True),
    title="外部试图"
)

if __name__ == "__main__":

    model = ModelManager()

    # 内部试图
    model.configure_traits()
    model.configure_traits(view='traits_view')

    # 外部视图
    model.configure_traits(view=global_view)
