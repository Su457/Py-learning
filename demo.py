numbers=[1,2,3,4,5,6,7,8,9,10]
max = numbers[0]
for number in range(len(numbers)):
    if numbers[number] > max:
        max = numbers[number]
print(max)

# numbers=[1,2,3,4,5,6,7,8,9,10]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)