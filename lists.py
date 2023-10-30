# li = []
# n = int(input("Enter length of the lenth: "))
# for i in range(0,n):
#    li1 = input("Enter your elememts: ")
#    li.append(li1)
# ele = input("enter element you want to check: ")   
# if ele in li:
#         print("true")
# else:
#         print("false")    


# flowers = []
# colors = []
# n = int(input("Enter length of the lenth: "))
# for i in range(0,n):
#     flowers1 = input("Enter the flower name: ")
#     color1 = input("Enter the flowers color: ")
#     flowers.append(flowers1)
#     colors.append(color1)
# z = zip(flowers,colors)
# for flowers,colors in z:
#     print("%s is in %s color" %(flowers,colors))


#interchanging first and last element in list
list = []
n = int(input("Enter length of the lenth: "))
#1
# def interchangelist(list):
for i in range(0,n):
    list1 = input("Enter your elements: ")
    list.append(list1)
#     size = len(list)    
#     temp = list[0]
#     list[0] = list[size-1]
#     list[size-1] = temp
#     return list
# print(interchangelist(list))

#2
# def change(list):
#     list[0],list[-1] = list[-1],list[0]
#     return list
# print(change(list))

#3
# def change(list):
#     get = list[0],list[-1]
#     list[-1],list[0] = get
#     return list
# print(change(list))

#4
# def change(list):
#     start,*middle,end = list
#     list = end,*middle,start
#     return list
# print(change (list)) 
 
#5
# def interchangelist(list):
#     if len(list) >= 2:
#         list = list[-1:] + list[1:-1] + list[:1]
#     return list
# print(interchangelist(list))

#program to swap 2 elements in a list
def swap_ele(list):
    pos1,pos2 = input("pos1","pos2")
 