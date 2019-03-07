card_list = []


def show_menu():
    """"显示菜单"""

    print("*" * 50)
    print("欢迎使用【菜单管理系统】v1.0")
    print("")
    print("1 新建名片")
    print("2 查询全部")
    print("3 查询名片")
    print("")
    print("0 退出系统")
    print("*" * 50)


def new_card():
    """"新建名片"""

    print("-" * 50)
    print("功能：新增名片")
    name = input("请输入姓名：")
    phone = input("请输入电话:")
    qq = input("请输入qq号码：")
    email = input("请输入email:")
    card_dict = {"name": name,
                 "phone": phone,
                 "qq": qq,
                 "email": email}
    card_list.append(card_dict)
    print(card_list)
    print("成功添加%s的名片" % card_dict["name"])


def show_all():
    """"显示全部"""

    print("-" * 50)
    print("功能：显示全部")
    if len(card_list) == 0:
        print("当前没有任何名片")
        return
    for name in ["姓名", "电话", "qq", "email"]:
        print(name, end="\t\t\t")
    print("")
    print("=" * 50)
    for card_dict in card_list:
        print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (card_dict["name"],
                                              card_dict["phone"],
                                              card_dict["qq"],
                                              card_dict["email"]))


def search_card():
    """"查询名片"""

    print("-" * 50)
    print("功能：搜索名片")
    find_name = input("请输入要搜索的姓名：")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t\t电话\t\t\tqq\t\t\temail")
            print("-" * 40)
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (card_dict["name"],
                                                  card_dict["phone"],
                                                  card_dict["qq"],
                                                  card_dict["email"]))
            print("-" * 40)
            deal_card(card_dict)
            break
        else:
            print("没有找到%s" % find_name)


def deal_card(find_dict):
    """"处理找到的字典"""

    print(find_dict)
    action_str = input("请输入要执行的操作"
                       "[1] 修改 [2] 删除 [0] 返回菜单 ")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "请输入姓名:")
        find_dict["phone"] = input_card_info(find_dict["phone"], "请输入phone:")
        find_dict["qq"] = input_card_info(find_dict["qq"], "请输入qq:")
        find_dict["email"] = input_card_info(find_dict["email"], "请输入email:")
        print("修改名片")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除成功")


def input_card_info(dict_value, tip_message):
    """
    输入名片信息
    :param dict_value: 字典原有值
    :param tip_message: 输入提示信息
    :return: 如果输入，返回内容，否则返回字典原有值
    """
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
