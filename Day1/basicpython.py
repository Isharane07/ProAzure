# a = 10
# b = 20
# print("Basic Arithmetic Operations:")
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)

# print("comparison operators:")
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)

# print("logical operators:")
# print(a == 10 and b == 20)
# print(a == 10 or b == 30)
# print(not(a == 10))

# print("bitwise operators:")
# print(a & b)
# print(a | b)
# print(a ^ b)
# print(~a)
# print(a << 2)
# print(a >> 2)

# print("assignment operators:")
# a += 5
# print(a)
# a -= 5
# print(a)
# a *= 2
# print(a)
# a /= 2
# print(a)
# a %= 3
# print(a)
# a **= 2
# print(a)
# a //= 2
# print(a)

# print("type conversion:")
# a = "2"
# b = int(a)
# print(b)

# a = 10
# b ="23"
# c = int(b)
# print(type(c))
# print(a + c)

# a, b = 10, "20"
# b = int(b)
# print(a + b)

# a = "Isha"
# b = "Rane"
# print(a + b)


# a = 1000
# b = str(a)
# print(type(b), b)

# a = 10.56
# b = int(a)
# print(b,type(b))


# num = int(input("Enter a number: "))
# print(num)
# print(type(num))

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print("addition is :",a + b)
# print("subtraction is :",a - b)
# print("multiplication is :",a * b)
# print("division is :",a / b)

# print("total Average")
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# total = a + b + c
# print("Total is :", total)
# average = total / 3
# print("Average is :", average)

# str ="day3 of python"
# str ="python"
# print(str[1])
# print(str[-2])

# str ="my programming"
# print(str[4])
# print(str[-3])

# str ="python" + "programming"
# print(str)

# str1 ="Hello"
# str2 ="World"
# str3 = str1 + " " + str2
# print(str3)

# str ="string repetition"
# str ="hello"
# str1 =str*2
# print(str1)

# str ="membership operator(in, not in)"
# str ="python"
# print("py" in str)

# str ="slicing operator"
# str ="python"
# print(str[2:4:1])
# print(str[2:5:2])

# str ="my programming language"
# print(str[2:14:1])
# print(str[2:10:1])
# print(str[14:18:1])
# print(str[-8:-4:1])
# print(str[-19:-8:1])
# print(str[-20:-14:1])

# str ="string formatting,f sting, .format()"
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# grade = input("Enter your grade: ")
# # print("my name is",name,",age is",age,",grade is",grade)
# print(f"My name is {name},and age is {age},and grade is {grade}")

# name =input("Enter your name: ")
# age =input("Enter your age: ")
# grade =input("Enter your grade: ")
# print("My name is {}, age is {}, grade is {}".format(name,age,grade))

# str ="methods and functions"
# str ="Python"
# print(len(str))
# print(str.upper())
# print(str.lower())
# print(str.title())
# str ="python"
# str1 ="123"
# roll ="prime123"
# print(str.isalpha())
# print(str1.isdigit())
# print(roll.isalnum())

# str ="My Programming Programming Language"
# str1 ="   hello    world   "
# print(str.find("Program"))
# print(str.count("m"))
# print(str.count("a"))
# print(str.replace("Programming","Best"))
# print(str1.strip())

# str ="python"
# print(str[::-1])
# print(str[::-])
# str ="my programming language"
# print(str[::-1])
# print(str[-1:-9:-1][::-1])
# print(str[-10:-20:-1][::-1])
# print(str[-21:-24:-1][::-1])

# str ="python"
# rev =str[::1]
# print(rev)
# word =rev[0:8][::-1]
# print(word)

# if-else example
# age =eval(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# if-elif-else example
# print("1.tea 2.coffee 3.cold drink 4.biscuit 5.milkshake")
# order =eval(input("Enter your order number: "))
# if order == 1:
#     print("You have ordered tea.")
# elif order == 2:
#     print("You have ordered coffee.")
# elif order == 3:
#     print("You have ordered cold drink.")
# elif order == 4:
#     print("You have ordered biscuit.")
# elif order == 5:
#     print("You have ordered milkshake.")
# else:
#     print("Invalid order number.")

# nested if-else example
# username ="Admin"
# password ="1234"
# if username == "Admin":
#     if password == "1234":
#         print("Login successful.")
#     else:
#         print("Incorrect password.")
# else:
#  print("Invalid username.")

# username =input("Enter username: ")
# password =input("Enter password: ")
# if username == username:
#     if password == password:
#         print("Login successful.")
#     else:
#         print("Incorrect password.")
# else:
#     print("Invalid username.")

