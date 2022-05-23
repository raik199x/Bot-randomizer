import random
names = list()

with open("name.txt","r") as file:
    for lines in file.readlines():
        lines = lines.replace("\n","")
        names.append(lines)
temp = len(names)
for i in range(temp):
    j = random.randint(0,temp-i-1)
    print(str(i+1)+" "+names[j]+" ")
    names.remove(names[j])