# import os
# os.system('cls')

word='eightonefgtwoonenoneight'

numList = ['zero','one','two','three','four','five','six','seven','eight','nine']


for i in range(len(numList)):
    while numList[i] in word:
        num = i
        word = word.replace(numList[i],f'{i}', 1)
while("1ight" in word):
    word = word.replace('1ight', '18', 1)

print(word)