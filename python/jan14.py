
# 15/01/2025
# 1.Write a program to accept a string from the user and print its reverse.
# Example Input: "hello"
# Expected Output: "olleh"
# s = "hello"
# print("Reversed string:", s[::-1])


# 2.Write a program to check if a given string is a palindrome.
# Example Input: "madam"
# Expected Output: "Palindrome"
# word = "madam"
# if word == word[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")
    
# 3.Write a program to count the number of vowels and consonants in a given string.
# Example Input: "education"
# Expected Output: Vowels: 5, Consonants: 4
# def count_vowels_and_consonents(s):
#     vowels = "aeiouAEIOU"
#     vowel_count = 0
#     consonant_count = 0
#     for char in s:
#         if char.isalpha():
#            if char in vowels:
#                vowel_count += 1
#         else:
#             consonant_count += 1
#     return vowel_count, consonant_count
# input_string = "education"
# vowels, consonants = count_vowels_and_consonents(input_string)
# print(f"Vowels: {Vowels}, Consonents: {consonants}")

# 4.Write a program to accept a string from the user and display its length without using the len() function.
# Example Input: "Python"
# Expected Output: 6
# s = ("python")
# length = len(s)
# print(f"the length of the string is : {length}")

# 5.Write a program to remove all spaces from a user-provided string.
# Example Input: "Hello World"
# # Expected Output: "HelloWorld"
# s = "Hello World"
# no_spaces = s.replace(" ", "")
# print(f"String without spaces: {no_spaces}")

def check_substring(string, substring):
    if substring in string:
        print("Yes, it's a substring")
    else:
        print("No, it's not a substring")

# Example usage
string = "programming"
substring = "gram"
check_substring(string, substring)


def count_character(string, char):
    count = string.count(char)
    print(count)

# Example usage
string = "banana"
char = "a"
count_character(string, char)




def swap_case(string):
    swapped = string.swapcase()
    print(swapped)

# Example usage
string = "Python123"
swap_case(string)

def swap_case(string):
    swapped = string.swapcase()
    print(swapped)

# Example usage
string = "Python123"
swap_case(string)



def replace_word(string, old_word, new_word):
    updated_string = string.replace(old_word, new_word)
    print(updated_string)

# Example usage
string = "I love Python"
old_word = "Python"
new_word = "coding"
replace_word(string, old_word, new_word)
