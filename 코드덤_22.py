import turtle

turtle.shape("turtle") #turtle, square, triangle, arrow, circle
turtle.bgcolor("skyblue")

turtle.color("hotpink")
for i in range(4) : # 0,1,2,3
    turtle.forward(100) #앞으로 100px 만큼 이동
    turtle.left(90)     #왼쪽으로 90만큼 이동


turtle.color("blue")
for i in range(3):
    turtle.forward(100)
    turtle.left(120)


turtle.color("yellow")
for i in range(5):
    turtle.forward(100)
    turtle.left(72) #360 / 5

