def emoji_converter (message):
    words = message.split(' ')
    emojis = {
        ":)":"😊",
        ":(":"🙁"
    }
    output =""
    for word in words:
        output +=emojis.get(word,word)+" "
    return output
x = input('>')
print(emoji_converter(x))