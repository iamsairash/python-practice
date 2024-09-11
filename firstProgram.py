# print("Hello world!")
# name = "Sairash"
# age = 23
# phone = 9821838301

# print("My name is ", name, " I am ", age, " phone numer is ", phone)

# # this is comment 
# """
# this is multi line comment

# """

#program to input two numbers, and print their sum 

# num1 = input("Enter first number: ")
# num2 = input ("Enter second number: ")

# sum = int(num1) + int(num2)

# print(sum)



# program to input side of square and print area

# side = input("Enter the side of square: ")
# area  = int(side) * int(side)
# print("The are of square is ",area)





# avg

# n1 = float(input("Enter num1: "))
# n2 = float(input("Enter num2: "))
# avg =( n1 + n2 )/2
# print(avg)



# T or F
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if(a>b):
#     print("t")
# else:
#     print("f")



# fname = input("Enter your first name: ")

# print(fname.count("a"))





#conditional practice:

# mark = int(input("Enter your mark: "))
# if mark>=90:
#     print("A+")
# elif mark>=80 and mark <90:
#     print("A")
# elif mark>=70 and mark<80:
#     print("B+")
# elif mark>=50 and mark<70:
#     print(" Just Pass")
# else:
#     print("Fail ")





#odd or even

# number = int(input("Enter a number: "))

# if(number%2==0):
#     print("even")
# else:
#     print("odd")



#greatest of 3 numbers:

# n1 = input("Enter first number: ")
# n2 = input("Enter second number: ")
# n3 = input("Enter third number: ")

# if(n1>n2 and n1> n3):
#     print(n1)
# elif n2>n1 and n2>n3:
#     print(n2)
# elif n3>n1 and n3>n2:
#     print(n3)



#check if it is multiple of 7 or not ?

# number = int(input("Enter a number: "))
# if(number%7==0):
#     print("multiple of 7")
# else:
#     print("not ")





#Create a list of your favorite fruits. 
# Add a new fruit to the list and remove an existing one.
#  Print the updated list.

# fruits = ["apple", "mango", "banana", "litchi"]
# print(fruits)
# #print(len(fruits))
# print(type(fruits))

# fruits[1] = "Maldo aam"
# print(fruits)

# fruits.append("kiwi")
# print(fruits)

# fruits.remove("banana")
# print(fruits)



#playing with list

# numbers = [122, 23, 34, 304, 75, 98]
# print(numbers[:2])
# print(numbers[2:6])
# numbers.sort()
# print(numbers)
# numbers.insert(1,100)
# numbers.reverse()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)






# #tuples are immutable but list are mutable. 

# tup = (23,43,5,3,23,322) #we can access each el, but can't update el

# print(tup)

# # tup.sort() # can't be done. but by converting it to list we can do. 
# print(tup)


# tup.count(23) # return the occurance of 23
# tup.index(5) # return 1st inx of occurence




#WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

# ez



# check palindrom or not using copy()

# list = [1,2,3,2,1]
# copylist = list.copy()
# copylist.reverse()

# if(list == copylist):
#     print("palindrom")
# else: 
#     print( "not p")



#count A graded students: 
# grades = ("A", "B", "A", "A", "C","D")
# print(grades.count("A"))

# gradesList = list(grades)
# gradesList.sort()
# print(gradesList)





# dictionary 

# dict = {
#     "name": "Sairash",
#     "age": 23,
#     "email": "iamsairash@gmail.com",
#     "college": "BMC"
# }

# dict["name"] = "Sairash Chaudhary"
# dict["phone"] = "9821838301"

# print(dict)


# null_dict = {} 
# value can be added later

# user= {
#     "name": "rishi",
#     "subjects": {
#         "physics": 90,
#         "chemistry": 80,
#         "math": 70
#     }
# }
# print(type(user.keys())) 
# # print(user["subjects"]["math"])
# print(list(user.keys()))




# my_Dict = {
#     "name": "apna college",
#     "courses": ["java", "C","JS","python"],
#     "fees": {
#         "java":5000,
#         "c":"free",
#         "JS":3000,
#         "python": 1200
#     }
# }

# print(my_Dict.keys()) # return keys
# print(my_Dict.values())  #return values
# print(my_Dict.items())  # returns key: value as tuple
# print(my_Dict.get("fees")) # return the respective value of the key

# new_Dict= {
#     "teacher": "Shraddha mam"
# }
# my_Dict.update(new_Dict)
# print(my_Dict)







#set

# A = {"ram","Shyam","hari","sita"}
# B={"dhir","ramesh","sumit","sagar"}

# print(A,B)

# A.add("hira")
# print(A)

# B.remove("dhir")
# print(B)

