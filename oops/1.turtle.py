from turtle import Turtle, done

t1 = Turtle()
t2 = Turtle()

t1.color("orange")
t2.color("green")

t1.forward(distance=100)
t1.left(angle=90)

t2.left(angle=90)
t2.forward(distance=50)

done()
