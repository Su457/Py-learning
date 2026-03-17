def text_create(name,msg):
    desktop_path = 'C:/Users/su/Desktop/github/git_demo/Py-Learning-Journey/text/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path,'w')
    file.write(msg)
    file.close()
    print('Done')#仅表明上面所有语句已经执行完毕


def text_filter(word,censored_word = 'lem',changed_word = 'Awesome'):
    return word.replace(censored_word,changed_word)
text_filter('Python is lem!')


def censored_text_create(name,msg):
    clean_msg = text_filter(msg)
    text_create(name,clean_msg)

censored_text_create('Try','lem! lem! lem!')
