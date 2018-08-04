#!/usr/bin/python


# def checkout():
# 	total = 0
# 	count = 0
# 	moreItems = True
# 	while moreItems:
# 		price = float(input('Enter price of item (0 when done): '))
# 		if price > 0:
# 			count = count + 1
# 			total = total + price
# 			print('Subtotal: $', total)
# 		elif price < 0:
# 			print("ERROR: please enter a valid price")
# 		else:
# 			moreItems = False

# 	if count != 0:
# 		average = total / count
# 		print('Total items:', count)
# 		print('Total $', total)
# 		print('Average price per item: $', average)
# 	else:
# 		print("ERROR: Can't compute an average without data")

# checkout()



def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price != 0:
            count = count + 1
            total = total + price
            print('Subtotal: ${:.3}'.format(total))
        else:
            moreItems = False
    average = total / count
    print('Total items:', count)
    print('Total ${:.3}'.format(total))
    print('Average price per item: ${:.3}'.format(average))

checkout()

