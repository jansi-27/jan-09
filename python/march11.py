# def check_inc_order(input_num):
#     temp = input_num
#     prev_digit = 10
#     while temp > 0:
#         digit = temp % 10
#         if digit >= prev_digit:
#             return False
#         prev_digit = digit
#         print(digit)
#         temp //= 10
#     return True


# list1 = [123, 341, 566, 223, 11]
# print(check_inc_order(454))

# list1 = [1, 2, 3, 4, 6, 8]
# def bin_search(list1, search_elem):
#     low = 0
#     high = len(list1) -1
#     flag = False
    
#     while low <= high:
#         mid = (low + high) // 2
#         if list[mid] == search_elem:
#             return mid
#         elif list1[mid] > search_elem:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return -1


list1 = [2, 1, -3, 55, 4.7, -32, 77, -89]

for j in range(len(list1) -1):
    for i in range(len(list1)-1):
        if list1[i]  list1[i + 1]:
            list1[i], list1[i + 1] = list[i + 1], list1[i]
    print(list1)              
        


