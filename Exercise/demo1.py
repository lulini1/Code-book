import random
import turtle

def tree(branch_len):
    if branch_len > 5:
        if branch_len<20:
            t.forward(branch_len)
        #t.pensize(size_len)
        #size_len = size_len + 1
            i = random.randint(15,45)
            t.right(i)
            tree(branch_len - 35)
        t.left(2 * i)
        tree(branch_len - 35)
        t.right(i)
        t.backward(branch_len)
    elif branch_len in range(5,35):
        t.forward(branch_len)
        #t.pensize(size_len)
        #size_len = size_len + 1
        i = random.randint(15,45)
        t.right(i)
        tree(branch_len - 5)
        t.left(2 * i)
        tree(branch_len - 5)
        t.right(i)
        t.backward(branch_len)

#def pensize(size_len):
    #if size_len > 0:
        #t.pensize(size_len)
        #size_len = size_len - 1

t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(300)
t.pendown()
t.pencolor('green')
t.pensize(6)
tree(200)

t.hideturtle()
turtle.done()