# RECURSIVE FUNCTION:
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
     return fact(n-1)*n

print("The factorial of 4 is:",fact(6))


# FIBONACCI SERIES 
# def add(n):
#     if n == 0:
#         return 0
#     return (n-1)+(n-2)
# print(add(10))