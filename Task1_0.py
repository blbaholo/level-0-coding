def split(word1):
    return list(word1)
split("houses")

def split(word2):
    return list(word2)
split("computers")

List_of_letters=[]

def common_letters(word1,word2):

    for i in word2:
        if (i in word1):
            List_of_letters.append(i)
    print(','.join(List_of_letters))

common_letters("houses","computers")

