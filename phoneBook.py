#liy
import os

PATH = "E:\kiarash\AI\phoneBook\phoneBook.txt"

#validation
def validation():
    if not os.path.exists(PATH):
       f = open(PATH, "w+")
       f.write("")
#phonebook 
def add(name, number):
    validation()
    f = open(PATH, "a+")
    new_phone = name + ":" + number + "\n"
    f.write(new_phone)
    f.close()
    
 def search(name):
     validation()
     f = open(PATH, "r")
     for line in f.readlines():
         if name == line.split(":")[0]:
             print(name + ":" + line.split(":")[1])
         f.close()

 def delet(name):
    validation()

 def show_all(): 
    validation()
    
#######Start Function#######

#######Start#######
# ch is choice
from os import path


ch = 1
while ch != 0 :
    print("1-Add User\n2-Search\n3-Delet Phone\n4-Show All\n0-Exit")
    ch = int(input("Enter Your Chpice :"))
    os.system('cls')
    if ch == 1:
        name = input("Enter Name : ")
        number = input("Enter Number : ")
        add(name, number)
    elif ch == 2:
        name = input("Enter Name : ")
        search(name)

    elif ch == 3:
        name = input("Enter Name : ")
        delet(name)

    elif ch == 4:
        show_all()            