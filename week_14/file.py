x = 25
y = "Badar"
print(y)

def welcome():
    # global x 
    x = 15
    print(globals()['x'], globals()['y'])
    

welcome()
print(x)