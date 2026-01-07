# calc area of rectangle

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length*width

print(f"The area of the rectangle is {area}cm²")

# shopping cart

item1 = input("Enter the name of the first item: ")
price1 = float(input(f"Enter the price of {item1}: "))
qunatity1 = int(input(f"how many would you like of {item1}: "))

total1 = price1 * qunatity1 

print(f"The total price for {qunatity1} {item1} is {total1}")