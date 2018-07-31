def mirror(mystr):
    
    reverseString = []
    for i in range(len(mystr)-1, -1, -1):
        reverseString.append(mystr[i])
    result = "".join(reverseString)
    
    mirro = mystr+result
    #print(mirro)
    return mirro

mirror("hello")