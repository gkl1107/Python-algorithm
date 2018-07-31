
#a function that removes all occurrences of a string from another string

def remove_all(substr,theStr):
    
    span = len(substr)
    found = []
    for start in range(0, len(theStr)):
        end = start + span
        if end <= len(theStr):
            if theStr[start:end] == substr:
                found.append(theStr[start:end])
 
    found = "".join(found)

    result = theStr.replace(found,"")

    return result
        


remove_all("an","banana")