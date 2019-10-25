class House:

    def __init__(self, house_type, area):
        """

        :param house_type: 户型
        :param area: 总面积
        """
        self.house_type = house_type
        self.area = area
        
        # 剩余面积默认和总面积一致
        self.free_area = area
        # 默认没有任何的家具
        self.item_list = []

    def __str__(self):

        # Python 能够自动的将一对括号内部的代码连接在一起
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):

        print("要添加 %s" % item)


# 2. 创建房子对象
my_home = House("两室一厅", 60)

my_home.add_item("bed")
my_home.add_item("chest")
my_home.add_item("table")

print(my_home)
