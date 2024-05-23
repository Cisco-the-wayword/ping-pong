from random import randrange
from turtle import *

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, other):
        self.x += other.x
        self.y += other.y

    def copy(self):
        return Vector(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

def square(x, y, size, color):
    """Draw square at (x, y) with given size and color."""
    up()
    goto(x, y)
    down()
    begin_fill()
    fillcolor(color)
    for _ in range(4):
        forward(size)
        left(90)
    end_fill()

food = Vector(0, 0)
snake = [Vector(10, 0)]
aim = Vector(0, -10)

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
