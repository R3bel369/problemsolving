#1.print 1 to 10 numbers
for i in range(1,11) :
 print(i)   

#2.even between 1 t0 10
for i in range(2,21,2) :
 print(i) 

#3.Squares of 1 to 10
n=11
for i in range(1,n) :
 print(i**2)

#4.factorial of 5!
a=1
for i in range(1,6) :
 a=a*i
print(a)  

#5.sum of numbers between 1 to 10
a=0
for i in range(1,11) :
 a=a+i
print(a) 

#6.Hello on new line
for i in "hello":
    print(i)

#7. 5 Table   
a=5
for i in range(1,11) :
 print(a,'*',i,'=',a*i)

#8.Problem: Check if a Number is Even or Odd.
a=int(input('Enter Number'))
if a%2==0 :
  print('Even')
else :
  print('Odd') 

# 9.Problem: Check if a Year is a Leap Year
year=int(input("Enter Year"))
if year%4==0 or year%400==0 :
  print('Leap year') 
elif year%100!=0 :  
  print('Not Leap Year')

#10. Check if a Number is Divisible by Both 3 and 5
number=int(input('Number'))
if number%3==0 and number%5==0 :
    print('Divisble By 3 and 5')
else :
    print('Not Divisble By 3 and 5')    

#11.Problem: Check if a Person is Eligible to Vote
a=int(input("Enter age"))
if a>=18 :
    print("Elgible for vote")
else :
    print('Not elgible for Vote')

#12.   Problem: Check if a Number is a Multiple of 10
a=int(input('Number'))
if a%10==0 :
    print('Multiple of 10')
else :
    print('Not Multiple of 10')    

#13. Problem: Compare Two Numbers and Print the Smaller One
a=int(input('Number'))
b=int(input('Number'))
if a<b :
    print("A is Small")
elif a>b :
    print('B is Small') 

#14.Largest among three numbers
a=int(input('digit'))
b=int(input('digit'))
c=int(input('digit'))
if a>b and a>c :
    print('largest is a')
elif b>c and b>a :
    print('largest is b')
if c>a :
     print('largest is c')   
elif  c>b :
      print('largest is c')

#15.Positive or Negative Number
a=int(input('Number'))
if a>0 :
    print('given number is positive')
elif a<0 :
    print('given number is negative')              

#16.Vowel or consonant
a=int(input('Enter an alphabet'))
if (a==a or a==e or a==i or a==o or a==u) :
  print('Vowel')
else :
  print('Consonant')

### ASCII Values
a='aPpLe'
cap=''
sma=''
for i in a:
    if ord(i)>64 and ord(i)<90:
     cap+=i
    else:
       sma+=i
print(f"{cap}{sma}")
### replace vowel consonant
a='banana'
b='a,e,i,o,u,A,E,I,O,U'
for i in a:
   if i in b:
      print(i.replace(i,"k"))
## Palindrome##
a='madam'
b=a[::-1]
if a==b:
   print('it is palindrome')
else:
   print('Not palindrome')
## count vowel
a='apple'
b='a,e,i,o,u,A,E,I,O,U'
count=0
for i in a:
   if i in b:
      count+=1
print(count)
## count specific characters
a='teach'
s='a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
count=0
for i in s:
    if i in a:
        print(i)
        count+=1
print(count)
## remove white spaces
a='kumar raj'
b=a.replace(' ','')
print(b)
##using for loop
a='raj kumar'
b='' 
for i in a:
   if i==' ':
      continue
   print(i)
## using replace
a='raj kumar'
print(a.replace(' ',''))
## replace a with i
a='chaitanya'
for i in a:
   if i=="a":
      print('i')   
   else:
      print(i)  
# replace _ and after it would be cap
a='cha_iyy_ku'
c=a.split("_")
for word in c:
 b= ''.join(word.capitalize())
 print(b,end='')
###
a='Hello,World!'
i=0
while i<len(a):
    print(a[i],end='')
    i+=1
