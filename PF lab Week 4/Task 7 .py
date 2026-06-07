# Task 7
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))

def maximum(a,b,c):
     if a > b and a > c:
      print(f"{a} is greater than {b} and {c}")

     elif b > c:
        print(f"{b} is grater than {c}")
    
     else:
         print(f"{c} is greater than both {a} and {b}")

     return c

maximum(a,b,c)