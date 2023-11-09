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

def add(x, lst = []):
    if x not in lst:
        lst.append(x)
        
    return lst

def ListAppend():
    list1 = add(1)
    print(list1)

    list2 = add(2)
    print(list2)

    list3 = add(3, [11, 12, 13, 14])
    print(list3)

    list4 = add(4)
    print(list4)

def count(s, c) :
    res = 0
    for i in range(len(s)) :
        # Checking character in string
        if (s[i] == c):
            res = res + 1
    return res

# The function for sorting elements in ascending order 
def selectionSort(lst):
    for i in range(len(lst) - 1):
        # Find the minimum in the lst[i : len(lst)]
        currentMin = min(lst[i : ])
        currentMinIndex = i + lst[i: ].index(currentMin)
        
        # Swap lst[i] with lst[currentMinIndex] if necessary
        if currentMinIndex != i:
            lst[currentMinIndex], lst[i] = lst[i], currentMin
def twoDimentionList():
    distances = [
        [0, 983, 787, 714, 1375, 967, 1087],
        [983, 0, 214, 1102, 1763, 1723, 1842],
        [787, 214, 0, 888, 1549, 1548, 1627],
        [714, 1102, 888, 0, 661, 781, 810],
        [1375, 1763, 1549, 661, 0, 1426, 1187],
        [967, 1723, 1548, 781, 1426, 0, 239],
        [1087, 1842, 1627, 810, 1187, 239, 0]
                ]
    print ("List Orginal ", distances)
    
#Read Table Data which include number of Rows & Colum
def ReadTableData():
    matrix = [] # Create an empty list
    numberOfRows = eval(input("Enter the number of rows: "))
    numberOfColumns = eval(input("Enter the number of columns: "))
    for row in range(0, numberOfRows): 
        matrix.append([]) # Add an empty new row 
        for column in range(0, numberOfColumns): 
            print("Row#",row+1 , " Cloumn# " , column+1)
            value = eval(input("Enter an element and press Enter: " ))
            matrix[row].append(value) 
    print(matrix) 
    print()
def ReadTableDatak():
    matrix=[]
    NumOfRows=eval(input("Enter the number of rows : "))
    NumOfcols=eval(input("Enter the number of cols : "))

    for row in range(0,NumOfRows):
        matrix.append([])
        for Cols in range(0,NumOfcols):
            print("Row#",row+1 , " Cloumn# " , column+1)
            value=eval(input("Enter the element and enter "))
            matrix[row].append(value)
    print(matrix)

def SumTable():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Assume a list is given
    total = 0
    for row in range(0, len(matrix)): 
        for column in range(0, len(matrix[row])): 
            total += matrix[row][column]

    print("Total is " + str(total)) # Print the total  

    print(matrix)  
def QuizSystem():
    # Students' answers to the questions
    answers = [
      ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
      ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
      ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
      ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
      ['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
      ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
      ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
      ['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D']]
      
    # Key to the questions
    keys = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']
    
    # Grade all answers
    for i in range(len(answers)):
        # Grade one student
        correctCount = 0
        for j in range(len(answers[i])): 
            if answers[i][j] == keys[j]:
                correctCount += 1

        print("Student", i, "'s correct count is", correctCount,"/10")

altanta = [714,1102,43,765,98,54,543]

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
print("1: Python List Methods\n 2: Python List index \n 3:Python List append \n Python List extend")
print("Python List insert \n Python List remove \n Python List count \n Python List pop")
print(" Python List reverse\n Python List sort \n Python List copy \n Python List clear")
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
    list1 = [2, 4, 6]
    list2 = [1, 3, 7]
    list3 = list1 + list2
    print(list3)
    i = 0
    while i < len(list3):
        print(list3[i])
        i += 1

    print("List 1 before copy.... ", list1)
    list1=list3
    print("List 1 After copy.... ", list1)

if x==7:
    items = "Welcome to the SCME".split() 
    print(items)
    items = "34#13#78#45".split("#")
    print(items)
if x==8:
    # reverse the order of list elements
    list3 = [2, 3, 5, 7]
    list3.reverse()
    print('Reversed List:', list3)
if x==9:
    ListAppend()
if x==10:
    str= input("add text to search text: ")
    c = input("add character to search count within the text you add: ")
    print(count(str, c))
if x==11:
    input_list = input('Enter elements of a list separated by space \n')
    user_list = input_list.split()
    selectionSort(user_list)
    print (user_list) 
if x==12:
    twoDimentionList()
if x==13:
    ReadTableDatak()
if x==14:
    SumTable()
if x==15:
    QuizSystem()
else:
    print("Error! Try Again....")


