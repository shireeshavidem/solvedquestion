# lst = [1,2,1,3,4,1]
# lst2 = []
# for i in lst:
#     if i not in lst2:
#         lst2.append(i)
# print(lst2)  
# k = input("Enter a key: ")
# dic = {1:2, 2:3}
# if k == dic.keys():
#     print("already exists")
# else:
#     print(k)    

# a = [1,3,4,6,7,8]

# a.sort()
# a.reverse()
# print(a[0],a[1])
# total_sum = sum(dic.values())
# print(total_sum)
age = 20
print(age,  'is my age')

l = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]

u = []
d = []
for i in l:
    if i not in u:
        u.append(i)
    elif i not in u:
        d.append(i)


print(u)

print(d)

