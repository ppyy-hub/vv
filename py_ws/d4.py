#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

'''
in  not in  成员运算符
'''


x = r'<script src="https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/js/s_super_index-855fcfd82e.js"></script>'
#
if "superman" in x:
    print("测试通过")



# list1 = ["abc" , 'efg' , "hello"]
#
# if "abc" in list1:
#
#     print("pass")

# value = {
#     "name" : "kevin"
# }
#
# key = "name"
# if  key in value:
#     print(value[key])


age=16;
if age>20:
    print("恭喜你被录用了！")
else:
    print("很遗憾年龄不符合要求")
#0-500
list1=[i for i in range(501)]
print(list1)
'''
猜数字游戏：
（1）提示用户“猜数字游戏开始了”
（2）指定一个数字让用户来猜
（3）提示用户猜一个数字并获取用户猜的数字
（4）把用户猜的数字和指定的数字进行比较
	如果猜对了，输入“恭喜你，猜对了，可惜没有奖励！”
	如果猜错了，输出“猜错了，正确答案是**”
（5）猜完以后输出“游戏结束了，不玩了！”
'''