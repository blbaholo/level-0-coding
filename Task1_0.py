word1="houses"
word2="computers"

def split(word1):
    return list(word1)
split(word1)

def split(word2):
    return list(word2)
split(word2)
List_of_letters=[]
def common_letters(word1,word2):

    for i in word2:
        if (i in word1):
            List_of_letters.append(i)
    print(','.join(List_of_letters))

common_letters(word1,word2)

