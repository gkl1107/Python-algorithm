def computeFactorial(number):
    if number < 0:
        print("can't be negative number")
    elif number <= 1:
        return 1
    else:
        return number * computeFactorial(number-1)
    

computeFactorial(6)
    