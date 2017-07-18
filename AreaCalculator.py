"""This is a free-form calculator.  Its purpose is to do freeform calculations."""

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print "Alert: the calculator is starting up..."
print "Current time: %s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)

sleep(1)

hint = "Don't forget to unclude the correct units! \nExiting..."

option = raw_input("Enter C for Circle or T for Triangle: ")

option.upper()

if option == "C":
    radius = float(raw_input("Enter a radius: "))
    area = pi * radius**2
    print "The pie is baking..."
    sleep(1)
    print ("Area: %.2f. \n%s" % (area, hint))
elif option == "T":
    base = float(raw_input("Enter a base: "))
    height = float(raw_input("Enter a height: "))
    area = (0.5)*base*height
    print "Uni Bi Tri..."
    sleep(1)
    print ("Area: %.2f. \n%s" % (area, hint))
else:
    print "You picked garbage; the program will end in 3... 2... 1.."
    sleep(1)
