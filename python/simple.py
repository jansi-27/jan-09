# details={"name":"Jansi Valluri",
#          "age":"20",
#          "gender":"female",
#          "Qualificatiom":"BCA",
#          "University":"Adikavi Nannaya University",
#          "skills":"python",
#          "email":"jansivalluri27@gmail.com",
#          "single":"True",
#          "Address":"Rajahmumdry"}
# print(type(details))
# print(details["name"])
# print(details["single"])
# print(details["skills"])
# print(details["University"])


# def add_number(x, y):
#     return x + y
# print(add_number(5, 4))



# def find_max(*args):
#     return max(*args)
# result = find_max(15, 26, 6, 47, 39, 29)
# print(result)

# def check_or_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"   
# print(check_or_odd(28)) 
    
# def sum_of_digits(n):
#     total = 0
#     while n > 0:
#         total += n % 10
#         n //= 10 
#     return total

# print(sum_of_digits(12345))



def swap_key_value(d):
    swapped = {v: k for k, v in d.items()}
    keys_list = list(swapped.keys())
    return swapped , keys_list
d = {'a':1, 'b':2, 'c':3}
swapped_dict, keys = swap_key_value(d)
print("swapped dictionary:",swapped_dict)
print("keys list:",keys)





# dict1 = {'1':2, 'str':4, '55':12, 'apple':11}
# max_value= float('-inf')
# max_key= ''
# for i,j in dict1.items():
#     if j > max_value:
#         max_value = j
#         max_key = i
        
# if max_value != float('-inf'): 
#     print(max_key)
    
# else:
#     print("dictionary is empty so no max key")

def merge_dict(d1, d2):
    merged = d1.copy()
    for key, value in d2.items():
        merged[key] = merged.get(key, 0) + value
        return merged 
d1 = {'a': 10, 'b':20, 'c':30}
d2 = {'b': 5, 'c': 15, 'd': 25}
print("merged dictionary:", merge_dict(d1,d2))

