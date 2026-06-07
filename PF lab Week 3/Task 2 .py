# Task no.2:
num_1 = int(input("Enter 1st number: "))
num_2 = int(input("Enter 2nd number: "))

# Lambda function for Greater Number
greater = lambda num_1, num_2: num_1 if num_1 > num_2 else num_2 

# Table Function of Greatest Number
def table(g):
    print("\nTable of Greater Number: ")
    for i in range(1, 11):
        print(f"{g} * {i} = {g*i}")

# Main
g = greater(num_1, num_2)
table(g)

print(f"Greater Number: {g}")