# Control Statements (if-else, match-case)
# Write a Python program to check if a number is positive, negative, or zero.
# n = int(input("enter a number:"))
# if n > 0:
#     print("positive")
# elif n < 0:
#     print("negative")
# else:
#     print("zero")

# Write a Python program to find the largest of three numbers.
# a = 10
# b = 4
# c = 20
# if a >= b and a >= c:
#     print ("a is large")
# elif b >= a and b >= c:
#     print ("b is large")
# else:
#     print(" c is larger")

# Write a program to check whether a given year is a leap year or not.
# year = 2025
# if (year % 4 == 0 and  year % 100 != 0) or ( year % 400 == 0):
#     print(f"{year} it  is a leap year")
# else:
#     print(f"{year} is  not a leap year")

# Write a Python program to check if a number is even or odd.
# n = 78
# if n % 2 == 0:
#     print("even")
# else:
#     print("odd")

# Write a program to determine whether a character is a vowel or consonant.
# char = "v"
# if char == "a" "e" "i" "o" "u":
#     print("vowel")
# else:
#     print("consonent")

# Write a program to check whether a person is eligible to vote (age >= 18). 
# age = int(input("Enter your age:"))
# if age >= 18:
#     print("eligible to vote")
# else:
#     print("not eligible to vote")

# Write a Python program to find the greatest of two numbers using an if-else statement.
# a = 20
# b = 30
# if a >= b and b >= a:
#     print("greatest")
# else:
#     print("smallest")


# Loops (for, while)
# Write a Python program to print numbers from 1 to 10 using a for loop.
# for i in range (1, 11):
#     print(i)

# Write a Python program to print numbers from 10 to 1 using a while loop.
# i = 10
# while i > 0:
#     print(i)
#     i -= 1

# Write a program to calculate the sum of the first 20 natural numbers using a loop
# total = sum(range(1, 21))
# print(f"sum:{total}")

# for i in range(1, 21):
#     sum = sum =+ i
#     print(sum)


# 1. Print numbers from 1 to 10 but stop when you reach 5 (using break).
# for i in range (1, 11):
#     if i == 5:
#         break
#     print(i)

# 2. Print numbers from 1 to 10 but skip 5 using continue.
# for i in range (1, 11):
#     if i == 5:
#         continue
#     print(i)

#  Display the Fibonacci series up to n terms.
# n = int(input("enter a num of terms:"))
# a , b = 0, 1
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# 6. Print all prime numbers between 1 and 100.
for num in range(2, 101):
    if all (num % i  != 0 for i in range(2, int(num**0.5) +1)):
        print(num, end=" ")



