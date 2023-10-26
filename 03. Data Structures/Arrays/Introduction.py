#Arrays are one of the most commonly-used data structures
#The elements of an array are stored in contiguous memory locations
#Arrays are of two types : Static and Dynamic
#Static arrays have fixed, pre-defined amount of memory that they can use, whereas in dynamic arrays this is flexible
#In Python we only have dynamic arrays
#Some basic operations and their complexities are given below :

#Look-up/Accses - O(1)
#Push/Pop - O(1)*
#Insert - O(n)
#Delete - O(n)

import string
import random
# Sum Func 


def max(num1, num2): 
    if num1 > num2:
        result = num1
    else:
        result = num2

    return result # Return result

def main():
    i = 5
    j = 2
    k = max(i, j) # Call the max function
    print("The maximum between", i, "and", j, "is", k)

def nPrintln(message, n):
    for i in range(0, n):
        print(" Line #: ", i+1 , message) 

main() 
   
nPrintln("Welcome to SCME.ps", 10)



#22 Oct

print("session ss Oct 2023")

def printArea(width = 1, height = 2):
    area = width * height
    print("width:", width, "\theight:", height, "\tarea:", area)


def hashfun():
    string = "Hello, World!"
hash_value = hash(string)
print("The hash value of", string," is " ,hash_value)

#returne Multi Value 

def sort(number1, number2):
    if number1 < number2:
        return number1, number2
    else:
        return number2, number1

n1, n2 = sort(3, 2)
print("n1 is", n1)
print("n2 is", n2)
print ("SugPassword:")

randomLetter1 = random.choice(string.ascii_uppercase)
randomLetter2 = random.choice(string.ascii_uppercase)
randomLetter3 = random.choice(string.digits)
randomLetter4 = random.choice(string.hexdigits)


print(randomLetter1+randomLetter2+randomLetter3+randomLetter4+randomLetter2+randomLetter3) 
#print(getRandomCharacter('A', 'Z'),getRandomCharacter('a', 'z'),getRandomCharacter('A', 'Z'),getRandomCharacter('0', '9'),getRandomCharacter('A', 'Z'))

x =int( input("add your value"))
list1 = [2, 4, 6]
list2 = [1, 3, 7]
if x==1:
    list3 = list1 + list2
    print(list3)
if x==2:
    list3 = 2 * list2
    print(list3)
if x==3:
    list3 = list1 + list2
    print(list3)
    print(list3[2:4])
if x==4:
    list3 = 5* list1
    print(list3)
    print(list3[-3])
    if (2 in list3):
        print("2 Found in list 3")
    languages = ['Python', 'Swift', 'C++']
    print('C' in languages)    # False
    print('Python' in languages)    # True

if x==5:
    list3 = [21, 34, 54, 12]
    print("Before Append:", list3)
    list3.append(32)
    print("After Append:", list3)
if x==6:
    list3 = list1 + list2
    print(list3)
    i = 0
    while i < len(list3):
        print(list3[i])
        i += 1
if x==7:
    items = "Welcome to the SCME".split() 
    print(items)
    items = "34#13#78#45".split("#")
    print(items)

else:
    print("Error! Try Again....")


