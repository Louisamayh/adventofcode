
#load text file into python
with open("day2p1input.txt") as file:
    lines = [line.rstrip() for line in file]


#seperate column and turn into integers
counter = 0


for i in lines:
    linecols = i.split(" ")
        
    lineready = []

    for i in linecols:
        lineready.append(int(i))
    
    #convert lists to desending by checkin first and last integer

    if lineready[0] < lineready[-1]:
        lineready.reverse()
    lineready

    # rules met? Counter = counter + 1
    points = 0
    #check if the numbers in the row are all desending
    success = True
    for i in range(len(lineready)-1):
        if lineready[i] - lineready[i+1] < 1 or lineready[i] - lineready[i+1] > 3:
            print('breaking because ', lineready[i] , lineready[i+1])
            points = points + 1

    if points:
        points > 1
        success = False

    if success:
        counter = counter + 1
print(counter)

   


#check if the difference between the next number is more than 3

#check if the difference between the next number is 0





