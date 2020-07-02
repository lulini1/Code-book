import turtle

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def golden_spiral(n):
        for i in range(1,n):
            t.circle(fibonacci(i),90)
            i = i + 1

t = turtle.Turtle()

golden_spiral(12)

t.hideturtle()
turtle.done()