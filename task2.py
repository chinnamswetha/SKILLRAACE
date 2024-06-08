import turtle

def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_chakra(radius, spokes, color):
    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()
    turtle.color(color)
    turtle.circle(radius)
    
    # Draw the spokes
    turtle.penup()
    turtle.goto(0, 0)
    for _ in range(spokes):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.forward(radius)
        turtle.backward(radius)
        turtle.right(360 / spokes)

def draw_indian_flag():
    # Set up the turtle
    turtle.speed(10)
    turtle.bgcolor("white")

    # Dimensions for the flag
    flag_height = 300
    flag_width = 450
    stripe_height = flag_height / 3

    # Draw the three stripes
    draw_rectangle("orange", -flag_width / 2, flag_height / 2, flag_width, stripe_height)
    draw_rectangle("white", -flag_width / 2, flag_height / 6, flag_width, stripe_height)
    draw_rectangle("green", -flag_width / 2, -flag_height / 6, flag_width, stripe_height)

    # Draw the Ashoka Chakra
    draw_chakra(radius=50, spokes=24, color="blue")

    # Hide the turtle and display the result
    turtle.hideturtle()
    turtle.done()

# Call the function to draw the flag
draw_indian_flag()
