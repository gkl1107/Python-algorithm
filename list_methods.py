#!/usr/bin/python

#practice implement Python functions

# count
def count(i, aList):
    count = 0
    for item in aList:
        if item == i:
            count = count + 1
    return count

# in 
def existence(i, aList):
    existence = False
    for item in aList:
        if item == i:
            existence = True
            break
    return existence

# reverse
def reve(aList):
    result = []
    for index in range(len(aList)-1, -1, -1):
        result.append(aList[index])
    return result
    
# index
def index(i, aList):
    index = -1
    for item in aList:
        index = index + 1
        if item == i:
            return index

#insert(method 1)
def insert1(i, aList, index=0):
    first_half = aList[:index]
    second_half = aList[index:]
    i = [i]
    new = first_half + i + second_half
    return new
    
#insert(method 2)
def insert2(i, aList, index=0):
    result = []
    for item in aList:
        if index == aList.index(item):
            result.append(i)
        result.append(item)
    return result

# test
i = "a"
aList = ["b","f", "a", "y", "o", "a"]
r = count(i, aList)
print(r)