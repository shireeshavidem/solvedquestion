# 1
# string = input("Enter your string: ")
# char = input("Enter the char: ")
# if char in string:
#     str=string.replace(char,"")
#     print(str)
# else: print("invalid char")

# dict = {ord(char):None}
# print(string.translate(dict))

# 2
# str = input("Enter a string: ")
# char = input("Enter a char: ")
# print(str.count(char))

# 3
# str1 = input("Enter string 1: ")
# str2 = input("Enter string 2: ")
# if sorted(str1)==sorted(str2):
#     print("Two strings are Anagram")
# else: print("Two strings are not Anagram: ")

# 4
# str = input("Enter the input: ")
# str1 = str[::-1]
# if str==str1:
#     print("given string is palindrome")
# else: print("given string is not palindrome")

# 5
# char = input("Enter a char: ")
# vowels = "aeiouAEIOU"
# consonant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
# if char in vowels:
#     print(f"{char} is vowel")
# elif char in consonant:
#     print(f"{char} is consonant")
# else: print("invalid char") 

# 6
# num = input("Enter a number: ")
# if num.isdigit():
#     print("digit")
# else: print("not digit")

# 7
# str = input("Enter string: ")
# vowels = "aeiouAEIOU"
# consonant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
# v_count = 0
# c_count = 0
# for i in str:
#     if i in vowels:
#         v_count += 1
#     elif i in consonant:
#         c_count += 1   
#     else: print("invalid char") 
# print(v_count, c_count)

# 8
# str = input("Enter your string:")
# dict = {}
# for i in str:
#     if i in dict:
#         dict[i] += 1
#     else: dict[i] = 1
# max_val = max((dict.values()))
# for i in dict:
#     if dict[i] == max_val:
#         print(i,end=' ')


str = input("Enter string: ")
def replace_vowel(str):
    vowels = "aeiouAEIOU"
    for i in range(len(str)):
        if str[i] in vowels:
            str = str[:i] + '-'+ str[i+1:]
            break
    return str    
print(replace_vowel(str))