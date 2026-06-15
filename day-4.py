#Build a student grade tracker using a list of tuples
student=[("chetna",35),("shivani",92),("vandana",47),("bharti",78)]
print("student marks:")
for name, marks in student:
    print(f"{name}:{marks}") 
marks = float(input("Enter your marks(0-100): "))
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"
print("Grade:", grade)


#sort a list of names alphabetically and in reverse
names=["vandana","bharti","chetna","udita"]
ascending=sorted(names)
print("Alphabeically order:")
print(ascending)
descending=sorted(names,reverse=True)
print("\nReverse alphabetical order:")
print(descending)


#write a program toremove duplicates from a list
num=[1,2,3,1,4,6,4,5,5,6]
unique_num=list(set(num))
print("original list:",num)
print("without duplicates:",unique_num)


#use list comprehension to genrate squares of 1-20
squares=[x**2 for x in range(1,21)]
print(squares)


#shopping cart:add/remove items, display count
cart = []
while True:
    print("\n--- Shopping Cart Menu ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Item Count")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        item = input("Enter item to add: ")
        cart.append(item)
        print(f"{item} added to cart.")
    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            print(f"{item} removed from cart.")
        else:
            print("Item not found in cart.")
    elif choice == "3":
        if cart:
            print("\nItems in Cart:")
            for item in cart:
                print("-", item)
        else:
            print("Cart is empty.")
    elif choice == "4":
        print(f"Total items in cart: {len(cart)}")
    elif choice == "5":
        print("Thank you for shopping!")
        break
    else:
        print("Invalid choice. Please try again.")


#find the second largest and second smallest numbr in a list
numbers=[12,13,14,36,2,13,36]
unique_numbers=list(set(numbers))
unique_numbers.sort()
second_smallest=unique_numbers[1]
second_largest=unique_numbers[-2]
print("list:",numbers)
print("2nd smallest:",second_smallest)
print("2nd largest:",second_largest)


#matrix addition using nested lists
A = [[1, 2, 3],[4, 5, 6]]
B = [ [7, 8, 9], [10, 11, 12]]
result = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    result.append(row)
print("Sum of matrices:")
for row in result:
    print(row)