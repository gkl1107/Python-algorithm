import turtle

t = turtle.Turtle()
wn = turtle.Screen()
wn.screensize(400,400)
t.color("blue")

with open("mystery.txt") as dt:

    line = dt.readline()
    while line:
        values = line.split()
        if len(values) == 1:
            if values[0] == "UP":
                t.up()
            else: 
                t.down()
        else:
            x = int(values[0])
            y = int(values[1])
            t.goto(x,y)
        line = dt.readline()


wn.exitonclick()