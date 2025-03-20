#  Find the Largest Number in a List
# numbers = [10, 25, 5, 99, 34]
# max_num = numbers[0]
# for num in numbers:
#     if num > max_num:
#         max_num = num
# print ("the largest number is :", max_num)

# numbers = [10, 25, 5, 99, 34]
# print("The largest number is:", max(numbers))
# numbers = [7, 3, 15, 2, 8]
# max_num = numbers[0]
# for num in numbers:
#     if num > max_num:
#         max_num = num
# print("the largest num is:", max_num)

# Write a Python program to reverse a string
# using slicing
# text = "python"
# reversed_text = text[::-1]
# print('reversed string:', reversed_text)

# using loop
# text = "Python"
# reversed_text = ""
# for char in text:
#     reversed_text = char + reversed_text
# print("reversed string", reversed_text)


# Check if a Number is Prime

# def fibonacci(n):
#     a, b  = 0,1
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b
# num = int(input("enter a number:"))
# fibonacci(num)

# Reverse a Number
num = 123456
reversed_num = num[::-1]
print("reversed num is:", reversed_num)
