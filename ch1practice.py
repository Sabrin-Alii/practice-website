#3. logical operators 
# age = 20
# print(age > 18 and age < 25 )
# print(age > 18 or age < 15)
# print(not(age > 20))

# 1. write a program that checks if a number is even or odd using 
# num =  int(input ("Enter a number:"))
# if num % 2 == 0:
#         print("Even")
# else:
#         print("Odd")

# # 2. compare two variables, a=15 and b = 20 print whether a is 
# # agreater,smaller, or equal.
# a = 15
# b = 20
# if a > b:
#     print("a is agreater")
# elif a < b:
#     print("a is smaller")
# else:
#     print("a is equal")

# 3. create a variables age = 17  and check if its between 13 and 19 (teenager)
# using and.

# age = 17
# print(age > 13 and age < 19)

# #4.use or to check if a number x = 10 is either less than 5 or greater than 15.
# x = 10
# print(x > 5 or x < 15)

#control flow practice
# while True:
#     password = input("Enter your password:")
#     if len(password) >= 8:
#         print("Strong password")
#         break
#     else:
#         print("Weak password, try again.")
# score = int(input("Enter your score: "))
# if score >= 90:
#     print("Grade A") 
# elif score >= 80:
#     print("Grade B")
# elif score >= 70:
#     print("Grade C")
# elif score >= 60:
#     print("Grade D")
# else:
#     print("Grade F")

# if score >= 60:
#     print("Pass")
# else:
#     print("Fail")

# fruits = ["apple", "banana","cherry"]
# for fruit in fruits:
#     print(fruits)

# while loop    
# count = 1
# while count <= 5:   
#     print("Count:", count)
#     count += 1

#practice tasks 
# 1. write  if/else program that checks if a person is old enough
#  to vote (18 or older).
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are old enough to vote.")
# else:
#     print("You are not old enough to vote.")
# # 2. print numbers from 1 to 10 using a for loop.
# for i in range(1, 11):
#     print(i)
# # 3.print numbers from 10 down to 1 using a while loop.
# count = 10
# while count >= 1:
#     print(count)
#     count -= 1
# # 4. loop through a list of 5 countries and print each country.
# countries = ["USA", "Canada", "Germany", "France", "Japan"]
# for country in countries:
#     print(country)
# # 5. write a program that asks user to enter a number and prints    
# # whether it is positive, negative, or zero.
# number = float(input("Enter a number: "))
# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else:
#     print("Zero")   

# functions

# def greet():
#     print("Hello, welcome to the data science!")

# greet()
# def add_numbers(a, b):
#     return a + b
# result = add_numbers(5, 10)
# print("Sum:", result)
       

# def greet(name = "Sabrina"):
#     print(f"Hello, {name}!" )

# greet()
# greet("Salma Qurux")


# lambda function
# add = lambda x, y: x+y
# print(add(5, 10))

# print((lambda x,y: x * y)(6, 7))

# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, numbers))
# print(squared)

# # filtering lambda
# numbers = [10, 15, 20, 25, 30]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)

#1. Write a function that takes two numbers and returns their product.
def multiply(a, b):
    return a * b
print(multiply(4, 5))
#2. Create a function is_even(num) that returns True if a number is even, else False.
def is_even(num):
    return num % 2 == 0
print(is_even(4))

#3. Write a function with a default parameter: welcome(name="User").
def welcome(name="cali"):
    print(f"Welcome, {name}!")
welcome()

#4. Use a lambda function to get the cube of a number.
cube = lambda x: x**3
print(cube(3)) 

