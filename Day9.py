"""
6

l = [3,5,1,8,6]
m = l[0]
n = 0
for i in range(len(l)):
    if l[i] > m:
        m = l[i]
        n = i
l.pop(n)
m = l[0]
for i in l:
    if i > m:
        m = i
print(m)

or

l = [3,5,1,8,6]
l.remove(max(l))
print(max(l))

7

n = input("Enter The String: ")
i = 0 
j = len(n) - 1
while i <= j:
    if n[i] != n[j]:
        print("False")
        exit()
    i += 1
    j -= 1
print("True")

8

s = input("Enter The String: ")
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
for i, j in d.items():
    print(i,":",j)

9

l = [1,2,3,4,5]
tar = 6
n = len(l)
m = []
for i in range(n):
    j = i+1
    while j < n:
        if l[i] + l[j] == tar:
            m.append((l[i],l[j]))
        j += 1
print(m)

10

l = [1,2,3,4,1]
seen = set(l)
if len(seen) == len(l):
    print("False")
else:
    print("True")

or

l = [1,2,3,4,1]
seen = []
for i in l:
    if i not in seen:
        seen.append(i)
    else:
        print("True")
        exit()
print("False")
"""
n = int(input("Enter The Number: "))
b = ""
while n > 0:
    b = str(n%2) + b
    n //= 2
print(b)