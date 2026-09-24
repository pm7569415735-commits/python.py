# #Arthimetic operators
# a=10
# b=3

# print("Addition:" ,a+b)
# print("Subraction:", a-b)
# print("Multiplication:", a*b)
# print("Division:", a/b)
# print("Floor division:", a//b)
# print("remainder:", a%b)
# print("Power:", a**b)


# #simple calculator

# a=int(input("enter first number:"))
# b=int(input("enter second number:"))

# print("Addition:" ,a+b)
# print("Subraction:", a-b)
# print("Multiplication:", a*b)
# print("Division:", a/b)

# #student marks calculator
# name = input("enter your name:")

# m1 = int(input("enter python marks:"))
# m2 = int(input("enter java marks :"))
# m3 =int(input("enter sql marks:"))

# total =m1+m2+m3
# average=total/3

# print("/n---- students report-----")
# print(  "Name:", name)
# print("python marks:", m1)
# print("java marks:", m2)
# print("sql marks:", m3)
# print("total marks:", total)
# print("average marks:", average)


# #shopping bill calculator
# price1 = float(input("enter produt 1 price:"))
# price2 = float(input("enter product 2 price:"))
# price3 = float(input("enter product 3 price:"))

# total = price1+price2+price3

# discount =total*0.10
# finalamount  =  total-discount


# print("discount:", discount)
# print("final amount:", finalamount)
# print("total bill:", total)


# #bank balance
# balance=10000

# deposit=5000
# balance += deposit

# print("after deposit balance:", balance)
# withdraw=2000
# balance -= withdraw
# print("after withdrawal balance:", balance)

# #login validation
# username = input("enter username:")
# password = input("enter password:")

# if username == "admin" and password == "password":
#     print("login successful!")
# else:
#     print("invalid credentials!")


# #identity operators
#     a=None

#     print(a is None)
#     print(a is not None)


# #bitwise operators
# a=5
# b=3

# print(a&b) #bitwise AND
# print(a|b) #bitwise OR
# print(a^b) #bitwise XOR

# #Electricity bill calculator
# units = int(input("Enter the number of units consumed: "))

# rate=6

# bill=units*rate


# print("Electricity bill:", bill)

# #travel expense calculator
# travel = float(input(" travel expense: "))
# food = float (input )("food expeense: ")
# hotel =float (input )("hotel expeense: ")
# total_expense = travel + food +hotel

# #list python
# #list is an ordered and changeble collection  that can store multiple values.
# marks=[80,90,75,85]
       
# print(marks)

# #accessing list elements
# marks=[80,90,75,85]

# print(marks[0]) #accessing first element    
# print(marks[1]) #accessing second element   
# print(marks[2]) #accessing third element       

# #change  elements in a list
# marks=[80,90,75,85]
# marks[1]=95

# print(marks)


# #remove elements from a list
# marks=[80,90,75]

# marks.remove
# numbers = [10,20,20,30,20]
# print(number.count(20))

# numbers = [40'10,20,30]

# numbers.sort()
# print(numbers)
# numbers.sort(revers=true)

# numbers = [10,20,30,40,50]

# print(numbers[1:4])
# print(numbers[:3])
# print(numbers[2:])
# print(numbers[::-5)
age=29

if age >=18:
    pass

else:
    print("not eligiable")
#print odd numbers from 1 to 10    
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)

