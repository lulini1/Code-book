import turtle 

size =int(input("please input size:(20~200)"))

t = turtle.Turtle()
t.color('red')
t.pensize(3)

for i in range(5):
    t.forward(size)
    t.right(144)

t.hideturtle()
turtle.done()