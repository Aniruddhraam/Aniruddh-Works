#AREA AND PERIMETER OF CIRCLE
PI=3.14
r=float(input("Enter the radius of a circle:"))
area = PI * r * r
perimeter = 2 * PI * r
print("Area of a circle: ",area)
print("Perimeter of a circle:",perimeter)
#AREA AND PERIMETER OF A RECTANGLE
width = int(input("Enter the width of a rectangle:"))
height = int(input("Enter the height of a rectangle:"))
#calculate the area
Area = width * height
#calculate the perimeter
Perimeter = 2 * (width + height)
print("\n Area of a rectangle is:",Area)
print("Perimeter of a rectangle is:",Perimeter)
#AREA AND PERIMETER OF A SQUARE
side = float(input("Enter the length of the side of the square:"))
#calculate the area of square
Area = side * side
#calculate the perimeter of square
Perimeter = 4 * side
print("Area of a square:",Area)
print("Perimeter of a square:",Perimeter)
