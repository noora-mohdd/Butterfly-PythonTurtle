import turtle as tur
#screen setip
screen=tur.Screen()
screen.title("butterfly")
tur.colormode(255) 
screen.bgcolor(0,0,0)

left_t = tur.Turtle()
right_t = tur.Turtle()

for t in (left_t, right_t):
    t.shape("circle")
    t.shapesize(0.5, 0.5)
    t.pensize(5)
    t.speed(7)
    t.color((254,0,154), (242,41,82))

right_t.circle(20,180)
left_t.setheading(180)
left_t.circle(-20,180)
right_t.penup()
right_t.goto(0,0)
right_t.pendown()
left_t.penup()
left_t.goto(0,0)
left_t.pendown()


right_t.lt(45)
left_t.rt(45)
right_t.fd(40)
left_t.fd(40)
right_t.lt(50)
left_t.rt(50)
right_t.fd(150)
left_t.fd(150)
right_t.circle(40,52)
left_t.circle(-40,52)

right_t.penup()
right_t.goto(29,-31)
right_t.pendown()
left_t.penup()
left_t.goto(-29,-31)
left_t.pendown()


right_t.setheading(45)
left_t.setheading(135)
right_t.fd(200)
left_t.fd(200)
right_t.circle(-100,60)
left_t.circle(100,60)
right_t.setheading(280)
left_t.setheading(260)


right_t.circle(-150,60)
left_t.circle(150,60)
right_t.setheading(280)
left_t.setheading(260)
right_t.circle(-80,80)
left_t.circle(80,80)

right_t.seth(170)
left_t.seth(10)
right_t.fd(140)
left_t.fd(140)

left_t.penup()
left_t.goto(-165,-95)
left_t.seth(225)
left_t.pendown()
right_t.penup()
right_t.goto(165,-95)
right_t.seth(315)
right_t.pendown()

left_t.circle(90,90)
left_t.circle(80,40)
right_t.circle(-90,90)
right_t.circle(-80,40)

right_t.seth(135)
left_t.seth(45)
right_t.fd(135)
left_t.fd(135)



#ANTENNA HEHE
right_t.penup()
right_t.goto(15,34)
right_t.pendown()
right_t.seth(45)
right_t.fd(50)

left_t.penup()
left_t.goto(-15,35)
left_t.pendown()
left_t.seth(135)
left_t.fd(50)

right_t.seth(90)
left_t.seth(90)
right_t.fd(20)
left_t.fd(20)

#inside details?
right_t.penup()
left_t.penup()
right_t.seth(0)
left_t.seth(0)
right_t.goto(140,-70)
left_t.goto(-140,-70)
right_t.pendown()
left_t.pendown()
right_t.circle(50)
left_t.circle(50)#big circle in top wing



left_t.penup()
right_t.penup()
left_t.goto(-140,-42)
right_t.goto(140,-42)
left_t.pendown()  
right_t.pendown()
left_t.circle(20)
right_t.circle(20)



left_t.penup()
right_t.penup()
left_t.goto(-125,-200)
right_t.goto(125,-200)
left_t.pendown()  #-90 for on da wing
right_t.pendown()
left_t.circle(40)
right_t.circle(40)



left_t.penup()
right_t.penup()
left_t.goto(-125, -180)
right_t.goto(125,-180)
left_t.pendown()
right_t.pendown()
left_t.circle(30)
right_t.circle(30)


#for the upper details
left_t.penup()
right_t.penup()
left_t.goto(-247, 30)
right_t.goto(247,30)
left_t.pendown()
right_t.pendown()
left_t.seth(90)
right_t.seth(90)

left_t.circle(-100, 66)
right_t.circle(100, 66)

screen.mainloop()

