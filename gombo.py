import turtle
import random
import math

def draw_circle(x, y, radius, color):
    """Draws a filled circle with the given parameters."""
    turtle.penup()
    turtle.goto(x, y - radius)  # Move to the top of the circle
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    turtle.circle(radius)
    turtle.end_fill()

def draw_topping(x, y, radius, topping_count=60):
    """Draws many small toppings on the bread."""
    turtle.penup()
    for _ in range(topping_count):  # Increase topping count for more toppings
        angle = random.uniform(0, 2 * math.pi)  # Angle in radians
        dist = random.uniform(0, radius - 10)  # Ensure toppings are inside the bread
        topping_x = x + dist * math.cos(angle)
        topping_y = y + dist * math.sin(angle)
        turtle.goto(topping_x, topping_y)
        turtle.dot(random.randint(5, 8), "saddlebrown")  # Random small dots for toppings

def draw_soboro():
    """Draws a soboro bread."""
    turtle.speed(0)  # Max speed for drawing
    turtle.hideturtle()

    # Draw the main bread body
    draw_circle(0, 0, 150, "burlywood")

    # Draw toppings on the bread
    draw_topping(0, 0, 150, topping_count=100)  # Add more toppings

    # Prevent window from closing immediately
    turtle.done()

# Run the soboro drawing
draw_soboro()
