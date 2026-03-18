def format1(inp1):
    return f"{inp1:.2f}".rstrip('0').rstrip('.')
a = input("Enter the list:")
upp=low=dig=oth=0
for i in a:
    if i.isupper():
        upp += 1
    elif i.islower():
        low += 1
    elif i.isdigit():
        dig += 1
    else:
        oth += 1
tot = upp + low + dig + oth
upper=((upp/tot)*100)
low1=((low/tot)*100)
dig1=((dig/tot)*100)
other=((oth/tot)*100)
print(f'Uppercase letters are {format1(upper)}%')
print(f'Lowercase letters are {format1(low1)}%')
print(f'Digits Are {format1(dig1)}%')
print(f'Other Characters Are {format1(other)}%')