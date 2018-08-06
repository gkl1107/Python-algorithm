#!/usr/bin/python

# infile = open("qbdata.txt", "r")
# outfile = open("qbnames.txt", "w")

# aline = infile.readline()
# while aline:
#     items = aline.split()
#     dataline = items[1] + ',' + items[0]
#     outfile.write(dataline + '\n')
#     aline = infile.readline()

# infile.close()
# outfile.close()


with open('qbdata.txt') as md:
    print(md)
    aline = md.readline()
    while aline:
    	print(aline)
    	aline = md.readline()
    # for line in md:
    #     print(line)
print(md)