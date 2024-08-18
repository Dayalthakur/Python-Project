# Print First 10 natural numbers using while loop
for i in range(10):
    print(i)


# Write a program to print the following number pattern using a loop.
#   1
#   1 2
#   1 2 3
#   1 2 3 4
#   1 2 3 4 5
num=int(input("Enter no."))
for i in range(num):
    for j in range(i+1):
        print(j+1,end=" ")
    print()


# Calculate the sum of all numbers from 1 to a given number
num=int(input("Enter the number:"))
sum=0
for i in range (1,num+1):
    sum+=i
print(sum)


# Write a program to print multiplication table of a given number
for i in range(1,11):
    multi=num*i
    print(multi)


# Display numbers from a list using loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)


# Count the total number of digits in a number
count=0
while num>0:
    num=num//10
    count+=1
print(count)


# Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
for i in range(len(list1)-1,-1,-1):
    print(list1[i])


# Display numbers from -10 to -1 using for loop
for num in range(-10, 0, 1):
    print(num)


# Display Fibonacci series up to 10 terms
n=int(input("Enter number"))
for i in range (0,n):
    for j in range(0,i):
        print("*",end=" ")
    print()