# Accept marks and attendance percentage of a student and decide:
# Pass or Fail
# If passed, display Grade A, B, or C based on marks
# marks = eval(input("Enter marks obtained: "))
# attendance = eval(input("enter the attendance percentage:"))
# if marks >= 40 and attendance >= 75:
#     print("You have passed the exam.")
#     if marks >= 75:
#         print("Grade A")
#     elif marks >= 60:
#         print("Grade B")
#     else:
#         print("Grade C")
# else:
#     print("You have failed the exam.")

    
# Accept three sides of a triangle and determine:
# Whether a triangle is valid
# If valid, identify its type (equilateral, isosceles, scalene)
# side1 = eval(input("Enter side 1: "))
# side2 = eval(input("Enter side 2: "))
# side3 = eval(input("Enter side 3: "))
# if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 >side1):
#     print("The triangle is valid.")
#     if side1 == side2 == side3:
#         print("The triangle is equilateral.")
#     elif side1 == side2 or side1 == side3 or side2 == side3:
#         print("The triangle is isosceles.")
#     else:
#         print("The triangle is scalene.")
# else:
#     print("The triangle is not valid.")

    
# Accept account balance and withdrawal amount:
# Check sufficient balance
# Validate withdrawal amount rules
# Display transaction status
# balance = eval(input("Enter account balance: "))
# withdrawal = eval(input("Enter withdrawal amount: "))
# if withdrawal <= balance:
#     if withdrawal % 100 == 0 and withdrawal <= 10000:
#         balance -= withdrawal
#         print("Transaction successful. New balance is:", balance)
#     else:
#         print("Invalid withdrawal amount. Must be multiple of 100 and not exceed 10,000.")
# else:
#     print("Insufficient balance.")



# Online Exam Result System
# Accept:
# Total marks
# Negative marks
# Time taken
# Decide:
# Pass / Fail
# Distinction / First Class / Second Class
# Invalid attempt if rules are violated
# total_marks = eval(input("Enter total marks obtained: "))
# negative_marks = eval(input("Enter negative marks: "))
# time_taken = eval(input("Enter time taken (in minutes): "))
# if negative_marks <= total_marks * 0.3 and time_taken <= 180:
#     net_marks = total_marks - negative_marks
#     if net_marks >= 90:
#         print("Distinction")
#     elif net_marks >= 75:
#         print("First Class")
#     elif net_marks >= 50:
#         print("Second Class")
#     else:
#         print("Fail")

# str ="day 4 of python"
# str ="loops in python"
# print("check even odd number")
# num = eval(input("enter the number:"))
# if num %2 ==0:
#     print("even number")
# else:
#     print("odd number")
    
# print("check the largest number among three numbers")
# num1 = eval(input("enter first number:"))
# num2 = eval(input("enter second number:"))
# num3 = eval(input("enter third number:"))
# if num1 > num2 and num1 > num3:
#     print("largest number is:", num1)
# elif num2 > num1 and num2 > num3:
#     print("largest number is:", num2)
# else:
#     print("largest number is:", num3)

# print("check the given string is palindrome or not using if else statement")
# str = input("Enter a string: ")
# if str == str[::-1]:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

# print("range function example")
# for i in range (1,11,1):
#     print(i)

# num = eval(input("enter the number"))
# for i in range(0,num+1):
#     print(i)


# print("sum of n natural numbers")
# num =eval(input("enter the number:"))
# sum =0
# for i in range(num+1):
#     sum =sum +i
#     print("the sum is :",sum)

# num =eval(input("enter the number"))
# for i in range(num+1):
#     if i %2 ==0:
#         print("even number is :",i)
#     else:
#         print("odd number is :",i)

# print("table of 6 using for loop")
# num =6
# for i in range(1,11):
#     print(f"{num}*{i}={num*i}")
#     # print(num,"*",i,"=",num*i)

# print("factorial of a number using for loop")
# num =eval(input("enter the number:"))
# factorial =1
# for i in range(1,num+1):
#     factorial =factorial *i
# print(factorial)

#print("while loops examples")
#i =1 
#while i<=10:
#    print(i)
#     =i+1

# print("table of 6 using while loop")
# num =6
# while num <=60:
#     print(num)
#     num = num+6
    
# i =1
# while i <=10:
#     print(f"6*{i}={6*i}")
#     i = i+1
    
# i =1
# j =6
# while i<=10 and j<=60:
#     print(f"{j}={6*i}")
#     i = i+1
#     j = j+6

# print("sum of n natural numbers using while loop")
# num =eval(input("enter the number:"))
# sum =0
# i =1
# while i <=num:
#     sum =sum+i
#     i =i+1
# print(sum)

