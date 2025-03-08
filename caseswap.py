a=input("Enter the string: ")
outs=''
for i in a:
    if i.isupper():
        outs+=i.lower()
    elif i.islower():
        outs+=i.upper()
    else:
        outs+=i
print(outs)
