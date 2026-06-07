# Task no.3:
sent=input("Enter a string:")

upper_func = lambda a : a.upper()

upper_sent = upper_func(sent)

def invert(word):
    print(word[::-1])

invert(upper_sent)