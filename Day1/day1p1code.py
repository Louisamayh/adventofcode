
#load text file into python
with open("day1p1input.txt") as file:
    lines = [line.rstrip() for line in file]


#seperate column

leftcol = []
rightcol = []

#seperate column and turn into integers
for i in lines:
    linecols = i.split("   ")
    leftcol.append(int(linecols[0]))
    rightcol.append(int(linecols[1]))

#sort lists
leftcol.sort()
rightcol.sort()

#create list of differences and add together

diffcol = []

for i in range(len(leftcol)):
    diffcol.append(abs(leftcol[i] - rightcol[i]))

result = sum(diffcol)

print(result)



#find out how many time each number appears in right list

instances = []

for i in leftcol:
    instances.append(rightcol.count(i)*i)

resulttwo = sum(instances)

print(resulttwo)