# print("factorial of a number using while loop")
# num =eval(input("enter the number:"))
# factorial =1
# i =1
# while i<=num:
#     factorial =factorial *i
#     i =i+1
# print(factorial)

# i =5
# for i in range(1,i+1):
#     print("*"*i)
# i = 1
# while i<=5:
#     print("*"*i)
#     i =i+1
# i =5
# while i>=1:
#     print("*"*i)
#     i =i-1
    
# i =5
# for i in range(5,0,-1):
#     print("*"*i)

# print("break , continue and pass statement examples")
# for i in range (1,11):
#     if i == 5:
#         break
#     print(i)
    
# for i in range(5,16):
#     if i%2==0:
#         continue
#     print(i)

# for i in range(1,10):
#     if i ==5:
#         pass
#     else:
#         print(i)

# print("non-primitive data types: list, tuple, set, dictionary")
# print("list examples")
# my_list =["apple","chickoo","cherry",1,89,3.14]
# print(my_list)
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])
# print(my_list[5])
# my_list.append("cricket")
# print(my_list)
# my_list.insert(3,12.09)
# print(my_list)
# my_list.insert(-2,"cat")
# print(my_list)

# n1 =[70,80,90]
# my_list.extend(n1)
# print(my_list)

# list1 =[1,2,3,4,[10,20,30],90,100,[2,4,6,8],100,200]
# list2 =[1,2,3,4,5]
# print(list1)
# print(list1[-3])
# print(list1[4])
# print(list1[4])
# list1[-3].append(80)
# print(list1[-3])
# list1[4].append("append")
# print(list1[4])
# list1[-3].insert(2,"hockey")
# print(list1[-3])
# list1[-3].extend(list2)
# print(list1[-3])
# print(list1)
# list1[-3].remove("hockey")
# print(list1)
# list1 =[1,2,3,4,5,6,7,8,9,10]
# print(list1)
# list1.remove(5)
# print(list1)
# list1.pop()
# print(list1)
# list1.clear()
# print(list1)

# day5 of python
# list1 =[10,20,30,40,20,40,10,50]
# print(list1)
# unique =list(set(list1))
# print(unique)
# print(sum(list1))
# print(max(list1))
# print(len(list1))

# print(type(list1))
# tuple1 = (10,20,30,40,50)
# print(tuple1)
# print(type(tuple1))
# set1 ={1,2,3,4,5,3,4}
# set2 ={6,7,8,4,9,10}
# print(set1)
# print(set2)
# print(set1.union(set2))
# print(set1|set2)
# print(set1 & set2)

# print(type(set1))
# dictionary1 ={"name":"Isha","age":21,"city":"Pune"}
# dictionary2 ={"name":"sakshi","marks":85}
# print{}
# print(dictionary1)
# print(dictionary1.keys())
# print(dictionary1.values())
# print(type(dictionary1))

# count the occurrence of element in the list
# list1 =[10,20,30,30,46,34,20,46]
# num =20
# count =0
# for i in list1:
#     if i == num:
#         count +=1
# print(count)

# prime number or not
# num =eval(input("enter the number:"))
# if num <=1:
#      print("not a prime number")
#     
# else:
#     for i in range(2,num):
#         if num % i ==0:
#             print("not a prime number")
#             break
#         else:
#             print("prime number")

# prime number using flag
# num =eval(input("enter the number:"))
# flag =0
# if num <=1:
#      print("not a prime number")
# else:
#     for i in range(2,num):
#         if num % i ==0:
#             flag =1
#             break
#     if flag ==1:
#         print("not a prime number")
#     else:
#         print("prime number")

# prime number
# n=int(input("enter the number:"))
# flag =0
# for i in range(2,n):
#     if n%i==0:
#         flag=1
#         break
# if flag==0 and n>1:
#     print("prime number")
# else:
#     print("not a prime number")

# fabanacci series
# n =0
# m =1
# terms =eval(input("enter the number of terms:"))
# print(n)
# print(m)
# for i in range(2,terms):
#     c = n + m
#     print(c)
#     n = m
#     m = c

# fibonacci series using  for loop
# num = int(input("enter the number:"))
# n1 =0
# n2 =1
# print(n1)
# print(n2)
# for i in range(2,num):
#     n3 = n1 + n2
#     print(n3)
#     n1 = n2
#     n2 = n3
    
# num = int(input("enter the number:"))
# n1 =0
# n2 =1
# sum =0
# for i in range(0,num):
#     n1=n2
#     n2=sum
#     print(sum)
#     sum = n1 + n2

