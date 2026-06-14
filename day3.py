#Create a function to check whether a number is a palindrome
def is_palindrome(num):                 
    original = num
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return original == reversed_num
number = int(input("enter a number: "))       
if is_palindrome(number):                       
    print((number)," is a palindrome.")
else:
    print((number)," is not a palindrome.")



#Write a recursive function for fibonacci series
def fibonacci(n):                 
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the number of terms: "))    
print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i))

#program3
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
def cube(a):
    return a ** 3
print("addition :" , add(2,3))
print("subtraction ; " ,subtract(3,4))
print("multiply :" ,  multiply(3,4))
print("divide : ",divide(3,4))



#Use the random module to bulid a dice-roll simulator
import  random
def roll_dice():
    return random.randint(1,6)
while True:
    print("You rolled :", roll_dice())
    choice = input("Roll again : ")
    if choice != 'yes':
        print("Thanks for playing!")
        break



    
def quiz():
    questions = [
        ("Which planet is known as Red Planet?", "Mars"),
        ("Which planet we live on?", "Earth"),
        ("What is the capital of India?", "New Delhi"),
        ("How many days are there in a week?", "7"),
        ("How many hours are there in a day?", "24")
    ]
    
    score = 0
    
    for q, correct_answer in questions:
        user_answer = input(q + " ").strip().lower()
        
        if user_answer == str(correct_answer).lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    
    print("\nFinal Score:", score, "/", len(questions))
quiz()




#Password generator using random & string modules
import random 
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
password_length = int(input("Enter the length of the password: "))
password = generate_password(password_length)
print("Generated Password:", password)




#Factorial calculator : iterative and recursive approaches
def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact
def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
    #Take number as input from user
num = int(input("Enter a number: "))
print("Iterative Factorial: ", factorial_iterative(num))
print("Recursive Factorial: ", factorial_recursive(num))