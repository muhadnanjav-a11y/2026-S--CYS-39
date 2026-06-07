# Prime no.s taking range from user and also sum of prime no.s
initial=int(input("Enter your range:"))
final=int(input("Enter ur last value:"))
Sum_prime =0
for n in range(initial,final+1):
    count = 0
    for j in  range(1,n+1):
     if n % j == 0:
       count += 1
      
    if count == 2:
       print(" ",n)
       Sum_prime += n
print("sum of prime numbers",Sum_prime)
                            
# ----------------------------------------------------

# Alternative of prime no .s 
# Start = int(input("Enter the Starting Number: "))
# End = int(input("Enter the Ending Number: "))

# print("\n")
# for n in range(Start, End+1):
#     j = 1
#     count = 0
#     for j in range(j, n+1):
#         if n % j == 0:
#             count += 1
        
#     if count == 2:
#         print(" ", n)