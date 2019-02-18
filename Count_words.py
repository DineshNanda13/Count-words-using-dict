def count_words(text):

    table = str.maketrans("!?.",3*" ")
    new_text = text.translate(table)
    new_text1=new_text.replace('','').lower()
    list = new_text1.split()

    count = {}

    for word in list:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    return count


print(count_words('Text analytics derives information from the text.'))

