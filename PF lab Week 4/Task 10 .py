# Task 10

def add(a,b):
    print(f"Sum is :",a+b)

def subtract(a,b):
    print(f"Subtraction is :",a-b)

def multiply(a,b):
    print(f"Product is :",a*b)

def divide(a,b):
    print(f"Division is :",a/b)

while True:
    print("\n Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice : ")

    if choice =="5":
        print("Exiting claculator.")
        break

    if choice in ['1','2','3','4']:
        try:
            a=int(input("Enter value of a:"))
            b=int(input("Enter value of b:"))
    
        except ValueError:
            print("Please enter valid integers.")
            continue

        if choice == "1":
            add(a,b)

        elif choice =="2":
            subtract(a,b)

        elif choice =="3":
            multiply(a,b)

        elif choice =="4":
            divide(a,b)
       
    else:
        print("Invalid choice.")