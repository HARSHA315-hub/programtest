n = int(input("Enter the row:"))
for i in range(n):
    num = 1
    for _ in range(1,n-i):
        print(" ",end="")
    for j in range(i+1):
        print(int(num),end=" ")
        num = num * (i-j)/(j+1)
    print()