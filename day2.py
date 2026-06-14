#write a grade classifier : input marks , output A/B/C/D/F
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





#Print multiplication table of a number
num = int(input("Enter a number:  "))
print("Multiplication Table of", num)
for i in range(1, 11):
    print(num, "x", i, "=", num*i)



#Write a while loop that prints even numbers from 1 to 50
num = 2
while num <= 50:
    print(num)      
    num += 2



#FizzBuzz : print Fizz , Buzzz , FizzBuzz for multiples of 3 , 5 , both
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:    
        print("FizzBuzz")
    elif i % 3 == 0:                 
        print("Fizz")
    elif i % 5 == 0:                  
        print("Buzz")                  
    else:
        print(i)




#Number guessing game using a while loop
secret_number = 42       
while True:
    guess = int(input("Guess the number: "))
    if guess == secret_number:
        print("Found the secret number!")
        break
    elif guess != secret_number:
        print("Try again.")





#Pyramid star pattern using nested loops
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()




#Find all prime numbers between 1 and 100
print("Prime numbers between 1 and 100:")
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num) 