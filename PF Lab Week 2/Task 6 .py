# Random password
 
import random

upper_case = "ABCDEFGHIJKLMNOPQRSUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
digits = "1234567890"
special_chars = "!@#$%^&*()_`~,./;[<>?"
temp = ""
password = ""
choice = False

length = int(input("Enter password length: "))

choice = input("Do you want to add Upper case Letters (yes/no): ")
if choice == "yes":
    temp += upper_case

choice = input("Do you want to add Lower case Letters (yes/no): ")
if choice == "yes":
    temp += lower_case

choice = input("Do you want to add Digits (yes/no): ")
if choice == "yes":
    temp += digits

choice = input("Do you want to add Special Characters (yes/no): ")
if choice == "yes":
    temp += special_chars
    
if temp == "":    
    print("Atleast choose something!")
else:
    for i in range(1, length+1):
        password += random.choice(temp)
    
    print(f"Your Password: {password}")