#TurtleGraphics.py
#Name: Brock Hoover
#Date: 2-16-25
#Assignment: Lab 4.

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)
        
def fillCorner(alice, corner):
    #draw big square
    drawSquare(alice, 100)
    
    if corner == 1:
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 2:
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 3:
        alice.forward(100)
        alice.right(90)
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 4:
        alice.forward(100)
        alice.right(90)
        alice.forward(100)
        alice.right(90)
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()

def squaresinSquares(owen, squares):
    xcord = -199
    ycord = 199
    for o in range(squares):
        owen.penup()
        owen.goto( xcord, ycord)
        owen.pendown()
        drawSquare(owen, ycord * 2)
        xcord = xcord + 10
        ycord = ycord - 10
        
  
def main():
    myTurtle = turtle.Turtle()
    
    Program = input("Enter a program (drawPolygon, fillCorner, squaresinSquares): ")

    if(Program == "drawPolygon"):
        sides = input("Enter an Amount of Sides for a Polygon: ")
        sides = int(sides)
        drawPolygon(myTurtle, int(sides))
    elif(Program == "fillCorner"):
        corner = input("Enter desired filled corner: ")
        corner = int(corner)
        fillCorner(myTurtle, int(corner))
    elif(Program == "squaresinSquares"):
        squares = input("Enter desired amount of squares: ")
        squares = int(squares)
        squaresinSquares(myTurtle, squares)
    else:
        print("Run program again, enter desired program")

main()
