import math
print("AREA AND PERIMETER OF A CIRCLE\n")
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
perimeter = 2 * math.pi * radius
print(f"The area of the circle is: {area}")
print(f"The perimeter of the circle is: {perimeter}")