import mysql.connector

def main():
    print("DataBase Example \n\t")
    
def showDBFun():
    mydb=connection()
    print(mydb)
    
    mycursor = mydb.cursor()   
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)

def mysqlDB():
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="992002")
    print(mydb)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE Schooltest1")
    if mycursor!=0:
        print("Ok, DATABASE CREATED !!!!! ")
    else:
        print ("Error")

def CreatTable():
    mydb=connection()

    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
    mycursor.execute("CREATE TABLE Fatora (id Int, amount float, name VARCHAR(255) )")
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)

def connection():
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",port="3306",
    password="992002", database="Schooltest1")
    
    return mydb

def InsertCustData():
    mydb=connection()
    mycursor = mydb.cursor()
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    name =input("add your name\n")
    addr =input("add your addres ...\n")

    val = (name, addr)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def ShowCustomers():
    ##mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="992002", database="Schooltest1")
    mydb=connection()
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM customers")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def SearchAlg():
    mydb=connection()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM customers WHERE address = %s ORDER BY name DESC"

    addr =input("Enter Search addres Value...\n")
    val = (addr,)
    mycursor.execute(sql, val) 
    myresult = mycursor.fetchall()
    for x in myresult:
     print(x)

def DeletValue():
    mydb=connection()
    mycursor = mydb.cursor()
    sql = "DELETE FROM customers WHERE address = %s"
    addr =input("Enter addres Value to DELETE ...\n")
    adr = (addr, )
    mycursor.execute(sql, adr)
    mydb.commit()
    
    print(mycursor.rowcount, "record(s) deleted")

main()

print(" SCME DBMS 2023\n 1: To creat New database \n 2:SHOW DATABASES \n 3: CREATE Customer TABLE\n 4: Inster Customer Data \n5: Show All Customers \n 6: Search for Customer By ID or Name \n7: Delete recorde by address value \n")
x =int( input("add your value\n"))

if x==1:
    #dbname = input("enter DB Name\t")
    mysqlDB()
if x==2:
    showDBFun()
if x==3:
    CreatTable()
if x==4:
    InsertCustData()
if x==5:
    ShowCustomers()
if x==6:
    SearchAlg()
if x==7:
    DeletValue()


else:
    print("Error! Try Again....")