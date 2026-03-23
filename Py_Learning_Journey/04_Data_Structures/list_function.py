numbers = [2,2,3,4,5,5,5,6,6,7,2,10]
numbers1 = []
for number in numbers:
    if number not in numbers1:
        numbers1.append(number)
print(numbers1)