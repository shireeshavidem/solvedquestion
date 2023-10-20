# string = "shireesha"
# index = string[::-1]
# print(index)
# num = 12345
# rev = str(num)
# index = rev[::-1]
# print(index)

string = ("marolix technologies12345")
str = ("a","e","i","o","u")
emp = ""
# for i in string:
#     for j in str:
#         if i == j:
#             emp = emp+i
# print(emp)
# sum = 0
# for i in string:
#     if i.isdigit():
#         sum = sum + int(i)
# print(sum) 

for i in string:
    if i not in str:
        emp =emp+i
print(emp)   