"""Given S = "aabbb", the function should return True.
2. Given S = "ba", the function should return False.
3. Given S = "aaa", the function should return True. Note that 'b' does not need to occur in S.
4. Given S = "b", the function should return True. Note that 'a' does not need to occur in S.
5. Given S = "abba", the function should return False."""

# def ab_first_check(S):
#     b_present = False
#     for i in S:
#         if i == 'b':
#             b_present = True
#         elif i == 'a' and b_present:
#             return False
#     return True

"""
upgraded version 
Examples:

Given S = "aaabbbccc", the function should return True because all 'a's come before all 'b's, and all 'b's come before all 'c's.
Given S = "aabbcca", the function should return False because there is an 'a' after 'c', which violates the order.
Given S = "abc", the function should return True.
"""

def check_character_order(S):
    dict_of_char_with_numbers = {chr(ord('a') + i) : i+1 for i in range(26)}
    maximum_character = 0
    for char in S:
        number = dict_of_char_with_numbers[char]
        if number < maximum_character:
            return False
        else : 
            maximum_character = number
    return True
print(check_character_order('aabbccdda'))