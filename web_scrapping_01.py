import re

name = input("Enter file:")
if len(name) < 1: name = "data.txt"
handle = open(name)
x = list()
for line in handle:
    y = re.findall('[0-9]+', line)
    x = x + y
sum = 0
for i in x:
    sum = sum + int(i)
print(sum)
import re
fname = input("Insert file name: ")
if len(fname) < 1:
    fname = "data.txt"

data = open(fname)
lst = list()
value = 0
for line in data:
    nums = re.findall('[0-9]+', data1)
    data1 = nums.split()
    print(data1)
    for num in nums:
        numb = lst.append(int(num))
        #print(numb)