# Convert binary no into its deimal equivalent
n = 1101
sp_num = 0
ans = 0
i = 0

while n != 0:
    sp_num = n % 10  
    ans += sp_num * (2 ** i)  
    n = n // 10
    i += 1
    
print(f"Answer: {ans}") 
