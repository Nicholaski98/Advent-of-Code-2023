import os
os.system('cls')


with open("D:\Programs\Advent-of-Code-2023\Day 2\Day2.txt") as text:
    lines = text.readlines()

nums=[]
idx=0

while idx < 100:
    gMax = 0
    bMax = 0
    rMax = 0
    power=0
    line=lines[idx]
    idx+=1
    for i in range(1,len(line)):
        power = 0
        if line[i] == 'g':
            num = int(line[i-3] + line[i-2])
            if num > gMax:
                gMax = num
        if line[i] == 'b':
            num = int(line[i-3] + line[i-2])
            if num > bMax:
                bMax = num
        if line[i] == 'r':
            if line[i-1] == 'g':
                continue
            else:
                num = int(line[i-3] + line[i-2])
                if num > rMax:
                    rMax = num
    power = bMax * gMax * rMax
    nums.append(power)

print()
print(nums)

total = sum(nums)
print(total)