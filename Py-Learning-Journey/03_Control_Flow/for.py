'''
在 Python 中，for 循环被称为 “遍历循环”。它不像某些语言（如 C 或 Java）通过索引累加，而是像一个排队管理器，依次从一个“队列”里取出每一个元素。
'''
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    print('X' * number)

print('---------') 

for number in numbers:
    output = ''
    for count in range(number):
        output += 'x'
    print(output)

print('---------')

numbers=[1,2,3,4,5,6,7,8,9,10]
max_num = numbers[0]

#索引遍历
for number in range(len(numbers)):
    if numbers[number] > max_num:
        max_num = numbers[number]
print(max_num)

#直接遍历
for number in numbers:
    if number > max_num:
        max_num = number
print(max_num)

#python内置函数，返回列表中的最大值
print(max(numbers))