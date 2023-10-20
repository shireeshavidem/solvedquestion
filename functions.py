#getting the parameters list of methods
# import inspect
# #using inspect.signature() method
# import collections
# print(inspect.signature(collections.Counter))

# def fun(a,b):
#     return a**b
# print(inspect.signature(fun))

# print(inspect.signature(len))

# #using inspect.getfullargspec() method
# print(inspect.getfullargspec(collections.Counter))

# def fun(a,b):
#     return a**b
# print(inspect.getfullargspec(fun))

# print(inspect.getfullargspec(len))

#print multiple arguments in python
#simple argument
# def VS(name,num):
#      print("hello from",name+', '+num)
# # VS("videm shireesha","22")

#variable function argument
# def VS(name,num="22"):
#      print("hello from",name+', '+num)
# VS("videm shireesha")
# VS("videm shireesha","22")

#pass it as tuple
# def VS(name,num):
#     print("Hello from %s , %s"% (name,num))
# VS("videm shireesha","22")    

#pass it as dictionary
# def VS(name,num):
#     print("Hello from %(n)s ,%(s)s" %{'n':name,'s':num})
# VS("videm shireesha","22")

#using new style string formatting with number
# def VS(name,num):
#     print("Hello from {0} ,{1}". format(name,num))
# VS("videm shireesha","22")

#using new style string formatting with explicit names
# def VS(name,num):
#     print("Hello from {n} ,{r}". format(n=name,r=num))
# VS("videm shireesha","22")

#concatination strings
# def VS(name,num):
#     print("hello from " +str(name)+', '+str(num))
# VS("videm shireesha","22")    

#using new f-string formatting
# def VS(name,num):
#     print(f'Hello from {name} ,{num}')
# VS("videm shireesha","22")

#using *args
# def VS(*args):
#     for info in args:
#         print(info)
# VS(["Hello from","videm shireesha",22],["hello","VS",22])  

#using **kwargs (keywordsargs)
# def VS(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
# VS(name="videm shireesha",n="- 22")
# VS(name="best",n="- 2023") 

# numbers = []
# def max_of_num(numbers):
#     for i in range(0,3):
#         num = input("Enter your numbers: ")
#         numbers.append(num)
#     print(max(numbers))
# max_of_num(numbers)

# numbers = []
# sum = 0
# def sum_list(numbers,sum):
#     for i in range(0,3):
#         num = int(input("Enter your numbers: "))
#         numbers.append(num)
#     for j in numbers:
#         sum = sum + j
#     print(sum)
# sum_list(numbers,sum)

# program to print power of number.
# num = int(input("Enter your number: "))
# power = int(input("Enter the power: "))
# def mul(num,power):
#     result = num**power
#     print(result)
# mul(num,power)    

#above program using recursion method

# def power(N,P):
#     if P == 0:
#         return 1
#     return (N*power(N,P-1))
# if __name__ == '__main__':
#     N = 4
#     P = 3
#     print(power(N,P))

#for above recursion program we implement that 
# if power is even result=(func(N,p/2))^2
#if power is odd result = N*(func(n,(p-1)/2))^2

# def power(N,P):
#     if P == 0:
#         return 1
#     if P%2 == 0:
#         result = power(N,P//2)
#         return result*result
#     else:
#         result = power(N,(P-1)//2)
#         return N*result*result
# if __name__ == '__main__':
#     N = 4
#     P = 2 
#     print(power(N,P))

#sorting objects of user defined class
# print(sorted([4,5,2,8,4,1,2,5,3,2]))
# print(sorted("my Name is Siri".split(),key = str.lower))
#method 1
# class VS:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def __repr__(self):
#         return str((self.a, self.b))
# vs = [VS("My",2),
#       ("name",4),
#       ("Is",2),
#       ("siri",4)]
# print(sorted(vs, key=lambda x: x.b))        

# Python program to illustrate
# *args for variable number of arguments
# def fun(*argv):
#     for arg in argv:
#         print(arg)
# fun('Hello', 'Welcome', 'to', 'python')

#variable lenth key word argument
# Python program to illustrate
# *kwargs for variable number of keyword arguments


# def myFun(**kwargs):
# 	for key, value in kwargs.items():
# 		print("%s == %s" % (key, value))


# # Driver code
# myFun(first='Geeks', mid='for', last='Geeks')

#using docstring(__doc__)
# A simple Python function to check
# whether x is even or odd


def evenOdd(x):
	"""Function to check if the number is even or odd"""
	
	if (x % 2 == 0):
		print("even")
	else:
		print("odd")


# Driver code to call the function
print(evenOdd.__doc__)
