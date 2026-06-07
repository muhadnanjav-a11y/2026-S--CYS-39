# Task no.4:
def cel_to_fah(c):
    f=(c*9/5)+32
    return f

def fah_to_cel(f):
    c=(f-32)*5/9
    return c

celsius=float(input("Enter temperature in celsius:"))
fahreheit=float(input("Enter temperature in fahreheit:"))

f_result=cel_to_fah(celsius)
c_result=fah_to_cel(fahreheit)

print("Temperature in fahreheit is:",f_result)
print("Temperature in celsius is:",c_result)