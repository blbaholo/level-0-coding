def common_letters(word1,word2):
    list_of_letters=[]
    final_list=[]
    for i in word2:
        if i in word1.lower() or i in word1.upper():
            list_of_letters.append(i.lower())
    for i in list_of_letters:
        if i not in final_list:
            final_list.append(i)
    print("Common letters: " + ', '.join(final_list))

common_letters("houses","computerss")

