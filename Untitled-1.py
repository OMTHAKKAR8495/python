,# python codes 

# print("hello i have started learning the python")
# print("my self om thakkar","i have started my journey to learn python with apna college on the date:03/06/2025")
# print(2025)


# name ="om"
# age=35
# price=25.99
# print(type(name))
# print(type(age))
# print(type(price))
  

# x=5
# y="hello world!"
# print(x)
# print(y)


# x="om"
# print(x)
# x='rushil'
# print(x)

# a=4
# print(A)


# print('hello','world')

# a=5
# A=10
# print(a)
# print(A)


# arithmetic operator
# print(34+5)
# print(2*3)
# print(4/2)
# print(10-5)
# print(10**2)#a^b

# relational operator
# a=50
# b=20
# print(a!=b)

# assigment operator 
# num =10
# num+=5
# print("num:",num)

# not operator
# a=50
# b=20
# print(not False)
# print(not (a>b))

# input("enter your name:")
# int("25")
# val=int(input("enter some values:"))
# print(type(val),val)

# name=input("enter mame:")
# age=input("enter age:")
# marks=input("enter marks:")

# print("welcome",name)
# print("age",age)
# print("marks",marks)


# write a program to input 2 numbers & print their sum.
# first= int(input("enter 1st :"))
# second=int(input("enter 2nd :"))
# print("sum=",first+second)

# write a program to input side of square & print its area
# side=int(input("enter square side:"))
# print("area=",side*side)


# print two float numbers and show their average.
# a=float(input("enter first:"))
# b=float(input("enter second:"))
# print("avg=",(a+b)/2)


# wap to input 2 int number,a and b.print True if a >=b. if not print false.
# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# print(type(a>=b))

# a=10
# b=20
# print(type(a))
# print(type(b))

# a=10
# b=20
# sum=a+b
# print("sum is:",sum)


# to check maximum numbers
# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# if a>b:
#     print("maximum is",a)
# else:
#     print("maximum is",b)



# # to make simple calculator
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# op = input("Enter operator (+, -, *, /): ")

# if op == "+":
#     print("Result:", num1 + num2)
# elif op == "-":
#     print("Result:", num1 - num2)
# elif op == "*":
#     print("Result:", num1 * num2)
# elif op == "/":
#     if num2 != 0:
#         print("Result:", num1 / num2)
#     else:
#         print("Error: Division by zero")
# else:
#     print("Invalid operator")


# Program to calculate the factorial of a number using Python
# num = int(input("Enter a number: "))
# factorial = 1

# if num < 0:
#     print("Factorial does not exist for negative numbers")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1, num + 1):
#         factorial *= i
#     print(f"The factorial of {num} is {factorial}")


# swapping of two numbers
# a=5
# b=10
# a,b=b,a
# print("after swap:a=",a,"b=",b)

# Addition of strings and finding their length
# str1="apna"
# len1=len(str1)
# print(len1)

# str2="college"
# len2=len(str2)
# print(len2)

# final_str=str1+str2
# print(final_str)

# str="apna_college"
# print(str[:3])
# print(str[:7])

# str="MY SELF OM THAKKAR"
# print(str[-5:-1])


# str1="i am studying in gsfc college.\ni am a boy."
# # str2="i am studying in shree narayan vidhyalay. i am going by car."
# # print(str1.capitalize())
# # print(str2.capitalize())
# # print(str2.replace("am","was"))
# # print(str1.find("am"))#2
# # print(str2.find("in"))#10
# print(str1.count("i"))
# print(str2.count("am"))
# print(str1)

# wap to input users first name and print its length.
# name=input("enter your name:")
# print("length of your name:",len(name))

# wap to find the apperance of "$" in string
# str="i am $ my amount is $99.99 and i am a american$ amount."
# print(str.count("$"))


# conditional statements:
# light="pink"
# if(light=="red"):
#     print("stop")
# elif(light=="green"):
#     print("we can go...")

# elif(light=="yellow"):
#     print("wait for light to green")
# else:
#     print("light is broken")

# num=5
# if(num >10):
#     print("number grater than 5")
# elif(num > 2):
#     print("number greater than 5")
# here if statement is false than elif use to check the condition and "if"statement is true than elif dont check the statement.


# program to number is even or odd using if else condition:
# num=int(input("enter a number"))
# rem=num%2
# if(rem==0):
#     print("even")
# else:
#     print("odd")

# wap to find gretaest of 3 numbers enterd by the user.
# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# c=int(input("enter third number:"))
# if(a>=b and a>=c):
#     print("first number is greatest",a)
# elif("b>=c"):
#     print("second number is greatest",b)
# else:
#     print("third is largest",c)
    

# wap to check the number is multiple of 7 or not.
# num=int(input("enter a number:"))
# rem=num%7
# if(rem==0):
#     print("multiple of 7")
# else:
#     print("not a  multiple of 7")

# marks=[94.4,95.2,62.2,45.1]
# print(type(marks))
# print(marks)
# print(marks[0])
# print(marks[1])
# print(len(marks)) 

# strings codes
# student=["karan",95.4,17,"new delhi"]
# print(student)
# # print(student[0])
# student[0]="arjun"
# print(student)
# string is immutable(can't change  the assign value)
# list is mutable(can change the assign values)


# # # sring slicing
# marks=[23,34,45,67]
# print(marks[0:5])


# list method
# *append method(add the value at last:)
# list=[2,1,3,4,6,8,9,7,5,10]
# print(list.sort(reverse=True))
# print(list)
# print(list.sort())
# print(list)


# list=["apple","banana","lichi"]
# print(list.sort(reverse=True))  #descending order
# print(list)
# print(list.append("mango"))  #add mango at last
# print(list)
# print(list.sort())
# print(list)


# list=['a','b','c','d','e','f','g']
# list.reverse()
# print(list)

# list=[1,2,4,3]
# list.remove(1)
# # print(list)
# list.pop(3)
# print(list)

# tuple=(12,34,45,56)
# print(type(tuple))

# tup=(2,3,1,4,1,5,1,6,2,1)
# print(tup.index(1))
# print(tup.count(1))

# movie = []
# name1=input("first movie name:")
# name2=input("second movie name:")
# name3=input("third movie name:")
# movie.append(name1)
# movie.append(name2)
# movie.append(name3)
# print(movie)


# str=[1,2,3,1,3,1,3,4]
# print(str.count(1))
# print(list.count(1))
# print(list.count(3))


# to check number is palindrome or not
# list1=[1,2,1]
# list2=[1,2,3]

# copy_list1=list1.copy()
# copy_list1.reverse()

# if(copy_list1==list1):
#     print("palindrome")
# else:
#    print("not palindrome") 



# grade=["c","d","a","a","b","b","a"]
# grade.sort()
# print(grade)

# dict={
#     "name" : "shradha",
#     "cgpa" : "9.5", 
#     "age":35,
#     "marks":[34,45,67,78,99,89],
#     "topics":("dict","set"),
#     "is_adult":True,
# }
# print (dict["name"])
# print (dict["cgpa"])
# print (dict["marks"])
# print (dict["age"])
# print (dict["topics"])
# print (dict["is_adult"])

# dict["name"]="om"
# dict["surname"]="thakkar"
# print(dict)

# student={
#     "name":"om thakkar",
#     "subjects":{
#     "phy":97,
#     "chem":98,
#     "maths":99,
#     "english":89,
#     }
# }
# print(student.keys())

X="5"
Y="BANANA"
#Z="MANGO"
print(X)
print(Y)
# print(Z)

print("hello world")


