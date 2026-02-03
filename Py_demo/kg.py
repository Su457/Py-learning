try:
    weight_lbs = input('Weight (lbd): ')
    weight_kg = int(weight_lbs) * 0.5
    print(weight_kg)

    if weight_kg > 100:
        print('提示：哇，你的体重超过100公斤了！')
    else:
        print('提示：你的体重在正常范围内。')

except ValueError:
    print("错误：请输入有效数字（例如：70），不要输入文字或特殊符号（例如：#、$）。")