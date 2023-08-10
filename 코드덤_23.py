import turtle as t

t.bgcolor("pink")

t.color("red")
t.begin_fill()

for i in range(3):
    t.forward(200)
    t.right(360/3)
    
t.end_fill()

t.forward(100)
t.color("lightgreen")
t.begin_fill()
t.circle(100)
t.end_fill()

t.goto(150,150)
t.color("lightblue")
t.begin_fill()
t.circle(75)
t.end_fill()


t.color("yellow")
t.begin_fill()
for i in range(5):
    t.forward(30)
    t.right(144 )
t.end_fill()