##
for i in range(0,11):
    print(i)
##
for i in range(0,21,2):
 print(i)
##
 a='Aditya'
 print(a,len(a))
##
a=''
if a=='':
   print('sting is empty')
else:
   print('Not empty')   
##   
a='abcdef'
print(a.upper())
##
a='abcdef'
print(a.lower())
###
a='apple'
print(a[0])
##
a='apple'
print(a[0])
##
a='apple'
print(a[len(a)-1])
##
a='kumar'
b='a,e,i,o,u,A,E,I,O,U'
count=0
for i in a:
    if i in b:
        count+=1
        print(i,count)
###
def str():
 a=input()
 a=a.split(' ')
 a='-'.join(a)
 return a

print(str())        
   
#print Each Element:
#Given numbers = [1, 2, 3, 4, 5], use a for loop to print each number.
a=[1,2,3,4,5]
for i in a:
    print(i)
#Given fruits = ["apple", "banana", "cherry"], use a for loop to print:
#I like apple  
#I like banana  
#I like cherry
a=["apple", "banana", "cherry"]
for i in a:
    print('I like',i)
#Sum of List Elements:
#Given nums = [10, 20, 30, 40], use a for loop to calculate and print the total sum.
a=[10, 20, 30, 40]
sum=0
for i in a:
    sum+=i
    print(sum)
#Count Even Numbers:
#Given numbers = [1, 2, 3, 4, 5, 6], use a for loop to count how many numbers are even.
a=[1, 2, 3, 4, 5, 6]
count=0
for i in a:
    if i%2==0:
     count+=1
print(count)
#Find the Largest Number:
#Given nums = [3, 7, 2, 8, 5], use a for loop to find and print the largest number.
a= [3, 7, 2, 8, 5]
a.sort()
for i in a:
 print(a[len(a)-1])
 break
#Copy a List:
#Given original = [5, 10, 15, 20], use a for loop to copy all elements into a new list.
a= [5, 10, 15, 20]
b=[]
for i in a:
    b.append(i)
print(b)
#Multiply Each Element by 2:
#Given nums = [1, 2, 3, 4], use a for loop to create a new list where each number is doubled.    
a=[1, 2, 3, 4]
k=[]
for i in a:
    k.append(i*2)
print(k)
#Reverse a List (Using Loop):
#Given words = ["hello", "world", "python"], use a for loop to print the elements in reverse order.
w= ["hello", "world", "python"]
l=[]
for i in range(len(w)-1,-1,-1):
    l.append(w[i])
print(l)
#Find Words Starting with 'A':
#Given words = ["apple", "banana", "avocado", "grape"], use a for loop to print only the words that start with "a".
w=["apple","banana","avocado","grape"]
for i in w:
    if i=="apple" or i=='avocado'  : 
     print(i) 
#Create a New List with Only Positive Numbers:
#Given numbers = [-5, 10, -3, 7, -2, 8], use a for loop to create a new list containing only the positive numbers
a= [-5, 10, -3, 7, -2, 8]
b=[]
for i in a:
    if i>0:
     b.append(i)
print(b)
#Sum all elements in a list
#Given a list of numbers, find the sum of all the numbers in the list.
"""
a=[1,2,3,4,5,6]
sum=0
for i in a:
    sum+=i
print(sum)  
"""
#Find the smallest number in a list
#Given a list of numbers, find the smallest number in the list.
"""
a=[6,9,5,1,3,7]
a.sort()
print(a[0])
"""
#Count the number of elements in a list
#Write a function that takes a list and returns the number of elements in the list.
"""
def list():
    a=[1,2,3,4,6]
    count=0
    for i in a:
     count+=1
    return count,a
    
print(list())  
"""  
#Access the last element of a list
#Given a list, access and print the last element of the list.
"""
a=[2,3,4,5,6]
print(a[len(a)-1])

"""
#Check if a list is empty
#Write a function that checks if a given list is empty. Return True if it is empty, otherwise return False.
"""
def list():
    a=[]
    for i in a:
     if i  in a:
      return False
    else:
      return True
print(list())
"""

