# Arrange string characters such that lowercase letters should come first
str1=input("Enter the string : ")
upper=[]
lower=[]
for i in str1:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)
result=("").join(lower+upper)
print(result)


# Append new string in the middle of a given string
str1=input("ENter first string")
str2=input("Enter second string")
length=(len(str1)/2).__ceil__()
x=str1[:length]+str2+str1[length:]
print(x)


# Create a string made of the middle three characters
give=input("Enter the string:")
length=(len(give)/2).__ceil__()
fchar=length-1
lchar=length+1
print(f"{give[fchar-1]}{give[length-1]}{give[lchar-1]}")


# Count all letters, digits, and special symbols from a given string
str1=input("Enter the string : ")
alpha=0
number=0
symb=0
for i in str1:
    if i.isalpha():
        alpha+=1
    elif i.isdigit():
        number+=1
    else:
        symb+=1
print(f"The string \"{str1}\" consist of \n{alpha} = Alphabets \n{number} = Digits \n{symb} = Symbols")


# String characters balance Test
str1=input("Enter the string 1: ")
str2=input("Enter the string 2: ")
flag=0
for char in str1:
    if char not in str2:
        print("false")
        flag=1
        break
if flag==0:
    print("true")


# Calculate the sum and average of the digits present in a string
str1="htdh34$@#dfxgf34476898977"
count=0
sum=0
for i in str1:
    if i.isdigit():
        sum+=int(i)
        count+=1
print(f"The sum is {sum}")
print(f"The average is {sum/count}")


# Split a string on hyphens
str1="dayal-datta-thakur"
l=str1.split("-")
for i in l:
    print(i)


# Remove empty strings from a list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
for i in str_list:
    if i=="" or i==None:
        str_list.remove(i)

print(str_list)


# Remove special symbols / punctuation from a string
str1 = "/*Jon is @developer & musician"
str2=""
for i in str1:
    if i.isalpha():
        str2+=i
    if i==" ":
        str2 += i
print(str2)


# Removal all characters from a string except integers
str1 = 'I am 25 years and 10 months old'
str2=""
for i in str1:
    if i.isdigit():
        str2+=i
print(str2)


# Find words with both alphabets and numbers
str1 = "Emma25 is Data scientist50 and AI Expert"
lst=str1.split(" ")
for i in lst:
    if not i.isalpha() and not i.isdigit():
        print(i)


# Replace each special symbol with # in the following string
str1 = '/*Jon is @developer & musician!!'
str2=""
for i in str1:
    if i == " ":
        str2 += " "
    elif not i.isalpha():
        i="#"
        str2+=i
    else:
        str2+=i
print(str2)


