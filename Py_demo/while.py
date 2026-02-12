# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess:'))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won!")
#         break
# else:
#     print("Sorry, you failed!")
command = ''
started = False
while True:
    command = input('> ').lower()
    if command == 'start':
        if  started:
            print("车子已经启动了！")
        else:
            started = True
            print("车子启动了！")
    elif command == 'stop':
        if not started:
            print("车子已经停止了！")        
        else:
            started = False
            print("车子停止了！")
    elif command == 'help':
        print("""start - 启动车子
stop - 停止车子
quit - 退出游戏""")
    elif command == 'quit':
        break
    else:
        print("我不理解这个命令。")