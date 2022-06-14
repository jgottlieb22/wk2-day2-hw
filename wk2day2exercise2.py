# Exercise 2:

from cmath import pi


def area():
    length = float(input("Enter the length of the room in feet: "))
    width = float(input("Enter the width of the room in feet: "))

    square_footage = length * width
    print(f"The area of the room is {square_footage} square feet.")


def circumference():
    radius = float(input("Enter the radius of the circle in feet: "))
    circ = round(2 * pi * radius, 2)
    print(f"The circumference of the circle is {circ} square feet.")


