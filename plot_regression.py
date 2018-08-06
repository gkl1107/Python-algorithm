'''
Write a function called plotRegression that reads the data from this file and 
uses a turtle to plot those points and a best fit line according to the following formulas:
y=y¯+m(x−x¯)
m=∑xiyi−nx¯y¯∑x2i−nx¯2
where x¯
 is the mean of the x-values, y¯
 is the mean of the y- values and n
 is the number of points. If you are not familiar with the mathematical ∑
 it is the sum operation. For example ∑xi
 means to add up all the x values.
Your program should analyze the points and correctly scale the window using setworldcoordinates 
so that that each point can be plotted. Then you should draw the best fit line, in a different color, through the points.

'''

import turtle

def plotRegression(data):
    
    with open(data) as dt:
        x_cor = []
        y_cor = []
    
        line = dt.readline()
        while line:
            values = line.split()
            x_cor.append(int(values[0]))
            y_cor.append(int(values[1]))
            line = dt.readline()
        
        n = len(x_cor)    
        x_ave = sum(x_cor)/n
        y_ave = sum(y_cor)/n
        print(x_ave)
        print(y_ave)
        
        toBeSum1 = []
        for i in range(n):
            toBeSum1.append(x_cor[i] * y_cor[i])
        toBeSum2 = []
        for i in range(n):
            toBeSum2.append(x_cor[i] ** 2)
        m = (sum(toBeSum1)-(n*x_ave*y_ave))/(sum(toBeSum2)-(n*(x_ave**2)))
        print(m)
    
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setworldcoordinates(0,0,150,150)
    t.up()
    
    
    for i in range(len(x_cor)):
        t.setpos(x_cor[i],y_cor[i])
        t.shape("circle")
        t.shapesize(0.5,0.5,0.5)
        t.stamp()
        t.write((x_cor[i],y_cor[i]),font=("Arial", 12, "normal"))
        
    t.home()
    t.write("home")
    y_intercept = y_ave-(m*x_ave)
    print(y_intercept)
    x_intercept = (m*x_ave-y_ave)/m
    t.setpos(0,y_intercept)
    t.pencolor("red")
    t.down()
    t.setpos(x_intercept,0)

    wn.exitonclick()
    

plotRegression("labdata.txt")  