# A.pop() #remove random el
# print(A)

# C = A.union(B)
# print(C)

# D = A.intersection(B) 
# print(D) #empty as there is no same el

# #to create empty set

# E = set()

# D = {} #this will create empty dictionary




#practice time

# dict = {
#     "table": ("a piece of furniture", "list of facts and figures"),
#     "cat": "a small animal"
# }

# print(dict.get("table"))
# print(dict.get("cat"))



#Q. one class needed for one subject
# subjects = ["python", "python", "C++", "java", "JS", "C++", "JS", "python"]
# subjectSet = set(subjects)
# print("total class needed are: ",len(subjectSet))



#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
#an empty dictionary & add one by one. Use subject name as key & marks as value.

# subjects = {}
# subjects["python"] = 90
# subjects["java"] = 60
# subjects["JS"] = 70
# print(subjects)

# or 

# subjects = {}
# m1 = input("Enter marks of math")
# subjects.update({"math": m1})
# m2 = input("Enter marks of science")
# subjects.update({"science": m2})
# m3 = input("Enter marks of social")
# subjects.update({"social": m3})

# print(subjects)





# Figure out a way to store 9 & 9.0 as separate values in the set.
#(You can take help of built-in data types)

# num = {9, "9.0"}
# print(num)

# or

# num = {
#     ("float", 9.0),
#     ("int", 9)
# }
# print(num)





#loops

#1 t0 `100`

# count = 1
# while count <=100:
#     print(count, " ")
#     count+=1



# 100 to 1

# count =100
# while (count>=1):
#     print(count)
#     count-=1



#table of given number; 
# n = int(input("Enter a number"))

# m = 1
# while m<=10:
#     print(n," x ",m," = ",n*m)
#     m+=1



#print list using loop 

# list = [23,1,2,4,3,5,3,64,564,5,4,3,5,346]

# count = 0
# while count<len(list):
#     print(list[count])
#     count+=1


#Search for a number x in this tuple using loop:

# numbers = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x=int(input("Enter a number: "))
# i=0
# found = False
# while(i<len(numbers)):
#     if(numbers[i]==x):
#         found = True
#         break
#     i+=1

# if(found):
#     print(x," is found")
# else:
#     print(x, " is not found")





# Print the elements of the following list using a loop:

# list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# for el in list:
#     print(el)
    
    
# Search for a number x in this tuple using loop:

# tpl = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

# x = int(input("Enter x: "))
# found = False

# for el in tpl:
#     if(el==x):
#         found = True
#         break

# if found:
#     print(x," found")
# else:
#     print(x, "not found")




# 100 to 1
# for el in range(100,0,-1):
#     print(el)



#table 

# num = int(input("Enter a number: "))

# for el in range(1,10+1):
#     print(num," x ",el," = ",num*el)


# pass is the statement that does nothing, use where syntax is required but nothing to do 
# for el in range(5):
#     pass




# sum of 1st n numbers; (use while loop )

# n = int(input("Enter number: "))

# count = 1
# sum =0
# while count<=n:
#     sum = sum + count
#     count+=1
# print("The sum up to ", n, " is ", sum)


#factorial 

# n = int(input("Enter a numer: "))

# fact =1
# for el in range(1,n+1):
#     fact = fact * el

# print(fact)



#function to print length of list 

# list = ["sairash", "mundre","lokesh","pushpa","rishiraj"]

# def calc_len(l):
#     return len(l)

# l = calc_len(list)
# print(l)


#fun to print elements of list in single line
# list = ["sairash", "mundre","lokesh","pushpa","rishiraj"]

# def el_list(l):
#     for i in l:
#         print(i,end=" ")

# el_list(list)




# fun to find factorial

# n = int(input("enter a number: "))

# def fact(n):
#     p = 1
#     while n>0:
#         p=p*n
#         n-=1
#     return p

# print(fact(n))




#usd to npr

# def convert(usd):
#     return usd * 150
# npr = convert(5)
# print("npr is ", npr)




# recursion 

# def show(n):
#     if (n==0):
#         return
#     print(n)
#     show(n-1)

# show(5)




#factorial 

# def fact(n):
#     if(n==0 or n==1): return 1
#     return fact(n-1)*n

# print(fact(5))




#sum of first n natural num 

# n = int(input("Enter a numbers: "))

# def sum_natural(num):
#     if(num==0): return 0
#     return  num + sum_natural(num-1)

# print(sum_natural(n))



# print elements in list 

# list = [1,2,34,234,34,4534,3,43434,3,344323]

# def print_el(l,i=0):
#     if(i==len(l)): return
#     print(l[i], end=" ")
#     print_el(l,i+1)
    
# print_el(list)