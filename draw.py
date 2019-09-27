import turtle

def draw_square(dist):
    turtle.speed(6)
    for i in range(4):
        turtle.forward(dist)
        turtle.right(90)
    turtle.forward(dist)
    
def fibonacci(num):
    a = b = 1
    for j in range(1, num + 1):
        draw_square(a * 5)  # it could be 'a' times any number...
        if b > 1:
        # this will set the start point of the next square
            turtle.right(90)
            turtle.forward(a * 5)
        a, b = b, a + b

num = int(input("Enter the number of squares: "))
fibonacci(num)

turtle.exitonclick()

    
    
    