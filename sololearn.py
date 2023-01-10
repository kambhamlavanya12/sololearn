# convert to float
# height = float(input())
# print(height) 

# x = 9.34
# y = int(x)
# print(y)
# string
# age = 42
# print("His age is " + str(age)) 
# a = 5
# b = 9
# x = str(a)
# y = str(b)
# print(x+y)
# Multi Inputs:
# The last thing to mention is that you can use input() multiple times to take multiple user inputs.

# For example:

# name = input()
# age = input()

# print(name + " is " + age) 
# 
# In-Place Operators
# In-place operators let you write code like 'x = x + 3' more concisely, as 'x += 3'.

# Check it out:

# x = 2
# print(x)

# x += 3
# print(x)


# x = 4
# x *= 3
# print(x)

# In-Place Operators
# In-place operators can be used for any numerical operation (+, -, *, /, %, **, //)

# Some examples:

# x = 8
# x -= 2
# print(x)
# x /= 3
# print(x)
# x **= 5
# print(x)

# x = 9
# x %= 2
# x += 3
# print(x)
# In-Place Operators
# You can also use in-place operators for string concatenation:

# x = "spam"
# print(x)
# x += "eggs"
# print(x)
# x = "a"
# x *= 3
# print(x)

# spam = "7"
# spam = spam + "0"
# eggs = int(spam) + 3
# print(float(eggs))




# What's the output of this code if the user enters '42' as input:

# age = int(input())
# print(age+8)



#  x = 5
#  y = x + 3
#  y = int(str(y) + "2")
# print(y)

# x = 3

# num = 17

# print(num % x)
# bill=int(input(50*20/100))
# print(bill)
# Booleans 
# We can create Booleans by comparing values, by using the equal operator ==. Like this:

# my_boolean = True
# print(my_boolean)
# True

# print(2 == 3)
# False

# print("hello" == "hello")
# True



# 
# if Statements
# One thing you can do with Booleans is use if statements to run code based on a certain condition, say, if the Boolean evaluates to True.

# An if statement looks like this:
# if condition:
    # statements
# spam = 7

# if spam > 5:

#    print("five")

# if spam > 8:

#    print("eight")
#  
# x = 'a'
# if(x < 'c'):
#     x += 'b'
# if(x > 'z'):
#     x += 'c'
    
# print(x)
# if 1 + 1 == 2:

#    if 2 * 2 == 8:

#       print("if")
# else:
#       print("else")
# Boolean Logic
# Now it’s time to level up our Booleans with some operators, which allow us to combine multiple conditions.

# Let’s start with the and operator. It is True, if both conditions evaluate to True :

# print(1 == 1 and 2 == 2)
# True
# print(1 == 1 and 2 == 3)
# False
# print(1 != 1 and 2 == 2)
# False
# print(2 < 1 and 3 > 6)
# False
# if (1 == 1) and (2 + 2 > 3):

#   print("true")

# else:

#   print("false")

# if not True:

#    print("1")

# elif not (1 + 1 == 3):

#    print("2")

# else:

#    print("3")/
# (hour > 12 and day <= 15) or (hour < 10)
# i = 1
# while i <= 5:
#     print(i)
#   i = i + 1

# i = 3

# while i>=0:

#    print(i)

#    i = i - 1
# x = 1
# while x < 10:
#   if x%2 == 0:
#     print(str(x) + " is even")
#   else:
#     print(str(x) + " is odd")

#   x += 1
# x=1

# while x==1:

#    print("In the loop") 
# i = 5

# while True:

#   print(i)

#   i = i - 1

#   if i <= 2:

#     break
# i=0

# while True:

    # i+=1

    # if(i == 2):

    #     continue

    # if(i == 5):

    #     break

    

    # print(i)
#     while False:

#   print("Looping...")
# while False:

#     print("Looping...")
# i = 0

# x = 0

# while i < 4:

#     x+=i

#     i+=1



# print(x)
# x = int(input())

# if x > 5:

#     if x < 8:

#         print(x+1)

#     else:

#         print(x-1)

# else:
w=int(input())
h=float(input())
bmi=(w/(h**2))
 
while bmi<18.5:
     print("Underweight")
     break
     while bmi>18.5:
         print("Normal")
         break
         while bmi>30.0:
             print("Obesity")
             break
