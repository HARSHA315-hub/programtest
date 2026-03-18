m = int(input("Enter the number: "))
flag = 0
for i in range(2,m//2):
    if m%n == 0:
        flag += 1
if flag > 0:
    print("Not A Prime Number")
else:
    print("Prime Number")