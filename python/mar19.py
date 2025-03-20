# Swap keys and values of a dictionary. Store keys in a list.
# def swap_key_values(d):
#     swapped = {v: k for k, v in d.items()}
#     keys_list = list(swapped.keys())
#     return swapped, keys_list
# d = {'a': 1, 'b':2, 'c':3}
# swapped_dict, keys = swap_key_values(d)

# print("Swapped Dictionary:", swapped_dict)
# print("keys list:", keys)

# 6. Given a dictionary, find the key with the highest value.
# def max_key(d):
#     return max(d, key=d.get)

# d = {'a':10, 'b':20, 'c':5}
# print("key with the highest value:", max_key(d))



# Given a list of numbers, return a dictionary of elements 
# from collections import Counter
# def find_duplicates(list):
#     count = Counter(list)
#     return {k: v for k, v in count.items() if v > 1}
# list = [1, 2, 3, 4, 5, 2, 3, 3, 1,]
# print("duplicates counts:", find_duplicates(list))



# 8. Given two dictionaries, merge them into one. If a key exists in both, sum their values.
# def merge_dict(d1, d2):
#     merged = d1.copy()
#     for key, value in d2.items():
#         merged[key] = merged.get(key, 0) + value
#     return merged
# d1 = {'a': 10, 'b': 20, 'c': 30}  
# d2 = {'b': 5, 'c': 15, 'd': 25}
# print("merged dictionary:", merge_dict(d1, d2))

# 9. Find if 2 strings are anagrams outputs also and explanation of every single line

from collections import Counter
def are_anagrams(s1, s2):
    return Counter(s1) == Counter(s2)
s1 = "listen" 
s2 = "silent"
print("are anagrams:", are_anagrams(s1, s2))