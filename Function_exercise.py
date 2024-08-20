# Create a function in Python
def name(name,age):
    print(name,age)

name("dayal",21)


# Create a function with variable length of arguments
def func1(*args):
    for i in args:
        print(i,end=",")

func1("dayal","yash","bhushan","shubham")


# Create a function with a default argument
def func1(name,salary=10000):
    print(name,salary)

func1("dayal")
func1("bhushan",50000)


# Create an inner function to calculate the addition in the following way,an outer function will add 5 into addition and return it
def func1(a,b):
    sum=0
    def addition(a,b):
        sum = (a + b)
        return sum
    sum=addition(a,b)
    print(sum+5)
func1(5,5)


# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10
def func1(num):
    if num:
        return num+func1(num-1)
    else:
        return 0
addition=func1(10)
print(addition)


# Assign a different name to function and call it through the new name
def display_student(name, age):
    print(name, age)
display_student("Emma", 26)
showStudent = display_student
showStudent("Ram", 26)


# Generate a Python list of all the even numbers between 4 to 30
def func1(start,end):
    lst=[]
    for i in range(start,end,2):
        lst.append(i)
    print(lst)
func1(4,30)
