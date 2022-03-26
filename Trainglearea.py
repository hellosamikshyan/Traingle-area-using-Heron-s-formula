
def calculatetraingglearea(a,b,c):
    perimeter=a+b+c
    s=perimeter/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    return area

side1=float(input("Enter the first side "))
side2=float(input("Enter the second side"))
side3=float(input("Enter the third side"))
area=calculatetraingglearea(side1,side2,side3)
print(f"The area of the traingle is {area}")