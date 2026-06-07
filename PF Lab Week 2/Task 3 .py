# print pattern of "*"
n = 5

# Upper 
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end = "")
    print()

# Lower 
for i in range(n-1, 0, -1):
    for j in range(1, i+1):
        print("*", end = "")
    print()