# Task no.1:
def fact(n, f=1):
    for i in range(1, n+1):
        f = f * i
    return f
    
def Perm(n, r):
    return fact(n) // fact(n - r)
    
def Comb(n, r):
    return fact(n) // (fact(r) * fact(n - r))

# Main     
n = int(input("Enter n: "))
r = int(input("Enter r: "))

if r > n:
    print("r can't greater than n")
else:
    p = Perm(n, r)
    c = Comb(n, r)
    
    print(f"\nP({n}, {r}) = {p}")
    print(f"C({n}, {r}) = {c}")