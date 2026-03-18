n = int(input("Enter the Number: "))
size = (2*n) - 1
for i in range(size):
    for j in range(size):
        d = min(i,j,size-i-1,size-j-1)
        print(n-d,end=" ")
    print()