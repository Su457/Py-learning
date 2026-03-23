# import math
# print(10**3)#幂运算
# print(10//3)#整除，取商的整数部分
# print(10%3)#取余数
# x = 2.5
# y = -2.9
# print(round(x))#四舍五入
# print(abs(y))#取绝对值
name = input("请输入你的名字：")
# if len(name) < 3:
#     print("名称至少包含三个字符。")
# elif len(name) >50:
#     print("名字长度不能超过50个字符。")
if len(name) < 3 or len(name) >50:
    print("名字长度无效。")
else:
    print("名字看起来很好！")
