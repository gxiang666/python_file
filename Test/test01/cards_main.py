import cards_tool

while True:
    cards_tool.show_menu()
    action = input("请选择操作功能：")
    print("您的选择的操作：%s" % action)
    # 1,2,3 针对名片操作
    if action in ["1", "2", "3"]:
        # 1 新建名片
        if action == "1":
            cards_tool.new_card()
        # 2 显示全部
        elif action == "2": 
            cards_tool.show_all()
        # 3 查询名片
        elif action == "3":
            cards_tool.search_card()
    # 0 退出系统
    elif action == "0":
        print("欢迎再次使用【名片管理系统】")
        break
    else:
        print("输入错误,请重新输入")