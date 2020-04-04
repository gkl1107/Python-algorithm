
def crossRiver(num_of_miss, num_of_cann):
    bankLeft = {"miss":num_of_miss, "cann":num_of_cann}
    bankRight = {"miss":0, "cann":0}
    boat = []

    if bankLeft["miss"] == 0 and bankLeft["cann"] == 0:
    	print("finish")
    	return "bankLeft: (m {}, c {}); bankRight: (m {}, c {})".format(bankLeft["miss"], bankLeft["cann"], bankRight["miss"], bankRight["cann"])


    if bankLeft["miss"] == 1 and bankLeft["cann"] == 1:
    	# on boat 1c and 1m
    	boat.append("c")
    	boat.append("m")
    	bankLeft["miss"] = bankLeft["miss"] -1
    	bankLeft["cann"] = bankLeft["cann"] -1
    	print(boat)
    	print(bankLeft,bankRight)
    	
    	# off boat 1m

    	bankRight["miss"] = bankRight["miss"] + 1
    	boat.pop()
    	print(boat)
    	print(bankLeft,bankRight)

    	# off boat 1c
    	bankRight["cann"] = bankRight["cann"] + 1
    	boat.pop()
    	print(boat)
    	print(bankLeft,bankRight)

    else: 
    	
    	crossRiver(1, 1)
    	crossRiver(num_of_miss-1, num_of_cann-1)







    return "bankLeft: (m {}, c {}); bankRight: (m {}, c {})".format(bankLeft["miss"], bankLeft["cann"], bankRight["miss"], bankRight["cann"])



print(crossRiver(2,2))





