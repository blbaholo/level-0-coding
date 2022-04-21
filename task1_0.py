def common_letters(word1,word2):
    word1.split(word1)
    word2.split(word2)
    List_of_letters=[]
    for i in word2:
        if (i in word1):
            List_of_letters.append(i)
    print(','.join(List_of_letters))

common_letters("houses","computers")