#Remove an element from the list
#Write a function that removes a specific element from a list if it exists.
"""
def list():
    a=[6,7,8,9,10]
    a.remove(10)
    return a
print(list())
"""
#Find the length of a list
#Given a list, write a function that returns the length (number of elements) of the list.
"""
def list():
    a=[1,2,3,4,5,6,7]
    a=len(a)
    return a
print(list())
"""

#Merge two lists
#Write a function that takes two lists and returns a new list that contains the elements of both lists.
"""
def list():
    a=[1,2,3]
    b=[4,5,6]
    a.extend(b)
    return a
print(list())
"""
#Append an element to a list
#Write a function to add an element to the end of a list.
"""
def list():
    a=[1,2,3]
    a.append(4)
    return a
print(list())
"""
#Get the first N elements of a list
#Write a function that takes a list and a number N, and returns the first N elements from the list.
def list():
   a=[6,7,8,9,10]
   return a[0]
print(list())
#Sum all elements in a list
#Given a list of numbers, find the sum of all the numbers in the list.
"""
a=[1,2,3,4,5,6]
sum=0
for i in a:
    sum+=i
print(sum)  
"""
#Find the smallest number in a list
#Given a list of numbers, find the smallest number in the list.
"""
a=[6,9,5,1,3,7]
a.sort()
print(a[0])
"""
#Count the number of elements in a list
#Write a function that takes a list and returns the number of elements in the list.
"""
def list():
    a=[1,2,3,4,6]
    count=0
    for i in a:
     count+=1
    return count,a
    
print(list())  
"""  
#Access the last element of a list
#Given a list, access and print the last element of the list.
"""
a=[2,3,4,5,6]
print(a[len(a)-1])

"""
#Check if a list is empty
#Write a function that checks if a given list is empty. Return True if it is empty, otherwise return False.
"""
def list():
    a=[]
    for i in a:
     if i  in a:
      return False
    else:
      return True
print(list())
"""

#Remove an element from the list
#Write a function that removes a specific element from a list if it exists.
"""
def list():
    a=[6,7,8,9,10]
    a.remove(10)
    return a
print(list())
"""
#Find the length of a list
#Given a list, write a function that returns the length (number of elements) of the list.
"""
def list():
    a=[1,2,3,4,5,6,7]
    a=len(a)
    return a
print(list())
"""

#Merge two lists
#Write a function that takes two lists and returns a new list that contains the elements of both lists.
"""
def list():
    a=[1,2,3]
    b=[4,5,6]
    a.extend(b)
    return a
print(list())
"""
#Append an element to a list
#Write a function to add an element to the end of a list.
"""
def list():
    a=[1,2,3]
    a.append(4)
    return a
print(list())
"""
#Get the first N elements of a list
#Write a function that takes a list and a number N, and returns the first N elements from the list.
def list():
   a=[6,7,8,9,10]
   return a[0]
print(list())


#Sum all elements in a list
#Given a list of numbers, find the sum of all the numbers in the list.
"""
a=[1,2,3,4,5,6]
sum=0
for i in a:
    sum+=i
print(sum)  
"""
#Find the smallest number in a list
#Given a list of numbers, find the smallest number in the list.
"""
a=[6,9,5,1,3,7]
a.sort()
print(a[0])
"""
#Count the number of elements in a list
#Write a function that takes a list and returns the number of elements in the list.
"""
def list():
    a=[1,2,3,4,6]
    count=0
    for i in a:
     count+=1
    return count,a
    
print(list())  
"""  
#Access the last element of a list
#Given a list, access and print the last element of the list.
"""
a=[2,3,4,5,6]
print(a[len(a)-1])

"""
#Check if a list is empty
#Write a function that checks if a given list is empty. Return True if it is empty, otherwise return False.
"""
def list():
    a=[]
    for i in a:
     if i  in a:
      return False
    else:
      return True
print(list())
"""

