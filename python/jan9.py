
# Take a number, calculate the sum of its digits, and find the average of the digits
# Example: n=1234

n = 12345
sum_digits = sum(int(digit) for digit in str(n))
avg_digits = sum_digits / len(str(n))

print("Sum:", sum_digits)
print("Average:", avg_digits)