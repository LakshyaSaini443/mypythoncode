import turtle
import math

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
star = turtle.Turtle()
star.speed(0)  # Set the drawing speed

# Function to draw the circle star pattern
def draw_circle_star(radius, num_points):
    angle = 360 / num_points
    for _ in range(num_points):
        for _ in range(5):
            star.forward(radius)
            star.right(144)
        star.right(angle)

# Animation loop
for i in range(360):
    star.color("white")
    star.fillcolor("white")
    star.begin_fill()
    draw_circle_star(100, 5)
    star.end_fill()
    star.right(5)  # Rotate the pattern
    screen.update()

# Close the window on click
screen.exitonclick()