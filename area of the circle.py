Task 1 

import math
radius = float(input("Enter the radius of the circle : "))

area = math.pi*radius*radius
print("Area of the circle is : {0}".format(area))

Task 2

filename = input("Input filename : ")
f_extns = filename.split(".")
print("extension of file is:"+repr(f_extns[-1]))






