#作图程序模版
##•首先，导入turtle模块
##•然后，生成一只海龟
##•可以做一些初始化设定
##•程序主体：用作图语句绘图
##•最后结束作图
##•可选隐藏海龟：t.hideturtle()
# 1. 导入海龟模块
import turtle

n = 300
# 2. 生成一只海龟，做一些设定
t = turtle.Turtle()
t.pencolor("black")  # 画笔颜色
t.pensize(n*0.10)  # 画笔粗细
t.fillcolor("yellow")

# 3. 用海龟作图
#for i in range(5):
    #t.forward(50)
    #t.right(60)
t.forward(n)
t.left(120)
t.begin_fill()
t.forward(n)
t.left(120)
t.forward(n)
t.left(120)
t.end_fill()

t.penup()
t.goto(n*0.50,n*0.15)
t.pendown()
t.dot(n*0.08,"black")

t.penup()
t.goto(n*0.50,n*0.22)
t.pendown()
t.left(82)
t.pensize(1)
t.fillcolor("black")
t.forward(n*0.30)
t.begin_fill()
t.circle(n*0.04,180)
t.left(15)
t.forward(n*0.30)
t.end_fill()


# 4. 结束作图
t.hideturtle()
turtle.done()
#反向输出一个三位数
s_list = input('')
print(s_list[::-1])#切片
