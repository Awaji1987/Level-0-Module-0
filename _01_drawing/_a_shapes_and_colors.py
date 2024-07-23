import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
freddy_fazbear = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
freddy_fazbear.shape('turtle')
# Set your turtle's speed using .speed(2)
freddy_fazbear.speed(2)
# Set your turtle's color using .color('green') and .pencolor('blue')
freddy_fazbear.color('brown')
freddy_fazbear.pencolor('black')
# Move your turtle forward using .forward(100)
# TEST    Did your turtle move forward?
freddy_fazbear.forward(100)
# Move your turtle left or right using .left(90) or .right(90)
freddy_fazbear.left(90)
freddy_fazbear.right(90)
# Now put the forward and left/right code into a for loop to repeat 4 times.
# TEST    Did your turtle draw a square?
for i in range(4):
    freddy_fazbear.forward(100)
    freddy_fazbear.left(90)
    freddy_fazbear.right(90)
# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen
freddy_fazbear.goto(8, 7)
# Have your turtle draw a circle using .circle(radius, steps=30)
# TEST    Did your turtle draw a circle?
freddy_fazbear.circle(3, steps=30)
# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below
freddy_fazbear.begin_fill()
freddy_fazbear.end_fill()
# Draw 3 more shapes with different fill colors!

# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
