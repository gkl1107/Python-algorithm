import numpy

def multipli_table(n,m):
    table = []
    for i in range(1,n+1):
        row = []
        table.append(row)
        for x in range(1,m+1):
            result = x * i 
            row.append(result)
    #table.insert(0,[i for i in range(1, n+1)])
    
    a = numpy.array(table)

    print(a)

    # for row in table:
    #     print(row)
multipli_table(9,9)     

