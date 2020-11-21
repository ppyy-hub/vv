# 1、 一行代码把[1,2,3,1,2,3] 中的重复元素剔除。（5 分）
# list1=list(set([1,2,3,1,2,3]))
# print(list1)

# 2、 一行代码把” hello ”和” world ”两个字符串里面的空字符去掉，并把它们用一个空格连接
# 起来。（5 分）
# 提示：string.rstrip()用于删除 string 字符串末尾的空格、string.lstrip()用于截掉 string 左边的空格
print(str.rstrip("hello")," ",str.lstrip("world"))


# 3、 访问嵌套列表中 list1 = [1, "abcd", ['a', 'ed'], "fd"]中字符串’a’。（5 分）
list1 = [1, "abcd", ['a', 'ed'], "fd"]
print(list1[2][0])
# 4， 已知2个列表[“语文”,”数学”,”英语”] ， 成绩列表 [90, 80,70]，一一对应，使用 zip函数构造元组列表，并循环输出，科目和对应的成绩。
list1=['语文','数学','英语']
score=[90,80,70]
for x,y in zip(list1,score):
    print("科目是{}，成绩是{}".format(x,y))



# 5，Python 哪些数据结构是有序的？哪些是无序的？

