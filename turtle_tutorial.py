"""
Before we can create a turtle we need to import the python turtle module.
"""

import turtle


"""
Now that we have imported the python turtle module we can now create a turtle: 

"""

t = turtle.Turtle()
s = turtle.Screen()                                                                                                     
s.bgcolor("black")                                                                                                      
t.pencolor("white")  
t.speed(0)

"""
Lets encapsulate our turtle creation code into a function

"""
def create_turtle():
    t = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor("black")                                                                                                      
    t.pencolor("white")  
    t.speed(0)

"""
In order to change the turtle screen background and pen color. We will have to go into the functions and make
the changes. This is poor software engineering(Do you know why?). We can fix that my allowing our create_turtle function to
take parameters:

- create two variables turtle_background_color and turtle_pen_color and assign values for bgcolor and pencolor to them 
- modify your function so that they take two parameters and use them to set the bgcolor and the pencolor 
"""
turtle_background_color = "black"
turtle_pen_color = "green"


def create_turtle(turtle_background_color,turtle_pen_color):
    t = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor(turtle_background_color)                                                                                                      
    t.pencolor(turtle_pen_color)  
    t.speed(0)
    return t


"""
Now we can create our turtle
"""
my_turtle = create_turtle(turtle_background_color,turtle_pen_color)    



"""
Now that we have a lets create some simple shapes

"""

"""
 a: Create a fixed length line 
"""

# my_turtle.forward(50)

"""
b: how would you convert this to function
"""

def draw_line(my_turtle,length_of_line):
    my_turtle.forward(length_of_line)
    

"""
Now up can use your function to draw any line of arbitrary length
"""
length_of_line = 5
draw_line(my_turtle,length_of_line)


"""
 Using for loops to repeat actions
 
"""
# Lets draw a square, using our draw_line function? 
length_of_line = 300
"""
for side in range(0,4):
    draw_line(my_turtle,length_of_line)
    my_turtle.right(90)
"""    
# now lets convert it to a function so that it is easier to reuse later
def draw_square(my_turtle,side_length):
    for side in range(0,4):
        draw_line(my_turtle,side_length)
        my_turtle.right(90)
    
# let call it and see what happens
side_length = 300
#draw_square(my_turtle,side_length)


"""
Lets draw an arc
"""
"""
deg = 180
for rep in range(0, deg):
    my_turtle.forward(1)
    my_turtle.left(1)
"""

"""
 Let encapsulate the logic into a function
"""

def draw_arc_right(my_turtle,size,deg):
    for rep in range(0, deg):
        my_turtle.forward(size)
        my_turtle.right(1)

deg = 360
size = 1
draw_arc_right(my_turtle,size,deg)


def draw_arc_left(my_turtle,size,deg):
    for rep in range(0, deg):
        my_turtle.forward(size)
        my_turtle.left(1)



"""
Let use our arc to draw a circle 
"""


def draw_circle(my_turtle):
    deg = 360
    draw_arc(my_turtle,deg)
    

# draw_circle(my_turtle)

def draw_circles(my_turtle):
    deg = 360
    for cnt in range(0,10):
        draw_arc_right(my_turtle,size,deg)
        my_turtle.right(40)

# draw_circles(my_turtle)


"""
Lets use what we have so far to draw a flower
"""

def draw_petal(my_turtle, petal_size):
    pass


"""
count = 0
side_length = 1
while count < 360:
    draw_line(my_turtle,side_length)
    my_turtle.right(1)
    count = count + 1
"""

# once again we can convert it to function,to make it more reusable
"""
def draw_circle(my_turtle, number_of_degrees,forward_distance,rotation):
    count = 0
    while count < number_of_degrees:
        draw_line(my_turtle,forward_distance)
        my_turtle.right(rotation)
        count = count + 1

"""
"""
number_of_degrees = 60
forward_distance = 1
rotation = 1
draw_circle(my_turtle, number_of_degrees,forward_distance,rotation)


def draw_circles(my_turtle, number_of_degrees,forward_distance,rotation, number_of_circles):
    for cnt in range(0,number_of_circles):
        draw_circle(my_turtle, number_of_degrees,forward_distance,rotation)

number_of_degrees = 360
forward_distance = 1
rotation = 40
number_of_circles = 9        
draw_circles(my_turtle, number_of_degrees,forward_distance,rotation, number_of_circles)
"""

"""
One approach to programming is to take a large problem and break it up into
small pieces then solve the small pieces and then combine the solutions. 

"""
turtle.done()
