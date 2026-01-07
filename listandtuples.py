friends = ["Alice", "Bob", "Charlie", 35 , 5.9, True]

print(friends[0])
friends[1] = "David"
print(friends)  

friends.append("Eve")

l1 = [23, 5, 78, 1, 34]

value =l1.pop()
print(f"Popped value: {value}")

l1.reverse()
print(l1)


# tuples - immutable (cannot be changed)
a =( 10, 20, 30, "Hello", False)

a.count(10)
print(a[3])
fruits = []
f1 = input("Enter the name of fruit 1: ")
fruits.append(f1)
f2 = input("Enter the name of fruit 2: ")   
fruits.append(f2)
f3 = input("Enter the name of fruit 3: ")
fruits.append(f3)
print(fruits)