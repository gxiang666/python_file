player = int(input("请输入您要输入的拳 石头（1）/剪刀（2）/布（3）："))
computer = 1
print("玩家是%d - 电脑是%d" % (player, computer))
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("玩家获胜")
elif player == computer:
    print("平局")
else:
    print("电脑获胜")
