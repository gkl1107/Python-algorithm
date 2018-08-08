def division():
	dividend = int(input("Please enter the dividend: "))
	divisor = int(input("Please enter the divisor: "))
	quotient = dividend / divisor
	print(quotient)

try:
	division()
	
except ZeroDivisionError as ze:
	print("zero division error: ", ze)
except ValueError as ve:
	print("value error: ", ve)





