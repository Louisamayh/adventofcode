#load text file into python
with open("day3input.txt") as file:
    lines = [line.rstrip() for line in file]

text = "".join(lines)
#import regex
import re

# create pattern to be regonised
pattern = r"mul\(([1-9]?[0-9]{1,2}|0),([1-9]?[0-9]{1,2}|0)\)"\

# find pattern in text
# extract contents of brackets to list

matches = re.findall(pattern,text)

#convert to integers
#multiply the integers before the comma by the integers after the comma
#add result to list
products = [int(a) * int(b) for a, b in matches]

#add the list together
total_sum = sum(products)

print("Products:", products)
print("Total Sum:", total_sum)
