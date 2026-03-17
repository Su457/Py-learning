try:
    age = int(input('Age:'))
    income = 2000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('age的值不能为0。')
except ValueError:
    print('无效值')