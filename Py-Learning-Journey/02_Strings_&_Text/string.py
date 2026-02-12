course = 'Python for Beginners'
'''
course.upper() #转换成大写
course.lower() #转换成小写
course.title() #每个单词的首字母大写
course.find('B') #查找字符的位置，如是一段字符则返回第一个字符的位置
'Python' in course #检查某个字符是否包含在字符串中，返回布尔值
course.replace('Beginners','students') #替换字符
len(course) #返回字符串的长度
course[::2]#步长为2，表示每隔一个取一个字符
course[::-1]#步长为-1，表示反转字符串
another[0:20] #切片，包含第0个位置，不包含第20个位置
name[1:-1] #'-1'表示的倒数第一个位置
'''
print(course.upper())#转换成大写
print(course.lower())#转换成小写
print(course.title())#每个单词的首字母大写
print(course.find('B'))#查找字符的位置，如是一段字符则返回第一个字符的位置
print('Python' in course)#检查某个字符是否包含在字符串中，返回布尔值

print(course.replace('Beginners','students'))#替换字符

print(len(course))#返回字符串的长度
another = course
print(another[0:20])#切片，包含第0个位置，不包含第20个位置
name = 'Jennifer'
print(name[1:-1])#'-1'表示的倒数第一个位置


print(course[0:6])
print(course[::2])#步长为2，表示每隔一个取一个字符
print(course[::-1])#步长为-1，表示反转字符串