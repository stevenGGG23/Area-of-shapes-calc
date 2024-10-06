#calculator.py 
#In this Lab we will be creating a project where the user can get for 
#the calculations of the area of a triangle, circle, or rectangle if they provide us with the width and height 


PI = 3.1415929

print("1. Calculate the Area of a Triangle") 
print("2. Calculate the Area of a Circle") 
print("3. Calculate the Area of a Rectangle") 
print("4. Done")  

choice = int(input("Enter your choice (1-4): "))
if choice == 1: 
    width, height = input("Enter width and height separated by space: ").split()
    width = float(width)
    height = float(height)
    triangle_area = width * height * 0.5
    print(f"T Area: {triangle_area:12.4f}")

elif choice == 2:
    radius = float(input("Enter radius: ")) 
    circle_area = PI * (radius * radius)
    print(f"C Area: {circle_area:12.4f}")  

elif choice == 3:  
    width, height = input("Enter width and height separated by space: ").split()  
    width = float(width)
    height = float(height) 
    rectangle_area = width * height 
    print(f"R Area: {rectangle_area:12.4f}") 

elif choice == 4: 
    print("Goodbye!") 

else: 
    print("Did you even read the menu???")
