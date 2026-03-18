lis = list(map(int,input("Enter The List: ").split()))
total = 1
for i in lis:
    total *= i
result = []
for i in lis:
    result.append(total//i)
print(*result) 