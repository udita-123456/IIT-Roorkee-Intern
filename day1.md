program4
> num1=float(input("enter first number:"))
enter first number:50
>>> num2=float(input("enter second number:"))
enter second number:40
>>> print("addition=",num1+num2);
addition= 90.0
>>> print("subtraction=",num1-num2);
subtraction= 10.0
>>> print("multiplication=",num1*num2);
multiplication= 2000.0
>>> print("division=",num1/num2);
division= 1.25



program5
 weight=float(input("enter your weight in kg:  "))
enter your weight in kg:  50
>>> height=float(input("enteryour height in meters:  "))
enteryour height in meters:  60
>>>  bmi=weight/(height**2)
>>>  print(f"your BMI is: {bmi:.2f}");
your BMI is: 0.01
>>> if bmi<18.5:
...     category="Underweight"
...     elseif 18.5<=bmi<=24.9:
...         category="normal weight"
...         elseif 25<=bmi<29.9:
...             category="overweight"
...             else:
...                 category="obese"
...                    print(f"your are classified as:  {category}");



program 6
 celsius=float(input("enter temperature in celsius: "))
enter temperature in celsius:  35
>>> fahrenheit=(celsius*9/5)+32
>>>  print(f"{celsius}{chr(176)}C is equal to {fahrenheit}{chr(176)}F")
35.0°C is equal to 95.0°F



program 7
 P=float(input("enter the principal amount(P):  "))
enter the principal amount(P):  5000
>>> R=float(input("enter the rate of interest per year(R in %):    "))
enter the rate of interest per year(R in %):    5
>>> T=float(input("enter the time in year (T):  "))
enter the time in year (T):  3
>>> SI=(P*R*T)/100
>>> print(f"The Simple Interest is : {SI}");
The Simple Interest is : 750.0
