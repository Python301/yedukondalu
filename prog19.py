# WAPP to calculate area of polygon
import math
n=int(input("enter how many sides:"))
s=float(input("enter the side length:"))
Area=(n*s**2)/(4*math.tan(math.pi/n))
print(Area)
