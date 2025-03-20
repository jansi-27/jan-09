# 1.Sum and Difference:
# Question: Write a Python program to take two numbers as input and output their sum and difference.
# Example Input: 10, 5
# a = 10
# b = 5
# Sum_result = a + b
# Difference_result = a - b
# print("Sum:", Sum_result)
# print("Difference:", difference_result)

# Take two float numbers as input from the user, separated by a comma
input_numbers = input("Enter two float numbers separated by a comma: ")

# Split the input into two parts and convert them to float
a, b = map(float, input_numbers.split(","))

# Calculate the product
product_result = a * b

# Calculate the division
division_result = a / b

# Output the results
print("Product:", product_result)
print("Division:", division_result)