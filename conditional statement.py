#if statement:
print("Hello World")
age=int(input("enter age:"))
if(age>=18):
    print("eligible to vote")
    print("eligible for lisence")
else:
    print("not eligible to vote")
    print("not eligible for lisence")
print("hello class")

# elif statement:
number=int(input("enter number:"))
if(number==1):
    print("MRDU")
elif(number==2):
    print("MBU")
elif(number==3):
    print("SVCE")
else:
    print("select another collage")


# Nested if statement:
number=int(input("enter a number:"))
if(number>=0):               # 45>0--t   # 100>0---t  #-9>0--f
    
    if(number<50):  #45<50---t  #100<50---f
        print("number between 0 - 50")
    else:
        print("number greater than 50")
else:
    print("number is negative")


#h.w
number=int(input("enter a number:"))
if(number%2==0):
    print("number is even")
else:
    print("number is odd")
    
    #marks
marks=int(input("enter your marks:"))
if(marks >=45):
    print("Your are passed")
else:
    print("you are failed")
    
#multiply by 5:
number=int(input("enter the number:"))
if(number%5==0):
    print("Divisible by 5")

#temperature
temperature=float(input("enter a temperature:"))
if(temperature>=40):
    print("High Temperature")
else:
    print("temperature is normal")

#if number is grester than 100 then print positive,else print negitive. 
number=int(input("enter a number:"))
if(number>=100):
    print("number is greater than 100")
else:
    print("number is smaller than 100")
#print positive or negitive
number=int(input("enter a number:"))
if(number>=0):
    print("Positive")
else:
    print("Negitive")
 #   

marks=int(input("Enter marks:"))
if(marks >=90):
    print("Grade A")
elif(marks>=75):
    print("Grade B")
elif(marks >= 60):
    print("Grade C")
elif(marks >=50):
    print("Grade D")
else:
    print("fail")
    
#largest of 2 numbers:
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
if(a > b):
    print("Largest:",a)
elif(b > a):
    print("Largest:",b)
else:
    print("Both are Equal")
    
#largest of three numbers
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
if a>=b and a>=c :
    print("a is largest")
elif b>=a and b>=c :
    print("b is largest")
else :
    print("c is largest")
    
#
day=int(input("enter a number:"))
if(day==1):
    print("Monday")
elif(day==2):
    print("Tuesday")
elif(day==3):
    print("Wednesday")
elif(day == 4):
    print("Thursday")
elif(day == 5):
    print("Friday")
elif(day == 6):
    print("Saturday")
elif(day == 7):
    print("Sunday")
else:
    print("invalid day")

#
a=float(input("Enter First Number:"))
b=float(input("Enter Second Number:"))
operator = input("Enter operator(+,-,*,/):")

if operator == "+":
    print("Result:",a+b)
elif(operator=="-"):
    print("Result:", a-b)
elif(operator =="*"):
    print("Result:",a*b)
elif(operator == "/"):
    if b !=0:
        print("Result:",a/b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
    
#
username = input("Enter username:")
password = input("Enter password:")
if(username == "admin"):
    if(password == "1234"):
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")   
    

balance = float(input("Enter balance:"))
amount = float(input("Enter withdrawal amount:"))
if(amount >0):
    if(amount <= balance):
        balance = balance - amount
        print("Withdrawal successful")
        print("Remaining balance:",balance)
    else:
        print("Insufficient balance")
else:
    print("Invalid amount")
    

marks = int(input("Enter marks:"))
attendence = float(input("Enter attendence percentage:"))
if(marks >=40):
    if(attendence >=75):
        print("Eligible")
    else:
        print("Not eligible due to attendence")
else:
    print("Fail")


age = int(input("Enter age:"))
test = input("Did you pass the draving test?(yes/no):")
if(age >= 18):
    if(test == "yes"):
        print("Lisence can be issued")
    else:
        print("Pass theb driving test first")
else:
    print("Not eligible due to age")

#BODMAS

result=(10+5)*10
print("result",result)
