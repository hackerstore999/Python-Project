import turtle

t = turtle.Turtle()

t.screen.bgcolor("black")
t.pensize(2)
t.color("cyan")
t.left(90)
t.backward(80)
t.speed(80)

def pattern(i):
    if i < 10:
        return
    else:
        # Stems color
        stem_color = "green"

        # Leaves color
        leaves_color = "yellow"

        t.forward(i)
        t.fillcolor(leaves_color)
        t.begin_fill()
        t.circle(2)
        t.end_fill()
        t.color(stem_color)
        t.circle(i)
        t.left(30)
        pattern(3 * i / 4)
        t.right(60)
        pattern(3 * i / 4)
        t.left(30)
        t.backward(i)

pattern(80)
t.hideturtle()
turtle.done()
