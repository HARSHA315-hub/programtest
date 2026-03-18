l = list(map(int, input("Enter the list: ").split()))
k = int(input("Enter the window: "))
w = sum(l[:k])
m = w
for i in range(k,len(l)):
    w = w + l[i] - l[i-k]
    m = max(m,w)
print(m)