# Take sentence and check how many vowels and consonants it have.
sent= "Hi its me"
vowels= 0
consonants= 0
for s in sent:
     if s=='a'or s=='e'or s=='i'or s=='o'or s=='u'or s=='A'or s=='E'or s=='I'or s=='O'or s=='U':
        vowels+=1
     elif s!=" ":
         consonants+=1

print(f"Sentence is:",{sent})
print(f"Total vowels are:",{vowels})
print(f"Total consonants are:",{consonants})   