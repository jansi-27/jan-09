# def find_missing(input_num):
#     temp = input_num
#     digit_list = []
#     while temp > 0:
#         digit = temp % 10
#         digit_list.append(digit)
#         temp //= 10
#     list_max = max(digit_list) 
#     list_min = min(digit_list)  
    
    
#     for i in range(list_min, list_max + 1):
#         if i not in digit_list:
#             print(i) 
#     return
# num1 = 34571
# find_missing(num1)  



# def missing_even_numbers(num_lsit):
#     even_numbers = [num for num in num_list if num % 2 == 0]
#     if len(even_numbers) < 2:
#         return
#     min_even = min(even_numbers)
#     max_even = max(even_numbers) 
#     missing_evens = [i for i in range(min_even, max_even + 1, 2) if i not in even_numbers]
#     return missing_evens if missing_evens else "No missing even numbers."


# num_list = [-4, -2, 6, 10, 12]
# result = missing_even_numbers(num_list)
# print("Missing even numbers:", result) 



# given an array of n integer, the task is to replace each element of the array by its rank in the array
# input :[20 15 26 2 98 6] output:[4 3 5 1 6 2]
list1 = [20, 15, 26, 2, 98, 6]
temp1 = sorted(list1)
print(list1)
print(temp1)

output = []
for i in list1:
    res = temp1.index(i) + 1
    output.append(res)
print(output)
    
    
    
    
    
    
    
    
    
    
    
    
    
      