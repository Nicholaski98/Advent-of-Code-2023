import os
print(os.getcwd())

digits = []
result=0
num=0
numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']

text=open("text.txt")
lines = text.readlines()
def number(x,word):
    validNumber = word[x].isnumeric() 
    return validNumber

while num < 1000:
    word = lines[num]
    num+=1
    firstDigit = []
    while("igh2" in word):
        word = word.replace('igh2', 'L2', 1)
    while("1igh" in word):
        word = word.replace('1igh', '1L', 1)
    while('w1'in word):
        word = word.replace('w1' , "L1" , 1)
    for i in range(len(numbers)):
        while numbers[i] in word:
            word = word.replace(numbers[i],f'{i}', 1)
    while("eigh2" in word):
        word = word.replace('eigh2', '82', 1)
    while("1ight" in word):
        word = word.replace('1ight', '18', 1)
    while('tw1' in word):
        word = word.replace('tw1','21',1)
    print(word)
    for x in range(len(word)):
        if number(x,word):
            firstDigit += word[x]
    y = len(firstDigit)
    y-=1
    digits = firstDigit[0] + firstDigit[y]
    print(digits)
    result += int(digits)

print()
print(result)