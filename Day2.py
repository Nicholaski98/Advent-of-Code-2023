import os
os.system('cls')


idx = 0
real =[]
exist=[]

with open("D:\Programs\Advent-of-Code-2023\Day 2\Day2.txt") as text:
    lines = text.readlines()

red = 12
green = 13
blue = 14

while idx < 100:
    line = lines[idx]
    idx+=1
    overRed = False
    overGreen = False
    overBlue = False
    for i in range(1, len(line)):
        if line[i] == 'g':
            num = line[i-3] + line[i-2]
            print('G' , num)
            if int(num) > green:
                overGreen = True
        if line[i] == 'r':
            if line[i - 1] == 'g':
                continue
            else:
                num = line[i-3] + line[i-2]
                print('R' , num)
                if int(num) > red:
                    overRed = True
        if line[i] == 'b':
            num = line[i-3] + line[i-2]
            print('B' , num)
            if int(num) > blue:
                overBlue = True
    if overRed == False and overBlue == False and overGreen == False:
        exist.append(idx)
        

print(exist)
total = sum(exist)
print(total)


