# def add_number(a, b):
#     return a + b
# result = add_number(5, 3)
# print(result)

# def multiply_num(a, b):
#     return a * b
# result = multiply_num(3, 3)
# print(result)


# allows a fun to accept multiple positional arguements
# def sum_numbers(*args):
#     return sum(args)
# print(sum_numbers(1, 2, 4, 7))

# even or odd
# def is_even_or_odd(num):
#     if num % 2 == 0:
#         return f"{num} is Even"
#     else:
#         return f"{num} is Odd"
# print(is_even_or_odd(3))

# find sum of digits
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))
print(sum_of_digits(1234))