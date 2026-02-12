# '''
# 在 Python 中，for 循环被称为 “遍历循环”。它不像某些语言（如 C 或 Java）通过索引累加，而是像一个排队管理器，依次从一个“队列”里取出每一个元素。
# '''
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
max = numbers[0]
for number in range(len(numbers)):
    if numbers[number] > max:
        max = numbers[number]
print(max)

max1 = numbers[0]
for number in numbers:
    if number > max1:
        max1 = number
print(max1)