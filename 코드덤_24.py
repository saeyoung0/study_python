import turtle as t

t.bgcolor("black")
t.color("pink")
t.speed(0) #1~10(빠름)  0:최고

for i in range(200):
    t.pensize(i/50)
    t.forward(i)
    t.left(65)

t.color("lightblue")
t.setheading(270)

for i in range(50):
    t.pensize(25-i/2)
    t.forward(i/4)

t.color("yellowgreen")
t.setheading(60)
for x in range(100):
    t.pensize(100-x)
    t.forward(x/10)

t.ht() #hideturtle()=ht()  showturtle() = st()
