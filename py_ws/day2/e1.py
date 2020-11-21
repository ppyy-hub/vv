# 从键盘输入一个成绩，根据成绩输出对应的等级
# 	90（包含）---100（包含）  A
# 	70（包含）---90（不包含） B
# 	60（包含）---70（不包含） C
# 	0（包含）--60（不包含）	 D
# 	其它情况，输出“无效的成绩”
# score=input("请输入你的成绩")
# scores=int(score)
#
# if scores>=90 and scores<=100:
#     print('A')
# elif scores>=70 and scores<90:
#     print('B')
# elif scores>=60 and scores<70:
#     print('C')
# elif scores>=0 and scores<60:
#     print('D')
# else:
#     print("其他成绩输入无效的成绩")
# '''
#     猜数字游戏：
#     （1）提示用户“猜数字游戏开始了”
#     （2）指定一个数字让用户来猜
#     （3）提示用户猜一个数字并获取用户猜的数字
#     （4）把用户猜的数字和指定的数字进行比较
#     如果猜对了，输入“恭喜你，猜对了，可惜没有奖励！”
#     如果猜错了，输出“猜错了，正确答案是 **”
#     （5）猜完以后输出“游戏结束了，不玩了！”
# '''

# print("猜数字游戏开始了")
# H=6
# number=input("输入的数字")
# number=int(number)
# if number == H:
#     print("恭喜你，猜对了，可惜没有奖励！")
# else:
#     print("猜错了，正确答案是 **")
# input("游戏结束了，不玩了！")


# '''1）猜错了提示用户，猜大了还是猜小了
# （2）用户可以有3次猜的机会
# （3）猜玩两次以后提示用户"还有最后一次机会"
# （4）使用random模块，里面有一个函数randint()，可产生一个随机数
# 	a、导入模块
# 	import random
# 	b、产生随机数
# 	key=random.randint)#参数的意思是产生一个1(1,10-10之间的随机数
# '''
import random
print("-------游戏开始了-------")
H=random.randint(1,10)
a=0
while a<3:
    b=input("请输入你猜的数字")
    c=int(b)
    if c==H:
        print("回答正确")
        break
    else:
        print("回答错误")
    a=a+1
    if a==2:
        print("你还有一次机会")
print("正确答案是",H)