#Remove an element from the list
#Write a function that removes a specific element from a list if it exists.
"""
def list():
    a=[6,7,8,9,10]
    a.remove(10)
    return a
print(list())
"""
#Find the length of a list
#Given a list, write a function that returns the length (number of elements) of the list.
"""
def list():
    a=[1,2,3,4,5,6,7]
    a=len(a)
    return a
print(list())
"""

#Merge two lists
#Write a function that takes two lists and returns a new list that contains the elements of both lists.
"""
def list():
    a=[1,2,3]
    b=[4,5,6]
    a.extend(b)
    return a
print(list())
"""
#Append an element to a list
#Write a function to add an element to the end of a list.
"""
def list():
    a=[1,2,3]
    a.append(4)
    return a
print(list())
"""
#Get the first N elements of a list
#Write a function that takes a list and a number N, and returns the first N elements from the list.
def list():
   a=[6,7,8,9,10]
   return a[0]
print(list())


#Sum all elements in a list
#Given a list of numbers, find the sum of all the numbers in the list.
"""
a=[1,2,3,4,5,6]
sum=0
for i in a:
    sum+=i
print(sum)  
"""
#Find the smallest number in a list
#Given a list of numbers, find the smallest number in the list.
"""
a=[6,9,5,1,3,7]
a.sort()
print(a[0])
"""
#Count the number of elements in a list
#Write a function that takes a list and returns the number of elements in the list.
"""
def list():
    a=[1,2,3,4,6]
    count=0
    for i in a:
     count+=1
    return count,a
    
print(list())  
"""  
#Access the last element of a list
#Given a list, access and print the last element of the list.
"""
a=[2,3,4,5,6]
print(a[len(a)-1])

"""
#Check if a list is empty
#Write a function that checks if a given list is empty. Return True if it is empty, otherwise return False.
"""
def list():
    a=[]
    for i in a:
     if i  in a:
      return False
    else:
      return True
print(list())
"""

#Remove an element from the list
#Write a function that removes a specific element from a list if it exists.
"""
def list():
    a=[6,7,8,9,10]
    a.remove(10)
    return a
print(list())
"""
#Find the length of a list
#Given a list, write a function that returns the length (number of elements) of the list.
"""
def list():
    a=[1,2,3,4,5,6,7]
    a=len(a)
    return a
print(list())
"""

#Merge two lists
#Write a function that takes two lists and returns a new list that contains the elements of both lists.
"""
def list():
    a=[1,2,3]
    b=[4,5,6]
    a.extend(b)
    return a
print(list())
"""
#Append an element to a list
#Write a function to add an element to the end of a list.
"""
def list():
    a=[1,2,3]
    a.append(4)
    return a
print(list())
"""
#Get the first N elements of a list
#Write a function that takes a list and a number N, and returns the first N elements from the list.
def list():
   a=[6,7,8,9,10]
   return a[0]
print(list())
#Sum all elements in a list
#Given a list of numbers, find the sum of all the numbers in the list.
"""
a=[1,2,3,4,5,6]
sum=0
for i in a:
    sum+=i
print(sum)  
"""
#Find the smallest number in a list
#Given a list of numbers, find the smallest number in the list.
"""
a=[6,9,5,1,3,7]
a.sort()
print(a[0])
"""
#Count the number of elements in a list
#Write a function that takes a list and returns the number of elements in the list.
"""
def list():
    a=[1,2,3,4,6]
    count=0
    for i in a:
     count+=1
    return count,a
    
print(list())  
"""  
#Access the last element of a list
#Given a list, access and print the last element of the list.
"""
a=[2,3,4,5,6]
print(a[len(a)-1])

"""
#Check if a list is empty
#Write a function that checks if a given list is empty. Return True if it is empty, otherwise return False.
"""
def list():
    a=[]
    for i in a:
     if i  in a:
      return False
    else:
      return True
print(list())
"""

