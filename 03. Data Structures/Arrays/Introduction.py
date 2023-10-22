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
   
nPrintln("Welcome to SCME.ps", 100)

#22 Oct

print("session ss Oct 2023")


def printArea(width = 1, height = 2):
    area = width * height
    print("width:", width, "\theight:", height, "\tarea:", area)

printArea() # Default arguments width = 1 and height = 2
printArea(4, 2.5) # Positional arguments width = 4 and height = 2.5
printArea(height = 5, width = 3) # Keyword arguments width 
printArea(width = 1.2) # Default height = 2
printArea(height = 6.2) # Default widht = 1

#returne Multi Value 

def sort(number1, number2):
    if number1 < number2:
        return number1, number2
    else:
        return number2, number1

n1, n2 = sort(3, 2)
print("n1 is", n1)
print("n2 is", n2)