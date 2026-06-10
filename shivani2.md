marks = float(input("Enter marks (0-100): "))
Enter marks (0-100): 86
>>> if marks >= 90:
...     grade = "A"
... elif marks >= 80:
...     grade = "B"
... elif marks >= 70:
...     grade = "C"
... elif marks >= 60:
...     grade = "D"
... else:
...     grade = "F"
...
... print("Grade:", grade)
...
Grade: B
>>>
 num= int(input("Enter a number:"))
... for i in range(1,11):
...     print(num,"x",i,"=",num*i)
...
Enter a number:6
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60
 num=2
>>> while num<=50:
...     print(num)
...     num+=2
...
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
>> for i in range(1, 20):
...     if i % 3 == 0 and i % 5 == 0:
...         print("FizzBuzz")
...     elif i % 3 == 0:
...         print("Fizz")
...     elif i % 5 == 0:
...         print("Buzz")
...     else:
...         print(i)
...
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19>

 secret = 7
...
... guess = 0
...
... while guess != secret:
...     guess = int(input("Guess the number: "))
...
...     if guess == secret:
...         print("Correct!")
...     else:
...         print("Try again!")
...
Guess the number: 5
Try again!
Guess the number: 7
Correct!
 rows = 5
...
... for i in range(1, rows + 1):
...     for j in range(i):
...         print("*", end=" ")
...     print()
...
*
* *
* * *
* * * *
* * * * *

>>> for num in range(2, 101):
...     prime = True
...
...     for i in range(2, num):
...         if num % i == 0:
...             prime = False
...             break
...
...     if prime:
...         print(num)
...
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