#Remove an element from the list
#Write a function that removes a specific element from a list if it exists.
"""
def list():
    a=[6,7,8,9,10]
    a.remove(10)
    return a
print(list())
"""
#Find the length of a list
#Given a list, write a function that returns the length (number of elements) of the list.
"""
def list():
    a=[1,2,3,4,5,6,7]
    a=len(a)
    return a
print(list())
"""

#Merge two lists
#Write a function that takes two lists and returns a new list that contains the elements of both lists.
"""
def list():
    a=[1,2,3]
    b=[4,5,6]
    a.extend(b)
    return a
print(list())
"""
#Append an element to a list
#Write a function to add an element to the end of a list.
"""
def list():
    a=[1,2,3]
    a.append(4)
    return a
print(list())
"""
#Get the first N elements of a list
#Write a function that takes a list and a number N, and returns the first N elements from the list.
def list():
   a=[6,7,8,9,10]
   return a[0]
print(list())

#Create a list of integers from 1 to 10.
a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    print(i)
#How can you access the first element of a list?

a=[5,6,7,8,9,10]
print(a[0:1])

#Write a Python code to append an element to the end of a list.
k=['a','b','c']
k.append('d')
print(k)

#How do you remove the last element from a list?
c=[6,7,8,9,10]
c.pop(-1)
print(c)

#How can you find the length of a list?
d=[1,2,3,4,5,6,7,8]
print(len(d))

#Write a Python program to find the largest number in a list.
d=[1,2,3,4,5,6,7,8,10]
print(max(d))

#How can you sort a list in ascending order?
a=['a','b','A','B']
a.sort()
print(a)

#Write a code to check if an element is present in a list or not.
a=[1,2,3,4,5]
a=[i for i in a if i==5] 
print(a)
#How do you find the index of an element in a list?
a=[5,9,8,4,6]
print(a[0])## (list.index value of the element)
#How can you create a list of 5 elements, then remove all of them?
a=[2,5,8,9,1,5]
print(a.clear())
#How can you slice a list to get elements from index 2 to 5?
p=[1,3,5,7,9,11,13,15]
print(p[2:6])
#How can you concatenate two lists in Python?
a=[1,2]
b=[3,4]
a.extend(b)
print(a)
#How can you copy a list into another list?
a=[2,4,6,8]
b=a.copy()
print(b)

#Write a Python program to count the number of times an element appears in a list.
a=[1,3,3,7,9]
c=0
for i in a:
    if i==3:
        c+=1
print(c)
#How can you check if a list is empty?
a=[2]
if a==[]:
    print('Empty list')
else:
    print('Not empty list')  
#String Questions:
#Create a string variable that holds your name and print it.
a='shiva'
print(a)

#How do you convert a string to uppercase in Python?
a='shiva'
print(a.upper())
#Write a code to check if a string contains a specific substring.
a='abcd'
for i in a:
 if i in 'cd':
    print(i,'it is part of given string')
#How can you find the length of a string in Python?
a='abcdefgh'
print(len(a))
#Write a Python program to reverse a string. 
a='MOMDAD'
print(a[::-1])
#####
a=['apple','ball','mango']
b=[]
c=[]
for i in a:
    for j in i:
        if j in 'aeiouAEIOU' :
           if j not in b:
            b.append(j)
        else:
           if j not in c:
            c.append(j)
print(b,c)
#Max Values in list
a=[[1,2],[3,4,5],[6,7,8,9]]
b=[]
for i in a:
        b.append(max(i)) 
print(b)
#sum of individuals Lists
a=[[1,2],[3,4,5],[6,7,8,9]]
b=[]
for i in a:
        b.append(sum(i))
print(b) 
#Count Vowels in given list
a=['apple','grapes','melon']
b=[]
for i in a:
    c=0
    for j in i:
        if j in 'aeiouAEIOU':
         c+=1
    b.append(c)
print(b)









 
 


        




  



