import turtle
import math
import random

def tree(branch_len):
    if branch_len>5:
        c = ['light pink','misty rose']
        color = random.choice(c)
        if branch_len<20:
            t.pensize(6)
            print(color)
            t.color(color)
        else:
            t.pensize(10)
            t.color('saddle brown')
        i = random.randint(15,45)
        t.fd(branch_len)
        t.rt(i)
        tree(branch_len-15)
        t.lt(2*i)
        tree(branch_len-15)
        t.rt(i)
        t.backward(branch_len)

t = turtle.Turtle()
t.left(90)
t.back(50)
tree(100)

t.hideturtle()
turtle.done()