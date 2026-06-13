#pragram that takes name,age as input and prints a greeting
name="udita"
age=22
greetings="hello"
print(greetings)
print("my name is:",name)
print("my age is:",age) 


#create a variable of each data type and print their types using type ()
a="udita"
b=22
c=True
d=22.5
print(type(a))
print(type(b))
print(type(c))
print(type(d))


#build a simple calculator that adds, substract,multiplies, and divides two numbers
k=25
l=24
float(k)
float(l)
print("addition:",k+l)
print("subtraction:",k-l)
print("multiplication:",k*l)
print("division:",k/l)


#BMI calculator:input height & weight ,outputBMI category
weight=float(input("enter your weight in kg:"))
height=float(input("enter your height in meter:" ))
BMI=weight/(height*height)
if BMI<18.5:
    print("category=underweight")
elif BMI<25:
    print("category=normal")
else:
    print("category=overweight")

     
#temperature converter:celsius-fahrenheit
c=float(input("enter the value of c:"))
f=((c*9)/5)+32
print("f=",f)
c=(f-32)*5/9
print("c=",c)